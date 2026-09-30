#!/usr/bin/env python3
"""Lädt Clips herunter. Eingabe: JSON-Liste [{"name": "c02.mp4", "url": "https://..."}] -> clips/"""
import json, subprocess, sys, os
os.makedirs("clips", exist_ok=True)
for c in json.load(open(sys.argv[1])):
    subprocess.run(["curl", "-sSL", "-m", "180", "-o", os.path.join("clips", c["name"]), c["url"]], check=True)
    print("ok", c["name"])
