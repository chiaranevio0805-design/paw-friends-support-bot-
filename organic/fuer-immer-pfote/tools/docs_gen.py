#!/usr/bin/env python3
"""Erzeugt 03_schnittplaene/*.md und 04_captions/*.md aus ads.py (gleiche Daten wie der Render)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_all as R
from ads import ADS, SC, ANGLES

ROOT = R.E.ROOT
CTA = {"IG": "Kommentiere „PFOTE“ und ich schick dir den Link 🐾", "TT": "Link in Bio 🐾"}
STRUCT = {"LIN": "Hook-Emotion → Prozess → Ergebnis → CTA", "REV": "Reaktion/Ergebnis zuerst → so ist es entstanden → CTA",
          "TEASE": "goldenes Detail zuerst → Prozess → große Enthüllung → CTA"}


def fmt(t):
    return f"{t:05.2f}".replace(".", ",")


for ang in sorted(ANGLES):
    plan = [f"# Schnittpläne Angle {ang}: {ANGLES[ang]}\n",
            "Alle Zeiten in Sekunden. Quelle = Rohvideo + Ausschnitt (Originalzeit). Zoom 1,00 → 1,04/1,06 pro Shot.",
            "Text-Karte (warmes Weiß, Goldlinie, Fredoka Bold) liegt exakt über dem eingebrannten englischen Text "
            "und verdeckt ihn vollständig. Originalton stumm, Musik = eigener ElevenLabs-Track.\n"]
    cap = [f"# Captions Angle {ang}: {ANGLES[ang]}\n"]
    for a in [x for x in ADS if x["angle"] == ang]:
        n = R.name(a)
        e, dog = R.to_engine(a)
        plan.append(f"## {n}\n")
        plan.append(f"- Hook: **{a['shots'][0][2].replace(chr(92) + 'N', ' ')}**")
        plan.append(f"- Länge: {a['L']} s · Struktur: {a['struct']} ({STRUCT[a['struct']]}) · Textstil: {a['style']} · Hund: {dog}")
        plan.append(f"- Musik: `{os.path.basename(a['music'])}` · Dateien: `{n}_IG.mp4`, `{n}_TT.mp4`\n")
        plan.append("| # | Zeit im Ad | Szene | Quelle | Ausschnitt | Tempo |\n|---|---|---|---|---|---|")
        t = 0.0
        for i, (sh, es) in enumerate(zip(a["shots"], e["shots"])):
            sc, d = sh[0], sh[1]
            clip, ss = es[0], es[1]
            slow = es[5] if len(es) > 5 else 1.0
            plan.append(f"| {i + 1} | {fmt(t)}–{fmt(t + d)} | {sc} | {clip} | {ss:.2f}–{ss + d / slow:.2f} | "
                        f"{'Zeitlupe ' + format(1 / slow, '.0%') if slow > 1.02 else 'normal'} |")
            t += d
        plan.append("\n| Texttafel | Zeit | Text |\n|---|---|---|")
        for k, (t0, t1, tx) in enumerate(e["texts"]):
            plan.append(f"| {'Hook' if k == 0 else k + 1} | {fmt(t0)}–{fmt(t1)} | {tx.replace(chr(92) + 'N', ' / ')} |")
        plan.append(f"| CTA | {fmt(e['cta'])}–{fmt(a['L'])} | IG/FB: {CTA['IG']} · TT/YT: {CTA['TT']} |\n")

        cap.append(f"## {n}\n")
        cap.append(f"**Caption IG/FB:**\n{a['caption']}\n")
        tt = a["caption"].replace("Kommentiere PFOTE und ich schick dir den Link", "Link in Bio").replace("Kommentiere PFOTE", "Link in Bio")
        cap.append(f"**Caption TikTok/YT Shorts:**\n{tt}\n")
        cap.append(f"**Hashtags:** {a['tags']}\n")
        cap.append(f"**Sound-Empfehlung:** {a['sound']} – Datei ist bereits mit eigener Musik unterlegt; "
                   "in der App kann zusätzlich ein Trend-Sound (leise) darübergelegt werden.\n")
        cap.append(f"**Posting:** {a['post']}\n")
    os.makedirs(f"{ROOT}/03_schnittplaene", exist_ok=True); os.makedirs(f"{ROOT}/04_captions", exist_ok=True)
    open(f"{ROOT}/03_schnittplaene/A{ang}_schnittplaene.md", "w").write("\n".join(plan) + "\n")
    open(f"{ROOT}/04_captions/A{ang}_captions.md", "w").write("\n".join(cap) + "\n")
print("ok")
