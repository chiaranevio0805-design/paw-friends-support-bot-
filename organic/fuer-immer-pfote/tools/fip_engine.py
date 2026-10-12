#!/usr/bin/env python3
"""Schnitt-Motor FÜR IMMER PFOTE (abgeleitet aus dem ad-cutting-Skill, engine.py).

Unterschiede zum Skill-Motor:
- keine Sprecherspur, keine Karaoke-Untertitel: Story-Texte stehen in einer hellen Text-Karte oben
- die Text-Karte liegt pro Shot genau über dem eingebrannten englischen Text des Rohvideos (BANDS)
  und deckt ihn vollständig ab (deckend + darunter weichgezeichnet) -> alte Untertitel sind nie sichtbar
- Endkarte = CTA in derselben Karte (IG: "Kommentiere PFOTE ...", TT: "Link in Bio")
- Originalton der Rohvideos wird nie verwendet (mute), Musik = eigene ElevenLabs-Tracks

Ad-Plan (dict):
  name     Dateiname ohne Endung, z. B. FIP_A1_H03_12s
  shots    [(clip, ss, dauer, z0, z1)]   clip = "RAW_02", Zoom z0 -> z1 (Bildmitte)
  texts    [(t0, t1, text)]              "\\N" = Zeilenumbruch, max. 2 Zeilen
  cta      Startzeit der CTA-Karte (bis Videoende)
  music    Pfad zur Musikdatei, mus_ss Startsekunde
"""
import hashlib, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = f"{ROOT}/00_rohmaterial"
WORK = os.environ.get("FIP_WORK", "/tmp/fip_work")
W, H, FPS = 1080, 1920, 30
LINE_H = 0.047                  # Höhe einer Textzeile (Anteil der Bildhöhe) inkl. Luft
CARD_COL = "0xFFFBF4"           # warmes Weiß
INK = "&H00262A33&"             # Textfarbe (BGR) = dunkles Anthrazit-Braun
ACCENT = "&H0035A8D9&"          # Gold (BGR) für Hervorhebungen und die Pfote

# Eingebrannter Text je Rohvideo: (von_s, bis_s, y0, y1) als Anteil der Bildhöhe, gemessen mit textband.py
BANDS = {
    "RAW_01": [(0, 5.12, .160, .318), (5.12, 9.17, .160, .272), (9.17, 99, .145, .262)],
    "RAW_02": [(0, 99, .118, .258)],
    "RAW_03": [(0, 99, .150, .270)],
    "RAW_04": [(0, 4.0, .150, .290), (4.0, 7.67, .165, .245), (7.67, 99, .150, .290)],
    "RAW_05": [(0, 2.71, .105, .300), (2.71, 7.96, .115, .210), (7.96, 99, .125, .235)],
    "RAW_06": [(0, 10.29, .118, .270), (10.29, 99, .105, .275)],
    "RAW_07": [(0, 99, .150, .272)],
    "RAW_08": [(0, 3.04, .140, .295), (3.04, 9.0, .150, .258), (9.0, 99, .150, .270)],
}
MARGIN = 0.012


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(" ".join(cmd)[:2000]); print(r.stderr[-3000:]); sys.exit(1)
    return r.stdout


def band_for(clip, ss, d, zmax, need=None):
    y0, y1 = 1.0, 0.0
    for a, b, c0, c1 in BANDS[clip]:
        if a < ss + d and b > ss:
            y0, y1 = min(y0, c0), max(y1, c1)
    y0, y1 = y0 - MARGIN, y1 + MARGIN
    # Zoom aus der Bildmitte verschiebt den eingebrannten Text nach oben/unten -> Bereich über den ganzen Zoom abdecken
    lo = min(0.5 + (y0 - 0.5) * zmax, y0)
    hi = max(0.5 + (y1 - 0.5) * zmax, y1)
    if need:   # Platz für den Text, der während dieses Shots in der Karte steht
        lo, hi = min(lo, need[0]), max(hi, need[1])
    return lo, hi


def make_shot(shot, need=None):
    clip, ss, d, z0, z1 = shot[:5]
    slow = shot[5] if len(shot) > 5 else 1.0
    os.makedirs(f"{WORK}/shots", exist_ok=True)
    h = hashlib.md5(json.dumps([clip, ss, d, z0, z1, slow, BANDS[clip], need, CARD_COL]).encode()).hexdigest()[:12]
    out = f"{WORK}/shots/{clip}_{h}.mp4"
    if os.path.exists(out): return out
    y0, y1 = band_for(clip, ss, d / slow, max(z0, z1), need)
    by, bh = int(H * y0), int(H * (y1 - y0))
    z = f"({z0}+({z1}-{z0})*min(t/{d:.3f},1))"
    pre = f"setpts={slow:.4f}*PTS," if slow != 1.0 else ""
    fc = (f"[0:v]{pre}fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},setsar=1,"
          f"scale=w='trunc({W}*{z}/2)*2':h='trunc({H}*{z}/2)*2':eval=frame:flags=bicubic,crop={W}:{H},"
          f"unsharp=5:5:0.6,eq=contrast=1.04:saturation=1.08,"
          f"tpad=stop_mode=clone:stop_duration=1,trim=duration={d:.3f},setpts=PTS-STARTPTS,split[a][b];"
          f"[b]crop={W}:{bh}:0:{by},boxblur=30:5[bb];[a][bb]overlay=0:{by},"
          f"drawbox=x=0:y={by}:w={W}:h={bh}:color={CARD_COL}@1:t=fill,"
          f"drawbox=x=0:y={by + bh - 5}:w={W}:h=5:color=0xE3C46A@1:t=fill,format=yuv420p[v]")
    tmp = out + f".part{os.getpid()}.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-ss", str(ss), "-t", f"{d / slow + 0.1:.3f}", "-i", f"{RAW}/{clip}.mp4", "-an",
         "-filter_complex", fc, "-map", "[v]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-r", str(FPS),
         "-threads", "2", tmp])
    os.replace(tmp, out)
    return out


def ass_t(t):
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


# kleine Pfote als ASS-Zeichnung (Ballen + 4 Zehen), Ursprung oben links, ca. 60x56 px
PAW = ("m 18 30 b 6 30 2 46 10 52 b 16 56 22 50 30 50 b 38 50 44 56 50 52 b 58 46 54 30 42 30 b 34 26 26 26 18 30 "
       "m 4 14 b -2 18 0 30 8 28 b 14 26 12 12 4 14 "
       "m 18 2 b 12 4 12 18 20 20 b 26 20 28 4 18 2 "
       "m 42 2 b 32 4 34 20 40 20 b 48 18 48 4 42 2 "
       "m 56 14 b 48 12 46 26 52 28 b 60 30 62 18 56 14")

HEAD = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Story,Fredoka Light,70,{INK},{INK},&H00FFFFFF,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,5,60,60,0,1
Style: Paw,Fredoka Light,10,{ACCENT},{ACCENT},&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def layout(ad, cta_text, end):
    """Textposition je Texttafel = Mitte der Karte des ersten Shots; danach Karten so erweitern, dass der Text passt."""
    starts, t = [], 0.0
    for s in ad["shots"]:
        starts.append(t); t += s[2]
    items = list(ad["texts"]) + [(ad["cta"], end, cta_text)]
    placed = []
    for a, b, txt in items:
        i = max(k for k, st in enumerate(starts) if st <= a + 1e-6)
        clip, ss, d, z0, z1 = ad["shots"][i][:5]
        sl = ad["shots"][i][5] if len(ad["shots"][i]) > 5 else 1.0
        y0, y1 = band_for(clip, ss, d / sl, max(z0, z1))
        n = txt.count("\\N") + 1
        half = n * LINE_H / 2 + 0.012
        c = max((y0 + y1) / 2, 0.135 + half)     # nie in die obere Safe Zone (250 px)
        placed.append((a, b, txt, c, (c - half, c + half)))
    needs = []
    for k, s in enumerate(ad["shots"]):
        a, b = starts[k], starts[k] + s[2]
        ov = [p[4] for p in placed if p[0] < b - 1e-6 and p[1] > a + 1e-6]
        needs.append((min(o[0] for o in ov), max(o[1] for o in ov)) if ov else None)
    return placed, needs


def build_ass(ad, path, placed, end):
    ev = []
    for i, (a, b, txt, c, _) in enumerate(placed):
        y = int(H * c)
        fade = "\\fad(120,0)" if i else ""      # Hook ab Bild 1 sofort voll sichtbar
        txt = txt.replace("*", "")
        ev.append(f"Dialogue: 2,{ass_t(a)},{ass_t(b)},Story,,0,0,0,,{{\\pos(540,{y}){fade}}}{txt}")
    # Pfote rechts neben dem CTA-Text
    c = placed[-1][3]
    ev.append(f"Dialogue: 3,{ass_t(ad['cta'] + 0.15)},{ass_t(end)},Paw,,0,0,0,,"
              f"{{\\pos(955,{int(H * c) - 28})\\fad(150,0)\\p1}}{PAW}{{\\p0}}")
    open(path, "w").write(HEAD + "\n".join(ev) + "\n")


CTA = {
    "IG": "Kommentiere „PFOTE“ und\\Nich schick dir den Link",
    "TT": "Link in Bio",
}


def render(ad, platform, outdir):
    end = round(sum(s[2] for s in ad["shots"]), 3)
    placed, needs = layout(ad, CTA[platform], end)
    files = [make_shot(s, n) for s, n in zip(ad["shots"], needs)]
    name = f"{ad['name']}_{platform}"
    wd = f"{WORK}/ads/{name}"; os.makedirs(wd, exist_ok=True)
    lst = f"{wd}/list.txt"
    open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
    ass = f"{wd}/text.ass"
    build_ass(ad, ass, placed, end)
    os.makedirs(outdir, exist_ok=True)
    out = f"{outdir}/{name}.mp4"
    mus_ss = ad.get("mus_ss", 0)
    af = (f"[1:a]atrim=start={mus_ss},asetpts=PTS-STARTPTS,atrim=duration={end},"
          f"afade=t=in:d=0.15,afade=t=out:st={end - 1.2:.3f}:d=1.2,"
          f"loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-stream_loop", "-1", "-i", ad["music"],
         "-filter_complex", f"[0:v]ass={ass}:fontsdir=/root/.fonts,trim=duration={end},format=yuv420p[vout];{af}",
         "-map", "[vout]", "-map", "[aout]", "-c:v", "libx264", "-preset", os.environ.get("FIP_PRESET", "faster"), "-crf", "19",
         "-maxrate", "8M", "-bufsize", "16M", "-profile:v", "high", "-r", str(FPS), "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{end:.3f}", "-threads", os.environ.get("TH", "2"), out])
    return out
