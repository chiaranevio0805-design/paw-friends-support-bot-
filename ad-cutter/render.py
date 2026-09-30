#!/usr/bin/env python3
"""Ad-Cutter: rendert eine Ad aus einem Edit-Plan (JSON).

Plan-Felder:
  clips_dir, words (Whisper-Wortzeiten je Clip), out
  segments: [{clip, in, out, zooms: [[von, bis, faktor]], mute, captions}]
  replace: {"falsch erkanntes wort": "richtiges wort"}
  emphasis: {"wort": "&H0000FF&"}   (ASS-Farbe BGR)
  hook: {text, until}
  music: {file, vol}
  sfx: [{file, at, vol}] (at = globale Sekunde)  | auto_whoosh: {file, vol}
  word_sfx: [{seg, word, file, vol}]  (SFX auf ein bestimmtes Wort eines Segments)
"""
import json, subprocess, sys, os, re

W, H, FPS = 1080, 1920, 30


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-3000:]); sys.exit(1)


def ass_time(t):
    t = max(t, 0)
    return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"


def render_segments(plan, work):
    files = []
    for i, s in enumerate(plan["segments"]):
        src = os.path.join(plan["clips_dir"], s["clip"])
        dur = s["out"] - s["in"]
        z = "1"
        for a, b, f in s.get("zooms", []):
            # schneller Punch-In: in 0.12s rein, dann halten
            z = f"if(between(t,{a},{b}),1+({f}-1)*min(1,(t-{a})/0.12),{z})"
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
              f"scale=w='trunc({W}*({z})/2)*2':h='trunc({H}*({z})/2)*2':eval=frame,"
              f"crop={W}:{H},fps={FPS},setsar=1,format=yuv420p")
        af = "aresample=48000,aformat=channel_layouts=stereo"
        if s.get("mute"):
            af += ",volume=0"
        out = os.path.join(work, f"seg{i:02d}.mp4")
        run(["ffmpeg", "-y", "-v", "error", "-ss", str(s["in"]), "-t", str(dur), "-i", src,
             "-vf", vf, "-af", af, "-c:v", "libx264", "-preset", "fast", "-crf", "18",
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out])
        files.append(out)
    lst = os.path.join(work, "list.txt")
    open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
    base = os.path.join(work, "base.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])
    return base


def timeline(plan):
    """Startzeit jedes Segments auf der Gesamt-Timeline."""
    t, starts = 0.0, []
    for s in plan["segments"]:
        starts.append(t)
        t += s["out"] - s["in"]
    return starts, t


def global_words(plan):
    words = json.load(open(plan["words"]))
    starts, _ = timeline(plan)
    rep = {k.lower(): v for k, v in plan.get("replace", {}).items()}
    out = []
    for i, s in enumerate(plan["segments"]):
        if s.get("mute") or not s.get("captions", True):
            continue
        cap_until = s.get("captions_until", s["out"])
        for a, b, w in words[s["clip"]]:
            if a < s["in"] or a >= min(s["out"], cap_until):
                continue
            key = w.lower()
            if key in rep:
                w = rep[key]
                if w == "":
                    continue
            out.append({"t0": starts[i] + a - s["in"], "t1": starts[i] + b - s["in"],
                        "w": w, "seg": i, "end_seg": starts[i] + min(s["out"], cap_until) - s["in"]})
    return out


def build_ass(plan, path):
    ws = global_words(plan)
    emph = {k.lower(): v for k, v in plan.get("emphasis", {}).items()}
    # Gruppen: max 3 Wörter, Umbruch nach Satzzeichen oder Pause > 0.35s
    groups, cur = [], []
    for j, w in enumerate(ws):
        cur.append(w)
        nxt = ws[j + 1] if j + 1 < len(ws) else None
        brk = (len(cur) >= 3 or re.search(r"[.,!?]$", w["w"]) or nxt is None
               or nxt["t0"] - w["t1"] > 0.35 or nxt["seg"] != w["seg"])
        if brk:
            groups.append(cur); cur = []
    lines = []
    for g in groups:
        for k, w in enumerate(g):
            start = w["t0"]
            end = g[k + 1]["t0"] if k + 1 < len(g) else min(w["t1"] + 0.25, w["end_seg"])
            parts = []
            for m, x in enumerate(g):
                txt = x["w"].upper().rstrip(",.")
                col = emph.get(re.sub(r"[^a-z0-9'-]", "", x["w"].lower()))
                if m == k:
                    c = col or "&H00FFFF&"  # aktives Wort gelb (oder Akzentfarbe)
                    parts.append(r"{\c" + c + r"\fscx112\fscy112}" + txt + r"{\r}")
                else:
                    parts.append((r"{\c" + col + "}" + txt + r"{\r}") if col else txt)
            pop = r"{\fscx85\fscy85\t(0,90,\fscx100\fscy100)}" if k == 0 else ""
            lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Cap,,0,0,0,,{pop}{' '.join(parts)}")
    hook = plan.get("hook")
    if hook:
        lines.append(f"Dialogue: 1,{ass_time(0)},{ass_time(hook['until'])},Hook,,0,0,0,,"
                     r"{\fad(0,150)}" + hook["text"])
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Anton,124,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,1,0,1,7,3,2,70,70,560,1
Style: Hook,Anton,92,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,0,0,0,0,100,100,1,0,3,22,0,8,60,60,260,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    open(path, "w").write(head + "\n".join(lines) + "\n")


def sfx_events(plan):
    starts, total = timeline(plan)
    ev = list(plan.get("sfx", []))
    aw = plan.get("auto_whoosh")
    if aw:
        for t in starts[1:]:
            ev.append({"file": aw["file"], "at": max(t - 0.3, 0), "vol": aw.get("vol", 0.5)})
    words = json.load(open(plan["words"]))
    for ws in plan.get("word_sfx", []):
        s = plan["segments"][ws["seg"]]
        for a, b, w in words[s["clip"]]:
            if s["in"] <= a < s["out"] and re.sub(r"[^a-z0-9']", "", w.lower()) == ws["word"]:
                ev.append({"file": ws["file"], "at": starts[ws["seg"]] + a - s["in"] + ws.get("offset", 0),
                           "vol": ws.get("vol", 0.6)})
                break
    return ev, total


def final(plan, base, ass, work):
    ev, total = sfx_events(plan)
    inputs = ["-i", base]
    m = plan.get("music")
    if m:
        inputs += ["-stream_loop", "-1", "-i", m["file"]]
    for e in ev:
        inputs += ["-i", e["file"]]
    fc = [f"[0:v]ass={ass}:fontsdir=/root/.fonts[v]",
          "[0:a]loudnorm=I=-16:TP=-1.5:LRA=11,asplit=2[voice][sc]"]
    mix = ["[voice]"]
    idx = 1
    if m:
        fc.append(f"[1:a]aresample=48000,atrim=0:{total},volume={m['vol']},"
                  f"afade=t=out:st={total-1.5}:d=1.5[mraw]")
        fc.append("[mraw][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[music]")
        mix.append("[music]"); idx = 2
    else:
        fc[-1] = "[0:a]loudnorm=I=-16:TP=-1.5:LRA=11[voice]"
    for k, e in enumerate(ev):
        d = int(e["at"] * 1000)
        fc.append(f"[{idx+k}:a]aresample=48000,volume={e['vol']},adelay={d}|{d}[s{k}]")
        mix.append(f"[s{k}]")
    fc.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=first,"
              f"alimiter=limit=0.95[a]")
    run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(fc),
         "-map", "[v]", "-map", "[a]", "-t", str(total), "-c:v", "libx264", "-preset", "medium",
         "-crf", "19", "-profile:v", "high", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", plan["out"]])


if __name__ == "__main__":
    plan = json.load(open(sys.argv[1]))
    work = os.path.join(os.path.dirname(os.path.abspath(plan["out"])), "work")
    os.makedirs(work, exist_ok=True)
    base = render_segments(plan, work)
    ass = os.path.join(work, "captions.ass")
    build_ass(plan, ass)
    final(plan, base, ass, work)
    print("fertig:", plan["out"], f"{timeline(plan)[1]:.1f}s")
