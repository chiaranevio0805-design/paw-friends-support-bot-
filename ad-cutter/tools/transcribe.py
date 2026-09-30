#!/usr/bin/env python3
"""Transkribiert alle Clips in clips/ mit Wortzeiten -> clips/words.json"""
import glob, json, os, sys
from faster_whisper import WhisperModel
lang = sys.argv[1] if len(sys.argv) > 1 else "en"
m = WhisperModel("small", device="cpu", compute_type="int8")
out = {}
for f in sorted(glob.glob("clips/*.mp4")):
    segs, _ = m.transcribe(f, word_timestamps=True, language=lang)
    out[os.path.basename(f)] = [[round(w.start, 2), round(w.end, 2), w.word.strip()] for s in segs for w in s.words]
    print(os.path.basename(f), " ".join(w[2] for w in out[os.path.basename(f)]))
json.dump(out, open("clips/words.json", "w"))
