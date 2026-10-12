#!/usr/bin/env python3
"""Alle 50 Ads FÜR IMMER PFOTE als Schnittplan (Daten). Rendern: python3 render_all.py
Szenen-Zeiten aus 00_rohmaterial/clip_inventar.md (Schnitte per Szenenerkennung gemessen).
Pro Ad EIN Hund (Hundekürzel im Szenennamen)."""

# Szenen: name -> (clip, start, ende, hund)
SC = {
    # G = Golden Retriever (RAW_01)
    "G_press": ("RAW_01", 0.05, 2.66, "Golden"),
    "G_paint": ("RAW_01", 2.76, 5.08, "Golden"),
    "G_frame": ("RAW_01", 5.17, 7.29, "Golden"),
    "G_photo": ("RAW_01", 7.38, 9.12, "Golden"),
    "G_result": ("RAW_01", 9.21, 12.40, "Golden"),
    # L = schokobrauner Senior-Labrador (RAW_02, RAW_06 = 2. Take, RAW_07 = derselbe Hund, gleiche Fotos im Rahmen)
    "L_press": ("RAW_02", 0.0, 4.04, "Lab"),
    "L_paint": ("RAW_02", 4.13, 6.13, "Lab"),
    "L_frame": ("RAW_02", 6.21, 8.17, "Lab"),
    "L_photo": ("RAW_02", 8.25, 10.17, "Lab"),
    "L_result": ("RAW_02", 10.25, 13.86, "Lab"),
    "L6_press": ("RAW_06", 0.0, 4.04, "Lab"),
    "L6_paint": ("RAW_06", 4.13, 6.13, "Lab"),
    "L6_frame": ("RAW_06", 6.21, 8.17, "Lab"),
    "L6_photo": ("RAW_06", 8.25, 10.25, "Lab"),
    "L6_result": ("RAW_06", 10.34, 14.45, "Lab"),
    "L7_oma": ("RAW_07", 0.0, 2.66, "Lab"),
    "L7_press": ("RAW_07", 2.75, 4.71, "Lab"),
    "L7_paint": ("RAW_07", 4.79, 6.46, "Lab"),
    "L7_frame": ("RAW_07", 6.54, 8.46, "Lab"),
    "L7_result": ("RAW_07", 8.54, 11.62, "Lab"),
    # O = Opa mit Hund A (RAW_03); Prozess-Close-ups ohne Hundegesicht
    "O_hold": ("RAW_03", 0.0, 2.50, "Opa-Hund"),
    "O_hug": ("RAW_03", 2.58, 5.00, "Opa-Hund"),
    "O_paint": ("RAW_03", 7.79, 9.58, None),
    "O_frame": ("RAW_03", 9.67, 11.71, None),
    "O_end": ("RAW_03", 13.96, 17.05, "Opa-Hund"),
    # B = Buster, Terrier-Mix (RAW_03 Szene 3) – nur mit Prozess-Close-ups ohne Hund kombinieren
    "B_press": ("RAW_03", 5.08, 7.71, "Buster"),
    # F = Französische Bulldogge (RAW_04)
    "F_press": ("RAW_04", 0.0, 3.96, "Frenchie"),
    "F_paint": ("RAW_04", 4.04, 6.04, "Frenchie"),
    "F_frame": ("RAW_04", 6.12, 7.63, "Frenchie"),
    "F_photo": ("RAW_04", 7.71, 10.67, "Frenchie"),
    "F_result": ("RAW_04", 10.75, 13.84, "Frenchie"),
    # P = Shih-Tzu-Welpe (RAW_05)
    "P_press": ("RAW_05", 0.0, 2.67, "Welpe"),
    "P_paint": ("RAW_05", 2.75, 4.21, "Welpe"),
    "P_frame": ("RAW_05", 4.29, 6.25, "Welpe"),
    "P_photo": ("RAW_05", 6.33, 7.92, "Welpe"),
    "P_result": ("RAW_05", 8.00, 11.08, "Welpe"),
    # S = Blue Staffy + Kleinkind (RAW_08)
    "S_press": ("RAW_08", 0.0, 3.00, "Staffy"),
    "S_kidpaint": ("RAW_08", 3.08, 4.96, "Staffy"),
    "S_kidframe": ("RAW_08", 5.04, 7.08, "Staffy"),
    "S_photo": ("RAW_08", 7.16, 8.62, "Staffy"),
    "S_result": ("RAW_08", 8.71, 11.80, "Staffy"),
}

M = "/home/user/paw-friends-support-bot-/organic/fuer-immer-pfote/musik/"

ANGLES = {
    1: "Geschenk für Oma, Opa & Mama – glückliche Tränen",
    2: "Alter Hund – die Zeit festhalten",
    3: "Weihnachtsgeschenk für Hundemenschen",
    4: "Black Week & Bestellschluss – ein Geschenk, das bleibt",
    5: "Kleine Pfote, große Erinnerung (Welpe, Familie, Erinnerung)",
}

# Ad: (angle, hook_nr, länge, struktur, textstil, musik, [(szene, dauer, text|None, ss_offset)], caption, sound, posting)
# text gilt ab diesem Shot bis zum nächsten Text; letzter Shot = CTA (Text wird pro Plattform gesetzt)
# Strukturen: LIN = Hook-Emotion → Prozess → Ergebnis;  REV = Reaktion/Ergebnis zuerst → „so ist es entstanden“;
#             TEASE = goldenes Detail zuerst → Prozess → große Enthüllung
ADS = []


def ad(angle, h, L, struct, style, music, shots, caption, tags, sound, post):
    ADS.append(dict(angle=angle, h=h, L=L, struct=struct, style=style, music=M + music, shots=shots,
                    caption=caption, tags=tags, sound=sound, post=post))


# ---------------- ANGLE 1: Geschenk für Oma, Opa & Mama ----------------
ad(1, 1, 15, "REV", "Ich-Erzählung", "piano_1.mp3", [
    ("O_hold", 2.5, "Ich hab Opa etwas geschenkt,\\Ndas ihn zum Weinen brachte", 0),
    ("O_hug", 2.4, "Keine traurigen Tränen.\\NGlückliche Tränen.", 0),
    ("O_paint", 2.4, "Die Pfote seines Hundes –\\Nin Ton gedrückt, in Gold gemalt", 0),
    ("O_frame", 2.2, None, 0),
    ("O_hold", 2.5, "Seine Reaktion sagt alles", 0),
    ("O_end", 3.0, "CTA", 0)],
   "Ich wollte Opa etwas schenken, das man nicht einfach kaufen kann. Seine Reaktion sagt alles 🥹 Die Pfote seines Hundes, für immer festgehalten. Kommentiere PFOTE und ich schick dir den Link 🐾",
   "#geschenkfüropa #hundeliebe #pfotenabdruck #glücklichetränen #dogsoftiktok #geschenkidee #erinnerung",
   "ruhiges Klavier mit Streichern (eigener Track: piano_1)", "IG Reels + FB Reels, Sonntag 18–20 Uhr (Familienzeit)")

ad(1, 2, 12, "LIN", "Aussage", "piano_2.mp3", [
    ("O_hug", 2.4, "Das schönste Geschenk\\Nfür Opa kostet keine Uhr", 0),
    ("O_paint", 1.8, "Nur ein bisschen Ton …", 0),
    ("O_frame", 2.0, "… und die Pfote seines Hundes", 0),
    ("O_hold", 2.5, "Er hat es nicht mehr losgelassen", 0),
    ("O_end", 3.3, "CTA", 0)],
   "Opa hat schon alles. Außer das hier. Die Pfote seines Hundes – in Gold, im Rahmen, für immer. Kommentiere PFOTE 🐾",
   "#geschenkfüropa #opaundhund #hundeliebe #pfotenabdruck #weihnachtsgeschenk #giftideas",
   "emotionaler Trend-Sound / Klavier (piano_2)", "IG + FB, Samstag 10–12 Uhr")

ad(1, 3, 10, "REV", "Frage", "reveal_2.mp3", [
    ("O_end", 2.2, "Was schenkt man Opa,\\Nder schon alles hat?", 0.3),
    ("O_paint", 1.9, "Seinen Hund. Für immer.", 0),
    ("O_hug", 2.4, None, 0),
    ("O_hold", 3.5, "CTA", 0)],
   "Was schenkt man jemandem, der schon alles hat? Etwas, das es nur einmal gibt 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#geschenkidee #geschenkfüropa #hundeopa #pfotenabdruck #hund #fyp",
   "aufbauender Gitarren-Sound (reveal_2)", "TikTok 19–21 Uhr, IG Reels")

ad(1, 4, 15, "LIN", "POV", "piano_3.mp3", [
    ("L7_oma", 2.6, "POV: Oma packt dein\\NGeschenk aus", 0),
    ("L7_press", 1.9, "Ich hab heimlich die Pfote\\Nihres Hundes genommen", 0),
    ("L7_paint", 1.6, None, 0),
    ("L7_frame", 1.9, "In Gold ausgemalt.\\NMit zwei Fotos von ihm.", 0),
    ("L_photo", 1.9, None, 0),
    ("L7_result", 3.0, "Sie hat geweint.\\NVor Freude.", 0),
    ("L6_result", 2.1, "CTA", 1.8)],
   "Oma liebt ihren Hund mehr als alles andere. Also hab ich seine Pfote für immer festgehalten 🥹 Kommentiere PFOTE und ich schick dir den Link 🐾",
   "#geschenkfüroma #omaundhund #pfotenabdruck #hundeliebe #glücklichetränen #geschenkidee #dogmom",
   "ruhiges Klavier (piano_3)", "IG + FB Reels, Sonntag 17–19 Uhr")

ad(1, 5, 12, "REV", "Ich-Erzählung", "reveal_3.mp3", [
    ("F_result", 2.6, "Ich hab das für\\Nmeine Mama gemacht …", 1.2),
    ("F_press", 2.2, "Die Pfote ihres Hundes,\\Nin Ton gedrückt", 1.0),
    ("F_paint", 1.8, "Gold ausgemalt", 0),
    ("F_photo", 2.2, "Zwei Lieblingsfotos dazu", 0.3),
    ("F_result", 3.2, "CTA", 0.4)],
   "Für Mama, die ihren Hund wie ihr Kind liebt 🐶❤️ Sie hat geweint. Kommentiere PFOTE und ich schick dir den Link.",
   "#geschenkfürmama #dogmom #hundemama #pfotenabdruck #frenchie #geschenkidee",
   "warmer Akustik-Trend-Sound (reveal_3)", "IG Reels, Mittwoch 19–21 Uhr")

ad(1, 6, 10, "TEASE", "Aussage", "piano_4.mp3", [
    ("F_paint", 2.0, "Mama hat geweint.", 0),
    ("F_frame", 1.5, "Und ich auch.", 0),
    ("F_photo", 2.2, None, 0.5),
    ("F_result", 4.3, "CTA", 0.3)],
   "Manche Geschenke sagen mehr als Worte 🥹 Die Pfote ihres Hundes – für immer im Rahmen. Kommentiere PFOTE 🐾",
   "#geschenkfürmama #hundeliebe #pfotenabdruck #muttertag #dogsofinstagram",
   "ruhiges Klavier (piano_4)", "TikTok + IG, Donnerstag 20 Uhr")

ad(1, 7, 15, "LIN", "Ich-Erzählung", "piano_1.mp3", [
    ("O_hold", 2.5, "Opas bester Freund\\Nhat vier Pfoten", 0),
    ("O_paint", 1.8, "Also hab ich seine Pfote\\Nfestgehalten", 0),
    ("O_frame", 2.0, None, 0),
    ("O_hug", 2.4, "Opas Reaktion …", 0),
    ("O_end", 3.0, "Genau dafür.", 0),
    ("O_hold", 3.3, "CTA", 0)],
   "Opas bester Freund hat vier Pfoten. Jetzt hängt dieser Moment für immer an seiner Wand 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#opa #hundeopa #geschenkfüropa #pfotenabdruck #hundeliebe #weihnachten #giftforgrandpa",
   "ruhiges Klavier (piano_1)", "FB Reels (ältere Zielgruppe) + IG, Sonntag 11 Uhr")

ad(1, 8, 12, "TEASE", "Frage", "reveal_1.mp3", [
    ("L7_paint", 1.8, "Würde deine Oma\\Nbei diesem Geschenk weinen?", 0),
    ("L7_press", 1.9, None, 0),
    ("L7_frame", 1.9, "Die echte Pfote ihres Hundes.\\NIn Gold.", 0),
    ("L7_oma", 2.6, "Sie hat es nicht mehr\\Naus der Hand gelegt", 0),
    ("L7_result", 3.8, "CTA", 0)],
   "Würde deine Oma bei diesem Geschenk weinen? Unsere schon 🥹 Kommentiere PFOTE und ich schick dir den Link 🐾",
   "#geschenkfüroma #oma #hund #pfotenabdruck #weihnachtsgeschenk #geschenkidee",
   "aufbauender Akustik-Sound (reveal_1)", "TikTok 18–20 Uhr, FB Reels")

ad(1, 9, 10, "REV", "POV", "piano_2.mp3", [
    ("O_hug", 2.4, "POV: Du schenkst Opa\\Ndie Pfote seines Hundes", 0),
    ("O_paint", 1.8, None, 0),
    ("O_frame", 1.9, None, 0),
    ("O_end", 3.9, "CTA", 0)],
   "Der Moment, wenn Opa versteht, was in dem Rahmen ist 🥹🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#pov #opa #hundeliebe #pfotenabdruck #geschenkidee #glücklichetränen",
   "emotionaler Trend-Sound / Klavier (piano_2)", "TikTok 20 Uhr, IG Reels")

ad(1, 10, 12, "LIN", "Aussage", "reveal_2.mp3", [
    ("G_result", 2.4, "Für alle, deren Mama\\Nihren Hund mehr liebt als dich", 0.4),
    ("G_press", 2.2, "Seine Pfote in Ton …", 0),
    ("G_paint", 2.0, "… in Gold ausgemalt", 0.2),
    ("G_photo", 1.7, None, 0),
    ("G_result", 3.7, "CTA", 0)],
   "Seien wir ehrlich: Der Hund ist Mamas Lieblingskind 😅🐶 Also bekommt sie das hier zu Weihnachten. Kommentiere PFOTE 🐾",
   "#hundemama #geschenkfürmama #golden #pfotenabdruck #lustig #weihnachtsgeschenk #dogmom",
   "lockerer Trend-Sound (reveal_2)", "TikTok 19 Uhr, IG Reels")

# ---------------- ANGLE 2: Alter Hund – die Zeit festhalten ----------------
ad(2, 1, 15, "LIN", "Aussage", "piano_3.mp3", [
    ("L_press", 4.0, "Warte nicht, bis er\\Nnicht mehr da ist …", 0),
    ("L_paint", 2.0, "Halte seine Pfote fest,\\Nsolange sie neben dir liegt", 0),
    ("L_frame", 1.9, None, 0),
    ("L_photo", 1.9, "In Gold. Mit seinen Fotos.", 0),
    ("L_result", 3.6, "Für immer.", 0),
    ("L6_result", 1.6, "CTA", 2.4)],
   "Die graue Schnauze, die müden Pfoten … irgendwann ist die Zeit vorbei. Halte sie fest, solange er noch neben dir liegt 🤍 Kommentiere PFOTE und ich schick dir den Link.",
   "#alterhund #seniorhund #graueschnauze #pfotenabdruck #hundeliebe #seniordog #erinnerung",
   "ruhiges Klavier mit Streichern (piano_3)", "IG + FB Reels, Sonntag 19–21 Uhr")

ad(2, 2, 12, "LIN", "Ich-Erzählung", "piano_4.mp3", [
    ("L6_press", 3.0, "Er ist schon 13 …\\Nich wollte seine Pfote behalten", 0),
    ("L6_paint", 2.0, None, 0),
    ("L6_frame", 1.9, "Jeder Tag mit ihm zählt", 0),
    ("L6_photo", 1.9, None, 0),
    ("L6_result", 3.2, "CTA", 0.5)],
   "Er ist nicht mehr der Jüngste. Aber diese Pfote bleibt für immer 🤍 Kommentiere PFOTE und ich schick dir den Link.",
   "#seniorhund #alterhund #labrador #pfotenabdruck #hundeliebe #grauesgesicht",
   "ruhiges Klavier (piano_4) oder melancholischer Trend-Sound", "TikTok 20–22 Uhr, IG Reels")

ad(2, 3, 10, "TEASE", "Frage", "erinnerung_2.mp3", [
    ("L_paint", 2.0, "Wie lange wird seine Pfote\\Nnoch neben dir liegen?", 0),
    ("L_press", 2.6, None, 1.2),
    ("L_photo", 1.9, "Halte sie fest. Für immer.", 0),
    ("L_result", 3.5, "CTA", 0)],
   "Niemand weiß, wie viel Zeit bleibt. Aber diesen Abdruck kann dir niemand mehr nehmen 🐾 Kommentiere PFOTE.",
   "#alterhund #seniordog #hundeliebe #pfotenabdruck #erinnerungfürimmer",
   "sanftes Ambient-Klavier (erinnerung_2)", "IG Reels, Dienstag 21 Uhr")

ad(2, 4, 15, "REV", "POV", "erinnerung_3.mp3", [
    ("L7_result", 2.8, "POV: Seine Pfote ist jetzt\\Nfür immer an deiner Wand", 0),
    ("L7_press", 1.9, "So ist es entstanden:", 0),
    ("L7_paint", 1.7, "Abdruck in Ton,\\Nmit Gold ausgemalt", 0),
    ("L7_frame", 1.9, None, 0),
    ("L_photo", 1.9, "Zwei Fotos dazu", 0),
    ("L6_result", 4.8, "CTA", 0)],
   "Seine Pfote, die dich jeden Morgen geweckt hat. Jetzt für immer bei dir 🤍 Kommentiere PFOTE und ich schick dir den Link.",
   "#pov #alterhund #seniorhund #pfotenabdruck #labrador #hundeliebe #forever",
   "sanftes Klavier + Cello (erinnerung_3)", "IG + FB Reels, Samstag 20 Uhr")

ad(2, 5, 12, "LIN", "Ich-Erzählung", "piano_1.mp3", [
    ("G_press", 2.6, "Bevor seine Pfoten müde werden,\\Nhab ich das gemacht", 0),
    ("G_paint", 2.2, None, 0),
    ("G_frame", 2.0, "Ein Abdruck, der bleibt", 0),
    ("G_photo", 1.7, None, 0),
    ("G_result", 3.5, "CTA", 0)],
   "Er wird älter. Ich kann die Zeit nicht anhalten – aber ich kann sie festhalten 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#golden #goldenretriever #pfotenabdruck #hundeliebe #zeitfesthalten #dogsofinstagram",
   "ruhiges Klavier (piano_1)", "IG Reels, Mittwoch 20 Uhr")

ad(2, 6, 10, "LIN", "Ich-Erzählung", "erinnerung_1.mp3", [
    ("B_press", 2.6, "Buster ist 11 …", 0),
    ("O_paint", 1.8, "Also hab ich seinen Pfotenabdruck\\Nin Gold festgehalten", 0),
    ("O_frame", 2.0, None, 0),
    ("B_press", 3.6, "CTA", 0)],
   "Mit 11 merkt man: Jeder Tag ist ein Geschenk. Also hab ich seine Pfote für immer festgehalten 🤍 Kommentiere PFOTE.",
   "#seniorhund #terrier #mischling #pfotenabdruck #hundeliebe #11jahre",
   "sanftes Klavier (erinnerung_1)", "TikTok 21 Uhr, IG Reels")

ad(2, 7, 15, "LIN", "Aussage", "piano_2.mp3", [
    ("L6_press", 4.0, "Die graue Schnauze sagt dir:\\NDie Zeit läuft", 0),
    ("L6_paint", 2.0, "Halte diesen Moment fest", 0),
    ("L6_frame", 1.9, None, 0),
    ("L6_photo", 2.0, "Seine Pfote. In Gold.", 0),
    ("L6_result", 2.5, "Für immer bei dir.", 0),
    ("L_result", 2.6, "CTA", 1.0)],
   "Die graue Schnauze ist das Schönste und Schwerste zugleich 🤍 Halte seine Pfote fest, solange es geht. Kommentiere PFOTE.",
   "#graueschnauze #seniordog #alterhund #pfotenabdruck #labrador #hundeliebe",
   "emotionaler Klavier-Trend-Sound (piano_2)", "FB + IG Reels, Sonntag 20 Uhr")

ad(2, 8, 12, "TEASE", "Frage", "erinnerung_4.mp3", [
    ("L7_paint", 1.7, "Weißt du noch, wie klein\\Nseine Pfote mal war?", 0),
    ("L7_press", 1.9, "Heute ist sie grau und müde", 0),
    ("L7_frame", 1.9, None, 0),
    ("L_photo", 1.9, "Ich halte sie fest", 0),
    ("L7_result", 3.0, None, 0),
    ("L6_result", 1.6, "CTA", 2.4)],
   "Erst war sie winzig, jetzt ist sie grau. Diese Pfote hat mich durch so viele Jahre begleitet 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#alterhund #seniorhund #hundeleben #pfotenabdruck #hundeliebe #erinnerung",
   "sehr ruhiges Klavier (erinnerung_4)", "IG Reels, Donnerstag 21 Uhr")

ad(2, 9, 10, "REV", "Aussage", "piano_3.mp3", [
    ("L_result", 2.4, "Das hätte ich gern\\Nfrüher gemacht", 0.4),
    ("L_press", 2.6, "Mach es, solange er da ist", 1.2),
    ("L_paint", 1.6, None, 0.3),
    ("L6_result", 3.4, "CTA", 0.5)],
   "Viele sagen danach: Hätte ich das bloß früher gemacht. Mach es, solange er neben dir liegt 🤍 Kommentiere PFOTE.",
   "#alterhund #seniorhund #pfotenabdruck #hundeliebe #nichtwarten",
   "ruhiges Klavier (piano_3)", "TikTok 20 Uhr, IG")

ad(2, 10, 15, "LIN", "POV", "erinnerung_2.mp3", [
    ("G_paint", 2.3, "POV: Du willst seine Pfote\\Nnie vergessen", 0),
    ("G_press", 2.6, None, 0),
    ("G_frame", 2.1, "Ton, Gold, zwei Fotos", 0),
    ("G_photo", 1.7, None, 0),
    ("G_result", 3.2, "Jetzt bleibt sie für immer", 0),
    ("G_result", 3.1, "CTA", 0.1)],
   "Diese Pfote, die immer auf deinem Schoß liegt. Jetzt für immer festgehalten 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#pov #goldenretriever #pfotenabdruck #hundeliebe #zeitfesthalten #dogsoftiktok",
   "sanftes Klavier (erinnerung_2)", "IG + FB Reels, Samstag 19 Uhr")

# ---------------- ANGLE 3: Weihnachtsgeschenk für Hundemenschen ----------------
ad(3, 1, 12, "LIN", "Aussage", "weihnacht_1.mp3", [
    ("G_press", 2.6, "Das perfekte Geschenk für\\NHundemenschen gibt es nicht …", 0),
    ("G_paint", 2.2, "… bis du das hier siehst", 0),
    ("G_frame", 2.0, None, 0),
    ("G_photo", 1.7, None, 0),
    ("G_result", 3.5, "CTA", 0)],
   "Für alle, die bei Hundemenschen jedes Jahr ratlos sind 🎄🐶 Dieses Geschenk bleibt für immer. Kommentiere PFOTE und ich schick dir den Link.",
   "#weihnachtsgeschenk #geschenkidee #hundemenschen #pfotenabdruck #weihnachten #giftideas #hundeliebe",
   "Weihnachts-Spieluhr (weihnacht_1) oder Trend-Weihnachts-Sound", "TikTok + IG, ab 02.11. täglich 19 Uhr")

ad(3, 2, 15, "TEASE", "Frage", "weihnacht_2.mp3", [
    ("F_paint", 2.0, "Noch kein Geschenk für\\Ndeine hundeverrückte Freundin?", 0),
    ("F_press", 3.0, "Ihre Hundepfote in Ton", 1.0),
    ("F_frame", 1.5, None, 0),
    ("F_photo", 2.8, "Gold + zwei Lieblingsfotos", 0),
    ("F_result", 3.0, "Unterm Baum: Tränen garantiert", 0),
    ("F_result", 2.7, "CTA", 0.4)],
   "Für die Freundin, deren Handy nur aus Hundefotos besteht 😅🎄 Kommentiere PFOTE und ich schick dir den Link.",
   "#geschenkfürfreundin #weihnachtsgeschenk #hundemama #frenchie #pfotenabdruck #geschenkidee",
   "Weihnachts-Spieluhr (weihnacht_2)", "IG Reels, Freitag 18 Uhr")

ad(3, 3, 10, "REV", "Ich-Erzählung", "welpe_1.mp3", [
    ("P_result", 2.4, "Mein liebstes Geschenk\\Ndieses Jahr", 1.0),
    ("P_press", 2.6, "Seine winzige Pfote …", 0),
    ("P_paint", 1.5, None, 0),
    ("P_result", 3.5, "CTA", 0)],
   "Das hier liegt dieses Jahr unterm Baum 🎄 Seine kleine Pfote, für immer. Kommentiere PFOTE und ich schick dir den Link.",
   "#welpe #weihnachtsgeschenk #shihtzu #pfotenabdruck #puppy #geschenkidee",
   "verspielter Ukulele-Sound (welpe_1)", "TikTok 18 Uhr, IG Reels")

ad(3, 4, 12, "LIN", "POV", "weihnacht_3.mp3", [
    ("S_press", 3.0, "POV: Du hast das Geschenk,\\Ndas alle zum Weinen bringt", 0),
    ("S_kidpaint", 1.9, "Pfote in Ton,\\Nzusammen ausgemalt", 0),
    ("S_kidframe", 2.0, None, 0),
    ("S_photo", 1.5, None, 0),
    ("S_result", 3.6, "CTA", 0)],
   "Ein Geschenk, das die ganze Familie zusammen macht 🎄🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#weihnachten #familie #staffy #pfotenabdruck #geschenkidee #hundeliebe #christmasgift",
   "Weihnachts-Spieluhr (weihnacht_3)", "IG + FB Reels, Sonntag 16 Uhr (Adventssonntag)")

ad(3, 5, 15, "LIN", "Aussage", "weihnacht_4.mp3", [
    ("L_press", 4.0, "Das Weihnachtsgeschenk\\Nfür Hundemenschen 2026", 0),
    ("L_paint", 2.0, "Ein echter Pfotenabdruck", 0),
    ("L_frame", 1.9, None, 0),
    ("L_photo", 1.9, "In Gold, mit zwei Fotos", 0),
    ("L_result", 3.6, None, 0),
    ("L6_result", 1.6, "CTA", 2.4)],
   "Kein Kram, der in der Schublade landet. Ein Geschenk, das für immer an der Wand hängt 🎄🐾 Kommentiere PFOTE.",
   "#weihnachtsgeschenk2026 #geschenkidee #hundeliebe #pfotenabdruck #labrador #weihnachten",
   "warme Weihnachts-Spieluhr (weihnacht_4)", "FB + IG Reels, Samstag 11 Uhr")

ad(3, 6, 12, "TEASE", "Ich-Erzählung", "reveal_3.mp3", [
    ("G_photo", 1.7, "Ich hab das Geschenk gefunden,\\Ndas sie zum Weinen bringt", 0),
    ("G_press", 2.6, None, 0),
    ("G_paint", 2.2, "Ihr Hund. Seine Pfote. In Gold.", 0),
    ("G_frame", 2.0, None, 0),
    ("G_result", 3.5, "CTA", 0)],
   "Endlich ein Geschenk mit Bedeutung 🥹 Ihr Hund, für immer im Rahmen. Kommentiere PFOTE und ich schick dir den Link.",
   "#geschenkidee #geschenkfürsie #goldenretriever #pfotenabdruck #weihnachtsgeschenk #dogmom",
   "warmer Akustik-Sound (reveal_3)", "IG Reels, Donnerstag 19 Uhr")

ad(3, 7, 10, "LIN", "Frage", "welpe_2.mp3", [
    ("P_press", 2.6, "Erstes Weihnachten\\Nmit deinem Welpen?", 0),
    ("P_paint", 1.5, "Halte diese Pfote fest", 0),
    ("P_frame", 1.9, None, 0),
    ("P_result", 4.0, "CTA", 0)],
   "Das erste Weihnachten mit Welpe gibt es nur einmal 🎄🐶 Halte diese winzige Pfote fest. Kommentiere PFOTE.",
   "#erstesweihnachten #welpe #puppy #pfotenabdruck #shihtzu #weihnachten",
   "verspielter Glockenspiel-Sound (welpe_2)", "TikTok 17–19 Uhr, IG Reels")

ad(3, 8, 15, "REV", "Aussage", "weihnacht_1.mp3", [
    ("F_result", 3.0, "Das einzige Geschenk,\\Ndas niemand umtauscht", 1.2),
    ("F_press", 3.0, "So einfach geht's:\\NPfote in den Ton", 1.0),
    ("F_paint", 2.0, "Gold ausmalen", 0),
    ("F_frame", 1.5, "Einrahmen", 0),
    ("F_photo", 2.6, "Fotos rein", 0.4),
    ("F_result", 2.9, "CTA", 0.2)],
   "Pfote rein, Gold drauf, Fotos dazu – fertig ist das persönlichste Weihnachtsgeschenk 🎄 Kommentiere PFOTE und ich schick dir den Link.",
   "#diy #weihnachtsgeschenk #frenchie #pfotenabdruck #geschenkidee #hundeliebe #giftideas",
   "Weihnachts-Spieluhr (weihnacht_1)", "IG + FB, Sonntag 18 Uhr")

ad(3, 9, 12, "LIN", "POV", "welpe_3.mp3", [
    ("S_kidpaint", 1.9, "POV: Eure Tochter macht\\Ndas Weihnachtsgeschenk", 0),
    ("S_press", 3.0, "Die Pfote vom Familienhund", 0),
    ("S_kidframe", 2.0, None, 0),
    ("S_photo", 1.5, None, 0),
    ("S_result", 3.6, "CTA", 0)],
   "Kleine Künstlerin, großer Hund, ein Geschenk für Oma 🎄🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#familie #kinderundhund #weihnachtsgeschenk #pfotenabdruck #staffy #geschenkidee",
   "verspielter Ukulele-Sound (welpe_3)", "IG + FB Reels, Samstag 15 Uhr")

ad(3, 10, 10, "TEASE", "Aussage", "weihnacht_2.mp3", [
    ("G_paint", 2.2, "Unterm Baum dieses Jahr:", 0.1),
    ("G_frame", 2.0, "seine Pfote. In Gold.", 0),
    ("G_photo", 1.7, None, 0),
    ("G_result", 4.1, "CTA", 0)],
   "Dieses Jahr liegt etwas Besonderes unterm Baum 🎄 Kommentiere PFOTE und ich schick dir den Link 🐾",
   "#unterdembaum #weihnachten #goldenretriever #pfotenabdruck #geschenkidee",
   "Weihnachts-Spieluhr (weihnacht_2)", "TikTok + IG, Adventswochen 19 Uhr")

# ---------------- ANGLE 4: Black Week & Bestellschluss ----------------
# Keine Rabatte/Preise/Countdowns: Dringlichkeit nur über echten Bestellschluss (Datum vor Posting bestätigen!)
ad(4, 1, 12, "LIN", "Aussage", "reveal_2.mp3", [
    ("L_press", 3.0, "Statt Black-Friday-Kram:\\Nein Geschenk, das bleibt", 0),
    ("L_paint", 2.0, "Seine Pfote in Gold", 0),
    ("L_frame", 1.9, None, 0),
    ("L_photo", 1.9, None, 0),
    ("L_result", 3.2, "CTA", 0)],
   "Black Week = 1.000 Dinge, die keiner braucht. Oder ein Geschenk, das für immer bleibt 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#blackfriday #blackweek #geschenkidee #pfotenabdruck #weihnachtsgeschenk #hundeliebe",
   "aufbauender Trend-Sound (reveal_2)", "TikTok + IG, 23.–30.11. täglich 19 Uhr")

ad(4, 2, 10, "TEASE", "Aussage", "weihnacht_3.mp3", [
    ("G_paint", 2.2, "Soll es bis Weihnachten da sein?\\NDann bestell bis 30.11.", 0.1),
    ("G_frame", 2.0, None, 0),
    ("G_photo", 1.7, "Der Pfotenabdruck in Gold", 0),
    ("G_result", 4.1, "CTA", 0)],
   "Wichtig: Damit das Set rechtzeitig vor Weihnachten ankommt, bestell bis zum 30.11. 🎄 Kommentiere PFOTE und ich schick dir den Link.",
   "#weihnachtsgeschenk #bestellschluss #pfotenabdruck #geschenkidee #weihnachten #hundeliebe",
   "Weihnachts-Spieluhr (weihnacht_3)", "IG + TikTok, 20.–30.11.")

ad(4, 3, 15, "REV", "Frage", "weihnacht_4.mp3", [
    ("O_hold", 2.5, "Black Friday ausgegeben,\\Naber Opa noch nichts gekauft?", 0),
    ("O_hug", 2.4, "Das hier bringt ihn\\Nzum Weinen (vor Freude)", 0),
    ("O_paint", 1.8, None, 0),
    ("O_frame", 2.0, "Die Pfote seines Hundes", 0),
    ("O_end", 3.0, "Bis 30.11. bestellen =\\Nvor Weihnachten da", 0),
    ("O_hold", 3.3, "CTA", 0)],
   "Dieses Jahr mal kein Pulli für Opa 😅 Die Pfote seines Hundes, für immer. Bis 30.11. bestellen, damit es vor Weihnachten da ist. Kommentiere PFOTE 🐾",
   "#blackfriday #geschenkfüropa #weihnachtsgeschenk #pfotenabdruck #hundeliebe #bestellschluss",
   "Weihnachts-Spieluhr (weihnacht_4)", "FB + IG Reels, 26.–30.11. 18 Uhr")

ad(4, 4, 12, "LIN", "Ich-Erzählung", "weihnacht_1.mp3", [
    ("F_press", 3.0, "Ich kauf an Black Friday\\Nnur eine Sache:", 1.0),
    ("F_paint", 2.0, "ein Geschenk mit Bedeutung", 0),
    ("F_frame", 1.5, None, 0),
    ("F_photo", 2.2, "Ihre Hundepfote. In Gold.", 0.5),
    ("F_result", 3.3, "CTA", 0.4)],
   "Keine Gadgets, keine Deko. Nur dieses eine Geschenk, das sie nie vergessen wird 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#blackfriday #cybermonday #geschenkidee #frenchie #pfotenabdruck #weihnachtsgeschenk",
   "Weihnachts-Spieluhr (weihnacht_1)", "TikTok, 27.11. + 30.11. 12 Uhr und 19 Uhr")

ad(4, 5, 10, "REV", "Aussage", "welpe_4.mp3", [
    ("P_result", 2.4, "Cyber Monday ist der letzte\\Nsichere Bestelltag vor Weihnachten", 1.0),
    ("P_press", 2.6, None, 0),
    ("P_paint", 1.5, None, 0),
    ("P_result", 3.5, "CTA", 0)],
   "Cyber Monday (30.11.) ist unser letzter sicherer Bestelltag, damit es vor Weihnachten ankommt 🎄 Kommentiere PFOTE und ich schick dir den Link.",
   "#cybermonday #weihnachtsgeschenk #welpe #pfotenabdruck #bestellschluss #geschenkidee",
   "verspielter Sound (welpe_4)", "TikTok + IG, 28.–30.11.")

ad(4, 6, 15, "LIN", "POV", "reveal_3.mp3", [
    ("S_press", 3.0, "POV: Du bist dieses Jahr\\Nnicht der Last-Minute-Typ", 0),
    ("S_kidpaint", 1.9, "Pfote in Ton gedrückt", 0),
    ("S_kidframe", 2.0, "Gold ausgemalt", 0),
    ("S_photo", 1.5, None, 0),
    ("S_press", 3.0, "Bis 30.11. bestellt =\\Nentspannt unterm Baum", 0),
    ("S_result", 3.6, "CTA", 0)],
   "Dieses Jahr mal entspannt: bis 30.11. bestellen, dann liegt es pünktlich unterm Baum 🎄🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#weihnachtsgeschenk #lastminute #familie #pfotenabdruck #staffy #geschenkidee",
   "aufbauender Akustik-Sound (reveal_3)", "IG + FB Reels, 22.–29.11.")

ad(4, 7, 12, "TEASE", "Frage", "weihnacht_2.mp3", [
    ("L7_paint", 1.7, "Was bleibt von deinen\\NBlack-Friday-Käufen?", 0),
    ("L7_press", 1.9, "Das hier bleibt für immer", 0),
    ("L7_frame", 1.9, None, 0),
    ("L7_oma", 2.6, None, 0),
    ("L7_result", 3.9, "CTA", 0)],
   "Die meisten Black-Friday-Käufe sind im Januar vergessen. Diese Pfote nicht 🤍 Kommentiere PFOTE und ich schick dir den Link.",
   "#blackfriday #nachhaltig #geschenkidee #pfotenabdruck #oma #weihnachtsgeschenk",
   "Weihnachts-Spieluhr (weihnacht_2)", "IG + FB Reels, 24.–29.11. 19 Uhr")

ad(4, 8, 10, "LIN", "Aussage", "weihnacht_4.mp3", [
    ("L6_press", 3.0, "Nikolaus? Bestell bis 15.11.\\NWeihnachten? Bis 30.11.", 0),
    ("L6_paint", 2.0, None, 0),
    ("L6_photo", 2.0, "Seine Pfote, für immer", 0),
    ("L6_result", 3.0, "CTA", 0.5)],
   "Damit es rechtzeitig ankommt: Nikolaus bis 15.11., Weihnachten bis 30.11. bestellen 🎄 Kommentiere PFOTE und ich schick dir den Link.",
   "#nikolaus #weihnachtsgeschenk #bestellschluss #pfotenabdruck #hundeliebe #labrador",
   "Weihnachts-Spieluhr (weihnacht_4)", "IG + TikTok, 05.–15.11. und 20.–30.11.")

ad(4, 9, 15, "REV", "Ich-Erzählung", "reveal_1.mp3", [
    ("G_result", 2.8, "Mein einziger Black-Week-Kauf,\\Nden ich nicht bereue", 0.3),
    ("G_press", 2.6, "Seine Pfote in Ton", 0),
    ("G_paint", 2.3, "In Gold ausgemalt", 0),
    ("G_frame", 2.1, None, 0),
    ("G_photo", 1.7, "Zwei Fotos dazu", 0),
    ("G_result", 3.5, "CTA", 0.1)],
   "Von allem, was ich in der Black Week gekauft habe, ist das das Einzige, das bleibt 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#blackweek #blackfriday #goldenretriever #pfotenabdruck #geschenkidee #hundeliebe",
   "aufbauender Akustik-Sound (reveal_1)", "TikTok + IG, 27.11.–01.12.")

ad(4, 10, 12, "LIN", "Frage", "piano_4.mp3", [
    ("F_paint", 2.0, "Noch 6 Wochen bis Weihnachten.\\NSchon ein Geschenk?", 0),
    ("F_press", 3.0, "Seine Pfote in Ton", 1.0),
    ("F_frame", 1.5, None, 0),
    ("F_photo", 2.2, "In Gold, mit Fotos", 0.5),
    ("F_result", 3.3, "CTA", 0.4)],
   "Wer früh dran ist, schenkt entspannter 🎄 Die Pfote ihres Hundes, für immer im Rahmen. Kommentiere PFOTE und ich schick dir den Link.",
   "#weihnachtsgeschenk #geschenkidee #frenchie #pfotenabdruck #vorweihnachtszeit #hundeliebe",
   "ruhiges Klavier (piano_4)", "IG + TikTok, 09.–15.11.")

# ---------------- ANGLE 5: Kleine Pfote, große Erinnerung ----------------
ad(5, 1, 12, "LIN", "Aussage", "welpe_1.mp3", [
    ("P_press", 2.7, "So klein wird seine Pfote\\Nnie wieder sein", 0),
    ("P_paint", 1.5, None, 0),
    ("P_frame", 2.0, "Für immer festgehalten", 0),
    ("P_photo", 1.6, None, 0),
    ("P_result", 4.2, "CTA", 0)],
   "Welpen wachsen so schnell. Halte diese winzige Pfote fest, solange sie so klein ist 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#welpe #puppy #shihtzu #pfotenabdruck #welpenliebe #erinnerung #puppylove",
   "verspielter Ukulele-Sound (welpe_1)", "TikTok + IG, Dienstag 18 Uhr")

ad(5, 2, 15, "REV", "Ich-Erzählung", "erinnerung_1.mp3", [
    ("L7_result", 2.8, "Ich wollte eine Erinnerung,\\Ndie man anfassen kann", 0),
    ("L7_press", 1.9, None, 0),
    ("L7_paint", 1.7, "Nicht nur ein Foto im Handy", 0),
    ("L7_frame", 1.9, None, 0),
    ("L_photo", 1.9, "Seine echte Pfote", 0),
    ("L6_result", 4.8, "CTA", 0)],
   "Fotos verschwinden im Handy. Diese Pfote hängt für immer an der Wand 🤍 Kommentiere PFOTE und ich schick dir den Link.",
   "#erinnerung #hundeliebe #pfotenabdruck #labrador #fürimmer #seniordog",
   "sanftes Ambient-Klavier (erinnerung_1)", "IG + FB Reels, Sonntag 20 Uhr")

ad(5, 3, 10, "LIN", "POV", "welpe_2.mp3", [
    ("S_press", 3.0, "POV: Hund und Kind\\Nwachsen zusammen auf", 0),
    ("S_kidpaint", 1.9, None, 0),
    ("S_kidframe", 2.0, "Diesen Moment gibt's nur einmal", 0),
    ("S_result", 3.1, "CTA", 0)],
   "Sie wachsen so schnell – das Kind und der Hund 🥹 Diesen Moment gibt's nur einmal. Kommentiere PFOTE und ich schick dir den Link.",
   "#kinderundhunde #familie #staffy #pfotenabdruck #erinnerung #momlife",
   "verspielter Glockenspiel-Sound (welpe_2)", "IG + FB Reels, Samstag 10 Uhr")

ad(5, 4, 15, "TEASE", "Frage", "erinnerung_3.mp3", [
    ("G_paint", 2.3, "Was bleibt dir von ihm,\\Nwenn er irgendwann geht?", 0),
    ("G_press", 2.6, "Seine Pfote. Für immer.", 0),
    ("G_frame", 2.1, None, 0),
    ("G_photo", 1.7, "Mit seinen schönsten Fotos", 0),
    ("G_result", 3.2, "Eine Erinnerung,\\Ndie warm macht", 0),
    ("G_result", 3.1, "CTA", 0.1)],
   "Irgendwann ist die Zeit vorbei. Dann bleibt diese Pfote – und ganz viel Liebe 🤍🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#erinnerung #hundeliebe #goldenretriever #pfotenabdruck #fürimmer #regenbogenbrücke",
   "sanftes Klavier + Cello (erinnerung_3)", "IG + FB Reels, Sonntag 21 Uhr")

ad(5, 5, 12, "REV", "Aussage", "welpe_3.mp3", [
    ("P_result", 2.4, "Seine erste Pfote,\\Nfür immer", 1.0),
    ("P_press", 2.7, None, 0),
    ("P_paint", 1.5, "Vier kleine Abdrücke in Gold", 0),
    ("P_frame", 2.0, None, 0),
    ("P_result", 3.4, "CTA", 0)],
   "Seine erste Pfote. Irgendwann wirst du sie vermissen, diese Winzlings-Zeit 🥹 Kommentiere PFOTE und ich schick dir den Link.",
   "#welpe #ersterpfotenabdruck #puppy #pfotenabdruck #welpenzeit #erinnerung",
   "verspielter Sound (welpe_3)", "TikTok 18 Uhr, IG Reels")

ad(5, 6, 10, "TEASE", "Aussage", "erinnerung_2.mp3", [
    ("L_paint", 2.0, "Für alle, die ihren\\NSeelenhund nie vergessen wollen", 0),
    ("L_frame", 1.9, None, 0),
    ("L_photo", 1.9, "Seine Pfote. In Gold.", 0),
    ("L_result", 4.2, "CTA", 0)],
   "Für alle mit einem Seelenhund 🤍 Diese Pfote bleibt. Kommentiere PFOTE und ich schick dir den Link.",
   "#seelenhund #hundeliebe #pfotenabdruck #erinnerung #labrador #fürimmer",
   "sanftes Klavier (erinnerung_2)", "IG Reels, Mittwoch 21 Uhr")

ad(5, 7, 12, "LIN", "Ich-Erzählung", "welpe_4.mp3", [
    ("S_kidframe", 2.0, "Meine Tochter und ihr\\Nbester Freund", 0),
    ("S_press", 3.0, "Seine Pfote in Ton", 0),
    ("S_kidpaint", 1.9, "Sie hat sie selbst angemalt", 0),
    ("S_photo", 1.5, None, 0),
    ("S_result", 3.6, "CTA", 0)],
   "Ihr bester Freund hat vier Pfoten 🥹 Ein Andenken, das sie ihr Leben lang behält. Kommentiere PFOTE und ich schick dir den Link.",
   "#kinderundhunde #bestefreunde #staffy #pfotenabdruck #familie #erinnerung",
   "verspielter Sound (welpe_4)", "FB + IG Reels, Sonntag 11 Uhr")

ad(5, 8, 15, "LIN", "POV", "erinnerung_4.mp3", [
    ("L6_press", 4.0, "POV: Du willst nie vergessen,\\Nwie sich seine Pfote anfühlt", 0),
    ("L6_paint", 2.0, None, 0),
    ("L6_frame", 1.9, "Ein echter Abdruck, keine Kopie", 0),
    ("L6_photo", 2.0, None, 0),
    ("L6_result", 2.5, "Für immer bei dir", 0),
    ("L_result", 2.6, "CTA", 1.0)],
   "Wie sich seine Pfote in deiner Hand anfühlt – das willst du nie vergessen 🤍 Kommentiere PFOTE und ich schick dir den Link.",
   "#pov #erinnerung #seniorhund #pfotenabdruck #hundeliebe #fürimmer",
   "sehr ruhiges Klavier (erinnerung_4)", "IG + FB Reels, Samstag 21 Uhr")

ad(5, 9, 10, "REV", "Frage", "welpe_1.mp3", [
    ("F_result", 2.4, "Hast du seine Pfote schon\\Nfür immer festgehalten?", 1.2),
    ("F_press", 2.6, None, 1.2),
    ("F_paint", 1.8, "Gold ausgemalt", 0),
    ("F_photo", 3.2, "CTA", 0.2)],
   "Du denkst, du hast noch so viel Zeit. Halte sie trotzdem jetzt schon fest 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#frenchie #französischebulldogge #pfotenabdruck #hundeliebe #erinnerung",
   "lockerer Ukulele-Sound (welpe_1)", "TikTok 19 Uhr, IG Reels")

ad(5, 10, 12, "TEASE", "Aussage", "erinnerung_1.mp3", [
    ("G_photo", 1.7, "Ein Abdruck, ein Leben lang", 0),
    ("G_press", 2.6, "Gestern noch ein Welpe,\\Nheute mein bester Freund", 0),
    ("G_paint", 2.2, None, 0),
    ("G_frame", 2.0, "Jetzt für immer an der Wand", 0),
    ("G_result", 3.5, "CTA", 0)],
   "Gestern noch ein Welpe, heute mein bester Freund. Diese Pfote erzählt unsere ganze Geschichte 🐾 Kommentiere PFOTE und ich schick dir den Link.",
   "#goldenretriever #besterfreund #pfotenabdruck #erinnerung #hundeliebe #dogsofinstagram",
   "sanftes Klavier (erinnerung_1)", "IG + FB Reels, Freitag 19 Uhr")
