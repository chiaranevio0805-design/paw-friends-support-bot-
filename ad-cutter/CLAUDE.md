# Ad-Cutter

Automatischer Schnitt von Video-Ads (UGC, Comic, Produkt) für Meta/TikTok.
Clips kommen aus Higgsfield, Musik und Soundeffekte aus ElevenLabs, geschnitten
wird mit ffmpeg nach einem JSON-Edit-Plan.

## Ablauf pro Ad

1. `./setup.sh` (einmal pro Session: ffmpeg, Whisper, Schrift Anton).
2. **Clips holen**: Higgsfield `show_generations` bzw. `show_generation_by_ids` →
   `results.rawUrl` in eine Liste schreiben → `python3 tools/download.py liste.json`
   (landet in `clips/`). Vorher prüfen, ob vorhandene Clips reichen — Higgsfield-Credits
   nur ausgeben, wenn der Nutzer neue Clips will.
3. **Transkribieren**: `python3 tools/transcribe.py en` → `clips/words.json`.
   Clips mit eingebrannten Untertiteln/Wasserzeichen nicht verwenden (Kontaktbogen
   aus Einzelbildern anschauen).
4. **Story bauen**: Hook → Problem → Autorität/Glaubwürdigkeit → Produkt in Aktion →
   Beweis (Ergebnis zeigen) → Angebot/Garantie → Endkarte. Pausen am Clip-Ende wegschneiden,
   doppelte Aussagen vermeiden.
5. **Sounds**: erst `sounds/` wiederverwenden. Neue Musik/SFX über den ElevenLabs-Connector
   (`creative_generate_in_flow`, node_type `music` bzw. `sfx`, `generations_count: 1`),
   vorher `estimate_only` — Musik ~0,35 $, SFX ~0,01 $. Gute Sounds in `sounds/` ablegen.
6. **Plan schreiben** in `plans/<name>.json` (Vorlage: `plans/pawbesties_test_ad.json`),
   dann aus diesem Ordner: `python3 render.py plans/<name>.json`.
7. **Prüfen**: Einzelbilder an Schlüsselstellen ansehen (Untertitel lesbar, nichts über
   der Endkarte), Lautheit ca. -15 bis -16 LUFS.
8. **Liefern**: Datei mit SendUserFile schicken (Limit 30 MB — sonst mit ca. 4000k
   Video-Bitrate neu kodieren).

## Stil-Vorlage (vom Nutzer abgenommen, Test-Ad 30.09.2026)

- 9:16, 1080x1920, 30 fps, ca. 45 s (kürzere Varianten 15–30 s anbieten)
- Hook-Text oben in weißer Box, schwarze Schrift, erste ~3 s
- Untertitel: Anton, 124 px, weiß mit schwarzem Rand, max. 3 Wörter, aktives Wort gelb
  und leicht größer; Schlüsselwörter grün (Produkt, Nutzen, Garantie) bzw. rot (Mythos/„isn't“)
- Zoom-Punch (1.1–1.18) auf Pointen
- Whoosh an jedem Schnitt, Bass-Hit auf die Hook-Pointe, Pop auf Schlüsselwörter,
  „Whoa“ beim Ergebnis-Reveal, Ka-Ching bei Geld-zurück/Preis
- Musik: fröhlicher Acoustic-Pop, wird unter der Stimme automatisch abgesenkt
- Keine Untertitel über der Endkarte

## Marken

- Paw-Besties / FurWonder Brush (Schreibweise aus den Higgsfield-Prompts; Whisper
  versteht „Poor Besties“ → im Plan per `replace` korrigieren)

## Plan-Format (render.py)

`segments` (clip, in, out, zooms, mute, captions_until), `replace`, `emphasis`
(ASS-Farbe in BGR, z. B. `&H3CFF3C&` = grün), `hook`, `music`, `auto_whoosh`,
`sfx` (feste Zeitpunkte), `word_sfx` (Sound auf ein bestimmtes Wort eines Segments).
Pfade relativ zum Ordner `ad-cutter/`.
