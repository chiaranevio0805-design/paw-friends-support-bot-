#!/usr/bin/env python3
"""Rendert alle Ads aus ads.py in beiden CTA-Versionen (IG/TT) nach 05_ads_final/A<n>/.
python3 render_all.py [filter]   z. B. "A1_H0" -> nur passende Ads.  --check = nur Plan prüfen"""
import os, sys
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fip_engine as E
from ads import ADS, SC

OUT = f"{E.ROOT}/05_ads_final"


def name(a):
    return f"FIP_A{a['angle']}_H{a['h']:02d}_{a['L']}s"


def to_engine(a):
    shots, texts, t, cur, cta = [], [], 0.0, None, None
    dogs = set()
    for sh in a["shots"]:
        sc, d, txt, off = sh[:4]
        clip, s0, s1, dog = SC[sc]
        if dog: dogs.add(dog)   # None = Close-up ohne Hund (neutral)
        ss = s0 + off
        avail = s1 - ss
        slow = sh[4] if len(sh) > 4 else max(1.0, round(d / avail + 0.005, 3))
        assert d / slow <= avail + 0.02, (name(a), sc, d, slow, avail)
        assert slow <= 1.6, (name(a), sc, "zu langsam", slow)
        z1 = 1.04 if d < 3 else 1.06
        shots.append((clip, round(ss, 3), d, 1.0, z1, slow) if slow != 1.0 else (clip, round(ss, 3), d, 1.0, z1))
        if txt == "CTA":
            if cur: texts.append((cur[0], t, cur[1]))
            cur, cta = None, t
        elif txt:
            if cur: texts.append((cur[0], t, cur[1]))
            cur = (t, txt)
        t = round(t + d, 3)
    if cur: texts.append((cur[0], cta if cta is not None else t, cur[1]))
    assert abs(t - a["L"]) < 0.01, (name(a), "Länge", t)
    assert len(dogs) == 1, (name(a), "mehrere Hunde", dogs)
    assert cta is not None, (name(a), "kein CTA")
    if t - cta < 2.8:     # CTA mindestens 2,8 s: früher starten, vorherige Tafel kürzen
        cta = round(t - 2.8, 3)
        texts = [(x0, min(x1, cta), tx) for x0, x1, tx in texts if x0 < cta]
    assert texts[0][0] == 0, (name(a), "Hook nicht ab 0 s")
    for x in texts:
        assert x[1] - x[0] >= 1.5, (name(a), "Texttafel < 1,5 s", x)
        assert x[2].count("\\N") <= 1
    return dict(name=name(a), shots=shots, texts=texts, cta=cta, music=a["music"], mus_ss=0), dogs.pop()


def job(args):
    a, pf = args
    e, _ = to_engine(a)
    return E.render(e, pf, f"{OUT}/A{a['angle']}")


if __name__ == "__main__":
    flt = [x for x in sys.argv[1:] if not x.startswith("--")]
    sel = [a for a in ADS if not flt or any(f in name(a) for f in flt)]
    seen = set()
    for a in sel:
        e, dog = to_engine(a)
        key = (a["shots"][0][0], a["shots"][0][2])
        assert key not in seen, ("Hook-Szene + Hook-Text doppelt", name(a)); seen.add(key)
    print(len(sel), "Ads geprüft")
    if "--check" in sys.argv: sys.exit()
    jobs = [(a, pf) for a in sel for pf in ("IG", "TT")]
    with ProcessPoolExecutor(int(os.environ.get("PAR", "2"))) as ex:
        for r in ex.map(job, jobs):
            print("OK", os.path.basename(r), flush=True)
