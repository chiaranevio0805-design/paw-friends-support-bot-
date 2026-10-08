# Transkripte – DE-Personas: Gesund Leben Journal + Thomas Brandt (Lane `persona_de_journal_brandt`)

Stand 08.10.2026. Alle Video-Ads dieser Lane stammen von **Gesund Leben Journal** (Thomas Brandt hat nur Bild-Ads). 292 Video-Ads in 181 Video-Clustern, fast alle Long-Form (5–8 min; Ausnahmen: K05-189/190/191 ≈ 80 s, K23 ≈ 105 s).

**Quellen:** (1) GetHooked-Whisper-Transkripte (`transcribe_ads` für alle 292 Video-IDs angestoßen, Ergebnisse per `get_transcription_status` abgeholt), Segmente mit Zeitstempeln wörtlich übernommen (ASR-Fehler wie „HMO-Arzt“ statt „HNO-Arzt“ nicht korrigiert). (2) Wo GetHooked kein brauchbares Transkript lieferte: lokale Transkription mit faster-whisper „small“ (CPU), entsprechend markiert.

**ASR-Hinweis:** Whisper-Transkripte enthalten typische Fehler (z. B. „HMO-Arzt“ = HNO-Arzt, „Ruheraum“ = Hohlraum) und gelegentlich halluzinierte Abspann-Zeilen wie „Untertitel von Stephanie Geiges“ am Videoende – diese stehen nicht im Video. Alles wurde unverändert übernommen.

**Deduplizierung (damit die Datei lesbar bleibt, ohne Inhalt zu verlieren):** Viele Cluster nutzen denselben Video-Body mit anderem Hook. Je Konzept wurden die Volltranskripte per Wortabgleich zu **Body-Varianten** gruppiert (≥ 60 % Wortübereinstimmung). Jede Body-Variante steht unten einmal vollständig mit [mm:ss]-Segmenten. Je Cluster folgen: eingeblendeter Hook-Text, der **wörtliche Hook-/Abweichungsteil** mit Zeitstempeln bis zu dem Punkt, ab dem das Video wortgleich in die Body-Variante übergeht, sowie alle weiteren abweichenden Stellen (zusammenhängende Abweichungen ≥ 12 Wörter) wörtlich. Damit ist jedes Transkript vollständig rekonstruierbar.

## Übersicht Body-Varianten

| Body-Variante | Referenz-Cluster (Ad, Länge) | Cluster in dieser Variante | Einstieg (erste Sätze der Referenz) |
|---|---|---|---|
| K01-B1 | K01-001 (Ad 96489719, 352 s) | K01-001, K01-012, K01-013, K01-014, K01-015, K01-016, K01-017, K01-025, K01-026, K01-027, K01-028, K01-029, K01-061, K01-062 (14) | Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken oder Herzrasen? Was das wirklich bedeutet, erfährst du hier. |
| K01-B2 | K01-002 (Ad 100373716, 383 s) | K01-002, K01-003, K01-018, K01-019, K01-020, K01-021, K01-022, K01-023, K01-024, K01-034, K01-035, K01-036, K01-037, K01-038, K01-039, K01-040, K01-041, K01-048, K01-049, K01-060, K01-063, K01-064, K01-065, K01-066, K01-067, K01-068, K01-073, K01-074, K01-075, K01-076, K01-077, K01-078, K01-080, K01-081, K01-082, K01-088, K01-089, K01-090 (38) | Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen verursacht. Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist. |
| K01-B3 | K01-030 (Ad 98148692, 353 s) | K01-030, K01-031, K01-032, K01-033, K01-042, K01-043, K01-044, K01-045, K01-046, K01-047 (10) | Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und dir jeder Arzt sagt, alles ist völlig normal, dann schau das bitte bis zum Ende. Denn ich habe 18 Monate meines Lebens verloren  |
| K02-B1 | K02-091 (Ad 107108716, 311 s) | K02-091, K02-092, K02-095, K02-096, K02-097, K02-098, K02-099, K02-106, K02-107, K02-108 (10) | Das ist die schlechteste Schlafposition und wie du stattdessen schlafen solltest. Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule und klemmst dabei deinen Ischiasnerv ab. |
| K02-B2 | K02-109 (Ad 104077018, 318 s) | K02-109, K02-110, K02-111, K02-112, K02-113, K02-114, K02-115, K02-116, K02-118, K02-119 (10) | Wenn du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte Schäden in deiner Wirbelsäule. Sehe das jeden Tag. Menschen wachen mit stärkeren Schmerzen auf, mehr Steifheit im unteren Rücken, mehr Taubh |
| K05-B1 | K05-187 (Ad 74485763, 466 s) | K05-187, K05-188 (2) | So hört Schnarchen sofort auf. So sieht dein verengter Atemweg aus, wenn du schnarchst. Die meisten Leute denken nämlich, Schnarchen wäre einfach nur lautes Atmen. Aber das ist leider völlig falsch. Hier ist was wirklich |
| K05-B2 | K05-189 (Ad 90347406, 80 s) | K05-189, K05-190, K05-191 (3) | Wir haben einen Schlafapnoe-Patienten gebeten, sieben Tage lang mit dem Nacken-Therapie-Kissen zu schlafen. Und das ist passiert. In der ersten Nacht reagiert sein Körper auf eine Weise, wie es keine Maschine jemals scha |
| K09-B1 | K09-238 (Ad 74485768, 401 s) | K09-238 (1) | Das ist die schlechteste Schlafposition. Und wie du stattdessen schlafen solltest. Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ischias Schmerzen zu lindern, oder? Falsch. |
| K11-B1 | K11-247 (Ad 92876643, 341 s) | K11-247, K11-248, K11-249, K11-250, K11-251, K11-252, K11-253, K11-254, K11-255, K11-256 (10) | Das ist die schlechteste Schlafposition bei Nackenschmerzen und wie du stattdessen schlafen solltest. Was diese zwei MRT-Bilder aus Österreich aufgedeckt haben, hat alles verändert, was wir über Nackenschmerzen glaubten. |
| K15-B1 | K15-284 (Ad 184804208, 422 s) | K15-284 (1) | Mitten in der Präsentation blieb mein Kopf einfach leer Kein Wort kam raus für 10 Gesichter starten mich an Ich dachte wirklich, das ist der Anfang von dem Mensch |
| K16-B1 | K16-291 (Ad 181171395, 377 s) | K16-291 (1) | Wenn du morgens mit Schwinden laufst Deine arme Krippeln sobald du den Kopf drehst Und dir jeder Arzt sagt, alles ist völlig normal Dann schaue dir das unbedingt an Denn ich habe 18 Monate um ins Lebens verloren Und die  |
| K17-B1 | K17-296 (Ad 184804213, 436 s) | K17-296 (1) | Ich war 54, als ich mir einen Termin beim Neurologen ausmachte Ich dachte wirklich, ich würde dem entwerden Mit einem Satz fielen mir keine Wörter mehr ein |
| K22-B1 | K22-322 (Ad 91377966, 372 s) | K22-322, K22-323, K22-324, K22-325 (4) | Warum Seitenschläfer mit Migräne oder ständigen Kopfschmerzen jetzt zu diesen neuartigen Kissen wechseln? Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule. Falls du morgens also mit  |
| K23-B1 | K23-326 (Ad 89547484, 106 s) | K23-326 (1) | Das hier ist Jürgen und er leidet seit fünf Jahren an morgendlichen Nacken- und Schulterschmerzen. Hallo! Ich bin dein herkömmliches Kissen und ich bin der Grund, warum du jeden Morgen mit Nackenschmerzen aufwachst. Ich  |
| K23-B2 | K23-327 (Ad 90347400, 110 s) | K23-327, K23-328 (2) | Wenn du als Seitenschläfer jeden Morgen mit brennenden Nackenschmerzen aufwachst, solltest du dir Jürgens Geschichte ansehen. Das hier ist Jürgen. |
| K25-B1 | K25-332 (Ad 110088145, 399 s) | K25-332, K25-333, K25-334 (3) | Das ist die schlechteste Schlafposition und warum sie Taubheitsgefühle von der Schulter bis in die Fingerspitzen verursacht. Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Halswirbelsäule |

Cluster ohne Volltranskript (nur Hook-Teil lokal oder gar nichts): K01-004, K01-005, K01-006, K01-007, K01-008, K01-009, K01-010, K01-011, K01-050, K01-051, K01-052, K01-053, K01-054, K01-055, K01-056, K01-057, K01-058, K01-059, K01-069, K01-070, K01-071, K01-072, K01-079, K01-083, K01-084, K01-085, K01-086, K01-087, K02-093, K02-094, K02-100, K02-101, K02-102, K02-103, K02-104, K02-105, K02-117, K02-120, K02-121, K02-122, K02-123, K02-124, K02-125, K02-126, K02-127, K02-128, K15-285, K15-286, K15-287, K15-288, K15-289, K15-290, K16-292, K16-293, K16-294, K16-295, K17-297, K17-298, K17-299, K17-300, K17-301, K18-302, K18-303, K18-304, K18-305, K18-306, K24-329, K24-330, K24-331, K27-336

## Hook-Vergleich je Konzept (eingeblendet + gesprochen, erste ~3 s)

| Cluster | Body-Variante | Einordnung | Varianten | max. Tage | eingeblendeter Hook-Text (Startframe) | gesprochen (erste ~3 s) |
|---|---|---|---|---|---|---|
| K01-001 | K01-B1 | Winner | 5 | 119 | PLÖTZLICHER SCHWINDEL, OHRGERÄUSCHE → KOPFSCHMERZEN BIS HIN ZU MIGRÄNE → UND MANCHMAL SOGAR PANIKATTACKEN ODER HERZRASEN? (Hook-Balken wechselt synchron zum Voiceover, 0–5 s) | Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken |
| K01-002 | K01-B2 | Winner | 25 | 116 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION → UND WARUM SIE SCHWINDEL, … (0–3 s); danach Einblendung „ANTIDEPRESSIVA“ (rot, ~10 s) | Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen |
| K01-003 | K01-B2 | Winner | 7 | 106 | MORGENS SCHWINDELATTACKEN | Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen. |
| K01-004 | – | Winner | 6 | 38 | DER FEHLER NR. 1, WARUM DEIN MORGENDLICHER SCHWINDEL | Der Fehler Nummer eins, warum dein morgenlicher Schwindel einfach nicht verschwindet. |
| K01-005 | – | Winner | 3 | 38 | ARZT ERKLÄRT IN NUR 15 SEKUNDEN, WARUM MORGENDLICHER SCHWINDEL | Arzt erklärt in nur 15 Sekunden, warum morgendlicher Schwindel immer wieder kommt. |
| K01-006 | – | Winner | 1 | 38 | MORGENDLICHER SCHWINDEL, DER TROTZ ALLER UNTERSUCHUNGEN | Morgenglicher Schwindel, der trotz aller Untersuchungen nicht weggeht, hat selten etwas mit deinem Innenort zu tun. |
| K01-007 | – | Winner | 1 | 38 | DIE MEISTEN ÄRZTE ÜBERSEHEN DAS VÖLLIG | Die meisten Ärzte übersehen das völlig, wenn Menschen ab 40 morgens mit Schwindel und |
| K01-008 | – | Winner | 1 | 38 | ARZT ERKLÄRT: DESHALB GEHT DEIN MORGENDLICHER SCHWINDEL | Arzt erklärt, deshalb geht dein morgendlicher Schwindel einfach nicht weg. Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist. |
| K01-009 | – | Winner | 1 | 38 | DER GRÖSSTE FEHLER BEI MORGENDLICHEN SCHWINDEL IST ZU DENKEN, | Der größte Fehler beim morgendlichen Schwindel ist zu denken, es sei ein Problem mit den Ohren. |
| K01-010 | – | Winner | 1 | 38 | DEIN MORGENDLICHER SCHWINDEL KOMMT NICHT VOM INNENOHR | Dein morglicher Schwindel kommt nicht vom Innenohr. Er kommt von chronisch verspannten Muskeln tief in deinem Nacken, die auf C1 und C2 drücken. |
| K01-011 | – | Winner | 1 | 37 | WENN DU SO SCHLÄFST, DRÜCKST DU JEDE NACHT AUF DIE NERVEN BEI C1 UND C2 | Wenn du so schläft, drückst du jede Nacht auf die Nerven bei C1 und C2, die die wahre Ursache für Schwindel, Benommenheit und Herzrasen. |
| K01-012 | K01-B1 | Kandidat | 1 | 33 | MORGENS SCHWINDELATTACKEN? | Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand? Was das wirklich bedeutet, erfährst du hier. |
| K01-013 | K01-B1 | Kandidat | 1 | 33 | WAS HABEN VERSPANNUNGEN IM NACKEN | Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam? Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich |
| K01-014 | K01-B1 | Kandidat | 1 | 33 | PLÖTZLICHER SCHWINDEL, OHRGERÄUSCHE | Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken |
| K01-015 | K01-B1 | Kandidat | 1 | 33 | MORGENS SCHWINDELATTACKEN? | Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand? Was das wirklich bedeutet, erfährst du hier. |
| K01-016 | K01-B1 | Kandidat | 1 | 33 | SCHWINDEL HAT NICHTS MIT DEINEM KREISLAUF ODER GLEICHGEWICHT ZU TUN | Schwindel hat nichts mit deinem Kreislauf oder Gleichgewicht zu tun, hier ist der verstörende |
| K01-017 | K01-B1 | Kandidat | 1 | 33 | SCHWINDEL HAT NICHTS MIT DEINEM KREISLAUF ODER GLEICHGEWICHT ZU TUN | Schwindel hat nichts mit deinem Kreislauf oder Gleichgewicht zu tun, hier ist der verstörende |
| K01-018 | K01-B2 | Kandidat | 2 | 26 | MORGENS SCHWINDELATTACKEN | Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand, was das wirklich bedeutet, |
| K01-019 | K01-B2 | Kandidat | 1 | 26 | SCHWINDEL HAT NICHTS MIT DEINEM | Schwindel hat nichts mit deinem Kreislauf oder Gleichgewicht zu tun. Hier ist der verstörende Grund. |
| K01-020 | K01-B2 | Kandidat | 1 | 21 | PLÖTZLICHER SCHWINDEL, | Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken |
| K01-021 | K01-B2 | Kandidat | 1 | 21 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen |
| K01-022 | K01-B2 | Kandidat | 1 | 21 | WENN DU SO SCHLÄFST, | Wenn du so schläfst, schneidest du langsam die Blutzufuhr zu deinem Gehirn ab. |
| K01-023 | K01-B2 | Kandidat | 1 | 21 | PLÖTZLICHER SCHWINDEL, | Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken |
| K01-024 | K01-B2 | Kandidat | 1 | 21 | WENN DU SO SCHLÄFST, | Wenn du so schläfst, drückst du 8 Stunden lang auf deinen Vargusnerv. |
| K01-025 | K01-B1 | Kandidat | 1 | 18 | DER SCHWINDEL HÖRT EINFACH NICHT AUF? | Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen. Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich |
| K01-026 | K01-B1 | Kandidat | 1 | 18 | WENN DU MORGENS MIT SCHWINDEL AUFWACHST DEINE ARME KRIBBELN | Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und |
| K01-027 | K01-B1 | Kandidat | 1 | 18 | WENN DU MORGENS MIT SCHWINDEL AUFWACHST DEINE ARME KRIBBELN | Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und |
| K01-028 | K01-B1 | Kandidat | 1 | 18 | DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN? | Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu |
| K01-029 | K01-B1 | Kandidat | 1 | 18 | DER SCHWINDEL HÖRT EINFACH NICHT AUF? | Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen. Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich |
| K01-030 | K01-B3 | Kandidat | 1 | 18 | WENN DU MORGENS MIT SCHWINDEL AUFWACHST, | Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und dir jeder Arzt sagt, alles ist völlig normal, dann schau das bitte bis zum Ende. |
| K01-031 | K01-B3 | Kandidat | 1 | 18 | DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN? | Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper, dir etwas zu sagen, das du bisher ignoriert hast. |
| K01-032 | K01-B3 | Kandidat | 1 | 18 | WAS HABEN VERSPANNUNGEN IM NACKEN, SCHWINDEL UND MÜDIGKEIT GEMEINSAM? | Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam? |
| K01-033 | K01-B3 | Kandidat | 1 | 18 | MORGENS SCHWINDELATTACKEN | Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand? Was das wirklich bedeutet, erfährst du hier. |
| K01-034 | K01-B2 | Kandidat | 1 | 15 | DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN? | Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu |
| K01-035 | K01-B2 | Kandidat | 1 | 15 | WENN DU MORGENS MIT SCHWINDEL AUFWACHST, | Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und |
| K01-036 | K01-B2 | Kandidat | 1 | 15 | WENN DU MORGENS MIT SCHWINDEL AUFWACHST, | Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und |
| K01-037 | K01-B2 | Kandidat | 1 | 14 | DER SCHWINDEL HÖRT EINFACH NICHT AUF? | Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen. |
| K01-038 | K01-B2 | Verlierer | 1 | 13 | WENN DU SO SCHLÄFST, | Wenn du so schläfst, drückst du 8 Stunden lang auf deinen Vargusnerv. |
| K01-039 | K01-B2 | Verlierer | 1 | 11 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen |
| K01-040 | K01-B2 | Verlierer | 1 | 11 | PLÖTZLICHER SCHWINDEL, | Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken |
| K01-041 | K01-B2 | Verlierer | 1 | 11 | WENN DU MORGENS MIT SCHWINDEL AUFWACHST, | Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und |
| K01-042 | K01-B3 | Verlierer | 1 | 10 | PLÖTZLICHER SCHWINDEL, OHRGERÄUSCHE, KOPFSCHMERZEN BIS HIN ZU MIGRÄNE | Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken oder Herzrasen? |
| K01-043 | K01-B3 | Verlierer | 1 | 10 | WAS HABEN VERSPANNUNGEN IM NACKEN, SCHWINDEL UND MÜDIGKEIT GEMEINSAM? | Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam? |
| K01-044 | K01-B3 | Verlierer | 1 | 10 | WENN DU MORGENS MIT SCHWINDEL AUFWACHST, | Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und dir jeder Arzt sagt, alles ist völlig normal, dann schau das bitte bis zum Ende. |
| K01-045 | K01-B3 | Verlierer | 1 | 10 | DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN? | Der Boden fühlt sich beim Aufstehen wackelig an. Dann versucht dein Körper, dir etwas zu sagen, |
| K01-046 | K01-B3 | Verlierer | 1 | 10 | MORGENS SCHWINDELATTACKEN | Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand? Was das wirklich bedeutet, erfährst du hier. |
| K01-047 | K01-B3 | Verlierer | 1 | 10 | PLÖTZLICHER SCHWINDEL, OHRGERÄUSCHE, KOPFSCHMERZEN BIS HIN ZU MIGRÄNE | Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken oder Herzrasen? |
| K01-048 | K01-B2 | Verlierer | 1 | 10 | MORGENS SCHWINDELATTACKEN | Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand, was das wirklich bedeutet, |
| K01-049 | K01-B2 | Verlierer | 1 | 10 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen |
| K01-050 | – | Verlierer | 1 | 6 | WARNUNG: DAS IST DIE GEFÄHRLICHSTE SCHLAFPOSITION | Warnung, das ist die gefährlichste Schlafposition und warum sie Schwindel, |
| K01-051 | – | Verlierer | 1 | 6 | (erstes Bild schwarz – Hook-Text siehe Frame 1–3 s) | Warum Schwindele immer wieder kommt, Obwohl alle Tests unauffällig sind |
| K01-052 | – | Verlierer | 1 | 6 | DAS IST DER SCHNELLSTE WEG, UM MORGENDLICHEN SCHWINDEL | Das ist der schnellste Weg, um morgendlichen Schwindel von zu Hause aus loszuwerden. |
| K01-053 | – | Verlierer | 1 | 6 | MORGENDLICHER SCHWINDEL IST MEIST KEIN INNENOHR-PROBLEM, | Morgendlicher Schwindel ist meist kein Innenohrproblem, es ist ein Nackenproblem. |
| K01-054 | – | Verlierer | 1 | 6 | (kein Text im Startframe) | Wenn du morgens mit Schwinden laufst Deine arme Kribbeln sobald du den Kopf drehst |
| K01-055 | – | Verlierer | 1 | 6 | WENN DU UNTER SCHWINDEL, HERZRASEN UND BENOMMENHEIT LEIDEST, | Wenn du unter Schwindel, Herzrasen und Benommenheit leidest, hat dir dein Arzt wahrscheinlich nie erklärt, warum all diese Symptome zusammen auftreten. |
| K01-056 | – | Verlierer | 1 | 6 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition. Und warum sie Schwindel, Benommenheit und Herzrasen verursacht. |
| K01-057 | – | Verlierer | 1 | 6 | DER GRÖSSTE FEHLER BEI SCHWINDEL UND BENOMMENHEIT | Der größte Fehler bei Schwindel und Benommenheit ist zu denken, es sei ein Innenohrproblem. |
| K01-058 | – | Verlierer | 1 | 6 | MEIN NEUROLOGE | Mein Neurologe meinte, es sei Stress, mein Kardiologe meinte, es sei in die Nerven, mein Hanoarzt meinte |
| K01-059 | – | Verlierer | 1 | 5 | und wache morgens erholt auf. | Morgendlicher Schwindel, der trotz Behandlung nicht verschwindet, ist kein Innenohrproblem. |
| K01-060 | K01-B2 | Verlierer | 2 | 4 | ARZT ERKLÄRT IN NUR 15 SEKUNDEN | Arzt erklärt in nur 15 Sekunden, warum morgendlicher Schwindel immer wiederkommt. |
| K01-061 | K01-B1 | Verlierer | 1 | 4 | WAS HABEN VERSPANNUNGEN IM NACKEN | Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam? Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich |
| K01-062 | K01-B1 | Verlierer | 1 | 4 | DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN? | Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu |
| K01-063 | K01-B2 | Verlierer | 1 | 4 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen |
| K01-064 | K01-B2 | Verlierer | 1 | 4 | DER SCHWINDEL HÖRT EINFACH NICHT AUF? | Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen. |
| K01-065 | K01-B2 | Verlierer | 1 | 4 | MORGENS SCHWINDELATTACKEN | Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand, was das wirklich bedeutet, |
| K01-066 | K01-B2 | Verlierer | 1 | 4 | DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN? | Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu |
| K01-067 | K01-B2 | Verlierer | 1 | 4 | DER SCHWINDEL HÖRT EINFACH NICHT AUF? | Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen. |
| K01-068 | K01-B2 | Verlierer | 1 | 4 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen |
| K01-069 | – | Verlierer | 1 | 4 | DIE MEISTEN ÄRZTE ÜBERSEHEN DAS VÖLLIG | Die meisten Ärzte übersehen das völlig, wenn Menschen ab 50 morgens mit Schwindel, |
| K01-070 | – | Verlierer | 1 | 4 | DER FEHLER NR. 1, WARUM DEIN MORGENDLICHER SCHWINDEL | Der Fehler Nummer eins, warum dein Morgen dich erschwindel, einfach nicht verschwindelt. |
| K01-071 | – | Verlierer | 1 | 4 | WENN DU SO SCHLÄFST, DRÜCKST DU JEDE NACHT AUF DIE NERVEN BEI C1 UND C2 | Wenn du so schläft, drückst du jede Nacht auf die Nerven bei C1 und C2, die die wahre Ursache für Schwindel, Benommenheit und Herzrasen. |
| K01-072 | – | Verlierer | 1 | 4 | (Untertitel) in einer neutralen Position bleibt | Hier ist, warum dein morgenlicher Schwindel einfach nicht verschwindet. |
| K01-073 | K01-B2 | Verlierer | 1 | 3 | WARUM SEITENSCHLÄFER MIT RÄTSELHAFTEN SCHWINDELATTACKEN | Warum Seitenschläfer mit rätselhaften Schwindelattacken jetzt zu diesen 3-Zonen-Therapiekissen wechseln? |
| K01-074 | K01-B2 | Verlierer | 1 | 3 | ARZT ERKLÄRT IN NUR 15 SEKUNDEN | Arzt erklärt in nur 15 Sekunden, warum morgendlicher Schwindel immer wieder kommt. |
| K01-075 | K01-B2 | Verlierer | 1 | 3 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen verursacht. |
| K01-076 | K01-B2 | Verlierer | 1 | 3 | ARZT ERKLÄRT IN NUR 15 SEKUNDEN | Arzt erklärt nur 15 Sekunden, warum morgendlicher Schwindel immer wieder kommt. |
| K01-077 | K01-B2 | Verlierer | 1 | 3 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen |
| K01-078 | K01-B2 | Verlierer | 1 | 3 | WARUM SEITENSCHLÄFER MIT RÄTSELHAFTEN SCHWINDELATTACKEN | Warum Seitenschläfer mit rätselhaften Schwindelattacken jetzt zu diesen 3-Zonen-Therapiekissen wechseln? |
| K01-079 | – | Verlierer | 1 | 3 | MORGENS SCHWINDELATTACKEN | Morgens Schwindel attacken und plötzlich ist es ein Dauerzustand, was das wirklich bedeutet, erfährst du hier. |
| K01-080 | K01-B2 | Verlierer | 3 | 2 | DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN? | Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu |
| K01-081 | K01-B2 | Verlierer | 1 | 2 | DER SCHWINDEL HÖRT EINFACH NICHT AUF? | Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen. |
| K01-082 | K01-B2 | Verlierer | 1 | 2 | MORGENS SCHWINDELATTACKEN | Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand? |
| K01-083 | – | Verlierer | 1 | 2 | WENN DU MORGENS MIT SCHWINDEL UND BENOMMENHEIT AUFWACHST | Wenn du morgens mit Schwindel und Benommen halt aufwachst, hör jetzt genau zu. |
| K01-084 | – | Verlierer | 1 | 2 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition. Und warum sie Schwindel, Benommenheit und Herzrasen verursacht. |
| K01-085 | – | Verlierer | 1 | 2 | WENN DU AUF DER SEITE SCHLÄFST UND MORGENS MIT SCHWINDEL AUFWACHST | Wenn du auf der Seite schläft und morgens mit Schwindel aufwachst, hör jetzt genau zu. |
| K01-086 | – | Verlierer | 1 | 2 | DEIN MORGENDLICHER SCHWINDEL IST KEIN INNEN-OHR PROBLEM. | Dein morgendlicher Schwindel ist kein Innenohrproblem. Hier ist, was es wirklich ist. |
| K01-087 | – | Verlierer | 1 | 2 | WENN DU SO SCHLÄFST, DRÜCKST DU AUF DEINEN VAGUSNERV | Wenn du so schläft, drückst du auf deinen Varbusnerv und riskierst Schwindel, Herzrasen |
| K01-088 | K01-B2 | Verlierer | 1 | 1 | WAS HABEN VERSPANNUNGEN IM NACKEN, | Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam? |
| K01-089 | K01-B2 | Verlierer | 1 | 1 | WAS HABEN VERSPANNUNGEN IM NACKEN, | Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam? |
| K01-090 | K01-B2 | Verlierer | 1 | 1 | WENN DU SO SCHLÄFST, | Wenn du so schläfst, schneidest du langsam die Blutzufuhr zu deinem Gehirn ab. |
| K02-091 | K02-B1 | Winner | 17 | 109 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION → UND WIE DU STATTDESSEN SCHLAFEN SOLLTEST (0–3 s) | Das ist die schlechteste Schlafposition und wie du stattdessen schlafen solltest. |
| K02-092 | K02-B1 | Kandidat | 5 | 18 | DER GRÖSSTE FEHLER BEI NÄCHTLICHEM ISCHIAS IST ZU DENKEN | Das ist die schlechteste Schlafposition und wie du stattdessen schlafen solltest. |
| K02-093 | – | Kandidat | 1 | 18 | ISCHIASSCHMERZEN SIND MEIST KEIN BANDSCHEIBENPROBLEM | Ischias Schmerzen sind meist kein Bandscheibenproblem. Es ist ein Positionsproblem im Schlaf. |
| K02-094 | – | Kandidat | 1 | 18 | WARNUNG: DAS IST DIE GEFÄHRLICHSTE SCHLAFPOSITION FÜR SEITENSCHLÄFER | Warnung, das ist die gefährlichste Schlafposition für Seitenschläfer und warum sie Schmerzen |
| K02-095 | K02-B1 | Verlierer | 2 | 7 | ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN | Ishiyas Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv. |
| K02-096 | K02-B1 | Verlierer | 2 | 7 | ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN | Ishiyas Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv. |
| K02-097 | K02-B1 | Verlierer | 2 | 6 | SEITENSCHLÄFER AUFGEPASST: DU REIZT DEINEN ISCHIASNERV WÄHREND DU SCHLÄFST | Seitenschläfer aufgepasst! Du reizt deinen Ischiasnerv, während du schläfst. Wenn du so schläfst, |
| K02-098 | K02-B1 | Verlierer | 2 | 6 | WENN DU SO SCHLÄFST: QUETSCHT DU DEINEN ISCHIASNERV EIN | Wenn du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte Schäden in deiner Wirbelsäule. |
| K02-099 | K02-B1 | Verlierer | 2 | 6 | ISCHIASSCHMERZEN ENTSTEHEN | Wenn du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte Schäden in deiner Wirbelsäule. |
| K02-100 | – | Verlierer | 1 | 6 | ARZT ERKLÄRT IN NUR 15 SEKUNDEN, WARUM ISCHIASSCHMERZEN | Arzt erklärt in nur 15 Sekunden, warum Ichjas-Schmerzen jeden Morgen wiederkommen. |
| K02-101 | – | Verlierer | 1 | 6 | DER FEHLER NR. 1 WARUM DEINE MORGENDLICHEN ISCHIASSCHMERZEN | Der Fehler Nummer eins, warum deine morgendlichen Ischiaschmerzen einfach nicht verschwinden. |
| K02-102 | – | Verlierer | 1 | 6 | DIE MEISTEN ÄRZTE ÜBERSEHEN DAS VÖLLIG | Die meisten Ärzte übersehen das völlig, wenn Seitenschläfer ab 50 mit Ischias-Schmerzen |
| K02-103 | – | Verlierer | 1 | 6 | WENN DU AUF DER SEITE SCHLÄFST | Wenn du auf der Seite schläft und morgens mit einem tauben, brennenden Bein aufwachst, |
| K02-104 | – | Verlierer | 1 | 6 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition. Und warum sie Schmerzen und Taubheizgefühle in deinen Beinen verursacht. |
| K02-105 | – | Verlierer | 1 | 6 | WENN DU NACHTS EINEN SCHMERZ IM GESÄSS SPÜRST | Wenn du nachts einen Schmerz im Gesäß spürst, der bis ins Bein runterstrahlt, |
| K02-106 | K02-B1 | Verlierer | 1 | 5 | ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN | Ischias Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv. |
| K02-107 | K02-B1 | Verlierer | 1 | 5 | ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN | Ischias Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv. |
| K02-108 | K02-B1 | Verlierer | 1 | 5 | WENN DU SO SCHLÄFST: QUETSCHT DU DEINEN ISCHIASNERV EIN | Wenn du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte Schäden in deiner Wirbelsäule. |
| K02-109 | K02-B2 | Verlierer | 2 | 4 | WENN DU SO SCHLÄFST: QUETSCHT DU DEINEN ISCHIASNERV EIN | Wenn du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte Schäden in deiner Wirbelsäule. |
| K02-110 | K02-B2 | Verlierer | 2 | 4 | SO HÖREN NÄCHTLICHE ISCHIASSCHMERZEN SOFORT AUF | So hören nächtliche Ischia-Schmerzen sofort auf. Ich sehe das jeden Tag. |
| K02-111 | K02-B2 | Verlierer | 1 | 4 | ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN | Ichiyas Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv. |
| K02-112 | K02-B2 | Verlierer | 1 | 4 | WENN DU SO SCHLÄFST: VERDREHST DU JEDE NACHT DEINE WIRBELSÄULE | Wenn du so schläfst, verdrehst du jede Nacht deine Wirbelsäule und klemmst dabei deinen |
| K02-113 | K02-B2 | Verlierer | 1 | 4 | ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN | Ichiyas Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv. |
| K02-114 | K02-B2 | Verlierer | 1 | 4 | JEDE NACHT IN DER DU SO SCHLÄFST | Jede Nacht, in der du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte |
| K02-115 | K02-B2 | Verlierer | 1 | 4 | JEDE NACHT IN DER DU SO SCHLÄFST | Jede Nacht, in der du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte |
| K02-116 | K02-B2 | Verlierer | 1 | 4 | SEITENSCHLÄFER AUFGEPASST: DU REIZT DEINEN ISCHIASNERV WÄHREND DU SCHLÄFST | Seitenschläfer aufgepasst! Du reizt dein Ischiasnerv während du schläfst. Ich sehe das jeden Tag. Menschen wachen mit stärkeren Schmerzen auf. Mehr Steifheit im |
| K02-117 | – | Verlierer | 1 | 3 | ARZT ERKLÄRT: DESHALB GEHEN NÄCHTLICHE ISCHIASSCHMERZEN | Arzt erklärt, deshalb gehen nächtliche Ischiaschmerzen einfach nicht weg. |
| K02-118 | K02-B2 | Verlierer | 1 | 2 | SO HÖREN NÄCHTLICHE ISCHIASSCHMERZEN SOFORT AUF | So hören nächtliche Ischia-Schmerzen sofort auf. Ich sehe das jeden Tag. |
| K02-119 | K02-B2 | Verlierer | 1 | 2 | WENN DU SO SCHLÄFST: VERDREHST DU JEDE NACHT DEINE WIRBELSÄULE | Wenn du so schläfst, verdrehst du jede Nacht deine Wirbelsäule und klemmst dabei deinen |
| K02-120 | – | Verlierer | 1 | 1 | DER FEHLER NR. 1 WARUM DEINE MORGENDLICHEN ISCHIASSCHMERZEN | (kein Transkript) |
| K02-121 | – | Verlierer | 1 | 1 | ARZT ERKLÄRT IN NUR 15 SEKUNDEN, WARUM ISCHIASSCHMERZEN | (kein Transkript) |
| K02-122 | – | Verlierer | 1 | 1 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | (kein Transkript) |
| K02-123 | – | Verlierer | 1 | 1 | ISCHIASSCHMERZEN, DIE NACHTS TROTZ ÜBUNGEN WIEDERKOMMEN? | (kein Transkript) |
| K02-124 | – | Verlierer | 1 | 1 | ARZT ERKLÄRT: DESHALB GEHEN NÄCHTLICHE ISCHIASSCHMERZEN | (kein Transkript) |
| K02-125 | – | Verlierer | 1 | 1 | WENN DU NACHTS EINEN SCHMERZ IM GESÄß SPÜRST | (kein Transkript) |
| K02-126 | – | Verlierer | 1 | 1 | ISCHIASSCHMERZEN, DIE NACHTS TROTZ ÜBUNGEN WIEDERKOMMEN? | (kein Transkript) |
| K02-127 | – | Verlierer | 1 | 1 | WENN DU AUF DER SEITE SCHLÄFST | (kein Transkript) |
| K02-128 | – | Verlierer | 1 | 1 | (kein Text im Startframe) | (kein Transkript) |
| K05-187 | K05-B1 | Winner | 14 | 206 | So hört schnarchen sofort auf. (schwarzer Balken, „schnarchen“ rot hinterlegt) | So hört Schnarchen sofort auf. So sieht dein verengter Atemweg aus, wenn du schnarchst. |
| K05-188 | K05-B1 | Winner | 12 | 164 | So hört schnarchen sofort auf. | So hört Schnarchen sofort auf. So sieht dein verengter Atemweg aus, wenn du schnarchst. |
| K05-189 | K05-B2 | Winner | 3 | 67 | Wir haben einen Schlafapnoe Patienten gebeten | Wir haben einen Schlafapnoe-Patienten gebeten, sieben Tage lang mit dem Nacken-Therapie-Kissen zu schlafen. |
| K05-190 | K05-B2 | Kandidat | 1 | 31 | Wenn ein Mann von seinem CPAP Gerät auf | Wenn ein Mann von seinem CPAP-Gerät auf das Nacken-Therapie-Kissen umsteigt, passiert Folgendes. |
| K05-191 | K05-B2 | Kandidat | 1 | 31 | Wir haben einen Schlafapnoe Patienten gebeten | Wir haben einen Schlafapnoe-Patienten gebeten, sieben Tage lang mit dem Nacken-Therapie-Kissen zu schlafen. |
| K09-238 | K09-B1 | Winner | 13 | 203 | Das ist die schlechteste Schlafposition (schwarzer Balken, „die schlechteste“ rot) → „und wie du stattdessen schlafen solltest“ | Das ist die schlechteste Schlafposition. Und wie du stattdessen schlafen solltest. |
| K11-247 | K11-B1 | Verlierer | 1 | 10 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION BEI NACKENSCHMERZEN | Das ist die schlechteste Schlafposition bei Nackenschmerzen und wie du stattdessen schlafen solltest. |
| K11-248 | K11-B1 | Verlierer | 1 | 9 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION BEI NACKENSCHMERZEN | Das ist die schlechteste Schlafposition bei Nackenschmerzen und wie du stattdessen schlafen |
| K11-249 | K11-B1 | Verlierer | 1 | 8 | NACKENSCHMERZEN DIE TROTZ BEHANDLUNGEN NICHT VERSCHWINDEN | Nackenschmerzen, die trotz Behandlungen nicht verschwinden, sind keine Verspannung, sondern |
| K11-250 | K11-B1 | Verlierer | 1 | 7 | DER GRÖßTE FEHLER BEI NACKENSCHMERZEN IST ZU DENKEN | Der größte Fehler bei Nackenschmerzen ist zu denken, dass es ein Haltungsproblem ist. |
| K11-251 | K11-B1 | Verlierer | 1 | 7 | WENN DU SO SCHLÄFST ZERSTÖRST DU LANGSAM DEINE HALSWIRBELSÄULE | Wenn Du so schläfst, zerstörst Du langsam Deine Halswirbelsäule, besonders C5 und C6. |
| K11-252 | K11-B1 | Verlierer | 1 | 7 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION BEI NACKENSCHMERZEN | Das ist die schlechteste Schlafposition bei Nackenschmerzen und wie du stattdessen schlafen solltest. |
| K11-253 | K11-B1 | Verlierer | 1 | 6 | DER GRÖßTE FEHLER BEI NACKENSCHMERZEN IST ZU DENKEN | Der größte Fehler bei Nackenschmerzen ist zu denken, dass es ein Haltungsproblem ist. |
| K11-254 | K11-B1 | Verlierer | 1 | 6 | NACKENSCHMERZEN DIE TROTZ BEHANDLUNGEN NICHT VERSCHWINDEN | Nackenschmerzen, die trotz Behandlungen nicht verschwinden, sind keine Verspannung, sondern |
| K11-255 | K11-B1 | Verlierer | 1 | 5 | DER GRÖßTE FEHLER BEI NACKENSCHMERZEN IST ZU DENKEN | Der größte Fehler bei Nackenschmerzen ist zu denken, dass es ein Haltungsproblem ist. |
| K11-256 | K11-B1 | Verlierer | 1 | 4 | NACKENSCHMERZEN DIE TROTZ BEHANDLUNGEN NICHT VERSCHWINDEN | Nackenschmerzen, die trotz Behandlungen nicht verschwinden, sind keine Verspannung, sondern |
| K15-284 | K15-B1 | Verlierer | 1 | 2 | MITTEN IN | Mitten in der Präsentation blieb mein Kopf einfach leer |
| K15-285 | – | Verlierer | 1 | 2 | (kein Text im Startframe) | (kein Transkript) |
| K15-286 | – | Verlierer | 1 | 2 | (kein Text im Startframe) | (kein Transkript) |
| K15-287 | – | Verlierer | 1 | 2 | (kein Text im Startframe) | (kein Transkript) |
| K15-288 | – | Verlierer | 1 | 2 | (kein Text im Startframe) | (kein Transkript) |
| K15-289 | – | Verlierer | 1 | 1 | (kein Text im Startframe) | (kein Transkript) |
| K15-290 | – | Verlierer | 1 | 1 | (kein Text im Startframe) | (kein Transkript) |
| K16-291 | K16-B1 | Kandidat | 2 | 18 | WENN DU MORGENS MIT SCHWINDEL AUFWACHST | Wenn du morgens mit Schwinden laufst Deine arme Krippeln sobald du den Kopf drehst |
| K16-292 | – | Kandidat | 1 | 18 | MEIN NEUROLOGE MEINTE, ES SEI STRESS | (kein Transkript) |
| K16-293 | – | Kandidat | 1 | 18 | WARUM SCHWINDEL IMMER WIEDERKOMMT | (kein Transkript) |
| K16-294 | – | Verlierer | 1 | 6 | (erstes Bild schwarz) | (kein Transkript) |
| K16-295 | – | Verlierer | 1 | 5 | MEIN NEUROLOGE | (kein Transkript) |
| K17-296 | K17-B1 | Verlierer | 1 | 1 | (kein Text im Startframe) | Ich war 54, als ich mir einen Termin beim Neurologen ausmachte |
| K17-297 | – | Verlierer | 1 | 1 | UM 2 UHR | (kein Transkript) |
| K17-298 | – | Verlierer | 1 | 1 | MITTEN IN | (kein Transkript) |
| K17-299 | – | Verlierer | 1 | 1 | (kein Text im Startframe) | (kein Transkript) |
| K17-300 | – | Verlierer | 1 | 1 | (kein Text im Startframe) | (kein Transkript) |
| K17-301 | – | Verlierer | 1 | 1 | (kein Text im Startframe) | (kein Transkript) |
| K18-302 | – | Test | 1 | 4 | 14 JAHRE LANG HABEN MIR ÄRZTE GESAGT, ICH HÄTTE EINE ANGSTSTÖRUNG | (kein Transkript) |
| K18-303 | – | Test | 1 | 4 | DURCH DEINEN NACKEN LAUFEN NERVEN | (kein Transkript) |
| K18-304 | – | Test | 1 | 4 | MIT 34 BEKAM ICH DIE DIAGNOSE: ANGSTSTÖRUNG | (kein Transkript) |
| K18-305 | – | Test | 1 | 4 | (kein Text im Startframe) | (kein Transkript) |
| K18-306 | – | Verlierer | 1 | 2 | MRT: NORMAL / BLUTBILD: NORMAL / EKG: NORMAL | (kein Transkript) |
| K22-322 | K22-B1 | Verlierer | 1 | 2 | WARUM SEITENSCHLÄFER MIT MIGRÄNE | Warum Seitenschläfer mit Migräne oder ständigen Kopfschmerzen jetzt zu diesen neuartigen Kissen wechseln? |
| K22-323 | K22-B1 | Verlierer | 1 | 2 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition bei Migräne und wie du stattdessen schlafen solltest. |
| K22-324 | K22-B1 | Verlierer | 1 | 2 | SEITENSCHLÄFER: DU KLEMMST DEINEN TRIGEMINUSNERV EIN | Seitenschläfer. Du klemmst deinen Trigeminusnerv ein, während du schläfst und genau das führt zu deinen Migräneattacken. |
| K22-325 | K22-B1 | Verlierer | 1 | 2 | DAS IST DER GRUND WARUM SEITENSCHLÄFER UNTER MIGRÄNE | Das ist der Grund, warum Seitenschläfer unter Migräne oder starken Kopfschmerzen leiden |
| K23-326 | K23-B1 | Verlierer | 1 | 7 | warum du | Das hier ist Jürgen und er leidet seit fünf Jahren an morgendlichen Nacken- und Schulterschmerzen. |
| K23-327 | K23-B2 | Verlierer | 1 | 3 | Wenn du | Wenn du als Seitenschläfer jeden Morgen mit brennenden Nackenschmerzen aufwachst, |
| K23-328 | K23-B2 | Verlierer | 1 | 2 | Das hier | Das hier ist Jürgen. Hallo Jürgen. Jürgen ist Seitenschläfer und wacht jeden Morgen mit brennenden Nackenschmerzen, |
| K24-329 | – | Kandidat | 1 | 18 | MEIN NEUROLOGE MEINTE, ES SEI STRESS | (kein Transkript) |
| K24-330 | – | Kandidat | 1 | 18 | WARUM SCHWINDEL IMMER WIEDERKOMMT | (kein Transkript) |
| K24-331 | – | Verlierer | 1 | 3 | WENN DU MORGENS MIT SCHWINDEL AUFWACHST | (kein Transkript) |
| K25-332 | K25-B1 | Verlierer | 1 | 2 | DAS IST DIE SCHLECHTESTE SCHLAFPOSITION | Das ist die schlechteste Schlafposition und warum sie Taubheitsgefühle von der Schulter |
| K25-333 | K25-B1 | Verlierer | 1 | 2 | WENN DU SO SCHLÄFST, | Wenn du so schläfst, zerstörst du langsam deine Halswirbelsäule, besonders C5 und C6. |
| K25-334 | K25-B1 | Verlierer | 1 | 2 | TAUBHEITSGEFÜHLE IN DEN HÄNDEN | Taubheitsgefühle in den Händen kommen nicht von einer schlechten Durchblutung, sondern |
| K27-336 | – | Verlierer | 1 | 3 | MEINE FRAU WOLLTE SICH WEGEN MEINES SCHNARCHENS VON MIR SCHEIDEN LASSEN. KLINGT EIGENTLICH LÄCHERLICH, ODER? ABER NACH SIEBEN JAHREN HÖLLE STREIT UM 2 UHR NACHTS, GETRENNTE SCHLAFZIMMER UND DIE ENTDECKUNG, DASS SIE HEIMLICH BEI IMMOSCOUT24 NACH WOHNUNGEN IN HAMBURG SUCHTE | (kein Transkript) |

## Body-Varianten – vollständige Transkripte

### K01-B1 – Referenz K01-001 (Ad 96489719, [share_url](https://app.gethookd.ai/share/ad/96489719?signature=37040ca3da7330278cf944b4b9b89643e2ef4ada0847104ff151b8cd4dda1ac7), Länge 352 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken
[00:05] oder Herzrasen?
[00:06] Was das wirklich bedeutet, erfährst du hier.
[00:08] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
[00:12] ist alles instabil, als würde dir der Boden unter den Füßen wegrutschen.
[00:15] Du weißt nicht, ob du dich hinsetzen, hinlegen oder einfach hoffen sollst, dass es gleich
[00:19] vorbei geht.
[00:20] Dein Blutdruck?
[00:21] Normal.
[00:22] Dein MRT?
[00:23] Unauffällig.
[00:24] Die Ärzte?
[00:25] Ratlos.
[00:26] Doch tief in dir weißt du längst, da stimmt irgendwas nicht.
[00:27] Nur keiner kann dir sagen, was es ist.
[00:28] Aber was, wenn du dir das alles nicht einfach einbildest, sondern dein Körper dich versucht
[00:32] zu warnen?
[00:33] Was, wenn der Schwindel kein Fehler ist, sondern ein Schutzmechanismus, weil etwas in dir aus
[00:36] dem Takt geraten ist?
[00:37] In den letzten Jahren taucht in der Fachliteratur immer häufiger der Begriff cervicogener Schwindel
[00:42] auf und die Symptome reichen weit über den Schwindel hinaus.
[00:45] Nackenschmerzen, Kopfdruck, Benommenheit, Kribbeln in den Armen, Schlafstörungen, Panikattacken
[00:50] und manchmal sogar Herzrasen.
[00:51] Ärzte sehen oft nur das Symptom, aber nie den Zusammenhang.
[00:54] Denn all das ist meist nur die Reaktion eines Systems, das im Hintergrund still und leise
[00:58] nach Hilfe schreit.
[00:59] Cervicogener Schwindel wird durch Verspannungen in den tiefen Nackenmuskeln ausgelöst, die
[01:03] Blutfluss- und Nervensignale beeinträchtigen.
[01:05] Es ist also nicht dein Kreislauf, nicht deine Psyche und auch nicht dein Innenohr.
[01:09] Es ist dein Nacken.
[01:10] Und Studien zeigen, dass dieses Problem häufig durch eine nächtliche Fehlstellung der Halswirbelsäule
[01:14] verursacht wird.
[01:15] Wenn der Nacken nachts nämlich in einer vergründeten Position liegt, knickt die Halswirbelsäule
[01:19] ab und die tiefen Muskeln, rund um C1 und C2, verkrampfen sich dann die ganze Nacht
[01:23] über, um den Kopf irgendwie zu stabilisieren.
[01:26] Dadurch werden die Arterien zusammengedrückt, die zum Gehirn führen, der Vargusnerv wird
[01:29] gereizt und das Nervensystem bekommt ständig Alarmsignale, obwohl eigentlich keine echte
[01:34] Gefahr besteht.
[01:35] Das erklärt den Schwindel, das Kribbeln in den Armen, das Herzrasen und die verschwommene
[01:39] Sicht.
[01:40] Das alles ist nicht nur extrem einschränkend, sondern auch eine tickende Zeitbombe.
[01:43] Denn wenn du nichts dagegen unternimmst, wird dein Schwindel chronisch, die Nervenschäden
[01:47] dauerhaft und am Ende wartet womöglich ein Bandscheibenvorfall und damit auch das Risiko
[01:51] einer Operation.
[01:52] Nach und nach wirkt sich das alles auf deine Unabhängigkeit und deine Lebensqualität
[01:56] aus, was letztlich heißt, dass du dein Leben nicht so genießen kannst, wie du es verdienst.
[02:00] Gefangen in ständiger Unsicherheit, wann der nächste Schwindelanfall kommt.
[02:03] Also wie können wir diese nächtliche Fehlstellung der Halswirbelsäule lösen?
[02:06] Nun, wenn du nachts schläfst, ist es entscheidend, dass deine Halswirbelsäule in einer neutralen
[02:11] Position bleibt und die obersten Wirbel, C1 und C2, genug Platz haben.
[02:15] Dies verhindert den Druck auf den Vargusnerv und die Blutgefäße zum Gehirn, wodurch du
[02:19] endlich wieder durchschlafen kannst, ohne mit Drehschwindel, Benommenheit oder Herzrasen
[02:23] aufzuwachen.
[02:24] Herkömmliche Kissen sind geometrisch einfach nicht für den menschlichen Kopf ausgelegt.
[02:27] Sie sind oft zu weich oder zu hart und lassen die Halswirbeln absinken oder überstrecken.
[02:31] Außerdem bieten sie einfach nicht die Rundum-Unterstützung, die dein Kopf und Nacken eigentlich benötigt.
[02:36] Selbst teure Daunen, Feder- oder Memory-Schaumkissen ignorieren völlig, dass C1 und C2 Raum brauchen,
[02:42] wo deine Wirbelarterien verlaufen und dein Vargusnerv sitzt.
[02:45] Und genau aus diesem Grund hat ein renommierter deutscher Chiropraktiker gemeinsam mit einem
[02:49] österreichischen Gründerteam 21 orthopädische Kopfkissen getestet und dabei über 300 Nutzerbewertungen
[02:55] analysiert.
[02:56] Nach neun Monaten Entwicklungszeit und vier Prototypen entstand letztes Jahr schließlich
[02:59] das Nackentherapiekissen.
[03:00] Ein cervicales Nackenstützkissen, das genau dort entlastet, wo die meisten Beschwerden
[03:05] entstehen.
[03:06] Im Übergang von Kopf, Nacken und Schultern, genau dort, wo C1 und C2 sitzen und der Vargusnerv
[03:11] verläuft.
[03:12] Das intelligente Drei-Zone-Nackenstützsystem kehren Kopf, Nacken und Schultern in die natürliche
[03:16] Ausrichtung zurück und der Druck auf den Vargusnerv wird aufgehoben.
[03:20] Das heißt, dank der ergonomischen Nackenstütze wird deine Halswirbelsäule perfekt gestützt,
[03:24] ohne Hohlraum zwischen Kissen und Nacken.
[03:26] Und die geformte Kopfzone entlastet die kritische C1-C2-Region.
[03:30] Es gibt außerdem eine speziell integrierte Armablage, damit deine Arme bequem liegen
[03:34] und nicht die Schulter belasten.
[03:35] Das Nackentherapiekissen sorgt also dafür, dass genau solche Fehlstellungen nicht passieren
[03:40] und bietet sofortige Linderung für deine Symptome schon in der ersten Nacht.
[03:43] Egal ob du auf der Seite, dem Rücken oder dem Bauch schläfst.
[03:46] Der atmungsaktive und kühlende Bezug stellt sicher, dass du nachts nicht schwitzt und
[03:50] ständig die Position wechseln musst, was oft zu zusätzlichen Schwindelattacken führt.
[03:54] Du kannst aber auch einfach deinen gewohnten Kissenbezug weiterverwenden.
[03:57] Und genau das passiert, wenn du anfängst, mit dem Nackentherapiekissen zu schlafen.
[04:01] Nacht 1.
[04:02] Du wachst das erste Mal seit langem ohne Drehschwindel auf.
[04:04] Der Raum bleibt stabil.
[04:05] Woche 1.
[04:06] Die Benommenheit während deines Tages verschwindet.
[04:08] Das Kribbeln in deinen Armen lässt nach und die plötzlichen Herzraserei-Episoden werden
[04:12] seltener.
[04:13] Woche 2.
[04:14] Keine Schwindelattacken mehr.
[04:15] Dein Alltag wird endlich wieder stabil und kontrollierbar.
[04:17] Schon in der ersten Nacht habe ich gemerkt, das hilft ja.
[04:20] Das hast du direkt gespürt.
[04:21] Ich bin morgens aufgewacht und dachte mir sowieso, warte mal, Nacken tut gar nicht mehr
[04:27] weh.
[04:28] Nach zwei Wochen waren die kompletten Kopfschmerzen weg bei mir.
[04:30] Also einfach weg.
[04:31] Kein Ruheraum mehr zwischen Kissen und Nacken.
[04:34] Schultern werden entlastet.
[04:35] Und das Kribbeln im Arm, das ist auch ein Gefühl.
[04:37] Ich schlafe jetzt echt so gut wie seit langem nicht mehr und wache morgens erholt auf.
[04:42] Es hört sich vielleicht komisch an, aber dieses Kissen hat mir mein Leben zurückgegeben.
[04:47] Rund 92 Prozent der KundInnen berichteten bereits nach den ersten Nächten von einer
[04:51] spürbaren Linderung ihres Schwindels, ihrer Benommenheit und dem Kribbeln in den Armen.
[04:55] Und nach etwas mehr als 14 Tagen waren die Beschwerden meist vollständig verschwunden.
[04:59] Viele dieser Personen waren anfangs skeptisch, da sie bereits schon alles Mögliche ausprobiert
[05:03] hatten.
[05:04] Zum Beispiel Ärzte, Neurologen oder auch Physiotherapie.
[05:07] Doch nachdem sie die vielen positiven Bewertungen und einzigartige Garantie sahen, haben sie
[05:11] sich entschieden, dem Nacken-Therapie-Kissen eine Chance zu geben.
[05:14] Das sehr ambitionierte Team hinter dem Kissen bietet nämlich ein Versprechen an, das kein
[05:18] Pharmakonzern oder Arzt jemals geben würde.
[05:21] Wenn du nach 30 Nächten mit dem Nacken-Therapie-Kissen keinen großen Unterschied bei deinen Symptomen
[05:25] spürst, bekommst du dein volles Geld rückerstattet.
[05:27] Seitdem das Nacken-Therapie-Kissen im Internet vorgestellt wurde, hat das Produkt mit über
[05:31] 21 Millionen Aufrufen auf TikTok einen unglaublichen Hype ausgelöst und war bereits dreimal ausverkauft.
[05:37] Und deshalb ist der aktuelle Lagerbestand sehr limitiert.
[05:40] Klicke jetzt also unten auf den Link, um das Nacken-Therapie-Kissen ganz ohne Risiko für
[05:44] 30 Nächte zu testen.
[05:45] Oder du bekommst dein Geld zurück.
```

### K01-B2 – Referenz K01-002 (Ad 100373716, [share_url](https://app.gethookd.ai/share/ad/100373716?signature=e9951b4ee54d09b415ffda53800210bbb172cd4f7e0bb2aa150add7a36dbba1d), Länge 383 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen
[00:04] verursacht.
[00:05] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:08] Beim HMO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht, vielleicht
[00:12] hat dir sogar jemand Antidepressiva verschrieben und trotzdem, jeden Morgen wachst du auf und
[00:16] fühlst dich benommen.
[00:17] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:21] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche
[00:25] zu tun.
[00:26] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:29] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:32] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder
[00:36] deine Arme kribbeln und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich
[00:40] an deinem alten Kissen.
[00:41] Herkömmliche Kissen sind geometrisch nämlich nicht für den menschlichen Kopf ausgelegt.
[00:45] Das bedeutet, dein Nacken liegt die ganze Nacht in einer ungesunden, verdrehten Position,
[00:49] auch Zervikale Schlaffehlstellung genannt.
[00:51] Und du merkst es nicht mal.
[00:52] Du kannst dir das in etwa wie eine 8 Stunden lange, unnatürliche Yoga-Dehnung vorstellen,
[00:56] die dein Gehirn nicht wirklich registriert.
[00:58] Das heißt, die empfindlichen Wirbelarterien zwischen C1 und C2 werden Nacht für Nacht
[01:02] zusammengedrückt, wie ein Gartenschlauch, der abgeknickt wird.
[01:05] Konkreter gesagt, diese Arterien führen direkt zu deinem Gehirn und versorgen dein Gleichgewichtszentrum
[01:10] mit Blut.
[01:11] Wenn sie dann eingequetscht werden, kann nicht mehr genug Sauerstoff zu deinem Gehirn gelangen.
[01:14] Und genau das führt zu diesem schwebenden, wackeligen Gefühl, als würde der Boden unter
[01:18] dir pulsieren.
[01:19] Doch dabei bleibt es nicht.
[01:20] Eine dauerhaft falsche Schlafposition löst eine regelrechte Kettenreaktion aus.
[01:25] Denn anstatt sich nachts zu erholen, spannt sich deine Nackenmuskulatur extrem an, wie
[01:28] ein Gummiband, das permanent unter Spannung steht.
[01:31] Vor allem die vier winzigen Subokzipitalmuskeln an der Schädelbasis geraten unter extremen
[01:35] Druck.
[01:36] Und genau diese Muskeln liegen direkt neben dem Vagusnerv, dem Hauptnerv, der dein Herz,
[01:40] deine Atmung und dein Gleichgewicht steuert.
[01:42] Und wenn der Vagusnerv gestört ist, sendet er ständig Alarmsignale an dein Gehirn, obwohl
[01:46] eigentlich keine echte Gefahr besteht.
[01:48] Das führt zu Schwindel, Benommenheit, Kribbeln in den Armen, Herzrasen, Panikattacken und
[01:53] verschwommener Sicht.
[01:54] Und das Schlimmste?
[01:55] Kein Arzt findet die Ursache, weil alle Tests normal zurückkommen.
[01:58] Also bekommst du Antidepressiva verschrieben oder man sagt dir es sei nur der Stress.
[02:02] Aber wenn du nichts gegen dieses Problem unternimmst, riskierst du chronischen Schwindel, permanente
[02:06] Gleichgewichtsstörungen und die ständige Reizung deines Vagusnervs kann langfristig
[02:10] auch dein Herz-Kreislauf-System belasten.
[02:12] Nach und nach zieht sich das durch dein ganzes Leben.
[02:14] Deine Stimmung kippt, deine Energie verschwindet, deine Produktivität bricht ein.
[02:17] Du vermeidest Supermärkte, weil die Gänge sich anfühlen, als würden sie wanken.
[02:21] Du ziehst dich zurück, sagst Treffen mit deinen Freunden ab, verpasst Momente mit deiner
[02:24] Familie, nicht weil du willst, sondern weil dein Körper dir keine andere Wahl lässt.
[02:28] Also wie können wir dieses Problem lösen?
[02:30] Nun, wenn du nachts schläfst, ist es entscheidend, dass deine Halswirbelsäule in einer neutralen
[02:34] Position bleibt und die obersten Wirbel, C1 und C2, genug Platz haben.
[02:38] Dies verhindert den Druck auf den Vagusnerv und die Blutgefäße zum Gehirn, wodurch du
[02:42] endlich wieder ohne Drehschwindel aufwachst und den Tag ohne Benommenheit oder Herzrasen
[02:46] genießen kannst.
[02:47] Allkömmliche Kissen sind oft zu weich oder zu hart und lassen die Halswirbeln absinken
[02:51] oder überstrecken.
[02:52] Außerdem bieten sie einfach nicht die Rundum-Unterstützung, die dein Kopf und Nacken eigentlich benötigt.
[02:56] Selbst teure Downen, Feder- oder Memory-Schaumkissen ignorieren völlig, dass C1 und C2 Raum brauchen,
[03:03] wo deine Wirbelarterien verlaufen und dein Vagusnerv sitzt.
[03:06] Und genau aus diesem Grund hat ein renommierter deutscher Chiropraktiker gemeinsam mit einem
[03:10] österreichischen Gründerteam 21 orthopädische Kopfkissen getestet und dabei über 300 Nutzerbewertungen
[03:16] analysiert.
[03:17] Nach neun Monaten Entwicklungszeit und vier Prototypen entstand letztes Jahr schließlich
[03:21] das Nackentherapiekissen.
[03:22] Ein cervikales Nackenstützkissen, das genau dort entlastet, wo die meisten Beschwerden
[03:26] entstehen.
[03:27] Im Übergang von Kopf, Nacken und Schultern, genau dort, wo C1 und C2 sitzen und der Vagusnerv
[03:32] verläuft.
[03:33] Durch das intelligente 3-Zonen-Nackenstützsystem kehren Kopf, Nacken und Schultern in die
[03:38] natürliche Ausrichtung zurück und der Druck auf den Vagusnerv wird aufgehoben.
[03:42] Das heißt, dank der ergonomischen Nackenstütze wird deine Halswirbelsäule perfekt gestützt,
[03:46] ohne Hohlraum zwischen Kissen und Nacken.
[03:48] Und die geformte Kopfzone entlastet die kritische C1-C2-Region.
[03:52] Es gibt außerdem eine speziell integrierte Armablage, damit deine Arme bequem liegen
[03:56] und nicht die Schulter belasten.
[03:58] Das Nackentherapiekissen sorgt also dafür, dass genau solche Fehlstellungen nicht passieren
[04:02] und bietet sofortige Linderung für deine Symptome schon in der ersten Nacht, egal ob
[04:06] du auf der Seite, dem Rücken oder dem Bauch schläfst.
[04:09] Der atmungsaktive und kühlende Bezug stellt sicher, dass du nachts nicht schwitzt und
[04:13] ständig die Position wechseln musst.
[04:15] Was oft zu zusätzlichen Schwindelattacken führt.
[04:17] Du kannst aber auch einfach deinen gewohnten Kissenbezug weiterverwenden.
[04:20] Und genau das passiert, wenn du anfängst, mit dem Nackentherapiekissen zu schlafen.
[04:24] Nacht 1.
[04:25] Du wachst das erste Mal seit langem ohne Drehschwindel auf.
[04:27] Der Raum bleibt stabil.
[04:29] Woche 1.
[04:30] Die Benommenheit während deines Tages verschwindet.
[04:32] Das Kribbeln in deinen Armen lässt nach.
[04:33] Und die plötzlichen Herzraserei-Episoden werden seltener.
[04:36] Woche 2.
[04:37] Keine Schwindelattacken mehr.
[04:38] Dein Alltag wird endlich wieder stabil und kontrollierbar.
[04:41] Schon in der ersten Nacht habe ich gemerkt, das hilft ja.
[04:44] Das hast du direkt gespürt.
[04:45] Ich bin morgens aufgewacht und dachte mir so, warte mal, Nacken tut gar nicht mehr weh?
[04:51] Nach zwei Wochen waren die kompletten Kopfschmerzen weg von mir.
[04:54] Also einfach weg.
[04:55] Kein Ruheraum mehr zwischen Kissen und Nacken.
[04:58] Die Schultern werden entlastet und das Kribbeln im Arm ist jetzt auch endlich weg.
[05:01] Ich schlafe jetzt echt so gut wie seit langem nicht mehr und wache morgens erholt auf.
[05:07] Es hört sich vielleicht komisch an, aber dieses Kissen hat mir mein Leben zurückgegeben.
[05:11] Rund 92% der Kundinnen berichteten bereits nach den ersten Nächten von einer spürbaren
[05:16] Linderung ihres Schwindels, ihrer Benommenheit und dem Kribbeln in den Armen.
[05:20] Und nach etwas mehr als 14 Tagen waren die Beschwerden meist vollständig verschwunden.
[05:24] Viele dieser Personen waren anfangs skeptisch, da sie bereits schon alles mögliche ausprobiert
[05:28] hatten.
[05:29] HNO-Ärzte, Neurologen oder auch Physiotherapie.
[05:32] Doch nachdem sie die vielen positiven Bewertungen und einzigartige Garantie sahen, haben sie
[05:36] sich entschieden, dem Nacken-Therapie-Kissen eine Chance zu geben.
[05:39] Das sehr ambitionierte Team hinter dem Kissen bietet nämlich ein Versprechen an, das kein
[05:43] Pharmakonzern oder Arzt jemals geben würde.
[05:46] Wenn du nach 30 Nächten mit dem Nacken-Therapie-Kissen keinen großen Unterschied bei deinen Symptomen
[05:50] spürst, bekommst du dein volles Geld rückerstattet.
[05:52] Seitdem das Nacken-Therapie-Kissen im Internet vorgestellt wurde, hat das Produkt mit über
[05:56] 21 Millionen Aufrufen auf TikTok einen unglaublichen Hype ausgelöst und war bereits dreimal ausverkauft.
[06:03] Und deshalb ist der aktuelle Lagerbestand sehr limitiert.
[06:05] Klicke jetzt also unten auf den Link, um das Nacken-Therapie-Kissen ganz ohne Risiko
[06:09] für 30 Nächte zu testen oder du bekommst dein Geld zurück.
```

### K01-B3 – Referenz K01-030 (Ad 98148692, [share_url](https://app.gethookd.ai/share/ad/98148692?signature=a7f88997454c3b3a4745e18e31165094fe1a474a4e11274104bbfc717dd3962e), Länge 353 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und dir jeder Arzt sagt, alles ist völlig normal, dann schau das bitte bis zum Ende.
[00:08] Denn ich habe 18 Monate meines Lebens verloren und über 2400 Euro aus eigener Tasche bezahlt, bevor ich herausgefunden habe, was wirklich los war.
[00:16] Ich dachte zuerst, der Schwindel komme vom Stress oder zu wenig Schlaf. Es fing schleichend an, so ein leichtes Schwanken morgens beim Aufstehen, ein komisches Gefühl, als würde der Boden unter mir nachgeben.
[00:25] Ich dachte, das ist normal. Aber das Gefühl blieb, Tag für Tag. Also fing ich an zu googeln und fand die üblichen Lösungen. Gleichgewichtsübungen, mehr Wasser trinken, weniger Stress und mehr Schlafen.
[00:34] Aber nichts hat geholfen. Und fang mir bloß nicht mit Ärzten an. Hausarzt? Blutbild perfekt. HNO? Ihr Gleichgewichtsorgan ist in Ordnung. Neurologe? Ihr Gehirn sieht super aus.
[00:43] Klar, kurzzeitig beruhigend. Aber nach Monaten von Facharztterminen, endlosen Wartezeiten und immer neuen Überweisungen war ich am Ende meiner Kräfte.
[00:51] Und der Schwindel? Der blieb. Und Symptome? Die häuften sich. Wenn ich morgens aufwachte? Schwindel. Wenn ich den Kopf nach links drehte? Kribbeln in den Händen.
[00:57] Jede Nacht? Herzrasen. Als würde es aus der Brust springen wollen. Mein Mann meinte, vielleicht sind's die Wechseljahre. Mein Hausarzt sagte, vielleicht ist es der Stress.
[01:04] Mein Neurologe meinte, vielleicht eine Angststörung. Ich ertrank in Vielleichts. Und keins davon stimmte.
[01:10] Aber der absolute Tiefpunkt? Der Tag, an dem ich in der Gartenabteilung bei Hornbach zusammengebrochen bin. Jemand hat mich von hinten angesprochen.
[01:16] Entschuldigung, wissen Sie, wo die Rosendünger sind? Ich habe den Kopf schnell nach links gedreht, um zu antworten.
[01:20] In dem Moment kippte die Welt zur Seite. Meine Knie haben nachgegeben. Alles drehte sich. Ich saß da, hielt mich fest und versuchte, nicht ohnmächtig zu werden.
[01:28] Meine Hände haben gebrummt, als hätte ich einen Stromschlag bekommen. An dem Abend habe ich unter der Dusche geweint, damit mein Mann es nicht hört.
[01:34] Ich hatte insgesamt sechs verschiedene Ärzte und vier Spezialisten durch. Und war immer noch schwindelig. Ich war kurz davor, aufzugeben.
[01:41] Noch in derselben Nacht habe ich wieder gegoogelt. Schwindel trotz normaler Befunde. Kribbeln in den Armen schlimmer beim Kopfdrehen. Herzrasen trotz normalem EKG.
[01:48] Ich fand ein Diskussionsforum mit Menschen wie mir. Gleiche Symptome, gleiche normale Testergebnisse.
[01:53] Und die sprachen über etwas namens cervicogener Schwindel, ausgelöst durch Verspannungen in den tiefen Nackenmuskeln.
[01:59] Das Problem waren also nicht die Ohren, nicht das Gehirn, nicht das Herz, sondern der Nacken.
[02:04] Es stellte sich heraus, wenn der Nacken nachts in einer verkrümmten Position liegt, verkrampfen sich die tiefen Muskeln rund um C1 und C2 die ganze Nacht über.
[02:11] Dadurch werden die Arterien zusammengedrückt, die zum Gehirn führen und der Vagusnerv wird gereizt.
[02:16] Das erklärt den Schwindel, das Kribbeln, das Herzrasen, die verschwommene Sicht. Ein Kommentar ließ mich erstarren.
[02:21] Die Spannung baut sich auf, während du schläfst. Acht Stunden jede Nacht in der falschen Position.
[02:26] Jemand anderes sagte, hab mein Kissen gewechselt. Drei Wochen später waren die Symptome zu 80% weg.
[02:32] Nicht einer der sechs Ärzte hatte je nach meinem Kissen gefragt. Ich schaute auf mein Bett und sah mein Daunenkissen.
[02:37] Was, wenn es alles schlimmer machte? Die Leute erklärten, wie normale Kissen völlig ignorieren, was bei C1 bis C2 passiert.
[02:43] Wo deine Wirbelarterien verlaufen. Wo dein Vagusnerv sitzt.
[02:46] Acht Stunden arterielle Einschränkung. Acht Stunden Nervenreizung. Acht Stunden Schaden.
[02:51] Während ich dachte, ich würde mich erholen.
[02:53] Die Leute empfahlen ein bestimmtes Kissen, entwickelt für cervikogene Probleme, mit einem hohlen Zentrum, das den Druck von der Schädelbasis nimmt.
[02:59] Immer wieder tauchte derselbe Name auf. Nacken-Therapie-Kissen.
[03:02] Leute, die jahrelang gelitten hatten. Genau wie ich. Die alles probiert hatten. Und die plötzlich schmerzfrei waren.
[03:08] Die Produktbilder zeigten eine ungewöhnliche Schmetterlingsform. Eine tiefe Mulde in der Mitte.
[03:12] Ein Drei-Zonen-Stützsystem für optimale Halswirbelsäulen-Positionierung.
[03:16] Entwickelt, um die Halswirbelsäule in neutraler Ausrichtung zu halten.
[03:19] Um den Druck von der Schädelbasis zu nehmen. Um die Nerven zu entlasten.
[03:23] Ich hatte bereits tausende Euro für Antworten ausgegeben. Also, was war schon ein Kissen?
[03:27] Als es ankam, fühlte ich mich irgendwie lächerlich. Ein Kissen? Nach all diesen Spezialisten?
[03:31] Aber in der ersten Nacht fühlte sich was anders an. Mein Kopf legte sich in die hohle Mitte.
[03:35] Kein Druck auf die Arterien. Keine Kompression auf den Vagusnerv.
[03:38] Nach der ersten Nacht habe ich ehrlich gesagt nicht viel erwartet.
[03:41] Aber als ich aufgewacht bin, war da dieser eine Moment, so zwei, drei Sekunden, wo ich meinen Kopf gedreht habe und nichts passierte.
[03:47] Kein sofortiger Schwindel. Keine Panik. Nach sieben Nächten bin ich wieder mit dem Hund rausgegangen.
[03:51] Ganz normal, wie immer. Und auf dem Rückweg habe ich gemerkt, ich hatte die ganze Zeit nicht an meinen Schwindel gedacht.
[03:56] Zum ersten Mal seit Monaten. Nach zwei Wochen saß ich beim Frühstück und plötzlich ist mir aufgefallen, meine Hände kribbelten nicht mehr.
[04:02] Dieses ständige Kribbeln in den Fingern, das mich monatelang begleitet hatte.
[04:06] Als hätte ich permanent in eine Steckdose gefasst. Einfach weg.
[04:09] Nach einem Monat bin ich mit meinem Mann einkaufen gefahren. Ganz normal, wie früher.
[04:12] Wir stehen an der Kasse bei Rewe und jemand spricht mich von hinten an.
[04:15] Ich drehe den Kopf schnell, ohne nachzudenken. Nichts. Kein Schwindel. Keine kribbelnden Hände.
[04:20] Kein Festhalten am Einkaufswagen. Ich habe meinem Mann nur kurz in die Augen geschaut und er hat sofort verstanden.
[04:25] Und nachts? Das grundlose Herzrasen, das mich monatelang um drei Uhr morgens wachgemacht hat? Einfach nicht mehr da.
[04:31] Ich schlafe durch. Ich wache entspannt auf. Acht Stunden Regeneration jede Nacht. Das hat mir mein Leben zurückgegeben.
[04:37] Wenn du das hier siehst, während sich der Raum anfühlt, als würde er sich bewegen, du bist nicht verrückt.
[04:41] Deine Tests können normal sein. Dein MRT kann perfekt sein. Und du kannst trotzdem schwindelig, erschöpft oder panisch sein.
[04:47] Weil niemand das prüft, was es tatsächlich verursacht.
[04:50] Dein Kopfkissen beeinflusst einfach alles. Gleichgewicht, Blutfluss, Nerven.
[04:54] Das Unternehmen ist österreichisch. Das Kissen entwickelt mit einem deutschen Chiropraktiker.
[04:58] Kein billiges China-Produkt. Ich habe gerade gesehen, dass sie aktuell einen limitierten 40% Rabatt anbieten.
[05:03] Ich habe damals den vollen Preis bezahlt. Du musst das nicht.
[05:06] Außerdem bieten sie eine 30 Tage Geld-zurück-Garantie. Das ist ein ganzer Monat zum Testen.
[05:11] Ich bin kein Arzt. Ich verkaufe diese Kissen nicht. Ich bekomme keine Provision.
[05:14] Aber ich weiß, wie viele Menschen wie Zombies rumlaufen.
[05:17] Aber eins ist wichtig. Bestellen nur auf der offiziellen Webseite.
[05:21] Ich habe Nachahmerprodukte auf Amazon und Ebay gesehen, die ähnlich aussehen.
[05:24] Aber das sind billige Kopien, die nicht funktionieren.
[05:27] Meine Freundin hat so eine Fälschung gekauft, musste 15 Tage auf das Kissen warten und es war dann komplett nutzlos.
[05:32] Wenn du unten auf dieser Seite noch den Link oder auch den Button sehen kannst, hast du Glück.
[05:36] Das bedeutet, die Aktion läuft noch.
[05:38] Ein Bekannter von mir hat eine Woche gewartet und den letzten Sale total verpasst.
[05:42] Bei 40% Rabatt würde ich also nicht warten.
[05:44] Wenn du mehr erfahren willst, dann klicke einfach auf den Link unter diesem Video.
[05:50] Untertitel von Stephanie Geiges
```

### K02-B1 – Referenz K02-091 (Ad 107108716, [share_url](https://app.gethookd.ai/share/ad/107108716?signature=22fa77c2ee57cb148ce3f9f43c67b182cf97dd2c463c5e45bb11a658499ddfd9), Länge 311 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Das ist die schlechteste Schlafposition und wie du stattdessen schlafen solltest.
[00:03] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule
[00:07] und klemmst dabei deinen Ischiasnerv ab.
[00:09] Falls du nachts also aufwachst, weil dein Bein brennt, du Taubheitsgefühle vom Gesäß
[00:13] bis in die Zehen hast oder dich das stechende Ziehen aus dem Schlaf reißt, dann liegt das
[00:17] höchstwahrscheinlich an deiner Schlafposition.
[00:19] Wenn du auf der Seite schläfst, ohne die richtige Unterstützung, dann kippt deine Hüfte
[00:23] über und deine Wirbelsäule verdreht sich.
[00:25] Das bedeutet, deine Wirbelsäule liegt die ganze Nacht in einer ungesunden, verdrehten
[00:29] Position, auch posturale Schlaffehlstellung genannt.
[00:32] Und du merkst es nicht mal.
[00:33] Und diese dauerhaft falsche Schlafposition löst eine regelrechte Kettenreaktion aus.
[00:38] Denn sobald dein Becken verdreht wird, verkrampft sich dein piriformes Muskel und klemmt dabei
[00:42] deinen Ischiasnerv ein.
[00:43] Wie mit einer Zange, die sich nicht mehr löst.
[00:45] Der Ischiasnerv ist der längste Nerv in deinem Körper und verläuft vom unteren Rücken
[00:50] bis in die Zehen.
[00:51] Und wenn dieser Nerv jede Nacht 6, 7 oder sogar 8 Stunden eingequetscht wird, dann können
[00:56] die elektrischen Signale nicht mehr richtig fließen.
[00:58] All das führt zu einem ständigen Nervendruck.
[01:00] Ausgerechnet in der Zeit, in der dein Körper eigentlich heilen sollte.
[01:03] Und daher kommt auch das Taubheitsgefühl in den Beinen, das Kribbeln im Fuß und dieses
[01:07] brennende Ziehen, das vom Gesäß bis in die Wade strahlt.
[01:10] Das alles ist nicht nur extrem unangenehm und schmerzhaft, sondern auch eine tickende
[01:14] Zeitbombe.
[01:15] Ignorierst du das, dann riskierst du nicht nur vorübergehende Schmerzen, sondern eine
[01:19] ernsthafte Nervenschädigung sowie den Verlust von Gefühl und Beweglichkeit.
[01:23] Einige meiner Patientinnen haben allein durch diesen wiederholten Druck während des Schlafens
[01:27] die Kontrolle über ihre Beine oder Füße verloren.
[01:30] Nach und nach wirkt sich das alles auf deine Stimmung, Energie und deine Produktivität
[01:35] aus, was letztlich heißt, dass du dein Leben nicht so genießen kannst, wie du es möchtest
[01:39] und wie du und deine Familie es eigentlich verdient haben.
[01:42] Schließlich wachst du nachts ständig auf, weil dein Bein brennt oder taub ist und du
[01:46] es verzweifelt ausschütteln musst, nur um das Gefühl zurückzubekommen.
[01:49] Also, wie können wir am besten den Druck vom Ischias lösen?
[01:52] Nun, wenn du nachts schläfst, ist es entscheidend, dass deine Wirbelsäule in einer neutralen
[01:56] Position bleibt.
[01:57] Dies verhindert den Druck auf deinen Ischiasnerv, wodurch du in der Nacht endlich wieder durchschlafen
[02:02] kannst, ohne mit Schmerzen im unteren Rücken und Kribbeln im Bein aufzuwachen.
[02:06] Aber wie halten wir Hüfte, Rücken und Beine in der richtigen Position?
[02:09] Naja, indem wir zwar auf der Seite schlafen, aber mit der richtigen Unterstützung.
[02:13] Herkömmliche Kissen oder typische Kniekissen sind hier keine große Hilfe.
[02:17] Sie rutschen in der Nacht oft weg, verlieren ihre Form und bieten einfach keinen Halt,
[02:21] sodass dein Rücken völlig ungestützt bleibt.
[02:23] Das verschlimmert die Schmerzen nur.
[02:24] Und genau aus diesem Grund hat ein renommierter deutscher Chiropraktiker gemeinsam mit einem
[02:28] österreichischen Gründerteam 18 orthopädische Seitenschläferkissen getestet und dabei auch
[02:33] über 300 Nutzerbewertungen analysiert.
[02:35] Nach 9 Monaten Entwicklungszeit und 6 Prototypen entstand vor 2 Jahren schließlich das Schlaftherapiekissen.
[02:41] Ein orthopädisches Ganzkörperkissen, das genau dort entlastet, wo die meisten Beschwerden
[02:46] entstehen.
[02:47] Im Übergang von Hüfte, Wirbelsäule und Beine.
[02:49] Das heißt, durch das intelligente 3-Zonen-Stützsystem kehren Hüfte, Wirbelsäule und Beine somit
[02:54] wieder in die natürliche Ausrichtung zurück.
[02:57] Außerdem stellen die eigens entwickelten kühlenden Bezüge aus Baumwolle und Bambus
[03:00] sicher, dass du nachts nicht schwitzt und ständig die Position wechseln musst, was
[03:04] meist bei nächtlichen Hitzewallungen der Fall ist.
[03:07] Im Gegensatz zu einem normalen Kissen oder sogenannten Kniekissen bleibt das Schlaftherapiekissen
[03:12] also die ganze Nacht an seinem Platz und stützt deinen Körper von allen Seiten.
[03:15] Und genau das passiert, wenn du anfängst mit dem Schlaftherapiekissen zu schlafen.
[03:19] Nacht 1.
[03:20] Du wachst das erste Mal seit langem ohne Ischias oder Hüftschmerzen auf.
[03:24] Woche 1.
[03:25] Die Taubheitsgefühle in deinem Bein verschwinden und die Verspannungen in deinem unteren Rücken
[03:29] und Gesäß lösen sich.
[03:30] Du schläfst endlich wieder erholsam durch.
[03:32] Woche 2.
[03:33] Keine chronischen Schmerzen mehr.
[03:35] Dein Alltag wird endlich wieder schmerzfrei.
[03:36] Nach 2 Wochen mit dem Kissen kann ich sagen, dass ich jetzt endlich wieder ungestört durchschlafen
[03:41] kann und morgens wieder ohne Schmerzen aufwachen.
[03:44] Rund 89% der KundInnen berichteten bereits nach den ersten Nächten von einer spürbaren
[03:49] Linderung ihrer chronischen Ischias-Schmerzen sowie den Taubheitsgefühlen im Bein und Fuß.
[03:54] Und nach etwas mehr als 14 Tagen waren die Beschwerden meist vollständig verschwunden.
[03:58] Viele dieser Personen waren anfangs skeptisch, da sie bereits schon einiges ausprobiert hatten.
[04:03] Doch nachdem sie die vielen positiven Bewertungen und einzigartige Garantie sahen, haben sie
[04:07] sich entschieden, dem Schlaftherapiekissen eine Chance zu geben.
[04:10] Das sehr ambitionierte Team hinter dem Kissen bietet nämlich ein Versprechen an, das kein
[04:15] Pharmakonzern oder Arzt jemals geben würde.
[04:17] Wenn du nach 30 Nächten mit dem Schlaftherapiekissen keinen großen Unterschied bei deinen Taubheitsgefühlen
[04:23] oder deinen Ischias-Schmerzen spürst, bekommst du dein volles Geld rückerstattet.
[04:27] Klicke jetzt also einfach auf den Link unter diesem Video, um dein Schlaftherapiekissen
[04:31] noch heute zu bestellen.
[04:32] So kannst du endlich wieder ungestört durchschlafen, am nächsten Tag schmerzfrei und ohne Kribbeln
[04:37] im Bein aufwachen und den Tag mit deinen Liebsten genießen.
[04:40] Oder du kannst weiterhin Nacht für Nacht deinen Ischias-Nerv und deine Wirbelsäule
[04:43] beschädigen, indem du ohne die richtige Unterstützung schläfst.
[04:47] Seitdem das Schlaftherapiekissen im Internet vorgestellt wurde, hat das Produkt mit über
[04:51] 18 Millionen Aufrufen auf TikTok einen unglaublichen Hype ausgelöst und war bereits viermal ausverkauft.
[04:57] Und deshalb ist der aktuelle Lagerbestand sehr limitiert.
[05:00] Klicke jetzt also unten auf den Link, um das Schlaftherapiekissen ganz ohne Risiko für
[05:04] 30 Nächte zu testen.
[05:06] Oder du bekommst dein Geld zurück.
[05:10] Bis zum nächsten Mal.
[05:11] 
```

### K02-B2 – Referenz K02-109 (Ad 104077018, [share_url](https://app.gethookd.ai/share/ad/104077018?signature=8afaf7baf82d8ef41c62dcca0eb0be2ce692166f1a0af52b8be08a8d18492239), Länge 318 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Wenn du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte Schäden in deiner Wirbelsäule.
[00:04] Sehe das jeden Tag.
[00:06] Menschen wachen mit stärkeren Schmerzen auf, mehr Steifheit im unteren Rücken, mehr Taubheitsgefühle in den Beinen.
[00:11] Und die meisten Betroffenen haben überhaupt keinen Plan, warum das eigentlich passiert.
[00:15] Aber ich kann dir ganz genau sagen, was passiert.
[00:17] Du schädigst deine eigene Wirbelsäule. Und zwar jede einzelne Nacht.
[00:20] Wenn du auf der Seite schläfst, ohne die richtige Unterstützung, dann fällt dein oberes Bein nach vorne.
[00:25] Dadurch verdreht sich deine Hüfte und deine untere Wirbelsäule.
[00:28] Und genau das klemmt dann deinen Ischiasnerv ein.
[00:30] Wie mit einer Zange. Und zwar 6, 7 oder oft sogar 8 Stunden lang.
[00:34] Und zwar jede einzelne Nacht.
[00:36] All das führt zu einem ständigen Nervendruck.
[00:38] Ausgerechnet in der Zeit, in der dein Körper eigentlich heilen sollte.
[00:41] Und die Folgen sind nicht nur vorübergehende Schmerzen, sondern eine ernsthafte Nervenschädigung sowie der Verlust von Gefühl und Beweglichkeit.
[00:47] Einige meiner Patientinnen haben allein durch diesen wiederholten Druck während des Schlafens die Kontrolle über ihre Beine oder Füße verloren.
[00:53] Was steckt also dahinter?
[00:54] Im Grunde handelt es sich hier um eine langsame Verdrehung der unteren Wirbelsäule, die durch eine schlechte Schlafhaltung verursacht wird.
[01:00] Auch Lumbaltorsion genannt.
[01:02] Es ist also kein Bandscheibenvorfall und auch kein Muskelriss.
[01:05] Es passiert quasi still und leise, Nacht für Nacht, während dein Körper ruhig liegt.
[01:09] Und es wird immer schlimmer.
[01:10] Nachdem ich jahrelang miterlebt habe, wie viele meiner Patientinnen Nacht für Nacht aufs Neue litten, begann ich nach einer echten Lösung zu suchen.
[01:17] Nach etwas, das die Wirbelsäule im Schlaf in der richtigen Position hält, ohne unzuverlässige Kniekissen, die nachts ständig verrutschen, ohne teure Spezialbetten und ohne, dass man auf dem Rücken schlafen muss.
[01:27] Also habe ich als Orthopäde Nachforschungen angestellt.
[01:30] Ich habe Schlafstudien analysiert und zahlreiche MRTs ausgewertet.
[01:34] Was ich dabei herausgefunden habe, war schockierend.
[01:36] Wenn Hüfte, Rücken und Beine nachts nicht richtig gestützt werden, fällt das oben liegende Bein nach vorne.
[01:41] Die Hüfte dreht sich.
[01:42] Und die untere Wirbelsäule wird in eine verdrehte Position gezwungen, die den Ischiasnerv stundenlang einklemmt.
[01:47] Und genau aus diesem Grund habe ich gemeinsam mit einem österreichischen Gründerteam 18 Seitenschläfer und Kniekissen getestet und dabei auch über 300 Nutzerbewertungen analysiert.
[01:57] Nach neun Monaten Entwicklungszeit und drei Prototypen entstand vor zwei Jahren schließlich das Schlaftherapiekissen.
[02:03] Ein orthopädisches Ganzkörperkissen, das genau dort entlastet, wo die meisten Beschwerden entstehen.
[02:07] Im Übergang von Hüfte, Wirbelsäule und Beine.
[02:10] Das heißt, durch das intelligente Drei-Zonen-Stützsystem kehren Hüfte, Wirbelsäule und Beine somit wieder in die natürliche Ausrichtung zurück.
[02:17] Also genau die Position, die dein Körper braucht, um den Druck vom Piriformis-Muskel und den Ischias zu nehmen.
[02:22] Der Piriformis ist ein kleiner Muskel tief im Gesäß, der deinen Ischiasnerv wie eine Klammer zusammendrücken kann.
[02:28] Und wenn sich der Piriformis entspannt, kann auch der Ischiasnerv endlich aufatmen und deine Wirbelsäule bekommt die Chance zu heilen.
[02:33] Das heißt, keine Medikamente, keine Schienen, nur die richtige Position die ganze Nacht lang.
[02:38] Und ich weiß, es gibt viele andere Kissen da draußen.
[02:41] Ein Kniekissen hält zwar deine Knie auseinander, aber es stützt nur einen einzigen Punkt.
[02:45] Und der Rest deines Körpers, also Kopf, Schultern, Hüfte und Rücken bekommt keinerlei Unterstützung.
[02:50] Dein Körper verdreht sich also trotzdem.
[02:52] Und billige Ganzkörperkissen, die haben keinerlei ergonomische Formgebung.
[02:55] Und besitzen oft eine minderwertige Füllung, die verklunkt oder bereits schon nach ein paar Wochen zusammensackt.
[03:01] Das Schlaftherapiekissen ist anders.
[03:03] Jede Zone hat die exakte Form und Festigkeit, um deinen Körper in neutraler Ausrichtung zu halten.
[03:08] Die Premium-Hohlfaserfüllung bleibt formstabil, Nacht für Nacht, kein Verklunken.
[03:12] Du legst dich hinein und dein Körper findet automatisch die richtige Position.
[03:16] Das ist der Unterschied zwischen irgendeinem Kissen und einem orthopädischen Therapiesystem.
[03:20] Und deshalb ist das Schlaftherapiekissen das einzige Kissen, das von echten Ärzten getestet und empfohlen wird.
[03:26] Außerdem stellen die eigens entwickelten kühlenden Bezüge aus Baumwolle oder Bambus sicher,
[03:30] dass du nachts nicht schwitzt und ständig die Position wechseln musst,
[03:33] was meist bei nächtlichen Hitzewallungen der Fall ist.
[03:36] Nach zwei Wochen mit dem Kissen kann ich sagen, dass ich jetzt endlich wieder ungestört durchschlafen kann
[03:41] und morgens wieder ohne Schmerzen aufwachen.
[03:43] Seit der Einführung des Schlaftherapiekissens haben bereits tausende Menschen in Deutschland, Österreich und der Schweiz
[03:49] echte, lebensverändernde Ergebnisse erzielt.
[03:51] Sie wachen mit weniger Druck im unteren Rücken auf, weniger Nervenschmerzen in den Beinen
[03:56] und mit mehr Kraft und Bewegungsfreiheit, ganz ohne Ängste und Beschwerden.
[03:59] Denn sobald deine Wirbelsäule richtig ausgerichtet ist, muss dein Körper nicht mehr gegen sich selbst ankämpfen.
[04:04] Ich kenne Menschen, die jahrelang gelitten und schon alles versucht haben
[04:07] und innerhalb weniger Nächte echte Schmerzlinderung erfahren haben.
[04:10] Stell dir mal kurz vor, du wachst morgen ohne diese stechenden, brennenden Schmerzen im Rücken oder den Beinen auf.
[04:16] Du schläfst die ganze Nacht durch, ohne dich hin und her zu wälzen oder aufzuwachen.
[04:19] Du gehst spazieren, sitzt auf dem Sofa oder gehst einfach deinem Alltag nach, ohne ständig an Schmerzen zu denken.
[04:25] Genau das erleben tausende Menschen gerade mit dem Schlaftherapiekissen.
[04:29] Und es kann auch bei dir so sein.
[04:30] Viele dieser Personen waren anfangs skeptisch, da sie bereits schon einiges ausprobiert hatten.
[04:34] Doch nachdem sie die vielen positiven Bewertungen und einzigartige Garantie sahen,
[04:38] haben sie sich entschieden, dem Schlaftherapiekissen eine Chance zu geben.
[04:42] Das sehr ambitionierte Team hinter dem Kissen bietet nämlich ein Versprechen an,
[04:45] das kein Pharmakonzern oder Arzt jemals geben würde.
[04:48] Wenn du nach 30 Nächten mit dem Schlaftherapiekissen keinen großen Unterschied bei deinen Rückenschmerzen spürst,
[04:54] bekommst du dein volles Geld rückerstattet.
[04:56] Seitdem das Schlaftherapiekissen im Internet vorgestellt wurde,
[04:59] hat das Produkt mit über 21 Millionen Aufrufen auf TikTok einen unglaublichen Hype ausgelöst
[05:05] und war bereits dreimal ausverkauft.
[05:07] Und deshalb ist der aktuelle Lagerbestand sehr limitiert.
[05:10] Klicke jetzt also unten auf den Link, um das Schlaftherapiekissen ganz ohne Risiko für 30 Nächte zu testen.
[05:15] Oder du bekommst dein Geld zurück.
```

### K05-B1 – Referenz K05-187 (Ad 74485763, [share_url](https://app.gethookd.ai/share/ad/74485763?signature=445d441d4f97c39e641c6c8dee7be327243afc43c3723eecf3f5ebf9d029f7a7), Länge 466 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] So hört Schnarchen sofort auf. So sieht dein verengter Atemweg aus, wenn du schnarchst.
[00:04] Die meisten Leute denken nämlich, Schnarchen wäre einfach nur lautes Atmen.
[00:07] Aber das ist leider völlig falsch. Hier ist was wirklich passiert.
[00:10] Dein Atemweg kollabiert langsam, als würdest du versuchen,
[00:13] acht Stunden lang durch einen halb zusammengedrückten Strohhalm zu atmen.
[00:17] Und genau das machst du jede einzelne Nacht.
[00:20] Das Ziel wäre eigentlich, von diesem Zustand hier zu diesem zu kommen.
[00:23] Doch genau das schaffen die meisten Lösungen eben nicht.
[00:26] Wenn nächtliches Schnarchen anfängt, Beziehungen zu belasten, folgt meist immer das gleiche Muster.
[00:31] Einer verdrängt das Problem. Und der andere verliert Nacht für Nacht den Schlaf.
[00:34] Und irgendwann dann auch die Geduld. Liebe macht blind, aber eben nicht taub.
[00:38] Über 90.000 Paare in Deutschland schlafen in getrennten Zimmern.
[00:42] Und zwar wegen einer einzigen Sache. Dem Schnarchen.
[00:45] Mit anderen Worten, wenn einer schnarcht, dann hören beide auf zu schlafen.
[00:48] Und das führt dann zu weitaus mehr als nur Müdigkeit und Schlafproblemen.
[00:52] Erst kommen die Streitereien, dann die emotionale Kälte.
[00:55] Und schließlich stirbt auch die Intimität, die man früher für selbstverständlich hielt.
[00:59] Bis sich schließlich einer von beiden in ein anderes Zimmer zurückzieht.
[01:02] Die meisten Leute probieren dann alle möglichen Notlösungen aus.
[01:05] CPAP-Geräte sind laut, teuer und der perfekte Nährboden für gefährliche Bakterien.
[01:10] Denn wenn man das Gerät nicht täglich reinigt, ziehst du mit jedem Atemzug gesundheitsgefährdende Keime direkt in deine Lungen.
[01:16] Nasenstrips sind oft komplett nutzlos.
[01:18] Sie helfen dir zwar besser durch die Nase zu atmen, aber was viele nicht wissen,
[01:22] Schnarchen passiert nicht in der Nase.
[01:23] Dann bleiben noch Mundpflaster übrig.
[01:25] Aber das ist die mit Abstand gefährlichste Option.
[01:28] Denn ein Mensch hat nämlich genau zwei Wege, um zu atmen.
[01:31] Und wenn du einen davon blockierst, na ja, dann verdoppelst du dein Erstickungsrisiko.
[01:35] Das ist etwa so, als würdest du den einzigen Notausgang in einem brennenden Gebäude abschließen.
[01:39] Und genau aus diesem Grund scheitern all diese Lösungen.
[01:42] Sie konzentrieren sich nämlich nicht auf die eigentliche Ursache des Schnarchens.
[01:46] Hier ist was wirklich passiert.
[01:47] Herkömmliche Kissen sind geometrisch nicht für den menschlichen Kopf ausgelegt.
[01:51] Das bedeutet, dein Nacken liegt die ganze Nacht in einer ungesunden, abgeknickten Position.
[01:55] Auch Zervikale Atemwegsblockade genannt.
[01:58] Und du merkst es nicht mal.
[01:59] Die meisten Leute denken, Schnarchen kommt von verstopften Nasennebenhöhlen oder Übergewicht.
[02:03] Aber normale Kissen stützen den Nacken nicht richtig.
[02:06] Er schwebt quasi die ganze Nacht in der Luft und knickt dabei ab.
[02:09] Und genau das löst eine gefährliche Kettenreaktion aus.
[02:12] Deine Halswirbelsäule knickt ab.
[02:14] Dein Unterkiefer fällt leicht nach hinten.
[02:16] Deine Zunge sinkt automatisch in Richtung Rachenraum.
[02:19] Und gleichzeitig senkt sich auch der weiche Gaumen.
[02:21] Du kannst dir das in etwa wie bei Dominosteinen vorstellen.
[02:24] Sobald die Halswirbelsäule abknickt, folgt der Rest automatisch, bis der gesamte Atemweg blockiert ist.
[02:30] Das heißt, dein Atemweg verengt sich dadurch massiv.
[02:32] Und die Luft muss sich durch eine immer enger werdende Passage zwängen.
[02:36] Stelle dir mal kurz vor, du versuchst dich durch eine schmale Tür zu zwängen.
[02:39] Während es dir zwar gelingt, deinen Körper hindurchzudrücken, verursacht die Reibung quietschende und kratzende Geräusche.
[02:45] Und genau das führt zu diesem lauten Schnarchgeräusch.
[02:47] Aber es geht nicht nur um den Lärm.
[02:49] Denn dieser nächtliche Kampf löst eine verheerende Kettenreaktion aus.
[02:52] Dein Sauerstoffgehalt im Blut sinkt rapide und dein Herz rast, um das auszugleichen.
[02:57] Gleichzeitig schickt dein Gehirn Paniksignale durch deinen Körper.
[03:00] Und deshalb wachen auch so viele Menschen mit Kopfschmerzen auf, fühlen sich total ausgelaugt,
[03:04] egal wie lange sie geschlafen haben, und kriegen diesen mentalen Nebel den ganzen Tag nicht los.
[03:09] Was noch schlimmer ist, der kumulierte Sauerstoffmangel lässt deinen Körper buchstäblich schneller altern.
[03:13] Studien zeigen nämlich, dass chronische Schnarcher bis zu 8 Jahre an gesunder Lebenszeit verlieren.
[03:18] Das heißt, wenn deine Zellen Nacht für Nacht ausgehungert werden, bricht dein Immunsystem zusammen.
[03:23] Dein Stoffwechsel wird langsamer und dein Risiko für ernsthafte Gesundheitsprobleme steigt massiv.
[03:28] Also wie können wir diese zervikale Atemwegsblockade lösen?
[03:31] Nun, wenn du nachts schläfst, ist es entscheidend, dass deine Halswirbelsäule in einer neutralen Position bleibt.
[03:36] Denke mal kurz an eine Reanimation.
[03:38] Was macht ein Rettungssanitäter als erstes, wenn jemand nicht mehr atmet?
[03:41] Er neigt den Kopf nach hinten und hebt das Kinn leicht an.
[03:44] Warum? Weil das sofort die Atemwege öffnet.
[03:46] Es macht buchstäblich den Unterschied zwischen Leben und Tod.
[03:49] Mit anderen Worten, die richtige Kopf- und Nackenposition entscheidet also darüber, ob Luft frei fließen kann oder nicht.
[03:55] Aber die Herausforderung ist, wie macht man das bequem, ohne teure Geräte, ohne komplizierte Anpassungen?
[04:00] Die Lösung ist nicht, Luft durch einen blockierten Durchgang zu zwingen, wie CPAP-Geräte es tun.
[04:05] Nicht mit Nasenstrips durch die Nase atmen zu wollen.
[04:07] Nicht gefährlich den Mund zuzukleben.
[04:09] Und auch nicht, sperrige verstellbare Geräte zu benutzen.
[04:12] Die Lösung liegt im Kissen selbst.
[04:14] Und genau aus diesem Grund hat ein renommierter deutscher Chiropraktiker gemeinsam mit einem österreichischen Gründerteam 21 orthopädische Kopfkissen getestet und dabei auch über 300 Nutzerbewertungen analysiert.
[04:25] Nach neun Monaten Entwicklungszeit und vier Prototypen entstand letztes Jahr schließlich das Nackentherapiekissen.
[04:31] Ein cervicales Nackenstützkissen, das den Nacken sanft in neutraler Position hält und die Atemwege die ganze Nacht offen hält.
[04:37] Durch das intelligente Drei-Zonen-Nackenstützsystem kehren Kopf, Nacken und Kinn somit wieder in die natürliche Ausrichtung zurück.
[04:44] Es zielt also direkt auf die eigentliche Ursache des Schnarchens ab.
[04:47] Das heißt, dank der ergonomischen Form wird deine Halswirbelsäule perfekt gestützt, ohne Hohlraum zwischen Kissen und Nacken.
[04:53] Dein Unterkiefer wird automatisch in der vorderen Position gehalten, sodass deine Zunge nicht in den Rachenraum rutschen kann.
[04:59] Und die geformte Kopfzone entlastet zusätzlich.
[05:02] Es gibt außerdem eine speziell integrierte Armablage, damit deine Arme bequem liegen und nicht zusätzlichen Druck auf Nacken und Schultern ausüben.
[05:09] Das Nackentherapiekissen sorgt also dafür, dass deine Atemwege weit geöffnet bleiben und genau solche Atemwegsblockaden nicht passieren.
[05:16] Und reduziert dein Schnarchen schon in der ersten Nacht.
[05:18] Egal ob du auf der Seite oder dem Rücken schläfst.
[05:21] Der atmungsaktive und kühlende Bezug stellt sicher, dass du nachts nicht schwitzt und ständig die Position wechseln musst.
[05:27] Was meist bei nächtlichen Hitzewallungen der Fall ist.
[05:29] Du kannst aber auch einfach deinen gewohnten Kissenbezug weiterverwenden.
[05:33] Normale Kissen sind oft einfach zu weich oder zu hart und lassen deine Halswirbelsäule absinken oder überstrecken, wodurch dein Kiefer nach hinten fällt.
[05:40] Sie bieten also einfach nicht die Rundum-Unterstützung, die dein Nacken und deine Halswirbelsäule eigentlich benötigt.
[05:46] Und genau das passiert, wenn du anfängst mit dem Nackentherapiekissen zu schlafen.
[05:50] Nacht 1.
[05:51] Du wachst auf und fühlst dich endlich wieder ausgeruht.
[05:53] Keine Kopfschmerzen mehr.
[05:55] Kein trockener Mund.
[05:56] Stattdessen hast du Energie und fühlst dich bereit für den Tag.
[05:59] Woche 1.
[06:00] Dein Partner schläft endlich wieder entspannt neben dir durch, anstatt mit Ohrstöpseln zu schlafen oder sich in ein anderes Zimmer zurückzuziehen.
[06:07] Die Anspannung zwischen euch löst sich.
[06:08] Woche 2.
[06:09] Du kommst voller Energie durch den Tag, während dein Partner dich anlächelt, statt genervt zu sein.
[06:14] Rund 91% der KundInnen berichteten bereits nach der ersten Nacht von einer spürbaren Reduktion ihres Schnarchens.
[06:20] Und nach etwas mehr als 14 Tagen schliefen die meisten völlig still und friedlich durch.
[06:25] Viele dieser Personen waren anfangs skeptisch, da sie bereits schon einiges ausprobiert hatten.
[06:29] Doch nachdem sie die vielen positiven Bewertungen und einzigartige Garantie sahen, haben sie sich entschieden, dem Nacken-Therapie-Kissen eine Chance zu geben.
[06:36] Das sehr ambitionierte Team hinter dem Kissen bietet nämlich ein Versprechen an, das kein CPAP-Gerätehersteller oder HNO-Arzt jemals geben würde.
[06:44] Wenn du nach 30 Nächten mit dem Nacken-Therapie-Kissen keinen großen Unterschied bei deinem Schnarchen spürst, bekommst du dein volles Geld rückerstattet.
[06:51] Klicke jetzt also einfach auf den Link unter diesem Video, um dein Nacken-Therapie-Kissen noch heute zu bestellen.
[06:56] So können du und dein Partner endlich wieder ungestört durchschlafen, ohne Schnarchgeräusche, ohne getrennte Zimmer und ohne erschöpft in den Tag zu starten.
[07:04] Oder du kannst weiterhin Nacht für Nacht deine Atemwege blockieren und deinen Körper von lebenswichtigem Sauerstoff abschneiden, indem du ohne die richtige Unterstützung schläfst.
[07:13] Seitdem das Nacken-Therapie-Kissen im Internet vorgestellt wurde, hat das Produkt mit über 18 Millionen Aufrufen auf TikTok einen unglaublichen Hype ausgelöst und war bereits dreimal ausverkauft.
[07:22] Und deshalb ist der aktuelle Lagerbestand sehr limitiert.
[07:25] Wenn du dieses Video also siehst, dann sind womöglich noch wenige Kissen verfügbar.
[07:29] Klicke jetzt also unten auf den Link, um das Nacken-Therapie-Kissen ganz ohne Risiko für 30 Nächte zu testen oder du bekommst dein Geld zurück.
```

### K05-B2 – Referenz K05-189 (Ad 90347406, [share_url](https://app.gethookd.ai/share/ad/90347406?signature=9843ec84451f8ab4d8f6d7c915e1eb52bb5b8d759d46b6d1eca873a92bd27c89), Länge 80 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Wir haben einen Schlafapnoe-Patienten gebeten, sieben Tage lang mit dem Nacken-Therapie-Kissen zu schlafen.
[00:04] Und das ist passiert.
[00:06] In der ersten Nacht reagiert sein Körper auf eine Weise, wie es keine Maschine jemals schaffen könnte.
[00:10] Denn ein CPAP-Gerät behebt nicht die wahre Ursache der Schlafapnoe.
[00:14] Es pustet lediglich Luft durch ein verstopftes Rohr, wie etwa ein Laubbläser.
[00:18] Und am Ende ist die Verstopfung immer noch da.
[00:20] Dabei ist das eigentliche Problem nicht die Atmung, sondern die Anatomie.
[00:23] Herkömmliche Kissen sind geometrisch nicht für den menschlichen Kopf ausgelegt.
[00:27] Das bedeutet, dein Nacken liegt die ganze Nacht in einer ungesunden, abgeknickten Position,
[00:31] auch Zervikale Atemwegsblockade genannt, und du merkst es nicht mal.
[00:35] Und wenn der Nacken die ganze Nacht lang keine Stütze hat,
[00:37] zieht die Schwerkraft Kiefer und Zunge nach hinten und die Atemwege kollabieren.
[00:41] Und genau hier kommt das Nacken-Therapie-Kissen ins Spiel.
[00:43] Ein zervikales Nackenstützkissen, das Kopf, Nacken und Kinn sanft in neutraler Position hält,
[00:49] damit die Atemwege die ganze Nacht offen bleiben.
[00:51] Das heißt, durch das intelligente Drei-Zonen-Nackenstützsystem
[00:54] kehren Kopf, Nacken und Kinn somit wieder in die natürliche Ausrichtung zurück.
[00:58] Kein Luftdruck, keine Schläuche, nur eine strukturelle Lösung für ein strukturelles Problem.
[01:03] Innerhalb einer Woche schlief der Mann wieder die ganze Nacht durch, ohne nach Luft zu schnappen.
[01:07] Seine Frau sagte zu ihm sogar, er würde gefühlt 10 Jahre jünger aussehen,
[01:10] und zwar einfach nur durch echten, erholsamen Schlaf.
[01:13] Klicke unten auf den Link, um das Nacken-Therapie-Kissen ganz ohne Risiko für 30 Nächte zu testen,
[01:18] oder du bekommst dein Geld zurück.
```

### K09-B1 – Referenz K09-238 (Ad 74485768, [share_url](https://app.gethookd.ai/share/ad/74485768?signature=b03d7e13a07ea52d0ae08ad055ded9040e093e7e6852caeb1940ba6d9a8ef3fe), Länge 401 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Das ist die schlechteste Schlafposition. Und wie du stattdessen schlafen solltest.
[00:04] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ischias Schmerzen zu lindern, oder?
[00:09] Falsch.
[00:10] Okay. Also sollte man auf dem Rücken schlafen, richtig?
[00:12] Leider nein.
[00:13] Warte mal. Heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:17] Genau. Wenn du Seitenschläfer bist und morgens mit brennenden Hüftschmerzen aufwachst,
[00:21] die sich anfühlen wie glühende Nadeln in deiner Gesäßtasche,
[00:24] dein unterer Rücken so steif ist, dass du dich beim Aufstehen am Nachttisch abstützen musst
[00:28] und diese stechenden Schmerzen wie Stromschläge von deinem Po bis in deine Zehen schießen,
[00:33] dann quetschst du deinen Ischiasnerv ein, und zwar acht Stunden lang,
[00:36] und das jede einzelne Nacht wie eine Hydraulikpresse, die langsam aber stetig zudrückt.
[00:41] Das ist nicht nur extrem unangenehm und schmerzhaft, sondern auch eine tickende Zeitbombe.
[00:45] Ignorierst du diese Warnsignale, dann stehen dir drei brutale Konsequenzen bevor.
[00:49] Erstens, chronische Ischias Schmerzen, die dich die nächsten 20 Jahre begleiten werden.
[00:53] Du wirst zu den 6,3 Millionen Deutschen gehören, die täglich Schmerzmittel schlucken, nur um durch den Tag zu kommen.
[00:59] Zweitens, dauerhafte Rückenprobleme, weil deine Bandscheiben verschleißen.
[01:02] Deine L4- und L5-Bandscheiben, die wichtigsten Stoßdämpfer deiner Wirbelsäule,
[01:07] trocknen aus wie alte Gummiringe und bekommen Risse.
[01:09] Und drittens, eine teure Bandscheibenoperation, bei der sie dir Titanschrauben in die Wirbelsäule bohren.
[01:14] Aber warum passiert das überhaupt?
[01:16] Naja, wenn du auf der Seite schläfst, ohne die richtige Unterstützung,
[01:19] dann kippt deine Hüfte über, deine Wirbelsäule verdreht sich und dein Ischiasnerv wird regelrecht eingequetscht.
[01:25] Mit jedem Atemzug und mit jeder kleinen Bewegung im Schlaf, reibt der Nerv gegen die Knochen.
[01:30] Nach zwei Stunden beginnt die Entzündung, nach vier Stunden schwillt er an
[01:33] und nach acht Stunden ist er so gereizt, dass schon die kleinste Bewegung Schmerzblitze auslöst.
[01:38] Diese verdrehte Haltung, auch Posturale Schlaffehlstellung genannt, passiert jede einzelne Nacht.
[01:43] Aber wie können wir diese Posturale Schlaffehlstellung endlich stoppen?
[01:46] Nun, damit deine Wirbelsäule während des Schlafens in einer neutralen Position bleibt
[01:50] und deine Hüfte nicht verdreht wird, ist es wichtig, dein oberes Bein anzuheben.
[01:54] Dein Körper benötigt schließlich Unterstützung.
[01:56] Herkömmliche Kissen oder sogenannte Kniekissen sind hier keine große Hilfe.
[02:00] Sie rutschen in der Nacht oft weg, verlieren ihre Form und sind nach 30 Minuten bereits plattgedrückt wie ein Pfannkuchen.
[02:06] Und wenn du morgens dann aufwachst, liegt es höchstwahrscheinlich auf dem Boden.
[02:10] Konkret bedeutet das also, dass dein Rücken acht Stunden völlig ungestützt ist.
[02:14] Was wiederum heißt, deine Hüfte kippt wieder nach vorne und dein Ischiasnerv wird erneut eingequetscht.
[02:19] Du wachst daher trotzdem wieder mit Schmerzen auf.
[02:21] In Wahrheit verschlimmerst du die Fehlstellung sogar, weil das verrutschte Kissen deinen Körper dann in eine noch viel unnatürlichere Position zwingt.
[02:28] Und genau aus diesem Grund wurde mithilfe eines renommierten deutschen Chiropraktikers an einer Lösung gearbeitet.
[02:33] Nach fünf verworfenen Prototypen und Tests mit 312 Schmerzpatienten entstand schließlich das Schlaftherapiekissen.
[02:40] Es sorgt dafür, dass genau solche Fehlstellungen nicht passieren und bietet sofortige Linderung für deine Schmerzen schon in der ersten Nacht.
[02:47] Dabei arbeitet das intelligente 3-Zonen-Stützsystem präzise an drei kritischen Bereichen.
[02:52] Zone 1 stabilisiert deine Hüfte in einem exakten 90-Grad-Winkel, damit dein Körper sich nicht mehr verdreht.
[02:58] Dann kommt Zone 2 ins Spiel, die für deine Beine zuständig ist.
[03:01] Dabei hebt sie dein oberes Knie genau 15 cm an, der biomechanische Sweet Spot, bei dem dein Ischiasnerv maximalen Raum bekommt.
[03:09] Und zuletzt Zone 3 für deinen Rücken.
[03:11] Die eingebaute Lendenwirbelstütze stabilisiert deinen unteren Rücken seitlich wie eine unsichtbare Hand, die dich die ganze Nacht stützt.
[03:17] Es zielt also direkt auf die eigentliche Ursache der Schmerzen ab.
[03:20] Im Gegensatz zu einem normalen Kissen oder sogenannten Kniekissen bleibt das Schlaftherapiekissen die ganze Nacht an seinem Platz.
[03:26] Selbst wenn du dich im Schlaf bewegst, führt das ergonomische Design deine Hüfte und Knie automatisch wieder zurück in die neutrale Position.
[03:34] Wie Schienen, die einen Zug auf der Spur halten.
[03:36] Und der Effekt ist sofort spürbar.
[03:38] Du legst dich hin, positionierst das Kissen zwischen deinen Beinen und spürst, wie dein Ischiasnerv zum ersten Mal seit Monaten aufatmet.
[03:45] Dieser konstante Druck, der dich wahnsinnig gemacht hat, ist weg.
[03:48] Es ist, als würdest du endlich deine festen Schuhe ausziehen, die du den ganzen Tag getragen hast.
[03:53] Deine Hüfte entspannt sich dabei, dein Piriformis-Muskel lässt los und die Spannung in deinem unteren Rücken schmilzt weg wie ein Eis in der Sonne.
[04:00] Und genau das passiert, wenn du es benutzt.
[04:02] Nacht 1. Du wachst das erste Mal seit langem ohne Ischias oder Hüftschmerzen auf.
[04:06] Woche 1. Die Verspannungen in deinem unteren Rücken lösen sich und du schläfst endlich wieder erholsam durch.
[04:12] Woche 2. Keine chronischen Schmerzen mehr. Dein Alltag wird endlich wieder schmerzfrei.
[04:16] Nach zwei Wochen mit dem Kissen kann ich sagen, dass ich jetzt endlich wieder ungestört durchschlafen kann und morgens wieder ohne Schmerzen aufwachen.
[04:24] Rund 92% der KundInnen berichteten bereits nach der ersten Nacht von einer spürbaren Linderung ihrer Ischias und Hüftschmerzen.
[04:32] Und nach etwas mehr als 14 Tagen waren die Beschwerden meist vollständig verschwunden.
[04:36] Viele dieser Personen waren anfangs skeptisch, da sie bereits schon einiges ausprobiert hatten.
[04:41] Von Akupunktur über Chiropraktika bis hin zur Physiotherapie.
[04:45] Du hast wahrscheinlich die Visitenkarten von 5 verschiedenen Therapeuten in deiner Schublade und jedes Mal hoffst du, dass es endlich aufhört.
[04:51] Aber du wirst leider trotzdem enttäuscht. Und vielleicht denkst du dir, warum sollte ausgerechnet ein Kissen helfen, wenn selbst teure Behandlungen versagt haben.
[04:58] Und weißt du was? Das Gründerteam hinter dem Schlaftherapie-Kissen weiß genau, wie du dich fühlst.
[05:02] Und genau deshalb gehen sie einen Schritt, den die wenigsten Unternehmen gehen würden.
[05:06] Das sehr ambitionierte Team hinter dem Kissen bietet nämlich ein Versprechen an, das kein Pharmakonzern oder Arzt jemals geben würde.
[05:13] Wenn du nach 30 Nächten mit dem Schlaftherapie-Kissen keinen großen Unterschied bei deinen Rückenschmerzen spürst, bekommst du dein volles Geld rückerstattet.
[05:20] Klicke jetzt also einfach auf den Link unter diesem Video, um dein Schlaftherapie-Kissen noch heute zu bestellen.
[05:25] Das heißt, heute Nacht schläfst du zwar noch mit Schmerzen ein, aber schon nächste Woche könntest du zum ersten Mal seit Monaten ohne dieses brennende Ziehen in der Hüfte aufwachen.
[05:34] Du hast jetzt also zwei Optionen. Option 1, du machst weiter wie bisher und schläfst jede Nacht 8 Stunden in der falschen Position.
[05:41] Dabei zerquetschst du deinen Ischiasnerv Millimeter für Millimeter.
[05:44] In 6 Monaten wirst du dann höchstwahrscheinlich nicht mehr ohne starke Schmerzmittel auskommen und in einem Jahr dann mit deinem Arzt bereits über eine riskante Operation diskutieren.
[05:52] Oder Option 2, du investierst in deine Gesundheit und testest das Kissen risikofrei für 30 Nächte.
[05:57] Mit anderen Worten, entweder deine Schmerzen verschwinden oder du bekommst dein Geld zurück.
[06:01] Die Entscheidung liegt bei dir, aber bedenke, jede weitere Nacht ohne richtige Unterstützung ist eine Nacht, in der du deinen Nerven und Gelenken irreparablen Schaden zufügst.
[06:10] Der Ischiasnerv verzeiht nicht. Und was heute noch heilbar ist, kann morgen bereits chronisch sein.
[06:15] Und hier kommt noch etwas, was du wissen musst.
[06:17] Seitdem das Schlaftherapie-Kissen im Internet vorgestellt wurde, hat das Produkt mit über 21 Millionen Aufrufen auf TikTok einen unglaublichen Hype ausgelöst und war bereits dreimal ausverkauft.
[06:26] Und deshalb ist der aktuelle Lagerbestand sehr limitiert.
[06:29] Wenn du dieses Video also siehst, dann sind womöglich noch wenige Kissen verfügbar.
[06:33] Klicke jetzt also unten auf den Link, um das Schlaftherapie-Kissen ganz ohne Risiko für 30 Nächte zu testen oder du bekommst dein Geld zurück.
```

### K11-B1 – Referenz K11-247 (Ad 92876643, [share_url](https://app.gethookd.ai/share/ad/92876643?signature=dcb43cc2149ff983bc159740405b5d73b252067a05076371cf492914d5e2612b), Länge 341 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Das ist die schlechteste Schlafposition bei Nackenschmerzen und wie du stattdessen schlafen solltest.
[00:04] Was diese zwei MRT-Bilder aus Österreich aufgedeckt haben, hat alles verändert, was wir über Nackenschmerzen glaubten.
[00:10] Links auf dem Bild siehst du eine Patientin mit einem Bandscheibenvorfall zwischen den Halswirbeln C5 und C6.
[00:17] Und rechts eine scheinbar völlig gesunde Wirbelsäule.
[00:20] Doch hier kommt das Schockierende.
[00:21] Die Patientin rechts mit dem gesunden Bild hatte die schlimmsten chronischen Nackenschmerzen und das seit über vier Jahren.
[00:28] Jeden Morgen wachte sie mit steifen Nacken und brennenden Schmerzen auf, die bis in die Finger ausstrahlten.
[00:33] Trotz Physiotherapie, trotz Dehnübungen und trotz sogenannten orthopädischen Kissen.
[00:38] Doch die Ärzte meinten, es sei alles in Ordnung und schickten sie einfach nach Hause, mit dem Rat, sich mehr zu bewegen.
[00:43] Die traurige Wahrheit ist, die meisten Menschen achten auf ihre Haltung beim Sitzen, vermeiden stundenlanges nach unten schauen aufs Handy
[00:50] und machen regelmäßig Pausen am Schreibtisch, aber sie leben trotzdem jahrelang weiter mit ständigen Nackenschmerzen.
[00:56] Und das, obwohl sie alles befolgen, was ihnen der Arzt empfohlen hat.
[00:59] Wie kann das also sein?
[01:00] Weil sie kein Haltungsproblem und keine Verspannungen haben, sondern ein Schlafpositionsproblem.
[01:05] Der Schmerz fühlt sich vielleicht so an, als käme er aus dem Nacken und der Orthopäde empfiehlt vielleicht Dehnübungen oder eine neue Matratze.
[01:12] Aber in den meisten Fällen beginnt das Problem zu einem Zeitpunkt, an den niemand denkt, und zwar während du schläfst.
[01:18] Denn wenn du auf einem normalen Kissen schläfst, liegt deine Halswirbelsäule nicht in ihrer natürlichen Position.
[01:23] Sie wird entweder überstreckt oder abgeknickt und das Nacht für Nacht, acht Stunden lang.
[01:28] Dabei werden die empfindlichen Nervenbahnen zwischen den C5 und C6 Wirbeln gereizt, deine Muskulatur verkrampft sich und es entsteht ein ständiger Druck auf die Halswirbelsäule.
[01:37] Und genau das verursacht diesen tiefen, stechenden Schmerz im Nacken und den Schultern, der oft bis in die Arme ausstrahlt und zu diesem unangenehmen Kribbeln in den Fingern führt.
[01:47] Und hier kommt der entscheidende Teil.
[01:48] Diese nächtliche Schlaffehlstellung ist auf einem MRT nicht sichtbar.
[01:52] Darum wird sie von so vielen Ärzten vollkommen übersehen.
[01:55] Und die meisten Menschen leben dann jahrelang mit diesen Schmerzen weiter, weil sie nie die eigentliche Ursache beheben.
[02:01] Plötzlich werden selbst einfache Dinge wie den Kopf drehen, Auto fahren oder morgens aufstehen zur Qual.
[02:06] Irgendwann planst du deinen ganzen Tag nur noch um den Schmerz herum, weil schon die kleinste falsche Bewegung die Nackenschmerzen nur noch schlimmer machen.
[02:13] Und das Frustrierende daran ist, dass Massagen, Physio, sogar teure Matratzen meist nur kurzzeitig helfen.
[02:20] Denn keine dieser Methoden behebt die nächtliche Verkrümmung der Halswirbelsäule.
[02:23] Und daher kehrt der Schmerz auch immer wieder zurück.
[02:26] Denn normale Kissen sind oft einfach zu weich oder zu hart und lassen die Halswirbeln absinken oder überstrecken.
[02:32] Sie bieten also einfach nicht die Rundum-Unterstützung, die dein Kopf und Nacken eigentlich benötigt.
[02:37] Doch die gute Nachricht ist, dass es jetzt eine einfache Methode gibt, die deine Halswirbelsäule direkt während des Schlafs in ihre natürliche Position bringt.
[02:45] Der entscheidende Ansatz dabei ist, die Halswirbelsäule während des Schlafs zu stabilisieren, damit die umliegenden Nerven und Muskeln nicht weiter gereizt werden.
[02:52] Und genau hier kommt das Nackentherapiekissen ins Spiel.
[02:55] Es ist ein cervikales Nackenstützkissen, das genau dort entlastet, wo die meisten Beschwerden entstehen.
[03:00] Im Übergang von Kopf, Nacken und Schultern.
[03:03] Durch das intelligente 3-Zonen-Nackenstützsystem kehren Kopf, Nacken und Schultern somit wieder in die natürliche Ausrichtung zurück.
[03:10] Es zielt also direkt auf die eigentliche Ursache der Schmerzen ab.
[03:13] Das heißt, dank der ergonomischen Form wird deine Halswirbelsäule perfekt gestützt, ohne Hohlraum zwischen Kissen und Nacken.
[03:20] Und die geformte Kopfzone entlastet zusätzlich.
[03:22] Es gibt außerdem eine speziell integrierte Armablage, damit deine Arme bequem liegen und nicht die Schulter belasten.
[03:28] Das Nackentherapiekissen sorgt also dafür, dass genau solche Fehlstellungen nicht passieren und bietet sofortige Linderung für deine Schmerzen schon in der ersten Nacht.
[03:37] Und genau das passiert, wenn du anfängst mit dem Nackentherapiekissen zu schlafen.
[03:41] Nacht 1. Du wachst das erste Mal seit langem ohne Nacken- oder Schulterschmerzen auf.
[03:46] Woche 1. Die Verspannungen in deinem oberen Rücken und deinen Schulterblättern lösen sich und du schläfst endlich wieder erholsam durch.
[03:52] Woche 2. Keine chronischen Schmerzen mehr. Dein Alltag wird endlich wieder schmerzfrei.
[03:57] Schon in der ersten Nacht habe ich gemerkt, das hilft. Das hast du direkt gespürt.
[04:01] Ich bin morgens aufgewacht und dachte mir so, warte mal, Nacken tut gar nicht mehr weh.
[04:06] Nach zwei Wochen waren die kompletten Kopfschmerzen weg bei mir.
[04:10] Also einfach weg. Kein Hohlraum mehr zwischen Kissen und Nacken. Schultern werden entlastet und das Kribbeln im Arm ist auch endlich weg.
[04:17] Ich schlafe jetzt echt so gut wie seit langem nicht mehr und wache morgens erholt auf.
[04:22] Es hört sich vielleicht komisch an, aber dieses Kissen hat mir mein Leben zurückgegeben.
[04:26] Rund 92% der KundInnen berichteten bereits nach der ersten Nacht von einer spürbaren Linderung ihrer Nacken- und Schulterschmerzen sowie dem Kribbeln in den Armen.
[04:35] Und nach etwas mehr als 14 Tagen waren die Beschwerden meist vollständig verschwunden.
[04:39] Viele dieser Personen waren anfangs skeptisch, da sie bereits schon einiges ausprobiert hatten.
[04:44] Doch nachdem sie die vielen positiven Bewertungen und einzigartige Garantie sahen, haben sie sich entschieden, dem Nacken-Therapie-Kissen eine Chance zu geben.
[04:52] Das sehr ambitionierte Team hinter dem Kissen bietet nämlich ein Versprechen an, das kein Pharmakonzern oder Arzt jemals geben würde.
[04:58] Wenn du nach 30 Nächten mit dem Nacken-Therapie-Kissen keinen großen Unterschied bei deinen Schmerzen spürst, bekommst du dein volles Geld rückerstattet.
[05:06] Klicke jetzt also einfach auf den Link unter diesem Video, um dein Nacken-Therapie-Kissen noch heute zu bestellen.
[05:11] So kannst du endlich wieder ungestört durchschlafen, am nächsten Tag schmerzfrei aufwachen und den Tag mit deinen Liebsten genießen.
[05:17] Doch seit das Nacken-Therapie-Kissen im Internet vorgestellt wurde, hat das Produkt mit über 21 Millionen Aufrufen auf TikTok einen unglaublichen Hype ausgelöst und war bereits dreimal ausverkauft.
[05:27] Und deshalb ist der aktuelle Lagerbestand sehr limitiert.
[05:30] Klicke jetzt also unten auf den Link, um das Nacken-Therapie-Kissen ganz ohne Risiko für 30 Nächte zu testen.
[05:36] Oder du bekommst dein Geld zurück.
```

### K15-B1 – Referenz K15-284 (Ad 184804208, [share_url](https://app.gethookd.ai/share/ad/184804208?signature=7d33e0dc073a963320e547b052d17f23860b2c558e0e3b2648c57f0081fa2eae), Länge 422 s, Quelle: lokal, faster-whisper „small“ (Volltranskript))

```text
[00:00] Mitten in der Präsentation blieb mein Kopf einfach leer
[00:05] Kein Wort kam raus für 10 Gesichter starten mich an
[00:10] Ich dachte wirklich, das ist der Anfang von dem Mensch
[00:18] Aber lass mich am besten von vorn anfangen
[00:22] Früher war ich geistig für die Personen Meetings, die immer eine Antwort parat hatte
[00:28] Wie sich jeden Namen merkte, jeden Termin
[00:31] Aber um meinen 52. Geburtstag herum verschwand diese Person
[00:35] Es fing klein an, ich verlor den Faden mitten im Gespräch
[00:40] Lass dieselbe E-Mail dreimal ohne zu verstehen, was drin stand
[00:44] Stand im Supermarkt und wusste nicht mehr, was ich kaufen wollte
[00:48] Dann wurde es schlimmer, mir viel während deiner Präsentation das Wort Kalender
[00:53] Ich stand einfach da und zeigte auf die Wand 14 Kollegen starten mich an
[00:59] Ich verfuhr mich auf den Weg zu meiner Zahnärztin meiner Praxis
[01:03] Zu dir, ich seit 8 Jahren ging, ich fing an mir an, alles aufzuschreiben
[01:07] Ich konnte meinem eigenen Kopf nicht mehr trauen
[01:10] Ab 15 Uhr war ich jeden Tag völlig unbrauchbar
[01:13] Trank meinen 4. Kaffee, nur um mich halbwegs noch zu fühlen
[01:16] Ich dachte, das wäre einfach das Alter, so fühlt sich 54 Eben an
[01:21] Dann sagte mein Mann, etwas, das mich zu Tode erschreckte
[01:24] Du hast mir gestern dieselbe Frage dreimal in 10 Minuten gestellt
[01:27] Du konntest dich nicht erinnern, dass du sie schon gestellt hattest
[01:32] Da rief ich meine Neurologin an, ich saß in ihrer Praxis und war überzeugt
[01:36] Sie würde frühes Alzheimer diagnostizieren
[01:39] Ich hatte hinterlich schon angefangen zu trauen
[01:41] Um die Person, die ich einmal war, sie machte Tests MRT, kognitive Test, Blutbild
[01:47] Alles kam normal zurück, ihr Gehirn sieht gut aus, sagte sie
[01:51] Aber wie schlafen sie denn?
[01:54] Ich erzählte ihr vom Schnaschen, vom nächtlichen Luft
[01:57] Schnappen von der Schöpfung jeden Morgen, egal wie lange ich im Bett lag
[02:01] Sie mitte langsam haben sie jemals ein Schlaflabor gemacht
[02:05] Hätte ich nicht, ich dachte Schnaschen wären nur nervig
[02:08] Nicht gefährlich, 2 Wochen später wurde bei mir eine Mitte schweres Schlaf
[02:11] Hat nur diagnostiziert, ich hörte bis zu 9 20 Mal pro Stunde auf zu atmen
[02:16] Ihr Gehirn bekommt jede Nacht zu wenig Sauerstoff, erklärte sie
[02:19] Deswegen der Nebel, die Gedächtnis, Probleme, Diastopfung
[02:23] Ihr Gehirn ist stick, macht quasi
[02:26] Ich hatte vor erleichter Ruf fast geweint, es war keine Dement
[02:31] Es war behandelbar, sie verschrieb mir ein C-Papel-Gerät
[02:34] Die Gasse zahlte ein Basismodell, einfache Maske
[02:38] Laute Pumpe aber kostenlos, ich wartete darauf, dass mein Kopf wieder funktioniert
[02:43] Ja, der aber nicht konnte die Maske mich ertragen
[02:46] Diese Klaus-Trophobie war unerträglich, ich riss hingelangt
[02:49] Und zwar japanisch von Gesicht, Herzrasen nach Luft schnappen
[02:52] Also kaufte ich privat ein besseres Gerät, 890 Euro leisere Pumpe
[02:57] Angenehmere Maske, 4 Monate lang probierte ich 3 verschiedene Masken
[03:02] Hasenpuls auf voll Maske, nichts funktionierte, der Gehirn Nebel blieb
[03:06] Die Erschöpfung blieb, das Wort vergessen blieb
[03:09] Meine Ärztin schlug, eine Aufbesschine, verweiltere 2, 180 Euro
[03:14] Davon tat mir der Kiefer so weh, dass ich morgens kein festes Frühstück mehr essen konnte
[03:20] Und auf 14 Uhr kommt ich trotzdem nicht klardenken
[03:23] Ich probierte Nahrungsergänzungsmittel B12, Genggo, Omega 3
[03:29] Nichts, ich fing an zu akzeptieren, dass das jetzt einfach mein Leben ist
[03:33] Dass die scharfzinnige Frau, die ich mal war für immer, wer gestern letzten November war
[03:38] Ich auf den Geburtstag meiner Nichte, ein entfernter Kusel war da
[03:42] Klaus, ein pensionierter Physiotherapeut, er fragte warum, um mich so müde aussehe
[03:49] Ich erzählte ihm alles den Nebel, die Abnoe, das CPAP, dass ich nicht ertragen konnte
[03:55] Er hörte zu, dann sagte er, etwas, was mich aufhorschen ließ
[03:58] Hat sich schon mal jemand deinen Nacken angeschaut, er, er, er, er, er
[04:02] Er erklärte das Schnarchen für viele Menschen, gar kein Atemproblem ist
[04:07] Es ist ein Haltungsproblem
[04:10] Wenn dein Kopf macht's in dem falschen Winkelfeld, kollabiert
[04:14] Das weiche Gewebe im Hals nach hinten ist blockiert, die Atemwege, das Verursacht, die Abnoe
[04:19] Den Sauerstoff, Abfall, den Nebel, das CPAP, pressen nur durch eine blockierte Passage
[04:24] Aber du kennst die ganze Nacht gegen die Schwerkraft
[04:27] Deswegen können wir so viele nicht ertragen
[04:30] Ich startte ihn nach mir, dem Monat, hatte ich mich mit deinem Gerät gequält
[04:34] Das Niederführ gemacht, Wacht da, das eigentliche zu beheben, mein Gehirn war nicht kaputt
[04:39] Das bekam kein Sauerstoff, war mein Nacken falsch lag
[04:42] Noch am selben Abend recherchierte ich Studie, um Studie zeigte
[04:46] Die Position der Halswirbelsäule entscheidet, ob die Atemwege im Schlaf offen bleiben oder kollabieren
[04:54] Und mein Uhr 30 fand ich etwas, dass sich Nackentherapie-Kissenante entwickelt
[04:59] Um die Halswirbelsäule neutral zu halten, um zu verhindern, dass der Kopf nach hinten kippt
[05:04] Um die Atemwege offen zu halten
[05:07] Ich wollte sofort bestellen, ich erzählte niemanden davon
[05:12] Ich war zu oft enttäuscht worden, ich legte es einfach aufs Bild und ging schlafen
[05:19] Ich wachte um 6 Uhr, 7 und 40 auf und ich fühlte mich klar, mich benebeln
[05:25] Ich hatte zu dich durchnassen zum Endding, einfach klar
[05:29] Um 15 Uhr arbeitete ich immer noch, immer noch konzentriert, immer noch ich
[05:37] Ich fing an zu weinen, möchte drehen, weil ich vergessen hatte wie es sich anfühlt
[05:43] Mein Verstand zurückzuhaben, das war vor 6 Monaten der Nebel ist weg
[05:49] Das Wort hat vergessen, es weg, der 15 Uhr, Zusammenbruch ist weg
[05:56] Ich bin wieder scharf, wieder schnell die Person, von der ich dachte, ich hätte sie für immer verloren
[06:02] Alles nur, weil ich das eigentlich überhoben habe, nicht meine Atmen, meine Nackenposition
[06:07] Vielleicht hast du Angst, dass du deine Verstand verliest, vielleicht hast du das C-Pay-Pay probiert
[06:13] Und konntest es nicht ertragen, vielleicht hast du den Nebel einfach akzeptiert
[06:18] Wenn was auf dich zutrifft, probier das Nackentherapie, kissen, korrigier deine Nackenposition und zieh
[06:24] Was passiert, wenn dein Gehirn endlich wieder Sauerstoff bekommt, das Unternehmen ist höchsterreich
[06:30] Ich entwickelte von meinem deutschen Chiropraktiker aktuell
[06:34] Gibt es einen limitierten 40% Rabatt und deine 60 Tage Geld zurück, garantier'n
[06:39] Einen ganz hohen und zum Testen verschwindet der Nebel nicht
[06:42] Bekommst du jeden Cent zurück, aber Achtung, bestell nur auf der offiziellen Seite
[06:47] Mit der 60 Nächte Probeschlafen, Garantie auf Amazon und Ebay gibt es billige Falschungen, die nicht funktionieren
[06:58] Der Link ist unter diesem Video
```

### K16-B1 – Referenz K16-291 (Ad 181171395, [share_url](https://app.gethookd.ai/share/ad/181171395?signature=ab762f76ef1747b82a49586e253e210d67822676e368f492a4c9012b530ebabf), Länge 377 s, Quelle: lokal, faster-whisper „small“ (Volltranskript))

```text
[00:00] Wenn du morgens mit Schwinden laufst Deine arme Krippeln sobald du den Kopf drehst
[00:05] Und dir jeder Arzt sagt, alles ist völlig normal Dann schaue dir das unbedingt an
[00:10] Denn ich habe 18 Monate um ins Lebens verloren Und die bezahlten 400 Euro aus eigener Tasche bezahlt
[00:16] Bevor ich herausgefunden habe Was wirklich los war
[00:20] Ich bin 5, 50, früher war ich selbstständig Bin überall hingefahren, hatte mein Garten
[00:25] Und hab blieben gern auf meine Enkelinnen aufgepasst
[00:29] Dann fing der Schwindel an, kein Drehen eher Als würde der Boden unter mir pulsieren
[00:34] Als wäre die Schwerkraft kaputt Mein Hausarztensblut abnehmen
[00:38] Ordnet sein MRT an Überwiesen nicht zum Kardiologen
[00:42] Perfekt, ihr Gehirn sieht super aus Sie sind sehr gesund für ihr Alter
[00:49] Gesund? Ich konnte nicht mal an der Kasse
[00:52] Im Supermarkt stehen ohne mich an mein Kaufwagen festzuhalten
[00:56] Und die Symptome häuften sich morgens Schwinde Kopf nach links drehen
[01:00] Krippeln in den Händen zu schnell aufstehen Verschwammene Sicht
[01:04] Und jede Nacht Herzrasen als würde es aus der Brust springen
[01:10] Mein Mann meinte, vielleicht die Wechseljahr Mein Arzt, vielleicht Stress, eine Hyrolorie
[01:15] Vielleicht eine Angststörung Ich ertrank ihn vielleicht zum Cancer von Stimmte
[01:20] Der Tiefpunkt kam in der Gartenabteilung Ich wollte nur einen Sack Blumen Erde heben
[01:25] Jemand sprach mich von hinten an Ich trete den Kopf schnell nach links und die Welt
[01:31] Kippte zur Seite an dem Abend Hab ich unter der Dusche geweint, damit mein Mann es nicht hör
[01:36] Dann kam die Behandlungen, achtsitzungen Bestibuläre Therapie als Privatleistung
[01:42] Hieran 80 Euro macht es schlimmer Der nächste Arzt, innen noch Entzündung
[01:47] Verschrieb Cortison, nichts
[01:51] Denn der Psychiater Antidepressiv Die machten mich nicht schwindeliger und emotional
[01:55] Tauch, 6 Ärzte, 4 Spezialisten Über 2,400 Euro
[02:01] Und ich war immer noch schwindelig Ich hörte auf Auto zu fahren
[02:05] Die Supermärkte bei der Tanzaufführung meiner Enkelin hielt ich 6 Minuten durch
[02:11] Dann war es nicht die Bewegung, es drehen meines Kopfes
[02:14] Und dieses furchtbare, schwebende Gefühl kam zurück
[02:17] Ich saß den Rest auf dem Flur an einen Automaten gelehnt
[02:21] Meine Enkelin kam später raus, uma alles okay
[02:25] Du warst weg, ich war hier, sagte ich, aber das stimmte nicht
[02:29] In der Nacht 18.50 Uhr hab ich wieder gegoogelt und ich fand ein Fohrung
[02:34] Kein Artikel, ichte Menschen, gleiche Symptome, gleiche, normale Testergebnisse
[02:38] Gleiche Angst, jemand erwähnte etwas Namste wie Kogen, ein Schwindel ausgelöst
[02:43] Durch Verspannungen in den tiefen Nackenmuskeln Die Blutfluss und Nerven, Signale stürmen
[02:49] Nicht die Ohren, nicht das Gehirn, nicht das Herz, dein Nacken
[02:54] Und hier wurde mir alles klar, wenn dein Nacken nachts in einer verkunden Position liegt
[03:00] Verkumpfen die tiefen Muskeln rund um C1 und C2
[03:04] Die ganze Nacht um den Kopf zu stabilisieren Dabei dücken sie die Arterien zusammen
[03:09] Die zum Gehirnführung, der Vargos nervt, wird gereizt
[03:12] Und dein Nervensystem bekommt ständig Alarmsignale
[03:15] Obwohl keine echte Gefahr besteht
[03:19] Das erklärt den Schwindel, das Kribbeln
[03:22] Das Herz rasen die verschwommenen Sicht Dein Kommentar ließ nicht erstarren
[03:27] Die Spannung baut sich auf, während du schläft
[03:30] Stunden, jede Nacht in der falschen Position
[03:35] Und dann hat mein Kissen gewechselt
[03:37] Drei Wochen später waren die Symptome zu 80% weg
[03:41] Kein Arzt hat je nach meinem Kissen gefragt
[03:44] Ich starte auf dem Bildschirm, ich einer der sechs erste hatte je nach meinem Kissen gefragt
[03:49] Nicht ein einziges Mal, immer wieder tauchte derselbe Name auf
[03:54] Das Nackentherapie-Kissen entwickelt für genau dieses Problem mit deiner Hohlen
[03:59] Mitte, die den Druck von der Schädelbasis nimmt
[04:02] Hunderte farrifizierte Käufer dieselben Geschichten wie meine
[04:06] Ich hatte schon 200, 400 Euro für Antworten ausgegeben
[04:10] Was war schon ein Kissen?
[04:12] Ich bestellte es, als es ankam, kam ich mir lächerlich vor ein Kissen
[04:17] Nach all diesen Spezialisten, aber die erste Nacht fühlte sich an der Sonne
[04:22] Mein Kopf legte sich in die Hohle Mitte
[04:25] Der Hinterkopf hatte Platz
[04:26] Kein Druck auf die Arterien, keine Kompression auf den Vargosnerf
[04:30] Tag drei, der Druck an der Schädelbasis wurde welcher Tag sechs mit dem Hump spazieren
[04:36] Ohne dass der geweckwankte Tag zehn
[04:39] Das Kribbeln in den Händen hörte auf Tag 14
[04:42] Ich stand morgens auf, ohne dass die Welt wackelte Woche vier
[04:46] Ich fuhr allein zum Wochenmarkt nur Probleme
[04:50] Wenn man starte mich an, als würde erwarten, dass ich umkippe
[04:55] Du wirkst wieder normal, sagte er, ich fühlte mich auch so
[04:59] Das hab ich gelernt, deine Testkönnissen können normal sein
[05:03] Deinem Arzt hier immer gelos und du kannst trotzdem Schwinchlich erschöpft und verängst dich sein
[05:09] Weil niemand prüft, was es wirklich verursacht
[05:12] Als mein Kissen aufhörte, meinen Nacken zu komprimieren
[05:16] wurden meine Symptome nicht nur besser, sie verschwanden
[05:20] Letzte Woche stand ich wieder in der Garten und Teilung
[05:24] Hab den Sackblumen Erde gehoben, kein Schwinde
[05:27] Keine Kribbeln in Händen, keine Angst
[05:30] Wenn du das liest, während sich der Raum bewegt
[05:33] Du bist nicht verrückt, deine Tests sind nicht falsch
[05:36] Sie sind nur unvollständig
[05:39] Und dein Kissen könnte genau das sein, was niemand gebrüht hat
[05:45] Es wurde mit einem durchen Chiropraktiker
[05:47] Entwickelkade läuft ein limitierter 40%-Rabback
[05:50] Mit 60 Tage Geld zurück Garantie
[05:53] Zwei ganze Monate zum Testen
[05:55] Wenn der Schwinde nicht besser wird, bekommst du jeden Sinn zurück
[06:00] Also wenn du erschöpft bist, vom Schwinde der nicht weg geht
[06:03] Egal was du versuchst, vielleicht ist es Zeit
[06:06] Endlich den Nacken zu entlasten, statt weiter nach Ursachen zu suchen
[06:10] Die gar nicht da sind, der Link ist unter diesem Video
```

### K17-B1 – Referenz K17-296 (Ad 184804213, [share_url](https://app.gethookd.ai/share/ad/184804213?signature=05a7eb19d98fabd498b00d09faf6ca88390bc70df071f46880b135361e089e39), Länge 436 s, Quelle: lokal, faster-whisper „small“ (Volltranskript))

```text
[00:00] Ich war 54, als ich mir einen Termin beim Neurologen ausmachte
[00:06] Ich dachte wirklich, ich würde dem entwerden
[00:12] Mit einem Satz fielen mir keine Wörter mehr ein
[00:15] Ich stand in Zimmern und wusste nicht mehr warum
[00:17] Und nach 14 Uhr konnte ich mich einfach nicht mehr konzentrieren
[00:22] Aber es war nicht mein Gehirn, das kaputt ging
[00:27] Es war etwas, das Nachts mit meinen Nacken passierte
[00:32] Aber lass mich am besten von vorn anfangen
[00:36] Früher war ich geistig, fit
[00:38] Die Person in Meetings, die immer eine Antwort parat hatte
[00:41] Die sich jeden Namen merkte, jeden Termin
[00:44] Aber um meinen 52. Geburtstag herum verschwand diese Person
[00:48] Es fing klein an, ich verlor den Faden mitten im Gespräch
[00:54] Lass dieselbe E-Mail dreimal ohne zu verstehen was drin stand
[00:57] Stand im Supermatt und wusste nicht mehr, was ich kaufen wollte
[01:01] Dann wurde es schlimmer, mir viel während deiner Präsentation
[01:04] Das Wort Kalender, nicht mehr ein
[01:06] Ich stand einfach da und zeigte auf die Wand
[01:09] 14 Kollegen starten mich an
[01:12] Ich verfuhr mich auf den Weg zu meiner Zahnärztin
[01:15] meiner Praxis, zu dir ich seit acht Jahren ging
[01:17] Ich fing an, mir alle alles aufzuschreiben
[01:20] Ich konnte meinem eigenen Kopf nicht mehr trauen
[01:23] Ab 15 Uhr war ich jeden Tag völlig unbrauchbar
[01:26] Trank meinen vierten Kaffee, nur um mich halbwegs noch zu fühlen
[01:29] Ich dachte, das wär' einfach das Alter
[01:31] So fühl' sich 54 eben an
[01:34] Dann sagte mein Mann etwas, das mich zu Tode erschreckte
[01:37] Du hast mir gestern dieselbe Frage dreimal in zehn Minuten gestellt
[01:41] Du konntest dich nicht erinnern, dass du sie schon gestellt hattest
[01:46] Da rief ich meine Neurologin an
[01:47] Ich saß in ihrer Praxis und war überzeugt sie würde frühes Alzheimer diagnostizieren
[01:52] Ich hatte hinterlich schon angefangen zu trauen
[01:54] Um die Person, die ich einmal war
[01:57] Sie mochte Test, MRT, kognitive Testblutbild
[02:00] Alles kam normal zurück
[02:02] Ihr Gehirn sieht gut aus, sagte sie
[02:05] Aber wie schlafen sie denn?
[02:07] Ich erzählte ihr vom Schnaschen, vom nächtlichen Luft
[02:10] Schnappen von der Schöpfung jeden Morgen
[02:12] Egal wie lange ich im Bett lag
[02:14] Sie mehtelangsam haben sie jemals ein Schlaflabor gemacht
[02:18] Hätte ich nicht, ich dachte Schnaschen wären nur nervig
[02:21] Nicht gefährlich, zwei Wochen später wurde bei mir eine Mitte schwere Schlaf hat nur
[02:25] Diagnostiziert, ich hörte bis zu 9 20 Mal pro Stunde aufzuatmen
[02:29] Und ihr Gehirn bekommt jede Nacht zu wenig Sauerstoff, erklärte sie
[02:33] Deswegen der Nebel, die Gedächtnis, Probleme, die Erschöpfung
[02:36] Ihr Gehirn ist stick, Nacht quasi
[02:39] Ich hatte vor erleichter Ruf fast geweint
[02:42] Es war keine Dement, es war behandelbar
[02:44] Sie verschrieb mir ein C-Papel gerät
[02:47] Die Kasse zeilte ein Basismodell, einfache Maske
[02:51] Laute Pumpe aber kostenlos
[02:53] Ich wartete darauf, dass mein Kopf wieder funktioniert hat
[02:56] Ja, aber nicht konnte die Maske mich ertragen
[02:59] Diese Klaus-Trophobie war unerträglich
[03:01] Ich riss ihn im Nachts und zwei opanisch von Gesicht
[03:04] Herzrasen nach Luft schnappen
[03:06] Also kaufte ich privat ein besseres Gerät
[03:08] 890 Euro leisere Pumpe, angenehmere Maske
[03:12] Vier Monate lang probierte ich drei Verschieden
[03:14] Masken, Nasen, Puls auf voll Maske
[03:16] Nichts funktionierte, der Gehirn nebel blieb
[03:19] Die Erschöpfung blieb, das Wörter vergessen blieb
[03:22] Meine Ärztin schlug eine Aufbeschiene
[03:25] Vor weitere 280 Euro davon tat mir der Kiefer
[03:29] So weh, dass ich morgens kein festes Frühstück mehr essen konnte
[03:34] Und auf 14 Uhr kommt ich trotzdem nicht klardenken
[03:36] Ich probierte Nahrungsergänzungsmittel
[03:38] B12 Genco Omega 3
[03:43] Ich fing an zu akzeptieren, dass das jetzt einfach mein Leben ist
[03:46] Dass die scharf, sinnige Frau, die ich mal war
[03:48] Für immer, wer gestern, letzten November
[03:50] War ich auf den Geburtstag meiner Nichte
[03:54] Mein Entferntakusel war da
[03:55] Klaus, ein pensionierter Physiotherapeut
[03:58] Er fragte warum, um mich so müde aussehe
[04:02] Ich erzählte ihm alles den Nebel
[04:05] Die Abnoe, das C.P.A. pillt
[04:06] Dass ich nicht ertragen konnte, er hörte zu
[04:09] Dann sagte er etwas, was mich aufhorschen ließ
[04:11] Hat sich schon mal jemand bei den Nacken angeschaut
[04:13] Eh eh eh eh eh eh eh eh
[04:15] Er erklärte das Schnarchen für viele Menschen
[04:18] Gar kein Atemproblem ist
[04:21] Es ist ein Haltungsproblem
[04:24] Wenn dein Kopf macht's in dem falschen Winkelfeld
[04:27] Kollabiert das weiche Gewebe im Hals nach hinten
[04:29] Es blockiert die Atemwege, das Varusach, die Abnoe
[04:32] Den Sauerstoff, Abfall, den Nebel
[04:34] Das C.P.A. pillt
[04:35] Press nur luft durch eine blockierte Passage
[04:37] Aber du kennst die ganze Nacht gegen die Schwerkraft
[04:40] Deswegen können wir so viele nicht ertragen
[04:43] Ich starb die Nacht in mir, dem Monat her
[04:45] Hatte ich mich mit deinem Gerät gequält
[04:47] Das Niederführ gemacht, wach da
[04:49] Das eigentliche zu beheben, mein Gehirn war nicht kaputt
[04:52] Das bekam kein Sauerstoff
[04:54] Weil mein Nacken falsch lag, noch am selben Abend
[04:56] Recherchierte ich Studie um Studie zeigte
[04:59] Die Position der Halswirbel, Säule entscheidet
[05:02] Ob die Atemwege im Schlaf offen bleiben oder kollabieren
[05:07] Und mein Uhr 30 fand ich etwas
[05:09] Dass sich Nackentherapie-Kissen, Nante entwickelt
[05:12] Um die Halswirbel, Säule neutral zu halten
[05:15] Um zu verhindern, dass der Kopf nach hinten kippt
[05:17] Um die Atemwege offen zu halten
[05:20] Ich wollte so vorbestellen
[05:23] Ich erzählte niemanden davon
[05:25] Ich war zu oft enttäuscht worden
[05:28] Ich legte es einfach aufs Bild und ging schlafen
[05:32] Ich wachte um 6 Uhr, 47 auf
[05:35] Und ich fühlte mich klar
[05:38] Ich bin Nebel, ich hatte zu dich durchnassen zum Ending
[05:41] Einfach klar
[05:43] Um 15 Uhr arbeitete ich immer noch
[05:46] Immer noch konzentriert
[05:49] Immer noch ich
[05:51] Ich fing an zu weinen, mich zu drehen
[05:54] Weil ich vergessen hatte wie es sich anfühlt
[05:57] Mein Verstand zurückzuhaben, das war vor sechs Monaten
[06:01] Der Nebel ist weg
[06:03] Das Wort hat vergessen, es weg
[06:05] Der 15 Uhr zusammenbruch ist weg
[06:10] Ich bin wieder scharf, wieder schnell die Person von der ich dachte
[06:13] Ich hätte sie für immer verloren
[06:15] Alles nur, weil ich das eigentliche Behoben habe
[06:18] Nicht meine Atmen, meine Nackenposition
[06:20] Vielleicht hast du Angst, dass du deine Verstand verlehrst
[06:24] Vielleicht, dass du das C-Pay probiert und konntest das nicht ertragen
[06:28] Vielleicht, dass du den Nebel einfach akzeptier
[06:31] Wenn du es auf dich zutrifft
[06:33] Probier das Nackentherapie, gissen
[06:35] Korrigier deine Nackenposition und zieh
[06:38] Was passiert, wenn dein Gehirn endlich wieder Sauerstoff bekommt
[06:42] Das Unternehmen ist höchstereich
[06:44] Ich entwickelt von meinem deutschen Chiropraktiker
[06:46] Aktuell gibt es einen limitierten 40%-Rabatt
[06:50] Und deine 60 Tage Geld zurück garantieren
[06:52] Ein ganzes Monat zum Testen verschwindet der Nebel nicht
[06:56] Bekommst du jeden Zahn zurück, aber Achtung
[06:58] Stell nur auf der offiziellen Seite mit der 60 Nächte pro Beschlafen
[07:03] Garantie auf Amazon und Ebay gibt es billige Fälschungen
[07:09] Die nicht funktionieren
[07:11] Der Link ist unter diesem Video
```

### K22-B1 – Referenz K22-322 (Ad 91377966, [share_url](https://app.gethookd.ai/share/ad/91377966?signature=a680de7ec44af071f84a780a9cb04871f923563a650c8c3ca21aada76f51df7d), Länge 372 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Warum Seitenschläfer mit Migräne oder ständigen Kopfschmerzen jetzt zu diesen neuartigen Kissen wechseln?
[00:05] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule.
[00:09] Falls du morgens also mit hämmernden Kopfschmerzen aufwachst, noch bevor du die Augen richtig öffnest
[00:14] oder pochenden Druck hinter den Augen verspürst, dann könnte das höchstwahrscheinlich an deinem alten Kissen liegen.
[00:19] Herkömmliche Kissen sind geometrisch nämlich nicht für den menschlichen Kopf ausgelegt.
[00:23] Das bedeutet, dein Nacken liegt die ganze Nacht in einer ungesunden, verdrehten Position,
[00:27] auch Zervikale Schlaffehlstellung genannt.
[00:30] Und du merkst es nicht mal.
[00:31] Du kannst dir das in etwa wie eine 8 Stunden lange, unnatürliche Yoga-Dehnung vorstellen,
[00:35] die dein Gehirn nicht wirklich registriert.
[00:37] Die meisten Leute denken dann, ihre Migräne kommt von Stress, Dehydration oder vom Wetter.
[00:42] Aber normale Kissen stützen den Nacken nicht richtig.
[00:45] Er schwebt quasi die ganze Nacht in der Luft.
[00:47] Das heißt, anstatt sich zu erholen, spannt sich deine Nackenmuskulatur extrem an und verspannt.
[00:52] Wie ein Gummiband, das permanent unter Spannung steht.
[00:55] Und hier kommt der entscheidende Teil.
[00:57] Diese chronische Verspannung drückt auf empfindliche Nervenbahnen,
[01:00] die direkt von deinem Nacken zu deinem Kopf führen.
[01:02] Besonders auf die Nerven, die mit dem Trigeminusnerv verbunden sind.
[01:05] Dem Hauptnerv, der für Migräne und Kopfschmerzen verantwortlich ist.
[01:09] Ärzte nennen das auch Zervikogene Kopfschmerzen.
[01:11] Also Kopfschmerzen, die ihren Ursprung in der Halswirbelsäule haben.
[01:15] Und genau diese sind oft der versteckte Auslöser für deine Migräneattacken.
[01:19] Ignorierst du das, dann riskierst du chronische Migräne, die immer häufiger auftritt,
[01:22] Tryptane, die irgendwann nicht mehr wirken und permanente Nervenschäden,
[01:26] die zu lebenslangen Kopfschmerzen führen können.
[01:28] Nach und nach wirkt sich das alles auf dein ganzes Leben aus.
[01:31] Du wirst zum Wetterfrosch.
[01:32] Sobald der Frühling kommt oder das Wetter umschlägt, weißt du genau, es geht wieder los.
[01:36] Mittlerweile bist du komplett abhängig von Tryptan,
[01:39] denn ohne die funktioniert dein Leben überhaupt nicht mehr.
[01:41] Selbst ein ganz normales Frühstück mit der Familie wird zur Herausforderung,
[01:45] wenn dir schon beim ersten Licht ein Fall schlecht wird.
[01:47] Du greifst zur Tryptanpackung, nimmst eine und wartest.
[01:50] Ein paar Stunden später ist es vielleicht ein bisschen besser,
[01:53] aber die Kopfschmerzen sind nicht ganz weg.
[01:55] Aber du weißt es doch eigentlich längst.
[01:56] Die Kopfschmerzen werden morgen immer noch da sein.
[01:59] Schließlich hast du ständig das Gefühl, du müsstest Schmerzmittel nehmen,
[02:02] Pläne absagen oder irgendwie durchhalten, nur um halbwegs durch den Tag zu kommen.
[02:06] Also, wie können wir diese cervikogenen Kopfschmerzen loswerden?
[02:10] Nun, wenn du nachts schläfst, ist es entscheidend,
[02:12] dass deine Halswirbelsäule in einer neutralen Position bleibt.
[02:15] Dies verhindert den Druck auf deine Muskeln und Nerven,
[02:18] besonders auf die Nervenbahnen, die mit dem Trigeminusnerv verbunden sind,
[02:21] wodurch du in der Nacht endlich wieder durchschlafen kannst,
[02:24] ohne mit Kopfschmerzen oder Migräne aufzuwachen.
[02:26] Und genau aus diesem Grund hat ein renommierter deutscher Chiropraktiker
[02:30] gemeinsam mit einem österreichischen Gründerteam 21 orthopädische Kopfkissen getestet
[02:35] und dabei auch über 300 Nutzerbewertungen analysiert.
[02:38] Nach neun Monaten Entwicklungszeit und vier Prototypen
[02:41] entstand letztes Jahr schließlich das Nacken-Therapie-Kissen.
[02:44] Ein cervikales Nackenstützkissen, das genau dort entlastet,
[02:47] wo cervikogene Kopfschmerzen und Migräneattacken entstehen.
[02:50] Im Übergang von Kopf, Nacken und Schultern.
[02:53] Dort, wo die Nervenbahnen zum Trigeminusnerv verlaufen.
[02:56] Durch das intelligente 3-Zonen-Nackenstützsystem
[02:58] kehren Kopf, Nacken und Schultern somit wieder in die natürliche Ausrichtung zurück.
[03:03] Es zielt also direkt auf die eigentliche Ursache der Kopfschmerzen ab.
[03:06] Das heißt, dank der ergonomischen Form wird deine Halswirbelsäule perfekt gestützt,
[03:10] ohne Hohlraum zwischen Kissen und Nacken.
[03:12] Und die geformte Kopfzone entlastet zusätzlich.
[03:15] Das Nacken-Therapie-Kissen sorgt also dafür, dass genau solche Fehlstellungen nicht passieren.
[03:20] Der Druck auf den Trigeminusnerv reduziert wird
[03:22] und bietet sofortige Linderung für deine Kopfschmerzen, schon in der ersten Nacht.
[03:26] Normale Kissen sind oft einfach zu weich oder zu hart
[03:29] und lassen die Halswirbeln absinken oder überstrecken.
[03:31] Sie bieten also einfach nicht die Rundum-Unterstützung,
[03:34] die dein Kopf und Nacken eigentlich benötigen,
[03:36] um die Nervenbahn zum Trigeminusnerv zu entlasten.
[03:39] Doch wenn du anfängst mit dem Nacken-Therapie-Kissen zu schlafen,
[03:42] passiert genau das, Nacht 1.
[03:43] Du wachst das erste Mal seit Langem ohne hämmernde Kopfschmerzen auf.
[03:47] Woche 1. Die Verspannungen im Nacken lösen sich,
[03:49] der Druck hinter den Augen verschwindet und du schläfst endlich wieder erholsam durch.
[03:53] Kopfschmerzen treten wesentlich seltener auf
[03:56] und das Bedürfnis nach Schmerztabletten nimmt deutlich ab.
[03:58] Keine morgendlichen Migräne-Attacken mehr.
[04:01] Dein Alltag wird endlich wieder schmerzfrei
[04:03] und du kannst wieder Pläne machen, ohne Angst vor der nächsten Attacke.
[04:06] Ich habe dann irgendwann dieses Nacken-Therapie-Kissen ausprobiert,
[04:10] was mir eine Freundin empfohlen hat.
[04:12] Und ehrlich gesagt, in der ersten Nacht habe ich gemerkt, das hilft.
[04:15] Ich bin dann morgens aufgewacht und dachte,
[04:18] warte mal, mein Nacken tut mir gar nicht weh.
[04:20] Nach zwei Wochen waren die Kopfschmerzen weg, einfach weg.
[04:24] Ich schlafe jetzt echt so gut wie seit langem nicht mehr
[04:27] und wache morgens erholt auf.
[04:29] Es hört sich vielleicht komisch an,
[04:31] aber dieses Kissen hat mir mein Leben zurückgegeben.
[04:34] Und nach der ersten Nacht war ich ehrlich gesagt total baff,
[04:37] denn ich bin das erste Mal seit Langem ohne Schmerzen aufgewacht.
[04:41] Viele dieser Personen waren anfangs skeptisch,
[04:43] da sie bereits schon einiges ausprobiert hatten.
[04:45] Doch nachdem sie die vielen positiven Bewertungen
[04:48] und einzigartige Garantie sahen,
[04:50] haben sie sich entschieden, dem Nacken-Therapie-Kissen eine Chance zu geben.
[04:53] Das sehr ambitionierte Team hinter dem Kissen bietet nämlich ein Versprechen an,
[04:57] das kein Pharmakonzern oder Arzt jemals geben würde.
[05:00] Wenn du nach 30 Nächten mit dem Nacken-Therapie-Kissen
[05:03] keinen großen Unterschied bei deinen Kopfschmerzen oder Migräne spürst,
[05:06] bekommst du dein volles Geld rückerstattet.
[05:08] Klicke jetzt also einfach auf den Link unter diesem Video,
[05:11] um dein Nacken-Therapie-Kissen noch heute zu bestellen.
[05:14] So kannst du endlich wieder ungestört durchschlafen,
[05:16] am nächsten Tag ohne Kopfschmerzen aufwachen
[05:18] und den Tag mit deinen Liebsten genießen.
[05:20] Du kannst wieder mit deiner Familie frühstücken,
[05:22] ohne dass dir schon beim Anblick von Licht und Lärm schlecht wird.
[05:25] Du kannst wieder arbeiten,
[05:27] ohne ständig an Tryptan oder Schmerzmittel in deiner Tasche zu denken
[05:30] oder daran, wann die nächste Attacke kommt.
[05:32] Du kannst wieder Pläne schmieden,
[05:34] ohne diese ständige innere Stimme, die sagt,
[05:36] Aber was, wenn ich an dem Tag wieder Migräne habe?
[05:38] Oder du kannst weiterhin Nacht für Nacht den Trigeminusnerv reizen
[05:42] und deine Nervenbahnen schädigen,
[05:43] indem du ohne die richtige Unterstützung schläfst.
[05:46] Seitdem das Nacken-Therapie-Kissen im Internet vorgestellt wurde,
[05:49] hat das Produkt mit über 21 Millionen Aufrufen auf TikTok
[05:52] einen unglaublichen Hype ausgelöst und war bereits dreimal ausverkauft.
[05:57] Und deshalb ist der aktuelle Lagerbestand sehr limitiert.
[05:59] Wenn du dieses Video also siehst,
[06:01] dann sind womöglich noch wenige Kissen verfügbar.
[06:04] Klicke jetzt also unten auf den Link,
[06:05] um das Nacken-Therapie-Kissen ganz ohne Risiko für 30 Nächte zu testen.
[06:10] Oder du bekommst dein Geld zurück.
```

### K23-B1 – Referenz K23-326 (Ad 89547484, [share_url](https://app.gethookd.ai/share/ad/89547484?signature=61bc0c0a30ef5b93bab7fc624404a4bf9b7d409fce74872b931362d2c976da44), Länge 106 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Das hier ist Jürgen und er leidet seit fünf Jahren an morgendlichen Nacken- und Schulterschmerzen.
[00:05] Hallo! Ich bin dein herkömmliches Kissen und ich bin der Grund, warum du jeden Morgen mit Nackenschmerzen aufwachst.
[00:13] Ich bin nämlich geometrisch gar nicht für deinen Kopf gemacht.
[00:17] Das heißt, dein Nacken schwebt die ganze Nacht in der Luft in einer verdrehten, unnatürlichen Position.
[00:24] Deine Nackenmuskulatur spannt sich an wie ein Gummiband unter Dauerspannung
[00:29] und dann übernimmt dein Trapezmuskel die Belastung vom Hinterkopf bis zu den Schultern.
[00:34] So wie bei Dominosteinen. Eine Muskelgruppe nach der anderen verspannt sich, bis dein ganzer Rücken blockiert ist.
[00:41] Das führt zu stechenden Schmerzen im Nacken und rückenden Kopfschmerzen und tiefsitzenden Knoten unter den Schulterblättern.
[00:48] Stopp! Genau hier komme ich ins Spiel. Ich bin das Nackentherapiekissen.
[00:54] Mit meinem intelligenten 3-Zonen-Nackenstützsystem bringe ich Kopf, Nacken und Schultern zurück in ihre natürliche Ausrichtung.
[01:01] Meine ergonomische Form stützt deine Halswirbelsäule perfekt und meine geformte Kopfzone entlastet zusätzlich.
[01:08] Durch meine integrierte Armablage liegen deine Arme bequem, ohne die Schulter zu belasten.
[01:13] So sorge ich dafür, dass die Fehlstellung der Wirbelsäule gar nicht erst passiert.
[01:18] 92% meiner Kundinnen berichten bereits nach der ersten Nacht von einer spürbaren Verbesserung ihrer Nacken-, Schulter- und Kopfschmerzen.
[01:27] Und nach etwa 14 Tagen waren die Beschwerden meist vollständig verschwunden.
[01:32] Teste mich 30 Nächte lang oder du bekommst dein Geld zurück.
[01:36] Klicke jetzt auf den Link unter diesem Video und sichere dir noch 40% Rabatt.
```

### K23-B2 – Referenz K23-327 (Ad 90347400, [share_url](https://app.gethookd.ai/share/ad/90347400?signature=db388ed6ceb597aeeb957f2c1e57a21bcb9212297aedd2cdff652b837904a414), Länge 110 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Wenn du als Seitenschläfer jeden Morgen mit brennenden Nackenschmerzen aufwachst,
[00:04] solltest du dir Jürgens Geschichte ansehen.
[00:07] Das hier ist Jürgen.
[00:08] Hallo Jürgen.
[00:09] Jürgen ist Seitenschläfer und wacht jeden Morgen mit brennenden Nackenschmerzen,
[00:14] verhärteten Schultern und diesem unangenehmen Kribbeln auf,
[00:18] das bis in seine Hände ausstrahlt.
[00:20] Dabei hat Jürgen bereits alles ausprobiert, um diese Schmerzen loszuwerden.
[00:25] Morgendliche Dehnroutinen, wöchentliche Physiotherapiesitzungen und auch Ibuprofen,
[00:30] das mittlerweile zu seinem Frühstücksritual gehört.
[00:33] Aber nichts davon hat funktioniert.
[00:35] Und weißt du warum?
[00:36] Weil Jürgen nie das eigentliche Problem behoben hat.
[00:39] Denn wenn du als Seitenschläfer auf einem herkömmlichen Kissen schläfst,
[00:43] passiert Folgendes.
[00:44] Dein Kopf sinkt zu tief ein, während deine Schulter gegen das Kissen drückt.
[00:49] Dabei kippt dein Nacken seitlich ab und die Wirbelsäule verdreht sich.
[00:54] Und genau das ist Jürgens wahres Problem.
[00:57] Denn herkömmliche Kissen wurden vor über 2000 Jahren erfunden,
[01:01] lange bevor irgendjemand verstanden hat, wie empfindlich unsere Halswirbelsäule wirklich ist.
[01:08] Aber ab heute ändert sich alles für Jürgen.
[01:10] Denn heute bekommt er das Nacken-Therapie-Kissen.
[01:14] Entwickelt von einem deutschen Chiropraktiker mit einem durchdachten Drei-Zonen-Stützsystem.
[01:20] Sein Kopf sinkt nicht mehr weg, sein Nacken verdreht sich nicht mehr
[01:24] und die Schmerzen sind endlich Geschichte.
[01:27] So sieht Jürgens Schlaf jetzt aus.
[01:29] Schmerzfrei, ohne Verspannungen und ohne dieses nervige Kribbeln in den Armen.
[01:33] Tausende Seitenschläfer erleben bereits in der allerersten Nacht eine deutliche Verbesserung.
[01:39] Probiere auch du das Nacken-Therapie-Kissen jetzt 30 Nächte risikofrei aus.
[01:44] Oder du erhältst dein Geld zurück.
[01:46] Bis später Jürgen.
```

### K25-B1 – Referenz K25-332 (Ad 110088145, [share_url](https://app.gethookd.ai/share/ad/110088145?signature=1ce40812a17e23a01c84ae871652249a4d9bb6903008591ffb02e18ba312b7f3), Länge 399 s, Quelle: GetHooked (Whisper, get_transcription_status))

```text
[00:00] Das ist die schlechteste Schlafposition und warum sie Taubheitsgefühle von der Schulter
[00:04] bis in die Fingerspitzen verursacht.
[00:06] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Halswirbelsäule
[00:10] und klemmst dabei die empfindlichen Halsnerven ab.
[00:12] Falls du also nachts aufwachst, weil deine Hand komplett taub ist, du Taubheitsgefühle
[00:15] von der Schulter bis in die Fingerspitzen hast oder dich das Ameisenlaufen aus dem Schlaf
[00:19] reißt, dann könnte das höchstwahrscheinlich an deinem alten Kissen liegen.
[00:22] Wenn du auf der Seite schläfst, ohne die richtige Unterstützung, dann knickt dein Kopf
[00:26] zur Seite und deine Halswirbelsäule verdreht sich.
[00:28] Das bedeutet, deine Halswirbelsäule liegt die ganze Nacht in einer ungesunden, verdrehten
[00:32] Position, auch Zervikale Schlaffehlstellung genannt, und du merkst es nicht mal.
[00:36] Und diese dauerhaft falsche Schlafposition löst eine regelrechte Kettenreaktion aus.
[00:40] Denn sobald deine Halswirbelsäule verdreht wird, verkrampfen sich die tiefen Nackenmuskeln
[00:44] und klemmen dabei die Halsnerven ein, wie mit einer Zange, die sich nicht mehr löst.
[00:48] Stell dir deinen Nacken mal kurz wie den Stromkasten deines Hauses vor.
[00:51] Und die Halsnerven bei C5 und C6, das sind die Hauptleitungen, die bis in deine Hände
[00:55] und Finger führen.
[00:56] Und wenn diese Nerven jede Nacht 6, 7 oder sogar 8 Stunden eingequetscht werden, dann
[01:00] können die elektrischen Signale nicht mehr richtig fließen.
[01:03] Du kannst dir das etwa so vorstellen wie ein Gartenschlauch, der abgeknickt wird.
[01:06] All das führt zu einem ständigen Nervendruck, ausgerechnet in der Zeit, in der dein Körper
[01:10] eigentlich heilen sollte.
[01:11] Und daher kommen auch die Taubheitsgefühle in den Händen, das Kribbeln in den Fingern
[01:15] und dieses brennende Ziehen, das vom Nacken bis in die Schulter und den Arm strahlt.
[01:18] Das alles ist nicht nur extrem unangenehm und schmerzhaft, sondern auch eine tickende
[01:22] Zeitbombe.
[01:23] Wenn du das tust, dann riskierst du nicht nur vorübergehende Taubheitsgefühle, sondern
[01:26] eine ernsthafte Nervenschädigung sowie den dauerhaften Verlust von Gefühl und Beweglichkeit.
[01:31] Einige meiner PatientInnen haben allein durch diesen wiederholten Druck während des Schlafens
[01:35] dauerhaft das Gefühl in einzelnen Fingern verloren.
[01:37] Nach und nach wirkt sich das alles auf deine Stimmung, Energie und deine Produktivität
[01:41] aus, was letztlich heißt, dass du dein Leben nicht so genießen kannst, wie du es möchtest
[01:45] und wie du und deine Familie es eigentlich verdient haben.
[01:47] Schließlich wachst du nachts ständig auf, weil deine Hand komplett taub ist und du sie
[01:51] verzweifelt ausschütteln musst, nur um das Gefühl zurückzubekommen.
[01:54] Also wie können wir am besten den Druck von den Halsnerven lösen?
[01:56] Nun, wenn du nachts schläfst, ist es entscheidend, dass deine Halswirbelsäule in einer neutralen
[02:01] Position bleibt.
[02:02] Dies verhindert den Druck auf C5 und C6, wodurch du in der Nacht endlich wieder durchschlafen
[02:06] kannst, ohne mit tauben Händen oder Kribbeln in den Fingern aufzuwachen.
[02:09] Aber wie halten wir Kopf, Nacken und Schultern in der richtigen Position?
[02:12] Naja, indem wir zwar auf der Seite schlafen, aber mit der richtigen Unterstützung.
[02:16] Die meisten Leute probieren dann alle möglichen Kissen aus.
[02:19] Schlauen- und Federkissen sind oft einfach zu weich, dein Kopf sinkt schon innerhalb weniger
[02:22] Minuten komplett durch, dein Nacken knickt seitlich ab und deine Halswirbelsäule hängt
[02:26] die ganze Nacht ungestützt in der Luft.
[02:28] Das ist etwa so, als würdest du versuchen, deinen Kopf mit einem Haufen Watte zu stützen.
[02:32] Außerdem sind sie der perfekte Nährboden für Hausstaubmilben und Bakterien, denn das
[02:35] Material saugt jede Nacht deinen Schweiß auf und gibt ihn nie wieder richtig ab.
[02:39] Dann landen viele bei klassischen Memory-Schaumkissen.
[02:41] Klingt erstmal gut, aber die meisten Memory-Schaumkissen sind im Grunde genommen einfach nur harte,
[02:46] rechteckige Blöcke ohne jede ergonomische Form.
[02:48] Und somit nichts anderes, als würdest du deinen Nacken 8 Stunden lang auf einen harten
[02:52] Ziegelstein legen.
[02:53] Und wer dann noch nicht aufgegeben hat, landet bei sogenannten orthopädischen Wellenkissen.
[02:57] Die starre Wellenform passt aber nur selten zur eigenen Anatomie und klemmt C5 und C6
[03:01] dann erst recht ab, was dann genau wieder zu den Nackenschmerzen und Taubheitsgefühlen
[03:05] führt, wie du eigentlich loswerden wolltest.
[03:07] Und genau aus diesem Grund scheitern all diese Lösungen.
[03:09] Sie konzentrieren sich nämlich nicht auf die eigentliche Ursache des Problems, den
[03:12] unkontrollierten Druck auf Nacken- und Halsnerven, während du schläfst.
[03:16] Und genau aus diesem Grund hat ein renommierter deutscher Chiropraktiker gemeinsam mit einem
[03:19] österreichischen Gründerteam 21 orthopädische Nackenkissen getestet und dabei auch über
[03:24] 3000 Nutzerbewertungen analysiert.
[03:26] Nach 9 Monaten Entwicklungszeit und 6 Prototypen entstand schließlich das Nackentherapiekissen,
[03:31] ein cervikales Nackenstützkissen, das genau dort entlastet, wo die meisten Beschwerden
[03:34] entstehen, im Übergang von Kopf, Nacken und Schultern.
[03:37] Durch das intelligente 3-Zonen-Nackenstützsystem kehren Kopf, Nacken und Schultern wieder
[03:41] in ihre natürliche Ausrichtung zurück und deine tiefen Nackenmuskeln können in der
[03:45] Nacht endlich entspannen, regenerieren und heilen.
[03:47] Das heißt, dank der ergonomischen Form wird deine Halswirbelsäule perfekt gestützt,
[03:51] ohne Hohlraum zwischen Kissen und Nacken.
[03:53] Kein unkontrollierter Druck mehr auf C5 und C6.
[03:56] Die geformte Kopfmulde stützt den Hinterkopf, damit dein Kopf nachts in der richtigen Position
[04:00] bleibt.
[04:01] Und dank der speziell integrierten Armablage liegen deine Arme bequem, ohne die Schulter
[04:05] zu belasten, was den Druck auf C5 und C6 zusätzlich reduziert.
[04:08] Egal ob du auf der Seite, dem Rücken oder dem Bauch schläfst.
[04:11] Außerdem stellen die eigens entwickelten kühlenden Bezüge aus Baumwolle und Bambus
[04:15] sicher, dass du nachts nicht schwitzt und ständig die Position wechseln musst, was
[04:19] meist bei nächtlichen Hitzewallungen der Fall ist.
[04:21] Und genau das passiert, wenn du anfängst mit dem Nacken-Therapie-Kissen zu schlafen.
[04:24] Nacht 1.
[04:25] Du wachst das erste Mal seit langem ohne Nacken- und Schulterschmerzen auf.
[04:28] Woche 1.
[04:29] Die Taubheitsgefühle in deinen Händen und Fingern verschwinden und die Verspannungen
[04:32] in deinem Nacken und deinen Schultern lösen sich.
[04:34] Du schläfst endlich wieder erholsam durch.
[04:36] Woche 2.
[04:37] Keine chronischen Beschwerden mehr.
[04:38] Dein Alltag wird endlich wieder beschwerdefrei.
[04:40] Schon in der ersten Nacht habe ich gemerkt, das hilft ja.
[04:43] Das hast du direkt gespürt.
[04:45] Ich bin morgens aufgewacht und dachte mir sowieso, warte mal, Nacken tut gar nicht mehr
[04:50] weh.
[04:51] Nach zwei Wochen waren die kompletten Kopfschmerzen weg bei mir.
[04:54] Also einfach weg.
[04:55] Kein Ruheraum mehr zwischen Kissen und Nacken.
[04:57] Schultern werden entlastet und das Kribbeln im Arm ist es auch endlich weg.
[05:01] Ich schlafe jetzt echt so gut wie seit langem nicht mehr und wache morgens erholt auf.
[05:06] Es hört sich vielleicht komisch an, aber dieses Kissen hat mir mein Leben zurückgegeben.
[05:11] Rund 91% der KundInnen berichteten bereits nach den ersten Nächten von einer spürbaren
[05:16] Linderung ihrer Taubheitsgefühle in Händen und Fingern sowie ihrer chronischen Nacken-
[05:20] und Schulterschmerzen.
[05:21] Und nach etwas mehr als 14 Tagen waren die Beschwerden meist vollständig verschwunden.
[05:25] Viele dieser Personen waren anfangs skeptisch, da sie bereits schon einiges ausprobiert hatten.
[05:29] Doch nachdem sie die vielen positiven Bewertungen und einzigartige Garantie sahen, haben sie
[05:33] sich entschieden, dem Nackentherapiekissen eine Chance zu geben.
[05:36] Das sehr ambitionierte Team hinter dem Kissen bietet nämlich ein Versprechen an, das kein
[05:39] Pharmakonzern oder Arzt jemals geben würde.
[05:42] Wenn du nach 60 Nächten mit dem Nackentherapiekissen keinen großen Unterschied bei deinen Taubheitsgefühlen
[05:46] in den Händen oder deinen Nackenschmerzen spürst, bekommst du dein volles Geld rückerstattet.
[05:51] Klicke jetzt also einfach auf den Link unter diesem Video, um dein Nackentherapiekissen
[05:54] noch heute zu bestellen.
[05:55] So kannst du endlich wieder ungestört durchschlafen, am nächsten Tag ohne taube Hände und Kribbeln
[06:00] in den Fingern aufwachen und den Tag mit deinen Liebsten genießen.
[06:03] Oder du kannst weiterhin Nacht für Nacht deine Halsnerven und deine Halswirbelsäule
[06:06] schädigen, indem du ohne die richtige Unterstützung schläfst.
[06:09] Seitdem das Nackentherapiekissen im Internet vorgestellt wurde, hat das Produkt mit über
[06:13] 18 Millionen Aufrufen auf TikTok einen unglaublichen Hype ausgelöst und war bereits viermal ausverkauft.
[06:19] Und deshalb ist der aktuelle Lagerbestand sehr limitiert.
[06:21] Klicke jetzt also unten auf den Link, um das Nackentherapiekissen ganz ohne Risiko für
[06:25] 60 Nächte zu testen.
[06:27] Oder du bekommst dein Geld zurück.
[06:33] Bis zum nächsten Video.
[06:34] 
```

## Je Video-Cluster

### K01-001 – Winner – 5 Ad(s), max. 119 Tage – aktiv

- **Ad-IDs:** 96489719, 98148650, 98148652, 107108732, 107108734
- **share_url (Rep. 107108734):** https://app.gethookd.ai/share/ad/107108734?signature=839bb0668b295566e78e7e0b7b9ab467f2a16ed262a620e58be756c2fffaa201
- **Länge:** 352 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „PLÖTZLICHER SCHWINDEL, OHRGERÄUSCHE → KOPFSCHMERZEN BIS HIN ZU MIGRÄNE → UND MANCHMAL SOGAR PANIKATTACKEN ODER HERZRASEN? (Hook-Balken wechselt synchron zum Voiceover, 0–5 s)“ — Bild: ältere Frau sitzt auf Bett, Hand an der Stirn (UGC-Look) → 3D-Schädel mit Puls-Linie → glühendes Gehirn → Herz/Gefäße; ab ~10 s Bild-im-Bild-Kreis mit grauhaarigem Experten (Polo) über UGC-Frau
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489719 / Medium 315444666
- **Volltranskript:** = Referenz der Body-Variante **K01-B1** (oben vollständig).

### K01-002 – Winner – 25 Ad(s), max. 116 Tage – aktiv

- **Ad-IDs:** 97625537, 100373717, 100373716, 107108727, 107108725, 117907048, 117357760, 117357754, 117357774, 117357783, 117907046, 117357778, 117357788, 117357769, 117357780, 198894539, 198894647, 198894430, 198894525, 198894517, 198894642, 198894659, 198894653, 198894535, 198894544
- **share_url (Rep. 117907048):** https://app.gethookd.ai/share/ad/117907048?signature=db35ce3eda619b14a62b9852bfd3eae59c44749aa52917705d18a61718e22eca
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION → UND WARUM SIE SCHWINDEL, … (0–3 s); danach Einblendung „ANTIDEPRESSIVA“ (rot, ~10 s)“ — Bild: Mann zeigt auf Frau in Seitenlage, Anatomie-/Nerven-Overlay (blau/rot), rundes Gehirn-Icon wechselt rot→grün → Talking-Head mit Sternen-Kreis (Schwindel) → grauhaariger Experte im Polo vor Anatomie-Postern ("Du warst wahrscheinlich schon bei jedem Arzt,") → UGC-Frau + Bild-im-Bild-Experte
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 100373716 / Medium 327517180
- **Volltranskript:** = Referenz der Body-Variante **K01-B2** (oben vollständig).

### K01-003 – Winner – 7 Ad(s), max. 106 Tage

- **Ad-IDs:** 97625518, 97625534, 97625523, 99458817, 99458824, 107108720, 107108722
- **share_url (Rep. 107108720):** https://app.gethookd.ai/share/ad/107108720?signature=4cffb9c3eeeb52ed0d4aac45e49473613b43edadadd9c9285da94b40c15064f5
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN“ — Bild: Talking-Head Mann, animierter Sternen-Kreis um den Kopf (Schwindel-Effekt)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625518 / Medium 319025313
- **Body-Variante:** K01-B2 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen.
[00:03] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:03] wortgleich mit K01-B2 ab [00:05].

### K01-004 – Winner – 6 Ad(s), max. 38 Tage – aktiv

- **Ad-IDs:** 169269101, 175509507, 175509482, 175509504, 175509495, 175509505
- **share_url (Rep. 169269101):** https://app.gethookd.ai/share/ad/169269101?signature=8427b4f16d2bb63888965089f48abbfccebe1cdc852d5d786574e9ba7408619f
- **Länge:** 381 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER FEHLER NR. 1, WARUM DEIN MORGENDLICHER SCHWINDEL“ — Bild: Finger zeigt auf Anatomie-Poster der Halswirbelsäule (rot markiert)
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169269101 / Medium 464344980
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Der Fehler Nummer eins, warum dein morgenlicher Schwindel einfach nicht verschwindet.
[00:03] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:06] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:10] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:13] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:15] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:19] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:24] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:27] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:30] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:35] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich an deinem alten Kissen.
[00:39] Herkümmer...
```
- **Abgleich (nur erste 40 s):** ab [00:03] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 381 s), aber nicht vollständig geprüft.

### K01-005 – Winner – 3 Ad(s), max. 38 Tage – aktiv

- **Ad-IDs:** 169269098, 169269092, 169991798
- **share_url (Rep. 169269098):** https://app.gethookd.ai/share/ad/169269098?signature=551a7e861616434a3aaed7dde89673ccc68a852d3a8d35392702bfb8e6199c83
- **Länge:** 382 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „ARZT ERKLÄRT IN NUR 15 SEKUNDEN, WARUM MORGENDLICHER SCHWINDEL“ — Bild: älterer Mann im weißen Hemd am Podcast-Mikrofon ("Arzt"), Skelett auf Kissen mit rotem Pfeil
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169269098 / Medium 464345000
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Arzt erklärt in nur 15 Sekunden, warum morgendlicher Schwindel immer wieder kommt.
[00:04] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:06] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:10] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:13] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:15] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:19] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner
[00:23] Psyche zu tun.
[00:24] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:28] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:30] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine
[00:34] Arme kribbeln und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich
[00:38] an deinem alten Kissen.
```
- **Abgleich (nur erste 40 s):** ab [00:04] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 382 s), aber nicht vollständig geprüft.

### K01-006 – Winner – 1 Ad(s), max. 38 Tage – aktiv

- **Ad-IDs:** 169269100
- **share_url (Rep. 169269100):** https://app.gethookd.ai/share/ad/169269100?signature=4999026a0b89efee946f2b5a86edefafe06e9b7a4ce8b0d7c6626a08fcb7c517
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENDLICHER SCHWINDEL, DER TROTZ ALLER UNTERSUCHUNGEN“ — Bild: Split-Screen: ältere Frau mit Gehirn-Overlay / Frau im Bett
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169269100 / Medium 464344981
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Morgenglicher Schwindel, der trotz aller Untersuchungen nicht weggeht, hat selten etwas mit deinem Innenort zu tun.
[00:05] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:08] Beim HNO Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:12] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:15] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:17] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:21] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:25] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:29] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:32] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:37] und jeder Arzt sagt, alles ist normal, dann liegt es höchstens...
```
- **Abgleich (nur erste 40 s):** ab [00:05] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 383 s), aber nicht vollständig geprüft.

### K01-007 – Winner – 1 Ad(s), max. 38 Tage – aktiv

- **Ad-IDs:** 169269091
- **share_url (Rep. 169269091):** https://app.gethookd.ai/share/ad/169269091?signature=ec6980d6bac499619efe10667c1964d8cff54eaf9fd956d39bb728a50d6a3778
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DIE MEISTEN ÄRZTE ÜBERSEHEN DAS VÖLLIG“ — Bild: Arzt untersucht Ohr einer Patientin (Praxis-Szene)
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169269091 / Medium 464345005
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Die meisten Ärzte übersehen das völlig, wenn Menschen ab 40 morgens mit Schwindel und
[00:04] Benommen halt aufwachen.
[00:05] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist, beim HNO Arzt wegen
[00:08] dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:11] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem jeden Morgen
[00:15] wachst du auf und fühlst dich benommen.
[00:16] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:20] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner
[00:24] Psyche zu tun.
[00:25] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:29] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:31] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine
[00:35] Arme kribbeln und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich
[00:39] an deinem Augenarzt.
```
- **Abgleich (nur erste 40 s):** ab [00:05] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 383 s), aber nicht vollständig geprüft.

### K01-008 – Winner – 1 Ad(s), max. 38 Tage – aktiv

- **Ad-IDs:** 169269096
- **share_url (Rep. 169269096):** https://app.gethookd.ai/share/ad/169269096?signature=7ddffa121bfab100eeee276c10689061e4bf1c7e06ad153c3c57a0e2ca68e511
- **Länge:** 381 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „ARZT ERKLÄRT: DESHALB GEHT DEIN MORGENDLICHER SCHWINDEL“ — Bild: Split-Screen: Skelett auf Kissen mit Pfeil / Frau im Bett
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169269096 / Medium 464345009
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Arzt erklärt, deshalb geht dein morgendlicher Schwindel einfach nicht weg.
[00:03] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:06] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:09] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:13] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:15] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:18] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:23] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:27] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:30] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:35] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich an deinem alten Kissen.
[00:39] Herkömmliche Kissen.
```
- **Abgleich (nur erste 40 s):** ab [00:03] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 381 s), aber nicht vollständig geprüft.

### K01-009 – Winner – 1 Ad(s), max. 38 Tage – aktiv

- **Ad-IDs:** 169269099
- **share_url (Rep. 169269099):** https://app.gethookd.ai/share/ad/169269099?signature=80361f57415ea848d1c71928bbc01cdebab5e82c3b78d30ca8e3e742693f47a2
- **Länge:** 382 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER GRÖSSTE FEHLER BEI MORGENDLICHEN SCHWINDEL IST ZU DENKEN,“ — Bild: Frau hält sich den Kopf (UGC-Look)
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169269099 / Medium 464345012
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Der größte Fehler beim morgendlichen Schwindel ist zu denken, es sei ein Problem mit den Ohren.
[00:04] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:06] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:10] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:13] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:16] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:19] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:24] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:28] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:30] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:35] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich an deinem alten Kissen.
```
- **Abgleich (nur erste 40 s):** ab [00:04] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 382 s), aber nicht vollständig geprüft.

### K01-010 – Winner – 1 Ad(s), max. 38 Tage – aktiv

- **Ad-IDs:** 169269103
- **share_url (Rep. 169269103):** https://app.gethookd.ai/share/ad/169269103?signature=5d932cc4b69e86cae87cc5129691ed7b38bd984fb4a4100210612ae0c5b968da
- **Länge:** 385 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DEIN MORGENDLICHER SCHWINDEL KOMMT NICHT VOM INNENOHR“ — Bild: Frau auf Sofa, Hand am Ohr
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169269103 / Medium 464344979
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Dein morglicher Schwindel kommt nicht vom Innenohr.
[00:02] Er kommt von chronisch verspannten Muskeln tief in deinem Nacken, die auf C1 und C2 drücken.
[00:07] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:10] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:13] Vielleicht hat dir sogar jemand antidepressiver verschrieben.
[00:16] Und trotzdem, jeden Morgen wachst du auf und fühlst dich benommen.
[00:19] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:23] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:27] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:31] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:34] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln und jeder Arzt sagt,
```
- **Abgleich (nur erste 40 s):** ab [00:07] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 385 s), aber nicht vollständig geprüft.

### K01-011 – Winner – 1 Ad(s), max. 37 Tage – aktiv

- **Ad-IDs:** 169991799
- **share_url (Rep. 169991799):** https://app.gethookd.ai/share/ad/169991799?signature=8f6daa0b9cf78059dda8edbbd80de9d2a9f5e569eb9234accdc45c47b8e10bd4
- **Länge:** 385 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST, DRÜCKST DU JEDE NACHT AUF DIE NERVEN BEI C1 UND C2“ — Bild: Split: Skelett auf Kissen mit Pfeil / Skelett in Seitenlage, Kreis-Einblendung
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169991799 / Medium 465714422
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Wenn du so schläft, drückst du jede Nacht auf die Nerven bei C1 und C2, die die wahre Ursache für Schwindel, Benommenheit und Herzrasen.
[00:07] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:10] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:14] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem jeden Morgen wachst du auf und fühlst dich benommen.
[00:19] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:23] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:28] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:34] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln und jeder Arzt...
```
- **Abgleich (nur erste 40 s):** ab [00:07] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 385 s), aber nicht vollständig geprüft.

### K01-012 – Kandidat – 1 Ad(s), max. 33 Tage

- **Ad-IDs:** 96489731
- **share_url (Rep. 96489731):** https://app.gethookd.ai/share/ad/96489731?signature=e9883a085ca57dc1a5e12625e82e07347053507a7b8d7b070a3d00ebae91437c
- **Länge:** 349 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN?“ — Bild: Frau hält Kopf, Bewegungsunschärfe
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489731 / Medium 315444701
- **Body-Variante:** K01-B1 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand?
[00:03] Was das wirklich bedeutet, erfährst du hier.
```
- **Übergang:** ab [00:03] wortgleich mit K01-B1 ab [00:06].

### K01-013 – Kandidat – 1 Ad(s), max. 33 Tage

- **Ad-IDs:** 96489725
- **share_url (Rep. 96489725):** https://app.gethookd.ai/share/ad/96489725?signature=e9a6bed7db74b7bffa86475a82770bfc88c6b34a687247babf94d0edd36269a2
- **Länge:** 347 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WAS HABEN VERSPANNUNGEN IM NACKEN“ — Bild: Mann neben Skelett-Modell mit roter Nackenmuskulatur
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489725 / Medium 315444675
- **Body-Variante:** K01-B1 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam?
[00:03] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:03] wortgleich mit K01-B1 ab [00:08].

### K01-014 – Kandidat – 1 Ad(s), max. 33 Tage

- **Ad-IDs:** 96489730
- **share_url (Rep. 96489730):** https://app.gethookd.ai/share/ad/96489730?signature=d78cf4222353cc598c2c72a0816b6d95ecae9c43fc1f708f47f31f348d75c19b
- **Länge:** 352 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „PLÖTZLICHER SCHWINDEL, OHRGERÄUSCHE“ — Bild: Frau stützt sich an Wand ab
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489730 / Medium 315444677
- **Body-Variante:** K01-B1 (Wortübereinstimmung 99 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
(kein eigener Vorspann – startet direkt wortgleich)
```
- **Übergang:** ab [00:00] wortgleich mit K01-B1 ab [00:00].

### K01-015 – Kandidat – 1 Ad(s), max. 33 Tage

- **Ad-IDs:** 97625532
- **share_url (Rep. 97625532):** https://app.gethookd.ai/share/ad/97625532?signature=f770a3f0fc7ff69134b65726d1fca906bd584d187ccff1d47f76b3617dd3fbac
- **Länge:** 349 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN?“ — Bild: Frau mit Kapuze im Bett, Augen geschlossen
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625532 / Medium 319025337
- **Body-Variante:** K01-B1 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand?
[00:03] Was das wirklich bedeutet, erfährst du hier.
```
- **Übergang:** ab [00:03] wortgleich mit K01-B1 ab [00:06].

### K01-016 – Kandidat – 1 Ad(s), max. 33 Tage

- **Ad-IDs:** 96489728
- **share_url (Rep. 96489728):** https://app.gethookd.ai/share/ad/96489728?signature=7c2c297efa45916f54b545358514ce3602bb68d799d173aa771d6842bc7444db
- **Länge:** 348 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „SCHWINDEL HAT NICHTS MIT DEINEM KREISLAUF ODER GLEICHGEWICHT ZU TUN“ — Bild: Frau greift sich an Brust/Hals
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489728 / Medium 315444686
- **Body-Variante:** K01-B1 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Schwindel hat nichts mit deinem Kreislauf oder Gleichgewicht zu tun, hier ist der verstörende
[00:03] Grund.
[00:04] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:04] wortgleich mit K01-B1 ab [00:08].

### K01-017 – Kandidat – 1 Ad(s), max. 33 Tage

- **Ad-IDs:** 97625533
- **share_url (Rep. 97625533):** https://app.gethookd.ai/share/ad/97625533?signature=bde269753df300349ddce55625ba9628ebbfac758cd80a06aa2c85ecd78c03b2
- **Länge:** 348 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „SCHWINDEL HAT NICHTS MIT DEINEM KREISLAUF ODER GLEICHGEWICHT ZU TUN“ — Bild: Frau im Wohnzimmer hält sich den Kopf
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625533 / Medium 319025341
- **Body-Variante:** K01-B1 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Schwindel hat nichts mit deinem Kreislauf oder Gleichgewicht zu tun, hier ist der verstörende
[00:03] Grund.
[00:04] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:04] wortgleich mit K01-B1 ab [00:08].

### K01-018 – Kandidat – 2 Ad(s), max. 26 Tage

- **Ad-IDs:** 97625519, 97625529
- **share_url (Rep. 97625529):** https://app.gethookd.ai/share/ad/97625529?signature=acaa9f36c1129c17e3442fad7870a71eee35f862a6f6029bf7bd96d24ca3f513
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN“ — Bild: Frau mit rotem Glüh-/Nerven-Overlay, rundes Gehirn-Icon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625529 / Medium 319025322
- **Body-Variante:** K01-B2 (Wortübereinstimmung 95 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand, was das wirklich bedeutet,
[00:04] erfährst du hier.
[00:05] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:05] wortgleich mit K01-B2 ab [00:05].
- **Weitere abweichende Stellen (wörtlich):**

```text
[03:17] Nach 9 Monaten Entwicklungszeit und 4 Prototypen entstand letztes Jahr schließlich das Nacken-Therapie-Kissen.
[03:23] Ein cervicales Nackenstützkissen, das genau dort entlastet, wo die meisten Beschwerden
…
```

### K01-019 – Kandidat – 1 Ad(s), max. 26 Tage

- **Ad-IDs:** 97625531
- **share_url (Rep. 97625531):** https://app.gethookd.ai/share/ad/97625531?signature=a2741fdf92f2b33ba5cdb04eff8c1c2afc5ba1481d5c4fb3daa3ef9f27a62d3c
- **Länge:** 382 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „SCHWINDEL HAT NICHTS MIT DEINEM“ — Bild: Frau stürzt, rote Glüh-Effekte
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625531 / Medium 319025324
- **Body-Variante:** K01-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Schwindel hat nichts mit deinem Kreislauf oder Gleichgewicht zu tun.
[00:03] Hier ist der verstörende Grund.
[00:04] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:04] wortgleich mit K01-B2 ab [00:05].

### K01-020 – Kandidat – 1 Ad(s), max. 21 Tage

- **Ad-IDs:** 97625541
- **share_url (Rep. 97625541):** https://app.gethookd.ai/share/ad/97625541?signature=546db3b828a66f972409d65ed324adee425338cd0f83e0be3e3512e7bd0107a1
- **Länge:** 387 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „PLÖTZLICHER SCHWINDEL,“ — Bild: Talking-Head Mann mit Sternen-Kreis
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625541 / Medium 319025354
- **Body-Variante:** K01-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken
[00:05] oder Herzrasen?
[00:06] Was das wirklich bedeutet, erfährst du hier.
[00:09] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:09] wortgleich mit K01-B2 ab [00:05].

### K01-021 – Kandidat – 1 Ad(s), max. 21 Tage

- **Ad-IDs:** 97625536
- **share_url (Rep. 97625536):** https://app.gethookd.ai/share/ad/97625536?signature=11ef285d3611d35f03575a7b14de3b63d75777c5624a75fbe1edd74785275e01
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Frau in Seitenlage mit Muskel-Overlay, Gehirn-Icon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625536 / Medium 319025342
- **Body-Variante:** K01-B2 (Wortübereinstimmung 100 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
(kein eigener Vorspann – startet direkt wortgleich)
```
- **Übergang:** ab [00:00] wortgleich mit K01-B2 ab [00:00].

### K01-022 – Kandidat – 1 Ad(s), max. 21 Tage

- **Ad-IDs:** 97625538
- **share_url (Rep. 97625538):** https://app.gethookd.ai/share/ad/97625538?signature=ef6153f28276303ccc36e30c755f26af6f58aee688aef87b77820cc350095d47
- **Länge:** 384 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST,“ — Bild: 3D-Anatomie Halswirbelsäule mit rotem Glühen
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625538 / Medium 319025345
- **Body-Variante:** K01-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, schneidest du langsam die Blutzufuhr zu deinem Gehirn ab.
[00:03] Und kein Arzt hat dir das jemals gesagt.
[00:06] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:06] wortgleich mit K01-B2 ab [00:05].

### K01-023 – Kandidat – 1 Ad(s), max. 21 Tage

- **Ad-IDs:** 97625535
- **share_url (Rep. 97625535):** https://app.gethookd.ai/share/ad/97625535?signature=c9d5327c7ced5ddd13fe67e64226dc4c27ce6893644f1796ded00264461a758a
- **Länge:** 387 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „PLÖTZLICHER SCHWINDEL,“ — Bild: Frau mit rotem Glüh-Overlay, Gehirn-Icon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625535 / Medium 319025339
- **Body-Variante:** K01-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken
[00:05] oder Herzrasen?
[00:06] Was das wirklich bedeutet, erfährst du hier.
[00:09] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:09] wortgleich mit K01-B2 ab [00:05].

### K01-024 – Kandidat – 1 Ad(s), max. 21 Tage

- **Ad-IDs:** 97625540
- **share_url (Rep. 97625540):** https://app.gethookd.ai/share/ad/97625540?signature=fe6e3116652ef5f2e32c875eee50241b514fd27655ed9e6eb1b54f2cb5d37403
- **Länge:** 384 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST,“ — Bild: Mann in Seitenlage, rote Nerven im Nacken
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625540 / Medium 319025350
- **Body-Variante:** K01-B2 (Wortübereinstimmung 95 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, drückst du 8 Stunden lang auf deinen Vargusnerv.
[00:03] Das erklärt deinen Schwindel und deine Panikattacken.
[00:06] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:06] wortgleich mit K01-B2 ab [00:05].

### K01-025 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 96489720
- **share_url (Rep. 96489720):** https://app.gethookd.ai/share/ad/96489720?signature=011bd5041493d78d869316165c9cdf98957d149fc292335afbbaea10ee3b7a8b
- **Länge:** 347 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER SCHWINDEL HÖRT EINFACH NICHT AUF?“ — Bild: ältere Frau stützt sich an Wand (s/w)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489720 / Medium 315444676
- **Body-Variante:** K01-B1 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen.
[00:03] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:03] wortgleich mit K01-B1 ab [00:08].

### K01-026 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 96489726
- **share_url (Rep. 96489726):** https://app.gethookd.ai/share/ad/96489726?signature=cbbe2c740ef5da918a1270c15455022c021196f382df8eef370f6189fb590c6e
- **Länge:** 353 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL AUFWACHST DEINE ARME KRIBBELN“ — Bild: Nacken mit rotem Glühen (Nahaufnahme)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489726 / Medium 315444682
- **Body-Variante:** K01-B1 (Wortübereinstimmung 95 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und
[00:03] dir jeder Arzt sagt, alles ist völlig normal, dann solltest du dieses Video unbedingt bis
[00:08] zum Ende ansehen.
[00:09] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:09] wortgleich mit K01-B1 ab [00:08].

### K01-027 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 96489722
- **share_url (Rep. 96489722):** https://app.gethookd.ai/share/ad/96489722?signature=5b20d4dc7366ce5f2be0b6c36fe895fa4acd52397e35fa49e34c1cc2e858ff69
- **Länge:** 353 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL AUFWACHST DEINE ARME KRIBBELN“ — Bild: Frau hält Kopf, Gehirn glüht orange
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489722 / Medium 315444670
- **Body-Variante:** K01-B1 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und
[00:03] dir jeder Arzt sagt, alles ist völlig normal, dann solltest du dieses Video unbedingt bis
[00:08] zum Ende ansehen.
[00:09] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:09] wortgleich mit K01-B1 ab [00:08].

### K01-028 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 96489733
- **share_url (Rep. 96489733):** https://app.gethookd.ai/share/ad/96489733?signature=8b6688562a090124dbf203509c726fa4047ca95007d7a0ba74f8edd680e2cf38
- **Länge:** 349 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN?“ — Bild: Frau hält sich den Kopf
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489733 / Medium 315444697
- **Body-Variante:** K01-B1 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu
[00:03] sagen, das du bisher ignoriert hast.
[00:05] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:05] wortgleich mit K01-B1 ab [00:08].

### K01-029 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 96489727
- **share_url (Rep. 96489727):** https://app.gethookd.ai/share/ad/96489727?signature=bed1bdfe543a6c6ec78f94f584736db8bebf6a293f0b990217eae573786e8c46
- **Länge:** 347 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER SCHWINDEL HÖRT EINFACH NICHT AUF?“ — Bild: Frau hält sich den Kopf
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489727 / Medium 315444690
- **Body-Variante:** K01-B1 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen.
[00:03] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:03] wortgleich mit K01-B1 ab [00:08].

### K01-030 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 98148692
- **share_url (Rep. 98148692):** https://app.gethookd.ai/share/ad/98148692?signature=a7f88997454c3b3a4745e18e31165094fe1a474a4e11274104bbfc717dd3962e
- **Länge:** 353 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL AUFWACHST,“ — Bild: ältere Frau mit Brille und Tasse in Küche
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 98148692 / Medium 320568541
- **Volltranskript:** = Referenz der Body-Variante **K01-B3** (oben vollständig).

### K01-031 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 98148717
- **share_url (Rep. 98148717):** https://app.gethookd.ai/share/ad/98148717?signature=384fc00494fc70d006d88eba5058ac764e64036d5133a1d42f2fb3fa2d32047f
- **Länge:** 343 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN?“ — Bild: ältere Frau liegt im Pyjama auf dem Bett
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 98148717 / Medium 320568561
- **Body-Variante:** K01-B3 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper, dir etwas zu sagen, das du bisher ignoriert hast.
[00:06] Ich dachte zuerst, der Schwindel komme vom Stress oder zu wenig Schlaf.
```
- **Übergang:** ab [00:06] wortgleich mit K01-B3 ab [00:16].

### K01-032 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 98148676
- **share_url (Rep. 98148676):** https://app.gethookd.ai/share/ad/98148676?signature=30b42fe387fb1de1f40f0f1f4336c6f94a672e3ef1db9e85720b894a22f56a1a
- **Länge:** 341 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WAS HABEN VERSPANNUNGEN IM NACKEN, SCHWINDEL UND MÜDIGKEIT GEMEINSAM?“ — Bild: 3D-Anatomie Hals mit glühendem Nerv/Muskel (pink)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 98148676 / Medium 320717370
- **Body-Variante:** K01-B3 (Wortübereinstimmung 99 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam?
[00:04] Ich dachte zuerst, der Schwindel komme vom Stress oder zu wenig Schlaf.
```
- **Übergang:** ab [00:04] wortgleich mit K01-B3 ab [00:16].

### K01-033 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 98148693
- **share_url (Rep. 98148693):** https://app.gethookd.ai/share/ad/98148693?signature=0261fd3baed34814bcfcadaffe4a99128121a593f71f8c5ccb52a2774fa9289f
- **Länge:** 343 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN“ — Bild: Frau liegt auf Sofa, Hand an der Stirn
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 98148693 / Medium 320568467
- **Body-Variante:** K01-B3 (Wortübereinstimmung 99 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand?
[00:03] Was das wirklich bedeutet, erfährst du hier.
[00:05] Ich dachte zuerst, der Schwindel komme vom Stress oder zu wenig Schlaf.
```
- **Übergang:** ab [00:05] wortgleich mit K01-B3 ab [00:16].

### K01-034 – Kandidat – 1 Ad(s), max. 15 Tage

- **Ad-IDs:** 97625517
- **share_url (Rep. 97625517):** https://app.gethookd.ai/share/ad/97625517?signature=51e5d9d49b991777091aa37367536a6fe03af0c7d647482c71d2ae12430a380d
- **Länge:** 384 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN?“ — Bild: Frau mit rotem Glitch-/Nerven-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625517 / Medium 319025314
- **Body-Variante:** K01-B2 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu
[00:04] sagen, das du bisher ignoriert hast.
[00:06] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:06] wortgleich mit K01-B2 ab [00:05].

### K01-035 – Kandidat – 1 Ad(s), max. 15 Tage

- **Ad-IDs:** 97625528
- **share_url (Rep. 97625528):** https://app.gethookd.ai/share/ad/97625528?signature=b619da628c88a0bf007fce428219bd86e2d58d55f65d9446277b3bf72365be97
- **Länge:** 388 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL AUFWACHST,“ — Bild: Frau steht auf neben Bett, Gehirn-Icon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625528 / Medium 319025329
- **Body-Variante:** K01-B2 (Wortübereinstimmung 95 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und
[00:04] dir jeder Arzt sagt, alles ist völlig normal, dann solltest du dieses Video unbedingt bis
[00:09] zum Ende ansehen.
[00:10] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:10] wortgleich mit K01-B2 ab [00:05].

### K01-036 – Kandidat – 1 Ad(s), max. 15 Tage

- **Ad-IDs:** 97625527
- **share_url (Rep. 97625527):** https://app.gethookd.ai/share/ad/97625527?signature=766944c7bc206ececad046f0f5ad6156b3d7b489488e3d134746764ab63e2afa
- **Länge:** 388 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL AUFWACHST,“ — Bild: Frau mit rotem Laser-/Nerven-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625527 / Medium 319025325
- **Body-Variante:** K01-B2 (Wortübereinstimmung 95 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und
[00:04] dir jeder Arzt sagt, alles ist völlig normal, dann solltest du dieses Video unbedingt bis
[00:09] zum Ende ansehen.
[00:10] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:10] wortgleich mit K01-B2 ab [00:05].

### K01-037 – Kandidat – 1 Ad(s), max. 14 Tage

- **Ad-IDs:** 97625516
- **share_url (Rep. 97625516):** https://app.gethookd.ai/share/ad/97625516?signature=f54bf1eca24f68507ea38d0a92c19a67631b45cef8dd12fefccbcbeae5f77bc5
- **Länge:** 381 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER SCHWINDEL HÖRT EINFACH NICHT AUF?“ — Bild: Frau mit rotem Glitch-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625516 / Medium 319025303
- **Body-Variante:** K01-B2 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen.
[00:03] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:03] wortgleich mit K01-B2 ab [00:05].

### K01-038 – Verlierer – 1 Ad(s), max. 13 Tage

- **Ad-IDs:** 97625539
- **share_url (Rep. 97625539):** https://app.gethookd.ai/share/ad/97625539?signature=9a03484a6e69c365324bb993e0e98a00a9c48590268169d76b6b9a4766b91e9c
- **Länge:** 384 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST,“ — Bild: schlafender Mann mit rotem Nerven-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625539 / Medium 319025352
- **Body-Variante:** K01-B2 (Wortübereinstimmung 95 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, drückst du 8 Stunden lang auf deinen Vargusnerv.
[00:03] Das erklärt deinen Schwindel und deine Panikattacken.
[00:06] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:06] wortgleich mit K01-B2 ab [00:05].

### K01-039 – Verlierer – 1 Ad(s), max. 11 Tage

- **Ad-IDs:** 101489238
- **share_url (Rep. 101489238):** https://app.gethookd.ai/share/ad/101489238?signature=7ae573888bf535c951bbdb722bc58e4d175aa4439f2ceb963fb7312441de0a31
- **Länge:** 390 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Mann in Seitenlage mit Gehirn-Overlay, rundes Wirbelsäulen-Icon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 101489238 / Medium 331073200
- **Body-Variante:** K01-B2 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen
[00:04] verursacht.
[00:05] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:05] wortgleich mit K01-B2 ab [00:26].

### K01-040 – Verlierer – 1 Ad(s), max. 11 Tage

- **Ad-IDs:** 101489239
- **share_url (Rep. 101489239):** https://app.gethookd.ai/share/ad/101489239?signature=231f7af1ed59ac7db02ec4fa1c7914f259860d1fc68f6ed021f3eb167c65caa3
- **Länge:** 366 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „PLÖTZLICHER SCHWINDEL,“ — Bild: Mann mit rotem Glitch-Overlay, Gehirn-Icon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 101489239 / Medium 331073202
- **Body-Variante:** K01-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken
[00:05] oder Herzrasen?
[00:06] Was das wirklich bedeutet, erfährst du hier.
[00:09] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:09] wortgleich mit K01-B2 ab [00:26].

### K01-041 – Verlierer – 1 Ad(s), max. 11 Tage

- **Ad-IDs:** 101489236
- **share_url (Rep. 101489236):** https://app.gethookd.ai/share/ad/101489236?signature=54a8cb2eed9c4b648df7826b00b0f7c573d8f449e16f43d4df354fabfa36d283
- **Länge:** 368 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL AUFWACHST,“ — Bild: Frau steht auf neben Bett, Gehirn-Icon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 101489236 / Medium 331073195
- **Body-Variante:** K01-B2 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du morgens mit Schwindel aufwachst, deine Arme kribbeln, sobald du den Kopf drehst und
[00:04] dir jeder Arzt sagt, alles ist völlig normal, dann solltest du dieses Video unbedingt bis
[00:09] zum Ende ansehen.
[00:10] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:10] wortgleich mit K01-B2 ab [00:26].

### K01-042 – Verlierer – 1 Ad(s), max. 10 Tage

- **Ad-IDs:** 99019506
- **share_url (Rep. 99019506):** https://app.gethookd.ai/share/ad/99019506?signature=2ac8b9fe6dbc5bb084625c20965e1d6820364d04a1638e0871dda4e6c6012b86
- **Länge:** 334 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „PLÖTZLICHER SCHWINDEL, OHRGERÄUSCHE, KOPFSCHMERZEN BIS HIN ZU MIGRÄNE“ — Bild: Frau in Küche, blickt nach unten
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 99019506 / Medium 323198588
- **Body-Variante:** K01-B3 (Wortübereinstimmung 90 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken oder Herzrasen?
[00:06] Was das wirklich bedeutet, erfährst du hier.
[00:09] Vor etwa einem Jahr fing es an, dieser komische Schwindel.
[00:12] Kein Drehen, eher so, als würde der Boden unter mir pulsieren.
[00:15] Morgens war es im Schlimmsten.
[00:17] Direkt nach dem Aufstehen.
[00:18] Als hätte mein Gleichgewichtssinn die ganze Nacht nicht funktioniert.
[00:20] Ich ging zum Hausarzt.
[00:21] Blutbild in Ordnung.
[00:22] Dann zum HNO, dann zur Neurologie.
[00:24] Alles gut.
[00:25] Ihr Gehirn sieht super aus.
[00:26] Sie sind sehr gesund für ihr Alter.
[00:28] Gesund?
[00:28] Ich konnte nicht mal an der Kasse bei Rewe stehen, ohne mich am Einkaufswagen festzuhalten.
[00:32] Und Symptome?
```
- **Übergang:** ab [00:32] wortgleich mit K01-B3 ab [00:51].

### K01-043 – Verlierer – 1 Ad(s), max. 10 Tage

- **Ad-IDs:** 98148672
- **share_url (Rep. 98148672):** https://app.gethookd.ai/share/ad/98148672?signature=dc4f99ec1ee6803893fb93aa766cfae1a6333812052800c7ed60e442a533e7b0
- **Länge:** 328 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WAS HABEN VERSPANNUNGEN IM NACKEN, SCHWINDEL UND MÜDIGKEIT GEMEINSAM?“ — Bild: 3D-Anatomie Hals mit glühendem Nerv
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 98148672 / Medium 320568438
- **Body-Variante:** K01-B3 (Wortübereinstimmung 91 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam?
[00:04] Vor etwa einem Jahr fing es an.
[00:06] Dieser komische Schwindel.
[00:07] Kein Drehen, eher so, als würde der Boden unter mir pulsieren.
[00:10] Morgens war es im Schlimmsten.
[00:11] Direkt nach dem Aufstehen.
[00:13] Als hätte mein Gleichgewichtssinn die ganze Nacht nicht funktioniert.
[00:15] Ich ging zum Hausarzt.
[00:16] Blutbild in Ordnung.
[00:17] Dann zum HNO, dann zur Neurologie.
[00:19] Alles gut.
[00:20] Ihr Gehirn sieht super aus.
[00:21] Sie sind sehr gesund für ihr Alter.
[00:23] Gesund?
[00:24] Ich konnte nicht mal an der Kasse bei Rewe stehen, ohne mich am Einkaufswagen festzuhalten.
[00:27] Und Symptome?
```
- **Übergang:** ab [00:27] wortgleich mit K01-B3 ab [00:51].

### K01-044 – Verlierer – 1 Ad(s), max. 10 Tage

- **Ad-IDs:** 98148706
- **share_url (Rep. 98148706):** https://app.gethookd.ai/share/ad/98148706?signature=a5ccc473aee91bb4a061d762681269aa065fcea95fb8a191878a5b73e5016f5e
- **Länge:** 341 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL AUFWACHST,“ — Bild: ältere Frau mit Tasse in Küche
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 98148706 / Medium 320568543
- **Body-Variante:** K01-B3 (Wortübereinstimmung 93 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
(kein eigener Vorspann – startet direkt wortgleich)
```
- **Übergang:** ab [00:00] wortgleich mit K01-B3 ab [00:00].
- **Weitere abweichende Stellen (wörtlich):**

```text
[00:16] Vor etwa einem Jahr fing es an, dieser komische Schwindel. Kein Drehen, eher so, als würde der Boden unter mir pulsieren.
[00:23] Morgens war es im Schlimmsten. Direkt nach dem Aufstehen. Als hätte mein Gleichgewichtssinn die ganze Nacht nicht funktioniert.
[00:28] Ich ging zum Hausarzt. Blutbild in Ordnung. Dann zum HNO, dann zur Neurologie. Alles gut. Ihr Gehirn sieht super aus. Sie sind sehr gesund für ihr Alter.
[00:35] Gesund? Ich konnte nicht mal an der Kasse bei Rewe stehen, ohne mich am Einkaufswagen festzuhalten. Und Symptome? Die häuften sich.
…
```

### K01-045 – Verlierer – 1 Ad(s), max. 10 Tage

- **Ad-IDs:** 98148727
- **share_url (Rep. 98148727):** https://app.gethookd.ai/share/ad/98148727?signature=93a4652b400676470be979150e578136b8e102ac66e5cb3722e0232081352964
- **Länge:** 331 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN?“ — Bild: ältere Frau liegt auf Bett
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 98148727 / Medium 320568527
- **Body-Variante:** K01-B3 (Wortübereinstimmung 90 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Boden fühlt sich beim Aufstehen wackelig an.
[00:02] Dann versucht dein Körper, dir etwas zu sagen,
[00:04] das du bisher ignoriert hast.
[00:06] Vor etwa einem Jahr fing es an.
[00:08] Dieser komische Schwindel.
[00:09] Kein Drehen, eher so, als würde der Boden unter mir pulsieren.
[00:12] Morgens war es im Schlimmsten.
[00:13] Direkt nach dem Aufstehen.
[00:15] Als hätte mein Gleichgewichtssinn die ganze Nacht nicht funktioniert.
[00:17] Ich ging zum Hausarzt.
[00:18] Blutbild in Ordnung.
[00:19] Dann zum HNO, dann zur Neurologie.
[00:21] Alles gut.
[00:22] Ihr Gehirn sieht super aus.
[00:23] Sie sind sehr gesund für ihr Alter.
[00:25] Gesund?
[00:25] Ich konnte nicht mal an der Kasse bei Rewe stehen,
[00:27] ohne mich am Einkaufswagen festzuhalten.
[00:29] Und Symptome?
```
- **Übergang:** ab [00:29] wortgleich mit K01-B3 ab [00:51].

### K01-046 – Verlierer – 1 Ad(s), max. 10 Tage

- **Ad-IDs:** 98148682
- **share_url (Rep. 98148682):** https://app.gethookd.ai/share/ad/98148682?signature=20083c3ab977b057a3bc43ec6feabf663f6e70d89a8f4d2568d87c50f2a0f178
- **Länge:** 330 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN“ — Bild: Frau auf Sofa, Hand an Stirn
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 98148682 / Medium 320568465
- **Body-Variante:** K01-B3 (Wortübereinstimmung 91 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand?
[00:03] Was das wirklich bedeutet, erfährst du hier.
[00:05] Vor etwa einem Jahr fing es an, dieser komische Schwindel.
[00:09] Kein Drehen, eher so, als würde der Boden unter mir pulsieren.
[00:12] Morgens war es im Schlimmsten.
[00:13] Direkt nach dem Aufstehen.
[00:14] Als hätte mein Gleichgewichtssinn die ganze Nacht nicht funktioniert.
[00:17] Ich ging zum Hausarzt.
[00:18] Blutbild in Ordnung.
[00:19] Dann zum HNO, dann zur Neurologie.
[00:21] Alles gut.
[00:21] Ihr Gehirn sieht super aus.
[00:23] Sie sind sehr gesund für ihr Alter.
[00:24] Gesund?
[00:25] Ich konnte nicht mal an der Kasse bei Rewe stehen,
[00:27] ohne mich am Einkaufswagen festzuhalten.
[00:29] Und Symptome?
```
- **Übergang:** ab [00:29] wortgleich mit K01-B3 ab [00:51].

### K01-047 – Verlierer – 1 Ad(s), max. 10 Tage

- **Ad-IDs:** 98148702
- **share_url (Rep. 98148702):** https://app.gethookd.ai/share/ad/98148702?signature=db4c903d4e87f617b50f9a61d464f7b9e8ebe33843c15202f322fd3634893b27
- **Länge:** 346 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „PLÖTZLICHER SCHWINDEL, OHRGERÄUSCHE, KOPFSCHMERZEN BIS HIN ZU MIGRÄNE“ — Bild: Frau in Küche
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 98148702 / Medium 320568526
- **Body-Variante:** K01-B3 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Plötzlicher Schwindel, Ohrgeräusche, Kopfschmerzen, bis hin zu Migräne und manchmal sogar Panikattacken oder Herzrasen?
[00:06] Was das wirklich bedeutet, erfährst du hier.
[00:09] Ich dachte zuerst, der Schwindel komme vom Stress oder zu wenig Schlaf.
```
- **Übergang:** ab [00:09] wortgleich mit K01-B3 ab [00:16].

### K01-048 – Verlierer – 1 Ad(s), max. 10 Tage

- **Ad-IDs:** 101489231
- **share_url (Rep. 101489231):** https://app.gethookd.ai/share/ad/101489231?signature=8c247de9db6550307fe0231bd02016ece16d4a83ed87bdd28d7ca16494fef0b4
- **Länge:** 390 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN“ — Bild: Talking-Head Mann mit Sternen-Kreis
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 101489231 / Medium 331073185
- **Body-Variante:** K01-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand, was das wirklich bedeutet,
[00:04] erfährst du hier.
[00:05] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:05] wortgleich mit K01-B2 ab [00:26].

### K01-049 – Verlierer – 1 Ad(s), max. 10 Tage

- **Ad-IDs:** 101489237
- **share_url (Rep. 101489237):** https://app.gethookd.ai/share/ad/101489237?signature=402f87efa4d2f20045b85d782889f1960c04e15190256519f23b9c3931155112
- **Länge:** 390 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Nacken von hinten mit rotem Pfeil auf HWS
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 101489237 / Medium 331073193
- **Body-Variante:** K01-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen
[00:04] verursacht.
[00:05] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:05] wortgleich mit K01-B2 ab [00:26].

### K01-050 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 169991791
- **share_url (Rep. 169991791):** https://app.gethookd.ai/share/ad/169991791?signature=5a5a005515593f854d8afc336191ec3c6d8d453fc6325ae68ffd5ee6a76a0ef4
- **Länge:** 384 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WARNUNG: DAS IST DIE GEFÄHRLICHSTE SCHLAFPOSITION“ — Bild: Skelett liegt auf Kissen, roter Warnpfeil
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169991791 / Medium 465714413
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Warnung, das ist die gefährlichste Schlafposition und warum sie Schwindel,
[00:03] Benommenheit und Herzrasen verursacht. Du warst wahrscheinlich schon bei jedem Arzt,
[00:07] der dir eingefallen ist, beim HNO Arzt wegen dem Schwindel, beim Augenarzt wegen
[00:11] der verschwommenen Sicht. Vielleicht hat dir sogar jemand antidepressiver
[00:14] verschrieben und trotzdem jeden Morgen wachst du auf und fühlst dich
[00:17] benommen. Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum
[00:20] konzentrieren. Aber diese Symptome haben nichts mit deinem Ohr, deinen
[00:24] Augen, Stress oder deiner Psyche zu tun. Wenn du so schläft, arbeitest du
[00:27] gegen die natürliche Krümmung deiner Halswirbelsäule und klemmst dabei die
[00:30] Arterien ab, die dein Gehirn versorgen. Falls du morgens also mit Schwindel
[00:34] aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln und
[00:37] jeder Arzt sagt, alles ist normal, dann liegt es
```
- **Abgleich (nur erste 40 s):** ab [00:00] wortgleich mit Body-Variante **K01-B2** ab [00:00] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 384 s), aber nicht vollständig geprüft.

### K01-051 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180754297
- **share_url (Rep. 180754297):** https://app.gethookd.ai/share/ad/180754297?signature=9730ad1ceb496d0ed36bbff1327f0a7bc48f68e57ba30c10fe9992614426fd2d
- **Länge:** 370 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „(erstes Bild schwarz – Hook-Text siehe Frame 1–3 s)“ — Bild: schwarzer Startframe
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754297 / Medium 484395060
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Warum Schwindele immer wieder kommt, Obwohl alle Tests unauffällig sind
[00:05] Dein Herz rast dir, Schwindele ich dein arme Kribbel
[00:10] Aber dein Arzt sagt du bist völlig geschehen
[00:13] Ich bin fünf, naftig früher war ich selbstständig
[00:16] Bin überall hingefahren, hatte mein Garten
[00:18] Und hab Leben gern auf meine Enkelinnen aufgepasst
[00:22] Dann fing der Schwindele an, kein Drehen eher
[00:25] Als würde der Boden unter mir pulsieren
[00:27] Als wäre die Schwerkraft kaputt
[00:29] Mein Hausarzt ließ Blut abnehmen
[00:31] Ordnet seine M.R.T. an
[00:33] Überwiesen mich zum Kardiologen
[00:35] Perfekt, ihr gehören sieht super aus
[00:38] Sie sind sehr geschehen
```
- **Abgleich:** keine Übereinstimmung mit einer bekannten Body-Variante in den ersten 40 s → eigener Body, Volltranskript fehlt (Lücke).

### K01-052 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180754303
- **share_url (Rep. 180754303):** https://app.gethookd.ai/share/ad/180754303?signature=1933949ab19e275292f8884011eeec394223dfe0674b3750fdf6e195b833a0b6
- **Länge:** 382 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DER SCHNELLSTE WEG, UM MORGENDLICHEN SCHWINDEL“ — Bild: Frau liegt mit Nacken auf Ball/Rolle, grüne Markierung, rote Pfeile
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754303 / Medium 484395073
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Das ist der schnellste Weg, um morgendlichen Schwindel von zu Hause aus loszuwerden.
[00:04] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:07] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:10] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:13] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:16] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:19] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:24] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:28] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:31] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:35] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich an deinem alten Kissen.
```
- **Abgleich (nur erste 40 s):** ab [00:04] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 382 s), aber nicht vollständig geprüft.

### K01-053 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180754309
- **share_url (Rep. 180754309):** https://app.gethookd.ai/share/ad/180754309?signature=c91d5deb4ee246ff979f913aa577547b3c7f9827d21a0c5e746f610d2c784c85
- **Länge:** 382 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENDLICHER SCHWINDEL IST MEIST KEIN INNENOHR-PROBLEM,“ — Bild: Split: Frau mit Muskel-Overlay / Arzt untersucht Ohr
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754309 / Medium 484395077
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Morgendlicher Schwindel ist meist kein Innenohrproblem, es ist ein Nackenproblem.
[00:04] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:06] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:10] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:13] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:16] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:19] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:24] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:28] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:30] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:35] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich an deinem alten Kissen.
```
- **Abgleich (nur erste 40 s):** ab [00:04] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 382 s), aber nicht vollständig geprüft.

### K01-054 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180754313
- **share_url (Rep. 180754313):** https://app.gethookd.ai/share/ad/180754313?signature=10f143d8ca1f079f07b47b1a68880d9b85716cd576574c3afe5b35e1444356ad
- **Länge:** 378 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animationsfigur (Pixar-Stil): ältere Frau sitzt im Bett, Hand an der Stirn
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754313 / Medium 484395074
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Wenn du morgens mit Schwinden laufst Deine arme Kribbeln sobald du den Kopf drehst
[00:05] Und dir jeder Arzt sagt, alles ist völlig normal Dann schaue dir das unbedingt an
[00:10] Denn ich habe 18 Monate um ins Lebens verloren Und überzeiten 400 Euro aus eigener Tasche bezahlt
[00:16] Bevor ich herausgefunden habe Was wirklich los war
[00:20] Ich bin fünf, auf dich früher war ich selbstständig
[00:23] Bin überall hingefahren, hatte mein Garten Und hab lieben gern auf meine Enkelinnen aufgepasst
[00:30] Dann fing der Schwinde an, kein Drehen eher
[00:32] Alles würde der Boden unter mir pulsieren Als wäre die Schwerkraft kaputt
[00:36] Mein Hausarzt ist Blut abnehmen Ordnet seine M-
```
- **Abgleich (nur erste 40 s):** ab [00:00] wortgleich mit Body-Variante **K01-B3** ab [00:00] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B3 (Länge 378 s), aber nicht vollständig geprüft.

### K01-055 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180754301
- **share_url (Rep. 180754301):** https://app.gethookd.ai/share/ad/180754301?signature=289a07a0e46faef262aead4992a45b249fff8e2e1cba4815699acbb2f6d286d0
- **Länge:** 385 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU UNTER SCHWINDEL, HERZRASEN UND BENOMMENHEIT LEIDEST,“ — Bild: Frau mit Muskel-/Nerven-Overlay in Küche
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754301 / Medium 484395090
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Wenn du unter Schwindel, Herzrasen und Benommenheit leidest, hat dir dein Arzt wahrscheinlich nie erklärt, warum all diese Symptome zusammen auftreten.
[00:07] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:10] Beim HMO Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:14] Vielleicht hat dir sogar jemand antidepressiver verschrieben.
[00:16] Und trotzdem, jeden Morgen wachst du auf und fühlst dich benommen.
[00:19] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:23] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:27] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:31] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:34] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln und jeder Arzt...
```
- **Abgleich (nur erste 40 s):** ab [00:07] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 385 s), aber nicht vollständig geprüft.

### K01-056 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180754298
- **share_url (Rep. 180754298):** https://app.gethookd.ai/share/ad/180754298?signature=93a73447bc77c5aa6b8fc5fd4dcc9eb7e7ddef145ada2bc893cfac5790cf813b
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Frau schläft, Nacken mit Muskel-Overlay
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754298 / Medium 484395069
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Das ist die schlechteste Schlafposition.
[00:02] Und warum sie Schwindel, Benommenheit und Herzrasen verursacht.
[00:05] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:08] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:11] Vielleicht hat dir sogar jemand antidepressiver verschrieben.
[00:14] Und trotzdem, jeden Morgen wachst du auf und fühlst dich benommen.
[00:17] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:20] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:25] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:29] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:32] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:37] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich...
```
- **Abgleich (nur erste 40 s):** ab [00:00] wortgleich mit Body-Variante **K01-B2** ab [00:00] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 383 s), aber nicht vollständig geprüft.

### K01-057 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180754306
- **share_url (Rep. 180754306):** https://app.gethookd.ai/share/ad/180754306?signature=5acbff3e1eb4c449cac0383fdeb036e0f2f6cd2e6b5a63a78f7118504070a9dc
- **Länge:** 382 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER GRÖSSTE FEHLER BEI SCHWINDEL UND BENOMMENHEIT“ — Bild: Split: Frau mit Muskel-Overlay hält Kopf
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754306 / Medium 484395070
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Der größte Fehler bei Schwindel und Benommenheit ist zu denken, es sei ein Innenohrproblem.
[00:04] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:07] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:11] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:14] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:16] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:20] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:25] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:28] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:31] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:36] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich an deinem Ohr.
```
- **Abgleich (nur erste 40 s):** ab [00:04] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 382 s), aber nicht vollständig geprüft.

### K01-058 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180754319
- **share_url (Rep. 180754319):** https://app.gethookd.ai/share/ad/180754319?signature=c2f448b1e77995b3820ea2aeafaa418489430de78eff371ab590bb66276a1259
- **Länge:** 380 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MEIN NEUROLOGE“ — Bild: schwarzer Bildschirm mit weißem Text
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754319 / Medium 484395078
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Mein Neurologe meinte, es sei Stress, mein Kardiologe meinte, es sei in die Nerven, mein Hanoarzt meinte
[00:07] Mit meinem Gleichgewicht, Sorgen sei alles in Ordnung und ich konnte zwei Jahre lang nicht vor die Tür gehen
[00:13] ohne Angst zu harmeten auf der Straße, um zu kippen, aber auf die Idee, sich mal meinen Nacken anzusehen,
[00:18] ist keiner von ihnen gekommen, aber ich fand das davon vorn
[00:22] Ich bin fünf, noch sich früher war ich selbstständig, bin überall hingefahren, hatte mein Garten
[00:28] und hab Leben gern auf meine Enkelinn aufgepasst
[00:31] Dann fing der Schwinde an, kein Drehen eher, als würde der Boden unter mir pulsieren, als wäre die Schwerkraft kaputt
[00:39] Mein Hausarzt...
```
- **Abgleich:** keine Übereinstimmung mit einer bekannten Body-Variante in den ersten 40 s → eigener Body, Volltranskript fehlt (Lücke).

### K01-059 – Verlierer – 1 Ad(s), max. 5 Tage

- **Ad-IDs:** 180754302
- **share_url (Rep. 180754302):** https://app.gethookd.ai/share/ad/180754302?signature=cb2dfe6b308018b99e2ba30ba8c5cf74d9240645bef5e1ff9d944512d400969e
- **Länge:** 382 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „und wache morgens erholt auf.“ — Bild: Frau hält das Nacken Therapiekissen (UGC-Testimonial), Untertitel
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754302 / Medium 484395086
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Morgendlicher Schwindel, der trotz Behandlung nicht verschwindet, ist kein Innenohrproblem.
[00:04] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:07] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:11] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem jeden Morgen wachst du auf und fühlst dich benommen.
[00:16] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:20] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:24] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:28] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:31] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:36] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich an deinem alten Kind.
```
- **Abgleich (nur erste 40 s):** ab [00:04] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 382 s), aber nicht vollständig geprüft.

### K01-060 – Verlierer – 2 Ad(s), max. 4 Tage

- **Ad-IDs:** 102485328, 102485336
- **share_url (Rep. 102485328):** https://app.gethookd.ai/share/ad/102485328?signature=5aebc0b5305d8c3a0d7bfcdbe9158613df34c1fa97904316cdc841ef7887009d
- **Länge:** 390 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „ARZT ERKLÄRT IN NUR 15 SEKUNDEN“ — Bild: Frau in Seitenlage mit Nerven-Overlay, Hand zeigt, Gehirn-Icon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 102485328 / Medium 334106769
- **Body-Variante:** K01-B2 (Wortübereinstimmung 90 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Arzt erklärt in nur 15 Sekunden, warum morgendlicher Schwindel immer wiederkommt.
[00:04] Es ist nicht dein Kreislauf, nicht dein Blutdruck.
[00:06] Und nein, du bildest dir das auch nicht ein, auch wenn Ärzte etwas anderes sagen.
[00:10] Tatsächlich liegt die wahre Ursache viel tiefer, versteckt in einem Teil deines Körpers,
[00:14] den du nie hinterfragen würdest.
[00:16] Wissenschaftler fanden heraus, dass Beschwerden wie Nacken- oder Kopfschmerzen,
[00:19] eingeschränkte Beweglichkeit, Schwindel oder Schlaflosigkeit entstehen,
[00:23] weil dein Nacken Nacht für Nacht in einer Fehlstellung verharrt
[00:25] und dein Nervensystem dadurch unter permanentem Stress steht.
[00:28] Und genau deshalb helfen Massagen, Dehnübungen oder Schmerzmittel nur kurzfristig.
[00:33] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:33] wortgleich mit K01-B2 ab [00:26].

### K01-061 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 96489723
- **share_url (Rep. 96489723):** https://app.gethookd.ai/share/ad/96489723?signature=9b9526d182b75a06261c85b8439e260f175755138af0475786e3b19c7a0649c4
- **Länge:** 347 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WAS HABEN VERSPANNUNGEN IM NACKEN“ — Bild: Split: Frau im Sessel mit Hand an Brust / Nacken von hinten mit glühender HWS
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489723 / Medium 315444672
- **Body-Variante:** K01-B1 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam?
[00:03] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:03] wortgleich mit K01-B1 ab [00:08].

### K01-062 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 96489724
- **share_url (Rep. 96489724):** https://app.gethookd.ai/share/ad/96489724?signature=4a408dcfeccb0327103b7b479071b3d377727ec9b0a063524bec053b7a494055
- **Länge:** 349 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN?“ — Bild: schwarzer Hintergrund mit Text (Bild lädt erst später)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 96489724 / Medium 315444667
- **Body-Variante:** K01-B1 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu
[00:03] sagen, das du bisher ignoriert hast.
[00:05] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
```
- **Übergang:** ab [00:05] wortgleich mit K01-B1 ab [00:08].

### K01-063 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 102485304
- **share_url (Rep. 102485304):** https://app.gethookd.ai/share/ad/102485304?signature=3d1ebb895a2f2e76310c6d2fae30381a9f4b6add068f039c6f41c84399510d84
- **Länge:** 392 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: 3D-Röntgen-Kopf auf Kissen mit Gehirn-Icon, rotem Pfeil
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 102485304 / Medium 334106704
- **Body-Variante:** K01-B2 (Wortübereinstimmung 91 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen
[00:04] verursacht.
[00:05] Es ist nicht Dein Kreislauf, nicht Dein Blutdruck und nein, Du bildest Dir das auch nicht ein,
[00:10] auch wenn Ärzte etwas anderes sagen.
[00:11] Tatsächlich liegt die wahre Ursache viel tiefer, versteckt in einem Teil Deines Körpers,
[00:16] den Du nie hinterfragen würdest.
[00:17] Wissenschaftler fanden heraus, dass Beschwerden wie Nacken- oder Kopfschmerzen, eingeschränkte
[00:21] Beweglichkeit, Schwindel oder Schlaflosigkeit entstehen, weil Dein Nacken Nacht für Nacht
[00:25] in einer Fehlstellung verharrt und Dein Nervensystem dadurch unter permanentem Stress steht und
[00:30] genau deshalb helfen Massagen, Dehnübungen oder Schmerzmittel nur kurzfristig.
[00:34] Wenn Du so schläfst, arbeitest Du gegen die natürliche Krümmung Deiner Halswirbelsäule
```
- **Übergang:** ab [00:34] wortgleich mit K01-B2 ab [00:26].

### K01-064 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 102485339
- **share_url (Rep. 102485339):** https://app.gethookd.ai/share/ad/102485339?signature=3727fdb2d9c5a8c363576c9cc0d3701506667d40b9932d1bb9f120be5c43e9fe
- **Länge:** 390 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER SCHWINDEL HÖRT EINFACH NICHT AUF?“ — Bild: Frau hält Kopf, Gehirn-/Nerven-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 102485339 / Medium 334106799
- **Body-Variante:** K01-B2 (Wortübereinstimmung 89 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen.
[00:03] Es ist nicht dein Kreislauf, nicht dein Blutdruck und nein, du bildest dir das auch nicht ein,
[00:08] auch wenn Ärzte etwas anderes sagen.
[00:10] Tatsächlich liegt die wahre Ursache viel tiefer, versteckt in einem Teil deines Körpers,
[00:14] den du nie hinterfragen würdest.
[00:15] Wissenschaftler fanden heraus, dass Beschwerden wie Nacken- oder Kopfschmerzen, eingeschränkte
[00:19] Beweglichkeit, Schwindel oder Schlaflosigkeit entstehen, weil dein Nacken Nacht für Nacht
[00:24] in einer Fehlstellung verharrt und dein Nervensystem dadurch unter permanentem Stress steht.
[00:28] Und genau deshalb helfen Massagen, Dehnübungen oder Schmerzmittel nur kurzfristig.
[00:32] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:32] wortgleich mit K01-B2 ab [00:26].

### K01-065 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 102485319
- **share_url (Rep. 102485319):** https://app.gethookd.ai/share/ad/102485319?signature=75247facc44c0501c9bafcd31ab73e47657f5662acee7649cd45c8cc5398afd8
- **Länge:** 392 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN“ — Bild: rote Glitch-/Laser-Linien im Raum
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 102485319 / Medium 334106755
- **Body-Variante:** K01-B2 (Wortübereinstimmung 90 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand, was das wirklich bedeutet,
[00:04] erfährst du hier.
[00:05] Es ist nicht dein Kreislauf, nicht dein Blutdruck und nein, du bildest dir das auch nicht ein,
[00:10] auch wenn Ärzte etwas anderes sagen.
[00:12] Tatsächlich liegt die wahre Ursache viel tiefer, versteckt in einem Teil deines Körpers,
[00:16] den du nie hinterfragen würdest.
[00:17] Wissenschaftler fanden heraus, dass Beschwerden wie Nacken- oder Kopfschmerzen, eingeschränkte
[00:21] Beweglichkeit, Schwindel oder Schlaflosigkeit entstehen, weil dein Nacken Nacht für Nacht
[00:25] in einer Fehlstellung verharrt und dein Nervensystem dadurch unter permanentem Stress steht.
[00:30] Und genau deshalb helfen Massagen, Dehnübungen oder Schmerzmittel nur kurzfristig.
[00:34] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:34] wortgleich mit K01-B2 ab [00:26].

### K01-066 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 102485349
- **share_url (Rep. 102485349):** https://app.gethookd.ai/share/ad/102485349?signature=9ca04b900f2429749c8250c1a9076b05419e614a75cff6ad4ed8e6461a59a179
- **Länge:** 392 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN?“ — Bild: Person stürzt, rotes Overlay, Gehirn-Icon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 102485349 / Medium 334106807
- **Body-Variante:** K01-B2 (Wortübereinstimmung 90 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu
[00:04] sagen, das du bisher ignoriert hast.
[00:06] Es ist nicht dein Kreislauf, nicht dein Blutdruck.
[00:08] Und nein, du bildest dir das auch nicht ein, auch wenn Ärzte etwas anderes sagen.
[00:12] Tatsächlich liegt die wahre Ursache viel tiefer, versteckt in einem Teil deines Körpers,
[00:16] den du nie hinterfragen würdest.
[00:18] Wissenschaftler fanden heraus, dass Beschwerden wie Nacken- oder Kopfschmerzen, eingeschränkte
[00:22] Beweglichkeit, Schwindel oder Schlaflosigkeit entstehen, weil dein Nacken Nacht für Nacht
[00:26] in einer Fehlstellung verharrt und dein Nervensystem dadurch unter permanentem Stress steht.
[00:30] Und genau deshalb helfen Massagen, Dehnübungen oder Schmerzmittel nur kurzfristig.
[00:34] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:34] wortgleich mit K01-B2 ab [00:26].

### K01-067 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 102485332
- **share_url (Rep. 102485332):** https://app.gethookd.ai/share/ad/102485332?signature=a97cc0745e4fc895acb7f2de3af9503d89144167592fe3b285a08b8d4e04b984
- **Länge:** 390 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER SCHWINDEL HÖRT EINFACH NICHT AUF?“ — Bild: junge Frau hält sich das Gesicht
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 102485332 / Medium 334106786
- **Body-Variante:** K01-B2 (Wortübereinstimmung 89 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen.
[00:03] Es ist nicht dein Kreislauf, nicht dein Blutdruck und nein, du bildest dir das auch nicht ein,
[00:08] auch wenn Ärzte etwas anderes sagen.
[00:10] Tatsächlich liegt die wahre Ursache viel tiefer, versteckt in einem Teil deines Körpers,
[00:14] den du nie hinterfragen würdest.
[00:15] Wissenschaftler fanden heraus, dass Beschwerden wie Nacken- oder Kopfschmerzen, eingeschränkte
[00:19] Beweglichkeit, Schwindel oder Schlaflosigkeit entstehen, weil dein Nacken Nacht für Nacht
[00:24] in einer Fehlstellung verharrt und dein Nervensystem dadurch unter permanentem Stress steht.
[00:28] Und genau deshalb helfen Massagen, Dehnübungen oder Schmerzmittel nur kurzfristig.
[00:32] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:32] wortgleich mit K01-B2 ab [00:26].

### K01-068 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 102485342
- **share_url (Rep. 102485342):** https://app.gethookd.ai/share/ad/102485342?signature=4f44c20e8d2d41bc75fa86fe3bd4c9f10049ca97fbaf3edebf39e817bdac4b98
- **Länge:** 392 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: 3D-Kopf auf Kissen mit rot glühender HWS, roter Pfeil
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 102485342 / Medium 334106805
- **Body-Variante:** K01-B2 (Wortübereinstimmung 91 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen
[00:04] verursacht.
[00:05] Es ist nicht Dein Kreislauf, nicht Dein Blutdruck und nein, Du bildest Dir das auch nicht ein,
[00:10] auch wenn Ärzte etwas anderes sagen.
[00:11] Tatsächlich liegt die wahre Ursache viel tiefer, versteckt in einem Teil Deines Körpers,
[00:16] den Du nie hinterfragen würdest.
[00:17] Wissenschaftler fanden heraus, dass Beschwerden wie Nacken- oder Kopfschmerzen, eingeschränkte
[00:21] Beweglichkeit, Schwindel oder Schlaflosigkeit entstehen, weil Dein Nacken Nacht für Nacht
[00:25] in einer Fehlstellung verharrt und Dein Nervensystem dadurch unter permanentem Stress steht und
[00:30] genau deshalb helfen Massagen, Dehnübungen oder Schmerzmittel nur kurzfristig.
[00:34] Wenn Du so schläfst, arbeitest Du gegen die natürliche Krümmung Deiner Halswirbelsäule
```
- **Übergang:** ab [00:34] wortgleich mit K01-B2 ab [00:26].

### K01-069 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 180754295
- **share_url (Rep. 180754295):** https://app.gethookd.ai/share/ad/180754295?signature=ff720b0d62b20dc2d260b64c400e6f8a07eb5fa1bb3072974295cb0cac593a20
- **Länge:** 384 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DIE MEISTEN ÄRZTE ÜBERSEHEN DAS VÖLLIG“ — Bild: Split: Nerven-Anatomie Hals / Frau mit Muskel-Overlay beim Arzt
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754295 / Medium 484395064
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Die meisten Ärzte übersehen das völlig, wenn Menschen ab 50 morgens mit Schwindel,
[00:04] Benommenheit und Herzrasen aufwachen.
[00:06] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist, beim HNO Arzt wegen
[00:10] dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:13] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem jeden Morgen
[00:16] wachst du auf und fühlst dich benommen.
[00:18] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:22] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner
[00:25] Psyche zu tun.
[00:26] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:30] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:33] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder
[00:37] deine Arme kribbeln und jeder Arzt sagt, alles ist normal.
```
- **Abgleich (nur erste 40 s):** ab [00:06] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 384 s), aber nicht vollständig geprüft.

### K01-070 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 180754293
- **share_url (Rep. 180754293):** https://app.gethookd.ai/share/ad/180754293?signature=c94b44a64cb03126a50e02faa3a1ae2f795615fffea3f17cb4dd0aea65c2e683
- **Länge:** 381 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER FEHLER NR. 1, WARUM DEIN MORGENDLICHER SCHWINDEL“ — Bild: Split: 3D-Skelett-Kopf auf Kissen / Frau im Bett, Gehirn-Icon
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754293 / Medium 484395065
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Der Fehler Nummer eins, warum dein Morgen dich erschwindel, einfach nicht verschwindelt.
[00:03] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:06] Beim HMO Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:10] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:13] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:15] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:19] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:24] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:27] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:30] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:35] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich an deinem alten Kissen.
[00:39] Herkümmer...
```
- **Abgleich (nur erste 40 s):** ab [00:03] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 381 s), aber nicht vollständig geprüft.

### K01-071 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 180754312
- **share_url (Rep. 180754312):** https://app.gethookd.ai/share/ad/180754312?signature=3f7ff12c50b87c78f62a4f82a5e973ccc741313112a4d67e42054618289ed9ba
- **Länge:** 385 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST, DRÜCKST DU JEDE NACHT AUF DIE NERVEN BEI C1 UND C2“ — Bild: Collage: Frau schläft / Skelett-Schädel / Kissen-Grafik
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754312 / Medium 484395072
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Wenn du so schläft, drückst du jede Nacht auf die Nerven bei C1 und C2, die die wahre Ursache für Schwindel, Benommenheit und Herzrasen.
[00:07] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:10] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:14] Vielleicht hat dir sogar jemand antidepressiver verschrieben.
[00:16] Und trotzdem, jeden Morgen wachst du auf und fühlst dich benommen.
[00:19] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:23] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:28] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:31] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:34] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln und jeder Arzt...
```
- **Abgleich (nur erste 40 s):** ab [00:07] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 385 s), aber nicht vollständig geprüft.

### K01-072 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 180754299
- **share_url (Rep. 180754299):** https://app.gethookd.ai/share/ad/180754299?signature=c4dbc6825deaa9efd9353087eaafe7783b7bad3d2230ac3982cac46a616351db
- **Länge:** 381 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „(Untertitel) in einer neutralen Position bleibt“ — Bild: grüner Haken, Person auf Kissen mit grün leuchtender Wirbelsäule (Lösungs-Frame)
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754299 / Medium 484395075
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Hier ist, warum dein morgenlicher Schwindel einfach nicht verschwindet.
[00:03] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:06] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:09] Vielleicht hat dir sogar jemand antidepressiver verschrieben.
[00:12] Und trotzdem, jeden Morgen wachst du auf und fühlst dich benommen.
[00:15] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:19] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:23] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:27] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:30] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist
[00:34] oder deine Arme kribbeln und jeder Arzt sagt, alles ist normal,
[00:37] dann liegt es höchstwahrscheinlich an deinem alten Kissen.
[00:39] Herkömmliche Kissen...
```
- **Abgleich (nur erste 40 s):** ab [00:03] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 381 s), aber nicht vollständig geprüft.

### K01-073 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 103278965
- **share_url (Rep. 103278965):** https://app.gethookd.ai/share/ad/103278965?signature=2208059bfcf154b2e1da1fbf2bab84dc5acf3423a9727ebf1e81aac8f9b586e5
- **Länge:** 439 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WARUM SEITENSCHLÄFER MIT RÄTSELHAFTEN SCHWINDELATTACKEN“ — Bild: Split: Behandlung Frau in Seitenlage / ältere Frau am Podcast-Mikrofon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 103278965 / Medium 336726049
- **Body-Variante:** K01-B2 (Wortübereinstimmung 80 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Warum Seitenschläfer mit rätselhaften Schwindelattacken jetzt zu diesen 3-Zonen-Therapiekissen wechseln?
[00:06] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
[00:11] ist alles instabil, als würde dir der Boden unter den Füßen wegrutschen.
[00:14] Du weißt nicht, ob du dich hinsetzen, hinlegen oder einfach hoffen sollst, dass es gleich
[00:19] vorbei geht.
[00:20] Dein Blutdruck?
[00:21] Normal.
[00:22] Dein MRT?
[00:23] Unauffällig.
[00:24] Die Ärzte?
[00:25] Ratlos.
[00:26] Doch tief in dir weißt du längst, da stimmt irgendwas nicht.
[00:27] Nur keiner kann dir sagen, was es ist.
[00:29] Aber was, wenn du dir das alles nicht einfach einbildest, sondern dein Körper dich versucht
[00:33] zu warnen?
[00:34] Was, wenn der Schwindel kein Fehler ist, sondern ein Schutzmechanismus, weil etwas in dir aus
[00:38] dem Takt geraten ist?
[00:39] In den letzten Jahren taucht in der Fachliteratur immer häufiger der Begriff cervicogener Schwindel
[00:44] auf und die Symptome reichen weit über den Schwindel hinaus.
[00:47] Nackenschmerzen, Kopfdruck, Benommenheit, Kribbeln in den Armen, Schlafstörungen, Panikattacken
[00:53] und manchmal sogar Herzrasen.
[00:55] Ärzte sehen oft nur das Symptom, aber nie den Zusammenhang.
[00:58] Denn all das ist meist nur die Reaktion eines Systems, das im Hintergrund still und leise
[01:02] nach Hilfe schreit.
[01:03] Cervicogener Schwindel wird durch Verspannungen in den tiefen Nackenmuskeln ausgelöst, die
[01:07] Blutfluss- und Nervensignale beeinträchtigen.
[01:10] Es ist also nicht dein Kreislauf, nicht deine Psyche und auch nicht dein Innenohr.
[01:14] Es ist dein Nacken.
[01:15] Und Studien zeigen, dass dieses Problem häufig durch eine nächtliche Fehlstellung der Halswirbelsäule
[01:20] verursacht wird.
[01:21] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [01:21] wortgleich mit K01-B2 ab [00:26].

### K01-074 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 103278983
- **share_url (Rep. 103278983):** https://app.gethookd.ai/share/ad/103278983?signature=c15597c291ec7953500269db1979ea7a6e02a17c58ae771a24317cebadad9cf9
- **Länge:** 438 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „ARZT ERKLÄRT IN NUR 15 SEKUNDEN“ — Bild: Split: Mann hält Kopf mit Sternen-Kreis / Arzt im Kittel am Podcast-Mikrofon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 103278983 / Medium 336726076
- **Body-Variante:** K01-B2 (Wortübereinstimmung 79 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Arzt erklärt in nur 15 Sekunden, warum morgendlicher Schwindel immer wieder kommt.
[00:05] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
[00:10] ist alles instabil, als würde dir der Boden unter den Füßen wegrutschen.
[00:14] Du weißt nicht, ob du dich hinsetzen, hinlegen oder einfach hoffen sollst, dass es gleich
[00:18] vorbei geht.
[00:19] Dein Blutdruck?
[00:20] Normal.
[00:21] Dein MRT?
[00:22] Unauffällig.
[00:23] Die Ärzte?
[00:24] Ratlos.
[00:25] Doch tief in dir weißt du längst, da stimmt irgendwas nicht.
[00:26] Nur keiner kann dir sagen, was es ist.
[00:28] Aber was, wenn du dir das alles nicht einfach einbildest, sondern dein Körper dich versucht
[00:32] zu warnen?
[00:33] Was, wenn der Schwindel kein Fehler ist, sondern ein Schutzmechanismus, weil etwas in dir aus
[00:37] dem Takt geraten ist?
[00:38] In den letzten Jahren taucht in der Fachliteratur immer häufiger der Begriff cervicogener Schwindel
[00:43] auf und die Symptome reichen weit über den Schwindel hinaus.
[00:46] Nackenschmerzen, Kopfdruck, Benommenheit, Kribbeln in den Armen, Schlafstörungen, Panikattacken
[00:52] und manchmal sogar Herzrasen.
[00:54] Ärzte sehen oft nur das Symptom, aber nie den Zusammenhang.
[00:57] Denn all das ist meist nur die Reaktion eines Systems, das im Hintergrund still und leise
[01:01] nach Hilfe schreit.
[01:02] Cervicogener Schwindel wird durch Verspannungen in den tiefen Nackenmuskeln ausgelöst, die
[01:07] Blutfluss- und Nervensignale beeinträchtigen.
[01:09] Es ist also nicht dein Kreislauf, nicht deine Psyche und auch nicht dein Innenohr.
[01:13] Es ist dein Nacken.
[01:14] Und Studien zeigen, dass dieses Problem häufig durch eine nächtliche Fehlstellung der Halswirbelsäule
[01:19] verursacht wird.
[01:20] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [01:20] wortgleich mit K01-B2 ab [00:26].

### K01-075 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 103278980
- **share_url (Rep. 103278980):** https://app.gethookd.ai/share/ad/103278980?signature=83fe39321caa737a56ae70bc76acd2f8c133127e54a148b3ddbc45989231d4c1
- **Länge:** 439 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Split: Behandlung Frau in Seitenlage / Arzt am Mikrofon, roter Pfeil
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 103278980 / Medium 336726106
- **Body-Variante:** K01-B2 (Wortübereinstimmung 81 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen verursacht.
[00:06] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich ist alles instabil.
[00:12] Als würde dir der Boden unter den Füßen wegrutschen.
[00:15] Du weißt nicht, ob du dich hinsetzen, hinlegen oder einfach hoffen sollst, dass es gleich vorbei geht.
[00:19] Dein Blutdruck? Normal.
[00:21] Dein MRT? Unauffällig.
[00:23] Die Ärzte? Ratlos.
[00:24] Doch tief in dir weißt du längst, da stimmt irgendwas nicht.
[00:27] Nur keiner kann dir sagen, was es ist.
[00:29] Aber was, wenn du dir das alles nicht einfach einbildest, sondern dein Körper dich versucht zu warnen?
[00:34] Was, wenn der Schwindel kein Fehler ist, sondern ein Schutzmechanismus, weil etwas in dir aus dem Takt geraten ist?
[00:39] In den letzten Jahren taucht in der Fachliteratur immer häufiger der Begriff cervicogener Schwindel auf
[00:45] und die Symptome reichen weit über den Schwindel hinaus.
[00:47] Nackenschmerzen, Kopfdruck, Benommenheit, Kribbeln in den Armen, Schlafstörungen, Panikattacken und manchmal sogar Herzrasen.
[00:55] Ärzte sehen oft nur das Symptom, aber nie den Zusammenhang.
[00:58] Denn all das ist meist nur die Reaktion eines Systems, das im Hintergrund still und leise nach Hilfe schreit.
[01:03] Cervicogener Schwindel wird durch Verspannungen in den tiefen Nackenmuskeln ausgelöst,
[01:07] die Blutfluss- und Nervensignale beeinträchtigen.
[01:10] Es ist also nicht dein Kreislauf, nicht deine Psyche und auch nicht dein Innenohr.
[01:14] Es ist dein Nacken.
[01:15] Und Studien zeigen, dass dieses Problem häufig durch eine nächtliche Fehlstellung der Halswirbelsäule verursacht wird.
[01:21] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [01:21] wortgleich mit K01-B2 ab [00:26].

### K01-076 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 103278969
- **share_url (Rep. 103278969):** https://app.gethookd.ai/share/ad/103278969?signature=5879ca1e556b7d498b4499af6d6d48f4319946752ea7d8fb8b58dc90720dd338
- **Länge:** 438 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „ARZT ERKLÄRT IN NUR 15 SEKUNDEN“ — Bild: Split: Röntgen-Skelett-Kopf / Mann liegt, Arzt am Mikrofon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 103278969 / Medium 336726075
- **Body-Variante:** K01-B2 (Wortübereinstimmung 80 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Arzt erklärt nur 15 Sekunden, warum morgendlicher Schwindel immer wieder kommt.
[00:05] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
[00:10] ist alles instabil, als würde dir der Boden unter den Füßen wegrutschen.
[00:14] Du weißt nicht, ob du dich hinsetzen, hinlegen oder einfach hoffen sollst, dass es gleich
[00:18] vorbei geht.
[00:19] Dein Blutdruck?
[00:20] Normal.
[00:21] Dein MRT?
[00:22] Unauffällig.
[00:23] Die Ärzte?
[00:24] Ratlos.
[00:25] Doch tief in dir weißt du längst, da stimmt irgendwas nicht.
[00:26] Nur keiner kann dir sagen, was es ist.
[00:28] Aber was, wenn du dir das alles nicht einfach einbildest, sondern dein Körper dich versucht
[00:32] zu warnen?
[00:33] Was, wenn der Schwindel kein Fehler ist, sondern ein Schutzmechanismus, weil etwas in dir aus
[00:37] dem Takt geraten ist?
[00:38] In den letzten Jahren taucht in der Fachliteratur immer häufiger der Begriff cervicogener Schwindel
[00:43] auf und die Symptome reichen weit über den Schwindel hinaus.
[00:46] Nackenschmerzen, Kopfdruck, Benommenheit, Kribbeln in den Armen, Schlafstörungen, Panikattacken
[00:52] und manchmal sogar Herzrasen.
[00:54] Ärzte sehen oft nur das Symptom, aber nie den Zusammenhang.
[00:57] Denn all das ist meist nur die Reaktion eines Systems, das im Hintergrund still und leise
[01:01] nach Hilfe schreit.
[01:02] Cervicogener Schwindel wird durch Verspannungen in den tiefen Nackenmuskeln ausgelöst, die
[01:07] Blutfluss- und Nervensignale beeinträchtigen.
[01:09] Es ist also nicht dein Kreislauf, nicht deine Psyche und auch nicht dein Innenohr.
[01:13] Es ist dein Nacken.
[01:14] Und Studien zeigen, dass dieses Problem häufig durch eine nächtliche Fehlstellung der Halswirbelsäule
[01:19] verursacht wird.
[01:20] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [01:20] wortgleich mit K01-B2 ab [00:26].

### K01-077 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 103278961
- **share_url (Rep. 103278961):** https://app.gethookd.ai/share/ad/103278961?signature=0e160f8fe1b57e960879638a557e4da003876984eeb84546b6b83759f21aa8fd
- **Länge:** 438 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Split: Röntgen-Skelett-Kopf / Mann liegt
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 103278961 / Medium 336726040
- **Body-Variante:** K01-B2 (Wortübereinstimmung 82 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist die schlechteste Schlafposition und warum sie Schwindel, Benommenheit und Herzrasen
[00:04] verursacht.
[00:05] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
[00:10] ist alles instabil, als würde dir der Boden unter den Füßen wegrutschen.
[00:14] Du weißt nicht, ob du dich hinsetzen, hinlegen oder einfach hoffen sollst, dass es gleich
[00:18] vorbei geht.
[00:19] Dein Blutdruck?
[00:20] Normal.
[00:21] Dein MRT?
[00:22] Unauffällig.
[00:23] Die Ärzte?
[00:24] Ratlos.
[00:25] Doch tief in dir weißt du längst, da stimmt irgendwas nicht.
[00:26] Nur keiner kann dir sagen, was es ist.
[00:28] Aber was, wenn du dir das alles nicht einfach einbildest, sondern dein Körper dich versucht
[00:32] zu warnen?
[00:33] Was, wenn der Schwindel kein Fehler ist, sondern ein Schutzmechanismus, weil etwas in dir aus
[00:37] dem Takt geraten ist?
[00:38] In den letzten Jahren taucht in der Fachliteratur immer häufiger der Begriff cervicogener Schwindel
[00:43] auf und die Symptome reichen weit über den Schwindel hinaus.
[00:47] Nackenschmerzen, Kopfdruck, Benommenheit, Kribbeln in den Armen, Schlafstörungen, Panikattacken
[00:52] und manchmal sogar Herzrasen.
[00:54] Ärzte sehen oft nur das Symptom, aber nie den Zusammenhang.
[00:57] Denn all das ist meist nur die Reaktion eines Systems, das im Hintergrund still und leise
[01:01] nach Hilfe schreit.
[01:02] Cervicogener Schwindel wird durch Verspannungen in den tiefen Nackenmuskeln ausgelöst, die
[01:07] Blutfluss- und Nervensignale beeinträchtigen.
[01:09] Es ist also nicht dein Kreislauf, nicht deine Psyche und auch nicht dein Innenohr.
[01:13] Es ist dein Nacken.
[01:14] Und Studien zeigen, dass dieses Problem häufig durch eine nächtliche Fehlstellung der Halswirbelsäule
[01:19] verursacht wird.
[01:20] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [01:20] wortgleich mit K01-B2 ab [00:26].

### K01-078 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 103278978
- **share_url (Rep. 103278978):** https://app.gethookd.ai/share/ad/103278978?signature=74ccaf652db02ca2d808366b01a0deec4eff21b350e6e6287b9b273157d5deb7
- **Länge:** 439 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WARUM SEITENSCHLÄFER MIT RÄTSELHAFTEN SCHWINDELATTACKEN“ — Bild: Split: Frau im Bett / ältere Frau am Podcast-Mikrofon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 103278978 / Medium 336726085
- **Body-Variante:** K01-B2 (Wortübereinstimmung 80 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Warum Seitenschläfer mit rätselhaften Schwindelattacken jetzt zu diesen 3-Zonen-Therapiekissen wechseln?
[00:06] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
[00:11] ist alles instabil, als würde dir der Boden unter den Füßen wegrutschen.
[00:14] Du weißt nicht, ob du dich hinsetzen, hinlegen oder einfach hoffen sollst, dass es gleich
[00:19] vorbei geht.
[00:20] Dein Blutdruck?
[00:21] Normal.
[00:22] Dein MRT?
[00:23] Unauffällig.
[00:24] Die Ärzte?
[00:25] Ratlos.
[00:26] Doch tief in dir weißt du längst, da stimmt irgendwas nicht.
[00:27] Nur keiner kann dir sagen, was es ist.
[00:29] Aber was, wenn du dir das alles nicht einfach einbildest, sondern dein Körper dich versucht
[00:33] zu warnen?
[00:34] Was, wenn der Schwindel kein Fehler ist, sondern ein Schutzmechanismus, weil etwas in dir aus
[00:38] dem Takt geraten ist?
[00:39] In den letzten Jahren taucht in der Fachliteratur immer häufiger der Begriff cervicogener Schwindel
[00:44] auf und die Symptome reichen weit über den Schwindel hinaus.
[00:47] Nackenschmerzen, Kopfdruck, Benommenheit, Kribbeln in den Armen, Schlafstörungen, Panikattacken
[00:53] und manchmal sogar Herzrasen.
[00:55] Ärzte sehen oft nur das Symptom, aber nie den Zusammenhang.
[00:58] Denn all das ist meist nur die Reaktion eines Systems, das im Hintergrund still und leise
[01:02] nach Hilfe schreit.
[01:03] Cervicogener Schwindel wird durch Verspannungen in den tiefen Nackenmuskeln ausgelöst, die
[01:07] Blutfluss- und Nervensignale beeinträchtigen.
[01:10] Es ist also nicht dein Kreislauf, nicht deine Psyche und auch nicht dein Innenohr.
[01:14] Es ist dein Nacken.
[01:15] Und Studien zeigen, dass dieses Problem häufig durch eine nächtliche Fehlstellung der Halswirbelsäule
[01:20] verursacht wird.
[01:21] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [01:21] wortgleich mit K01-B2 ab [00:26].

### K01-079 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 169991782
- **share_url (Rep. 169991782):** https://app.gethookd.ai/share/ad/169991782?signature=db6bd8128e5d849e8d12f098d8caf5acd652958e1d705a63cec09e2e95862e94
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN“ — Bild: ältere Frau im Wohnzimmer, Gehirn-Icon
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169991782 / Medium 465714415
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Morgens Schwindel attacken und plötzlich ist es ein Dauerzustand, was das wirklich bedeutet, erfährst du hier.
[00:05] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:08] Beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:12] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:15] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:17] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:21] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:25] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:29] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:32] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:37] und jeder Arzt sagt, alles ist normal, dann liegt es höchst verschwommen.
```
- **Abgleich (nur erste 40 s):** ab [00:05] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 383 s), aber nicht vollständig geprüft.

### K01-080 – Verlierer – 3 Ad(s), max. 2 Tage

- **Ad-IDs:** 103278967, 103278971, 103278976
- **share_url (Rep. 103278967):** https://app.gethookd.ai/share/ad/103278967?signature=dff8c39125640994db776a6c0f3e32d649f21f7b7e92016bd0cbb05720f0e0a3
- **Länge:** 438 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER BODEN FÜHLT SICH BEIM AUFSTEHEN WACKELIG AN?“ — Bild: Person im grauen Hoodie sitzt im Bett
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 103278967 / Medium 336726058
- **Body-Variante:** K01-B2 (Wortübereinstimmung 80 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Boden fühlt sich beim Aufstehen wackelig an, dann versucht dein Körper dir etwas zu
[00:04] sagen, das du bisher ignoriert hast.
[00:06] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
[00:10] ist alles instabil, als würde dir der Boden unter den Füßen wegrutschen.
[00:14] Du weißt nicht, ob du dich hinsetzen, hinlegen oder einfach hoffen sollst, dass es gleich
[00:18] vorbei geht.
[00:19] Dein Blutdruck?
[00:20] Normal.
[00:21] Dein MRT?
[00:22] Unauffällig.
[00:23] Die Ärzte?
[00:24] Ratlos.
[00:25] Doch tief in dir weißt du längst, da stimmt irgendwas nicht.
[00:27] Nur keiner kann dir sagen, was es ist.
[00:29] Aber was, wenn du dir das alles nicht einfach einbildest, sondern dein Körper dich versucht
[00:33] zu warnen?
[00:34] Was, wenn der Schwindel kein Fehler ist, sondern ein Schutzmechanismus, weil etwas in dir aus
[00:38] dem Takt geraten ist?
[00:39] In den letzten Jahren taucht in der Fachliteratur immer häufiger der Begriff cervicogener Schwindel
[00:44] auf und die Symptome reichen weit über den Schwindel hinaus.
[00:47] Nackenschmerzen, Kopfdruck, Benommenheit, Kribbeln in den Armen, Schlafstörungen, Panikattacken
[00:53] und manchmal sogar Herzrasen.
[00:54] Ärzte sehen oft nur das Symptom, aber nie den Zusammenhang.
[00:57] Denn all das ist meist nur die Reaktion eines Systems, das im Hintergrund still und leise
[01:02] nach Hilfe schreit.
[01:03] Cervicogener Schwindel wird durch Verspannungen in den tiefen Nackenmuskeln ausgelöst, die
[01:07] Blutfluss- und Nervensignale beeinträchtigen.
[01:10] Es ist also nicht dein Kreislauf, nicht deine Psyche und auch nicht dein Innenohr.
[01:14] Es ist dein Nacken.
[01:15] Und Studien zeigen, dass dieses Problem häufig durch eine nächtliche Fehlstellung der Halswirbelsäule
[01:20] verursacht wird.
[01:21] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [01:21] wortgleich mit K01-B2 ab [00:26].

### K01-081 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 101489233
- **share_url (Rep. 101489233):** https://app.gethookd.ai/share/ad/101489233?signature=384994219ee64cfbf2fc2b36a5563fc7efd036e7c01fb1ec0288e604dd2642d2
- **Länge:** 370 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DER SCHWINDEL HÖRT EINFACH NICHT AUF?“ — Bild: Frau mit rotem Glitch-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 101489233 / Medium 331073191
- **Body-Variante:** K01-B2 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der Schwindel hört einfach nicht auf, die wahre Ursache wird dich überraschen.
[00:03] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [00:03] wortgleich mit K01-B2 ab [00:26].

### K01-082 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 103278974
- **share_url (Rep. 103278974):** https://app.gethookd.ai/share/ad/103278974?signature=ae84b9e25d5d0a4aecb83b73017b73b569e5883be59a7c8b120abd5ef486ff2a
- **Länge:** 438 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MORGENS SCHWINDELATTACKEN“ — Bild: Split: Talking-Head Mann mit Sternen / ältere Frau am Mikrofon
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 103278974 / Medium 336726070
- **Body-Variante:** K01-B2 (Wortübereinstimmung 79 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Morgens Schwindelattacken und plötzlich ist es ein Dauerzustand?
[00:03] Was das wirklich bedeutet, erfährst du hier.
[00:06] Manchmal reicht schon eine schnelle Kopfbewegung, ein Geräusch oder ein Lichtwechsel und plötzlich
[00:10] ist alles instabil, als würde dir der Boden unter den Füßen wegrutschen.
[00:14] Du weißt nicht, ob du dich hinsetzen, hinlegen oder einfach hoffen sollst, dass es gleich
[00:18] vorbei geht.
[00:19] Dein Blutdruck?
[00:20] Normal.
[00:21] Dein MRT?
[00:22] Unauffällig.
[00:23] Die Ärzte?
[00:24] Ratlos.
[00:25] Doch tief in dir weißt du längst, da stimmt irgendwas nicht.
[00:27] Nur keiner kann dir sagen, was es ist.
[00:28] Aber was, wenn du dir das alles nicht einfach einbildest, sondern dein Körper dich versucht
[00:33] zu warnen?
[00:34] Was, wenn der Schwindel kein Fehler ist, sondern ein Schutzmechanismus, weil etwas in dir aus
[00:38] dem Takt geraten ist?
[00:39] In den letzten Jahren taucht in der Fachliteratur immer häufiger der Begriff cervicogener Schwindel
[00:44] auf und die Symptome reichen weit über den Schwindel hinaus.
[00:47] Nackenschmerzen, Kopfdruck, Benommenheit, Kribbeln in den Armen, Schlafstörungen, Panikattacken
[00:53] und manchmal sogar Herzrasen.
[00:54] Ärzte sehen oft nur das Symptom, aber nie den Zusammenhang.
[00:57] Denn all das ist meist nur die Reaktion eines Systems, das im Hintergrund still und leise
[01:02] nach Hilfe schreit.
[01:03] Cervicogener Schwindel wird durch Verspannungen in den tiefen Nackenmuskeln ausgelöst, die
[01:07] Blutfluss- und Nervensignale beeinträchtigen.
[01:10] Es ist also nicht dein Kreislauf, nicht deine Psyche und auch nicht dein Innenohr.
[01:14] Es ist dein Nacken.
[01:15] Und Studien zeigen, dass dieses Problem häufig durch eine nächtliche Fehlstellung der Halswirbelsäule
[01:20] verursacht wird.
[01:21] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
```
- **Übergang:** ab [01:21] wortgleich mit K01-B2 ab [00:26].

### K01-083 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 170682413
- **share_url (Rep. 170682413):** https://app.gethookd.ai/share/ad/170682413?signature=762c427ce0ed7ea1eb046e72f9c24fff64bfab2328346521f7ea6e06ca85d719
- **Länge:** 387 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL UND BENOMMENHEIT AUFWACHST“ — Bild: Split: ältere Frau mit Gehirn-Overlay / Person im Bett
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 170682413 / Medium 466951679
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Wenn du morgens mit Schwindel und Benommen halt aufwachst, hör jetzt genau zu.
[00:03] Das ist kein Innenor-Problem, sondern eine Nervenkompression bei C1 und C2 während des Schlafs.
[00:09] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist,
[00:12] beim HNO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:15] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:19] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:21] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:24] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:29] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:33] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:36] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder
```
- **Abgleich (nur erste 40 s):** ab [00:09] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 387 s), aber nicht vollständig geprüft.

### K01-084 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 170682404
- **share_url (Rep. 170682404):** https://app.gethookd.ai/share/ad/170682404?signature=92c447b1b41b31fbd60f5c3c830718c85d8a4f48e08b0f26c4034ccd9e556a2d
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Frau in Seitenlage mit Muskel-Overlay, glühender Nacken
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 170682404 / Medium 466951619
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Das ist die schlechteste Schlafposition.
[00:02] Und warum sie Schwindel, Benommenheit und Herzrasen verursacht.
[00:05] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:08] Beim HMO Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:11] Vielleicht hat dir sogar jemand antidepressiver verschrieben.
[00:14] Und trotzdem, jeden Morgen wachst du auf und fühlst dich benommen.
[00:17] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:20] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:25] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:29] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:32] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:37] und jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich...
```
- **Abgleich (nur erste 40 s):** ab [00:00] wortgleich mit Body-Variante **K01-B2** ab [00:00] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 383 s), aber nicht vollständig geprüft.

### K01-085 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 169991787
- **share_url (Rep. 169991787):** https://app.gethookd.ai/share/ad/169991787?signature=09b0680c035d760a4db19b309beeac899b7e9936b853ef0051fc190b7285199b
- **Länge:** 384 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU AUF DER SEITE SCHLÄFST UND MORGENS MIT SCHWINDEL AUFWACHST“ — Bild: Frau in Seitenlage mit Muskel-Overlay
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 169991787 / Medium 465714442
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Wenn du auf der Seite schläft und morgens mit Schwindel aufwachst, hör jetzt genau zu.
[00:04] Denn das Problem liegt nicht dort, wo dein Arzt sucht.
[00:06] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
[00:09] Beim HMO-Arzt wegen dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:12] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem.
[00:16] Jeden Morgen wachst du auf und fühlst dich benommen.
[00:18] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:22] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche zu tun.
[00:26] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:30] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:33] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln
[00:38] und jeder Arzt sagt, alles ist normal.
```
- **Abgleich (nur erste 40 s):** ab [00:06] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 384 s), aber nicht vollständig geprüft.

### K01-086 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 180754292
- **share_url (Rep. 180754292):** https://app.gethookd.ai/share/ad/180754292?signature=66d0385650a14d9ce77a35c2f5327e497b5c9a33486faa65a1f0c78d8bf0edde
- **Länge:** 382 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DEIN MORGENDLICHER SCHWINDEL IST KEIN INNEN-OHR PROBLEM.“ — Bild: Arzt untersucht Ohr einer Frau mit Muskel-Overlay
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754292 / Medium 484395063
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Dein morgendlicher Schwindel ist kein Innenohrproblem. Hier ist, was es wirklich ist.
[00:04] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist. Beim HNO-Arzt wegen
[00:08] dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht. Vielleicht hat dir sogar jemand antidepressiver
[00:13] verschrieben und trotzdem jeden Morgen wachst du auf und fühlst dich benommen. Dein
[00:16] Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren. Aber
[00:20] diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner Psyche
[00:24] zu tun. Wenn du so schläft, arbeitest du gegen die natürliche Krümung deiner
[00:27] Halswirbelsäule und klemmst dabei die Arterien ab, die dein Gehirn versorgen. Falls du morgens
[00:32] also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine Arme kribbeln und
[00:36] jeder Arzt sagt, alles ist normal, dann liegt es höchstwahrscheinlich an deinem alten
```
- **Abgleich (nur erste 40 s):** ab [00:04] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 382 s), aber nicht vollständig geprüft.

### K01-087 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 180754283
- **share_url (Rep. 180754283):** https://app.gethookd.ai/share/ad/180754283?signature=7afc1f2d48aae5506c298527e4db73f9bbb305769080c23aba510ca256889e79
- **Länge:** 383 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST, DRÜCKST DU AUF DEINEN VAGUSNERV“ — Bild: Frau in Seitenlage mit Muskel-Overlay
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180754283 / Medium 484395046
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Wenn du so schläft, drückst du auf deinen Varbusnerv und riskierst Schwindel, Herzrasen
[00:04] und Benommenheit.
[00:05] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist, beim HNO Arzt wegen
[00:09] dem Schwindel, beim Augenarzt wegen der verschwommenen Sicht.
[00:12] Vielleicht hat dir sogar jemand antidepressiver verschrieben und trotzdem jeden Morgen
[00:16] wachst du auf und fühlst dich benommen.
[00:17] Dein Herz rast manchmal ohne Grund und du kannst dich tagsüber kaum konzentrieren.
[00:21] Aber diese Symptome haben nichts mit deinem Ohr, deinen Augen, Stress oder deiner
[00:25] Psyche zu tun.
[00:26] Wenn du so schläft, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule
[00:29] und klemmst dabei die Arterien ab, die dein Gehirn versorgen.
[00:32] Falls du morgens also mit Schwindel aufwachst, du tagsüber ständig benommen bist oder deine
[00:36] Arme kribbeln und jeder Arzt sagt, alles ist normal, dann liegt es höchstens
```
- **Abgleich (nur erste 40 s):** ab [00:05] wortgleich mit Body-Variante **K01-B2** ab [00:05] – der Rest des Videos ist sehr wahrscheinlich identisch mit K01-B2 (Länge 383 s), aber nicht vollständig geprüft.

### K01-088 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 97625526
- **share_url (Rep. 97625526):** https://app.gethookd.ai/share/ad/97625526?signature=3dc9cdfd2230376a70a192f1ef3101068153d72b07f5c3f5662a629d780e7913
- **Länge:** 381 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WAS HABEN VERSPANNUNGEN IM NACKEN,“ — Bild: Hinterkopf/Nacken mit rot glühender HWS
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625526 / Medium 319025321
- **Body-Variante:** K01-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam?
[00:03] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:03] wortgleich mit K01-B2 ab [00:05].

### K01-089 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 97625522
- **share_url (Rep. 97625522):** https://app.gethookd.ai/share/ad/97625522?signature=0ba8eef1d80d93f6661741f5aae9122d43cfc2f66524c8d741ccc325edefd3c5
- **Länge:** 381 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WAS HABEN VERSPANNUNGEN IM NACKEN,“ — Bild: Hand massiert Nacken
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625522 / Medium 319025328
- **Body-Variante:** K01-B2 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Was haben Verspannungen im Nacken, Schwindel und Müdigkeit gemeinsam?
[00:03] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:03] wortgleich mit K01-B2 ab [00:05].

### K01-090 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 97625530
- **share_url (Rep. 97625530):** https://app.gethookd.ai/share/ad/97625530?signature=aeda05143457733231996993b085c5e3aa67e07239ee56684c8d6b8e0a2f5838
- **Länge:** 384 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST,“ — Bild: Person in Seitenlage mit glühender HWS, Kreis-Einblendung Schädel von oben
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 97625530 / Medium 319025330
- **Body-Variante:** K01-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, schneidest du langsam die Blutzufuhr zu deinem Gehirn ab.
[00:03] Und kein Arzt hat dir das jemals gesagt.
[00:06] Du warst wahrscheinlich schon bei jedem Arzt, der dir eingefallen ist.
```
- **Übergang:** ab [00:06] wortgleich mit K01-B2 ab [00:05].

### K02-091 – Winner – 17 Ad(s), max. 109 Tage

- **Ad-IDs:** 105856101, 105856102, 107108716, 107474406, 107474404, 107474405, 119048659, 119048724, 119048648, 119048643, 119048651, 119048655, 119048601, 119048721, 119048598, 119048662, 180307657
- **share_url (Rep. 107108716):** https://app.gethookd.ai/share/ad/107108716?signature=22fa77c2ee57cb148ce3f9f43c67b182cf97dd2c463c5e45bb11a658499ddfd9
- **Länge:** 311 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION → UND WIE DU STATTDESSEN SCHLAFEN SOLLTEST (0–3 s)“ — Bild: Hände an Hüfte einer Person in Seitenlage mit Muskel-Overlay → Wirbelsäulen-Kreis-Einblendung → Behandlungsszene (Therapeut + Experte im blauen Kasack) → UGC-Frau mit brennendem Bein
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 107108716 / Medium 349177087
- **Volltranskript:** = Referenz der Body-Variante **K02-B1** (oben vollständig).

### K02-092 – Kandidat – 5 Ad(s), max. 18 Tage

- **Ad-IDs:** 105856106, 105856111, 107474413, 180307755, 180307761
- **share_url (Rep. 180307755):** https://app.gethookd.ai/share/ad/180307755?signature=562a6fd0d548f58fab7508b43a2763694fbfeb8197977657df4d20946a61a1d2
- **Länge:** 312 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DER GRÖSSTE FEHLER BEI NÄCHTLICHEM ISCHIAS IST ZU DENKEN“ — Bild: Person in Seitenlage mit Muskel-Overlay, Ischiasnerv gelb
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 105856106 / Medium 344733307
- **Body-Variante:** K02-B1 (Wortübereinstimmung 100 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
(kein eigener Vorspann – startet direkt wortgleich)
```
- **Übergang:** ab [00:00] wortgleich mit K02-B1 ab [00:00].

### K02-093 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 180307721
- **share_url (Rep. 180307721):** https://app.gethookd.ai/share/ad/180307721?signature=99671d002632ce622360ecefc61ad8e29d0db307c3cc685084af255672deec0c
- **Länge:** 312 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN SIND MEIST KEIN BANDSCHEIBENPROBLEM“ — Bild: Frau stehend, Becken-/Nerven-Overlay, Therapeutenhand
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180307721 / Medium 483696498
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Ischias Schmerzen sind meist kein Bandscheibenproblem. Es ist ein Positionsproblem im Schlaf.
[00:04] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule
[00:08] und klimmst dabei dein Ischias-Nerv ab. Falls du nachts also aufwachst, weil dein Bein brennt,
[00:13] du Taubheitsgefühle vom Gesäß bis in die Zähnen hast oder dich das stechende Zin aus dem Schlaf reißt,
[00:18] dann liegt das höchstwahrscheinlich an deiner Schlafposition.
[00:20] Wenn du auf der Seite schläfst ohne die richtige Unterstützung, dann kippt deine Hüfte über und deine Wirbelsäule verdreht sich.
[00:26] Das bedeutet, deine Wirbelsäule liegt die ganze Nacht in einer ungesunden, verdrehten Position,
[00:31] auch posturale Schlaffehlstellung genannt und du merkst es nicht mal.
[00:34] Und diese dauerhaft falsche Schlafposition löst eine regelrechte Kettenreaktion aus.
[00:39] Denn sobald ein Bein...
```
- **Abgleich (nur erste 40 s):** ab [00:04] wortgleich mit Body-Variante **K02-B1** ab [00:03] – der Rest des Videos ist sehr wahrscheinlich identisch mit K02-B1 (Länge 312 s), aber nicht vollständig geprüft.

### K02-094 – Kandidat – 1 Ad(s), max. 18 Tage

- **Ad-IDs:** 180307731
- **share_url (Rep. 180307731):** https://app.gethookd.ai/share/ad/180307731?signature=e757adfb8731da46417989761f86f978a24d20c8a0f6ad4da54dbbf58e66a7a6
- **Länge:** 314 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WARNUNG: DAS IST DIE GEFÄHRLICHSTE SCHLAFPOSITION FÜR SEITENSCHLÄFER“ — Bild: Behandlung Frau in Seitenlage mit Muskel-Overlay
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180307731 / Medium 483696525
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Warnung, das ist die gefährlichste Schlafposition für Seitenschläfer und warum sie Schmerzen
[00:04] und Taubheitsgefühle in deinen Beinen verursacht.
[00:06] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule
[00:10] und klemmst dabei deinen Ischiasnerv ab.
[00:12] Haltst du nachts also aufwachsen, weil dein Bein brennt.
[00:15] Du Taubheitsgefühle vom Gesäß bis in die Zähnen hast oder dich das stechende Ziehen
[00:18] aus dem Schlaf reist, dann liegt das höchstwahrscheinlich an deiner Schlafposition.
[00:22] Wenn du auf der Seite schläfst ohne die richtige Unterstützung, dann kippt deine
[00:26] Hüfte über und deine Wirbelsäule verdreht sich.
[00:28] Das bedeutet, deine Wirbelsäule liegt die ganze Nacht in einer ungesunden, verdrehten Position.
[00:33] Auch posturale Schlaffehlstellung genannt.
[00:35] Und du merkst es nicht mal.
[00:36] Und diese dauerhaft falsche Schlafposition löst eine regelrechte
```
- **Abgleich (nur erste 40 s):** ab [00:06] wortgleich mit Body-Variante **K02-B1** ab [00:03] – der Rest des Videos ist sehr wahrscheinlich identisch mit K02-B1 (Länge 314 s), aber nicht vollständig geprüft.

### K02-095 – Verlierer – 2 Ad(s), max. 7 Tage

- **Ad-IDs:** 105856108, 107474422
- **share_url (Rep. 107474422):** https://app.gethookd.ai/share/ad/107474422?signature=3108011f8a365fc2007604055aadf395459f0c39856e161e9c7df85ae1c2cb78
- **Länge:** 311 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN“ — Bild: Therapeut behandelt Person auf Liege (Muskel-Overlay)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 107474422 / Medium 350222774
- **Body-Variante:** K02-B1 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Ishiyas Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv.
[00:03] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule
[00:07] und klemmst dabei deinen Ishiyas Nerv ab.
```
- **Übergang:** ab [00:07] wortgleich mit K02-B1 ab [00:07].

### K02-096 – Verlierer – 2 Ad(s), max. 7 Tage

- **Ad-IDs:** 105856105, 107474420
- **share_url (Rep. 107474420):** https://app.gethookd.ai/share/ad/107474420?signature=f70c6432fc00b664adadb727ee91d7c08985134c2de133227de9248f0eac04aa
- **Länge:** 311 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN“ — Bild: Behandlung + eingeblendeter Experte (Mann im blauen Kasack) erklärt
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 107474420 / Medium 350222771
- **Body-Variante:** K02-B1 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Ishiyas Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv.
[00:03] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule
[00:07] und klemmst dabei deinen Ishiyas Nerv ab.
```
- **Übergang:** ab [00:07] wortgleich mit K02-B1 ab [00:07].

### K02-097 – Verlierer – 2 Ad(s), max. 6 Tage

- **Ad-IDs:** 105856112, 107474416
- **share_url (Rep. 105856112):** https://app.gethookd.ai/share/ad/105856112?signature=533ab0803864fc3bba5583f2b67a9ce9a0b710f391fe874db1f55f5f28f29595
- **Länge:** 310 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „SEITENSCHLÄFER AUFGEPASST: DU REIZT DEINEN ISCHIASNERV WÄHREND DU SCHLÄFST“ — Bild: Hände an Hüfte, Muskel-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 105856112 / Medium 344733335
- **Body-Variante:** K02-B1 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Seitenschläfer aufgepasst! Du reizt deinen Ischiasnerv, während du schläfst. Wenn du so schläfst,
```
- **Übergang:** ab [00:00] wortgleich mit K02-B1 ab [00:03].

### K02-098 – Verlierer – 2 Ad(s), max. 6 Tage

- **Ad-IDs:** 105856104, 107474411
- **share_url (Rep. 105856104):** https://app.gethookd.ai/share/ad/105856104?signature=a411d5ab19c302b497b699abc958c3e6f0354be706e115f77858aa0fb6e9fc25
- **Länge:** 312 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST: QUETSCHT DU DEINEN ISCHIASNERV EIN“ — Bild: Frau in Seitenlage (real), schwarzes Shirt
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 105856104 / Medium 344733304
- **Body-Variante:** K02-B1 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte Schäden in deiner Wirbelsäule.
[00:04] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule und klemmst dabei dein Ischiasnerv ab.
```
- **Übergang:** ab [00:04] wortgleich mit K02-B1 ab [00:07].

### K02-099 – Verlierer – 2 Ad(s), max. 6 Tage

- **Ad-IDs:** 107474417, 180307763
- **share_url (Rep. 180307763):** https://app.gethookd.ai/share/ad/180307763?signature=6d66f1b01b20dc4a2f4f2251dcb0eb196d6c70f866169e79906d2363a6ed4523
- **Länge:** 326 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN ENTSTEHEN“ — Bild: Person in Seitenlage mit Muskel-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 107474417 / Medium 350222811
- **Body-Variante:** K02-B1 (Wortübereinstimmung 94 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte Schäden in deiner Wirbelsäule.
[00:04] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ischiasschmerzen zu lindern, oder?
[00:10] Falsch!
[00:10] Okay, also sollte man auf dem Rücken schlafen, richtig?
[00:13] Leider nein!
[00:14] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:18] Genau!
[00:18] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule und klemmst dabei deinen Ischiasnerv ab.
```
- **Übergang:** ab [00:18] wortgleich mit K02-B1 ab [00:03].

### K02-100 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180307741
- **share_url (Rep. 180307741):** https://app.gethookd.ai/share/ad/180307741?signature=d5efd0abe1cef95166b1403fe9c106c7af929583e79706739553b70a8a99ad51
- **Länge:** 325 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ARZT ERKLÄRT IN NUR 15 SEKUNDEN, WARUM ISCHIASSCHMERZEN“ — Bild: Rücken mit glühender Lendenwirbelsäule, Zeigefinger
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180307741 / Medium 483696518
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Arzt erklärt in nur 15 Sekunden, warum Ichjas-Schmerzen jeden Morgen wiederkommen.
[00:04] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ichjas-Schmerzen zu lindern, oder?
[00:10] Falsch.
[00:10] Okay, also sollte man auf dem Rücken schlafen, richtig?
[00:13] Leider nein.
[00:14] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:17] Genau, wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule und klemmst dabei dein Ichjas-Nerv ab.
[00:24] Falls du nachts also aufwachst, weil dein Bein brennt, du Taubheitsgefühle vom Gesäß bis in die Zähne hast
[00:29] oder dich das stechende Ziehen aus dem Schlaf reist, dann liegt das höchstwahrscheinlich an deiner Schlafposition.
[00:34] Wenn du auf der Seite schläfst ohne die richtige Unterstützung, dann kippt deine Hüfte über und deine Wirbelsäule verdreht sich.
```
- **Abgleich (nur erste 40 s):** ab [00:17] wortgleich mit Body-Variante **K02-B1** ab [00:03] – der Rest des Videos ist sehr wahrscheinlich identisch mit K02-B1 (Länge 325 s), aber nicht vollständig geprüft.

### K02-101 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180307744
- **share_url (Rep. 180307744):** https://app.gethookd.ai/share/ad/180307744?signature=425557b2be5b48f56b596680c7af67ebf01d931c1171b8a849d6bf1e1b6f6096
- **Länge:** 325 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DER FEHLER NR. 1 WARUM DEINE MORGENDLICHEN ISCHIASSCHMERZEN“ — Bild: Rückansicht Frau, Ischiasnerv-Overlay, Hand zeigt
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180307744 / Medium 483696519
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Der Fehler Nummer eins, warum deine morgendlichen Ischiaschmerzen einfach nicht verschwinden.
[00:04] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ischiaschmerzen zu lindern, oder?
[00:10] Falsch.
[00:10] Okay, Eise sollte man auf dem Rücken schlafen, richtig?
[00:13] Leider nein.
[00:14] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:17] Genau, wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule und klimmst dabei dein Ischiasnerv ab.
[00:24] Falls du nachts also aufwachst, weil dein Bein brennt, du Taubheitsgefühle vom Gesäß bis in die Zähnen hast
[00:29] oder dich das stechende Ziehen aus dem Schlaf reist, dann liegt das höchstwahrscheinlich an deiner Schlafposition.
[00:34] Wenn du auf der Seite schläfst ohne die richtige Unterstützung, dann kippt deine Hüfte über und deine Wirbelsäule verdreht sich.
```
- **Abgleich (nur erste 40 s):** ab [00:17] wortgleich mit Body-Variante **K02-B1** ab [00:03] – der Rest des Videos ist sehr wahrscheinlich identisch mit K02-B1 (Länge 325 s), aber nicht vollständig geprüft.

### K02-102 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180307697
- **share_url (Rep. 180307697):** https://app.gethookd.ai/share/ad/180307697?signature=208e0152b2772a6801733c84733a8ebd7b038b8855a1c4ee43481d429e7137c6
- **Länge:** 312 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DIE MEISTEN ÄRZTE ÜBERSEHEN DAS VÖLLIG“ — Bild: Arzt zeigt auf Patientin in Seitenlage (Muskel-Overlay)
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180307697 / Medium 483696446
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Die meisten Ärzte übersehen das völlig, wenn Seitenschläfer ab 50 mit Ischias-Schmerzen
[00:04] aufwachen.
[00:05] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule
[00:09] und klimmst dabei dein Ischias-Nerv ab.
[00:11] Falls du nachts also aufwachst, weil dein Bein brennt, du Taubheitsgefühle vom Gesäß
[00:15] bis in die Zähnen hast oder dich das stechende Ziehen aus dem Schlaf reist, dann liegt
[00:18] das höchstwahrscheinlich an deiner Schlafposition.
[00:21] Wenn du auf der Seite schläfst ohne die richtige Unterstützung, dann kippt deine
[00:24] Hüfte über und deine Wirbelsäule verdreht sich.
[00:27] Das bedeutet, deine Wirbelsäule liegt die ganze Nacht in einer ungesunden, verdrehten
[00:31] Position, auch posturale Schlaffehlstellung genannt.
[00:34] Und du merkst es nicht mal.
[00:35] Und diese dauerhaft falsche Schlafposition löst eine regelrechte Kettenreaktion aus.
```
- **Abgleich (nur erste 40 s):** ab [00:05] wortgleich mit Body-Variante **K02-B1** ab [00:03] – der Rest des Videos ist sehr wahrscheinlich identisch mit K02-B1 (Länge 312 s), aber nicht vollständig geprüft.

### K02-103 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180307752
- **share_url (Rep. 180307752):** https://app.gethookd.ai/share/ad/180307752?signature=4ad97145129795923a22bf765ef38934b99f9ecd8f54daac7090aec17dbb78ba
- **Länge:** 327 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU AUF DER SEITE SCHLÄFST“ — Bild: Rücken/Gesäß mit Muskel-Overlay, Hand
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180307752 / Medium 483696511
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Wenn du auf der Seite schläft und morgens mit einem tauben, brennenden Bein aufwachst,
[00:04] hier ist der Grund, den dir niemand erklärt hat.
[00:06] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ischias-Schmerzen zu lindern, oder?
[00:11] Falsch.
[00:12] Okay, also sollte man auf dem Rücken schlafen, richtig?
[00:14] Leider nein.
[00:15] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:19] Genau, wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule und klimbst dabei dein Ischias-Nerven ab.
[00:25] Falls du nachts also aufwachst, weil dein Bein brennt, du Taubheitsgefühle vom Gesäß bis in die Zähnen hast,
[00:30] oder dich das stechende Ziehen aus dem Schlaf reißt, dann liegt das höchstwahrscheinlich an deiner Schlafposition.
[00:35] Wenn du auf der Seite schläfst, ohne die richtige Unterstützung, dann kipp deine Hüfte über und dein...
```
- **Abgleich (nur erste 40 s):** ab [00:19] wortgleich mit Body-Variante **K02-B1** ab [00:03] – der Rest des Videos ist sehr wahrscheinlich identisch mit K02-B1 (Länge 327 s), aber nicht vollständig geprüft.

### K02-104 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180307673
- **share_url (Rep. 180307673):** https://app.gethookd.ai/share/ad/180307673?signature=aa805c5763f049d1af6596ad78762bd31b46d86b231ea8070a87477cdb05d5fb
- **Länge:** 326 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Frau auf Behandlungsliege mit Muskel-Overlay, Therapeut
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180307673 / Medium 483696410
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Das ist die schlechteste Schlafposition.
[00:02] Und warum sie Schmerzen und Taubheizgefühle in deinen Beinen verursacht.
[00:05] Ein Kissen zwischen den Beinen ist der beste Weg,
[00:08] um als Seitenschläfer Ischiaschmerzen zu lindern, oder?
[00:11] Falsch!
[00:11] Okay, Eise sollte man auf dem Rücken schlafen, richtig?
[00:14] Leider nein!
[00:15] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:19] Genau! Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung
[00:22] deiner Wirbelsäule und klimbst dabei dein Ischiasnerv ab.
[00:25] Falls du nachts also aufwachst, weil dein Bein brennt,
[00:27] du Taubheizgefühle vom Gesäß bis in die Zähnen hast,
[00:30] oder dich das stechende Ziehen aus dem Schlaf reist,
[00:32] dann liegt das höchstwahrscheinlich an deiner Schlafposition.
[00:35] Wenn du auf der Seite schläfst, ohne die richtige Unterstützung,
[00:37] dann kippt deine Hüfte über und deine Wirbelsäule...
```
- **Abgleich (nur erste 40 s):** ab [00:19] wortgleich mit Body-Variante **K02-B1** ab [00:03] – der Rest des Videos ist sehr wahrscheinlich identisch mit K02-B1 (Länge 326 s), aber nicht vollständig geprüft.

### K02-105 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180307735
- **share_url (Rep. 180307735):** https://app.gethookd.ai/share/ad/180307735?signature=cd7d34d0b24de479f9b2ef00248a8b25773f2a8f74aa4bf36f58dbed252829a9
- **Länge:** 327 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU NACHTS EINEN SCHMERZ IM GESÄSS SPÜRST“ — Bild: Frau auf Liege in Seitenlage, Ischiasnerv-Overlay
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180307735 / Medium 483696504
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Wenn du nachts einen Schmerz im Gesäß spürst, der bis ins Bein runterstrahlt,
[00:04] dann sind das typische Ishiyas-Symptome.
[00:06] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschlefer Ishiyas-Schmerzen zu lindern, oder?
[00:11] Falsch.
[00:12] Okay, Eise sollte man auf dem Rücken schlafen, richtig?
[00:15] Leider nein.
[00:15] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:19] Genau.
[00:20] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule
[00:24] und klimbst dabei dein Ishiyas-Nerv ab.
[00:25] Falls du nachts also aufwachst, weil dein Bein brennt,
[00:28] du Taubheitsgefühle vom Gesäß bis in die Zähnen hast, oder dich das stechende Ziehen aus dem Schlaf reißt,
[00:33] dann liegt das höchstwahrscheinlich an deiner Schlafposition.
[00:35] Wenn du auf der Seite schläfst ohne die richtige Unterstützung, dann kippt deine Hüfte über,
```
- **Abgleich (nur erste 40 s):** ab [00:20] wortgleich mit Body-Variante **K02-B1** ab [00:03] – der Rest des Videos ist sehr wahrscheinlich identisch mit K02-B1 (Länge 327 s), aber nicht vollständig geprüft.

### K02-106 – Verlierer – 1 Ad(s), max. 5 Tage

- **Ad-IDs:** 107474419
- **share_url (Rep. 107474419):** https://app.gethookd.ai/share/ad/107474419?signature=a57a07e110fccbc9e47d1d40992bee56b4790d58bd979d64be96a2f9b8b12abe
- **Länge:** 324 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN“ — Bild: Behandlung + Experte im blauen Kasack
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 107474419 / Medium 350222810
- **Body-Variante:** K02-B1 (Wortübereinstimmung 94 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Ischias Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv.
[00:03] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ischias Schmerzen zu lindern, oder?
[00:09] Falsch!
[00:09] Okay, also sollte man auf dem Rücken schlafen, richtig?
[00:12] Leider nein!
[00:13] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:16] Genau! Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule und klemmst dabei deinen Ischiasnerv ab.
```
- **Übergang:** ab [00:16] wortgleich mit K02-B1 ab [00:03].

### K02-107 – Verlierer – 1 Ad(s), max. 5 Tage

- **Ad-IDs:** 107474414
- **share_url (Rep. 107474414):** https://app.gethookd.ai/share/ad/107474414?signature=626130bef1a1ba945dd8e033e6d6717bea45e72007517f97efa6528f023bcb85
- **Länge:** 324 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN“ — Bild: Therapeut behandelt Person auf Liege
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 107474414 / Medium 350222801
- **Body-Variante:** K02-B1 (Wortübereinstimmung 94 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Ischias Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv.
[00:03] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ischias Schmerzen zu lindern, oder?
[00:09] Falsch!
[00:09] Okay, also sollte man auf dem Rücken schlafen, richtig?
[00:12] Leider nein!
[00:13] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:16] Genau! Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule und klemmst dabei deinen Ischiasnerv ab.
```
- **Übergang:** ab [00:16] wortgleich mit K02-B1 ab [00:03].

### K02-108 – Verlierer – 1 Ad(s), max. 5 Tage

- **Ad-IDs:** 107474408
- **share_url (Rep. 107474408):** https://app.gethookd.ai/share/ad/107474408?signature=72f8391b36d68c1593182821bc3351a9d707ac87e8a97036687e5bf4d32a462c
- **Länge:** 326 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST: QUETSCHT DU DEINEN ISCHIASNERV EIN“ — Bild: Frau in Seitenlage (real)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 107474408 / Medium 350222789
- **Body-Variante:** K02-B1 (Wortübereinstimmung 94 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte Schäden in deiner Wirbelsäule.
[00:04] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ischiasschmerzen zu lindern, oder?
[00:10] Falsch!
[00:10] Okay, also sollte man auf dem Rücken schlafen, richtig?
[00:13] Leider nein!
[00:14] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:18] Genau!
[00:18] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule und klemmst dabei deinen Ischiasnerv ab.
```
- **Übergang:** ab [00:18] wortgleich mit K02-B1 ab [00:03].

### K02-109 – Verlierer – 2 Ad(s), max. 4 Tage

- **Ad-IDs:** 104077018, 104077021
- **share_url (Rep. 104077018):** https://app.gethookd.ai/share/ad/104077018?signature=8afaf7baf82d8ef41c62dcca0eb0be2ce692166f1a0af52b8be08a8d18492239
- **Länge:** 318 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST: QUETSCHT DU DEINEN ISCHIASNERV EIN“ — Bild: Person in Seitenlage mit Muskel-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077018 / Medium 339067210
- **Volltranskript:** = Referenz der Body-Variante **K02-B2** (oben vollständig).

### K02-110 – Verlierer – 2 Ad(s), max. 4 Tage

- **Ad-IDs:** 104077015, 104077022
- **share_url (Rep. 104077015):** https://app.gethookd.ai/share/ad/104077015?signature=13b36a8e4cea2145f5fac86a2803af406bbb13f2c87880c46bf856897484b389
- **Länge:** 317 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „SO HÖREN NÄCHTLICHE ISCHIASSCHMERZEN SOFORT AUF“ — Bild: Therapeut an Person in Seitenlage (Muskel-Overlay)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077015 / Medium 339067213
- **Body-Variante:** K02-B2 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] So hören nächtliche Ischia-Schmerzen sofort auf.
[00:02] Ich sehe das jeden Tag.
```
- **Übergang:** ab [00:02] wortgleich mit K02-B2 ab [00:04].
- **Weitere abweichende Stellen (wörtlich):**

```text
[01:56] Nach 9 Monaten Entwicklungszeit und 3 Prototypen entstand vor 2 Jahren schließlich das Schlaftherapie-Kissen.
…
```

### K02-111 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 104077014
- **share_url (Rep. 104077014):** https://app.gethookd.ai/share/ad/104077014?signature=a016db04263dd2d2bb3333852c92372a571de947053c97ad4177398857b0a350
- **Länge:** 317 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN“ — Bild: Frau von hinten, steht in Wohnung
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077014 / Medium 339067202
- **Body-Variante:** K02-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Ichiyas Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv.
[00:03] Ich sehe das jeden Tag.
```
- **Übergang:** ab [00:03] wortgleich mit K02-B2 ab [00:04].
- **Weitere abweichende Stellen (wörtlich):**

```text
[01:56] Nach 9 Monaten Entwicklungszeit und 3 Prototypen,
[01:59] entstand vor 2 Jahren schließlich das Schlaftherapie-Kissen.
…
```

### K02-112 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 104077011
- **share_url (Rep. 104077011):** https://app.gethookd.ai/share/ad/104077011?signature=984eee3802dce241ab74dce05ff3dc9d8348166209814b37d94a72495a798bec
- **Länge:** 320 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST: VERDREHST DU JEDE NACHT DEINE WIRBELSÄULE“ — Bild: Person in Bauch-/Seitenlage mit Muskel-Overlay, Therapeut
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077011 / Medium 339067211
- **Body-Variante:** K02-B2 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, verdrehst du jede Nacht deine Wirbelsäule und klemmst dabei deinen
[00:04] Ischiasnerv ein.
[00:05] Ohne es überhaupt zu merken.
[00:06] Ich sehe das jeden Tag.
```
- **Übergang:** ab [00:06] wortgleich mit K02-B2 ab [00:04].
- **Weitere abweichende Stellen (wörtlich):**

```text
[01:59] Nach 9 Monaten Entwicklungszeit und 3 Prototypen entstand vor 2 Jahren schließlich das Schlaftherapie-Kissen.
…
```

### K02-113 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 104077019
- **share_url (Rep. 104077019):** https://app.gethookd.ai/share/ad/104077019?signature=bddf5c4a844c564c615ec38e8abd465fa7056e0fb35c1e721269574c76401580
- **Länge:** 317 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN KOMMEN NICHT AUS DEM BEIN“ — Bild: Therapeut kniet an liegender Person in Praxis
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077019 / Medium 339067220
- **Body-Variante:** K02-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Ichiyas Schmerzen kommen nicht aus dem Bein, sondern von einem eingeklemmten Nerv.
[00:03] Ich sehe das jeden Tag.
```
- **Übergang:** ab [00:03] wortgleich mit K02-B2 ab [00:04].
- **Weitere abweichende Stellen (wörtlich):**

```text
[01:56] Nach 9 Monaten Entwicklungszeit und 3 Prototypen entstand vor 2 Jahren schließlich das Schlaftherapie-Kissen.
…
```

### K02-114 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 104077023
- **share_url (Rep. 104077023):** https://app.gethookd.ai/share/ad/104077023?signature=d93214f28d3552ad63849b041146608521e624913e2cbcd1869d1343b924d59f
- **Länge:** 319 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „JEDE NACHT IN DER DU SO SCHLÄFST“ — Bild: Therapeut an Person in Seitenlage (Muskel-Overlay)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077023 / Medium 339067228
- **Body-Variante:** K02-B2 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Jede Nacht, in der du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte
[00:04] Schäden in deinen Beinen.
[00:05] Sehe das jeden Tag, Menschen wachen mit stärkeren Schmerzen auf, mehr Steifheit im unteren Rücken,
```
- **Übergang:** ab [00:05] wortgleich mit K02-B2 ab [00:04].
- **Weitere abweichende Stellen (wörtlich):**

```text
[01:58] Nach 9 Monaten Entwicklungszeit und 3 Prototypen entstand vor 2 Jahren schließlich das Schlaftherapie-Kissen.
…
```

### K02-115 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 104077025
- **share_url (Rep. 104077025):** https://app.gethookd.ai/share/ad/104077025?signature=979a7f63fe8107e43937abf550a0fbb5787fec912482ba90314e1f7a4627b70e
- **Länge:** 319 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „JEDE NACHT IN DER DU SO SCHLÄFST“ — Bild: Person in Seitenlage mit Muskel-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077025 / Medium 339067237
- **Body-Variante:** K02-B2 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Jede Nacht, in der du so schläfst, quetschst du dein Ischiasnerv ein und riskierst dauerhafte
[00:04] Schäden in deinen Beinen.
[00:05] Sehe das jeden Tag.
```
- **Übergang:** ab [00:05] wortgleich mit K02-B2 ab [00:04].
- **Weitere abweichende Stellen (wörtlich):**

```text
[01:58] Nach 9 Monaten Entwicklungszeit und 3 Prototypen entstand vor 2 Jahren schließlich das Schlaftherapie-Kissen.
…
```

### K02-116 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 104077024
- **share_url (Rep. 104077024):** https://app.gethookd.ai/share/ad/104077024?signature=f291c5aa309aff56911c8801424a55222874e420a7f302379faca94bef8b8831
- **Länge:** 317 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „SEITENSCHLÄFER AUFGEPASST: DU REIZT DEINEN ISCHIASNERV WÄHREND DU SCHLÄFST“ — Bild: Therapeut an Person in Seitenlage
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077024 / Medium 339067238
- **Body-Variante:** K02-B2 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Seitenschläfer aufgepasst! Du reizt dein Ischiasnerv während du schläfst.
[00:03] Ich sehe das jeden Tag. Menschen wachen mit stärkeren Schmerzen auf. Mehr Steifheit im
```
- **Übergang:** ab [00:03] wortgleich mit K02-B2 ab [00:04].
- **Weitere abweichende Stellen (wörtlich):**

```text
[01:55] Nach 9 Monaten Entwicklungszeit und 3 Prototypen entstand vor 2 Jahren schließlich das
[02:00] Schlaftherapie-Kissen. Ein orthopädisches Ganzkörperkissen, das genau dort entlastet,
…
```

### K02-117 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 180307750
- **share_url (Rep. 180307750):** https://app.gethookd.ai/share/ad/180307750?signature=cdeacfca5376e969f158b8ee4d0278174ecd2715bc09c608605687d769e09870
- **Länge:** 325 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ARZT ERKLÄRT: DESHALB GEHEN NÄCHTLICHE ISCHIASSCHMERZEN“ — Bild: Finger zeigt auf Anatomie-Tafel Ischias (Hüftschmerzen, Taubheitsgefühl …)
- **Transkript-Quelle:** lokal, faster-whisper „small“ – NUR erste 40 s · Ad 180307750 / Medium 483696507
- **Volltranskript:** GetHooked-Transkription bei Redaktionsschluss noch „processing“ → hier der lokal transkribierte **Anfang (erste 40 s)** wörtlich:

```text
[00:00] Arzt erklärt, deshalb gehen nächtliche Ischiaschmerzen einfach nicht weg.
[00:03] Ein Kissen zwischen den Beinen ist der beste Weg, um als Seitenschläfer Ischiaschmerzen zu lindern, oder?
[00:09] Falsch.
[00:09] Okay, Eise sollte man auf dem Rücken schlafen, richtig?
[00:12] Leider nein.
[00:13] Warte mal, heißt das etwa, dass ich mir meine Wirbelsäule im Schlaf ruiniere?
[00:17] Genau, wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Wirbelsäule
[00:21] und klimmst dabei dein Ischiasnerv ab.
[00:23] Falls du nachts also aufwachst, weil dein Bein brennt,
[00:25] du Taubheitsgefühle vom Gesäß bis in die Zähnen hast oder dich das stechende Ziehen aus dem Schlaf reißt,
[00:30] dann liegt das höchstwahrscheinlich an deiner Schlafposition.
[00:33] Wenn du auf der Seite schläfst ohne die richtige Unterstützung,
[00:36] dann kippt deine Hüfte über und deine Wirbelsäule verdreht sich.
[00:39] Das bedeutet...
```
- **Abgleich (nur erste 40 s):** ab [00:17] wortgleich mit Body-Variante **K02-B1** ab [00:03] – der Rest des Videos ist sehr wahrscheinlich identisch mit K02-B1 (Länge 325 s), aber nicht vollständig geprüft.

### K02-118 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 104077016
- **share_url (Rep. 104077016):** https://app.gethookd.ai/share/ad/104077016?signature=387c77b4f40ccfee310d34f15f5f4c7179e9f7d81f4ac458b68a4957396888da
- **Länge:** 317 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „SO HÖREN NÄCHTLICHE ISCHIASSCHMERZEN SOFORT AUF“ — Bild: Person in Seitenlage mit Muskel-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077016 / Medium 339067212
- **Body-Variante:** K02-B2 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] So hören nächtliche Ischia-Schmerzen sofort auf.
[00:02] Ich sehe das jeden Tag.
```
- **Übergang:** ab [00:02] wortgleich mit K02-B2 ab [00:04].
- **Weitere abweichende Stellen (wörtlich):**

```text
[01:56] Nach 9 Monaten Entwicklungszeit und 3 Prototypen entstand vor 2 Jahren schließlich das Schlaftherapie-Kissen.
…
```

### K02-119 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 104077012
- **share_url (Rep. 104077012):** https://app.gethookd.ai/share/ad/104077012?signature=744378ac45c7628346a2ffb89c1c0ea6ecd9d605f2cd04259ec9af35022a3aec
- **Länge:** 320 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST: VERDREHST DU JEDE NACHT DEINE WIRBELSÄULE“ — Bild: Frau schläft in Seitenlage (real, Bettwäsche)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 104077012 / Medium 339067204
- **Body-Variante:** K02-B2 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, verdrehst du jede Nacht deine Wirbelsäule und klemmst dabei deinen
[00:04] Ischiasnerv ein.
[00:05] Ohne es überhaupt zu merken.
[00:06] Ich sehe das jeden Tag.
```
- **Übergang:** ab [00:06] wortgleich mit K02-B2 ab [00:04].
- **Weitere abweichende Stellen (wörtlich):**

```text
[01:59] Nach 9 Monaten Entwicklungszeit und 3 Prototypen entstand vor 2 Jahren schließlich das Schlaftherapie-Kissen.
…
```

### K02-120 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 180307724
- **share_url (Rep. 180307724):** https://app.gethookd.ai/share/ad/180307724?signature=e754ad12e9a5853c655ceea2d95a58b1df792f03b5314c2c82cd5d3222dd1686
- **Länge:** 312 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DER FEHLER NR. 1 WARUM DEINE MORGENDLICHEN ISCHIASSCHMERZEN“ — Bild: Rückansicht Frau, Ischiasnerv-Overlay
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K02-121 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 180307711
- **share_url (Rep. 180307711):** https://app.gethookd.ai/share/ad/180307711?signature=ff299d6702ce8617c66261056569aec6d84b45eedbe0a6f5c3674dc4bb829a51
- **Länge:** 312 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ARZT ERKLÄRT IN NUR 15 SEKUNDEN, WARUM ISCHIASSCHMERZEN“ — Bild: Rücken mit glühender Lendenwirbelsäule, Zeigefinger
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K02-122 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 180307669
- **share_url (Rep. 180307669):** https://app.gethookd.ai/share/ad/180307669?signature=ee6bacf381a9af85f6e7523eadd5df9e7bec0a54345890389c00e7a072f28d62
- **Länge:** 313 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Frau auf Behandlungsliege mit Muskel-Overlay, Therapeut
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K02-123 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 180307747
- **share_url (Rep. 180307747):** https://app.gethookd.ai/share/ad/180307747?signature=84186b641aeb94ba1cc12605fb01a4257b4712d3ad5f02686e0806f26517e961
- **Länge:** 327 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN, DIE NACHTS TROTZ ÜBUNGEN WIEDERKOMMEN?“ — Bild: Gesäß-/Hüft-Anatomie mit glühendem Ischiasnerv, roter Pfeil
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K02-124 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 180307727
- **share_url (Rep. 180307727):** https://app.gethookd.ai/share/ad/180307727?signature=fff4922791a2564da80e4b786fff97f915cdad2296d975d9959221f09f7969b2
- **Länge:** 311 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ARZT ERKLÄRT: DESHALB GEHEN NÄCHTLICHE ISCHIASSCHMERZEN“ — Bild: Finger auf Anatomie-Tafel Ischias
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K02-125 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 180307708
- **share_url (Rep. 180307708):** https://app.gethookd.ai/share/ad/180307708?signature=439a5474bc18757a06f5786e5dd0ef3e764511da5bf9cac78b04b0aac0241a42
- **Länge:** 313 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU NACHTS EINEN SCHMERZ IM GESÄß SPÜRST“ — Bild: Frau in Seitenlage auf Liege, Ischias-Overlay
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K02-126 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 180307710
- **share_url (Rep. 180307710):** https://app.gethookd.ai/share/ad/180307710?signature=5b75c08ee8d39cbb34b6d58009ec742073fa4caee1e0344afda6f660b6a5e6ad
- **Länge:** 313 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „ISCHIASSCHMERZEN, DIE NACHTS TROTZ ÜBUNGEN WIEDERKOMMEN?“ — Bild: Gesäß-Anatomie mit glühendem Ischiasnerv
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K02-127 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 180307664
- **share_url (Rep. 180307664):** https://app.gethookd.ai/share/ad/180307664?signature=5a53289323135cf718d269ff3fbc583ef4340de09bedb21825f60c60a3b7f5cb
- **Länge:** 313 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU AUF DER SEITE SCHLÄFST“ — Bild: Rücken/Gesäß mit Muskel-Overlay, Hand
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K02-128 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 180307757
- **share_url (Rep. 180307757):** https://app.gethookd.ai/share/ad/180307757?signature=676442fa19d0b921df892e178451ca8418eba3da6d385daef25691deddc4438d
- **Länge:** 174 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: kleines Skelett-Modell liegt auf grauer Bettdecke
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K05-187 – Winner – 14 Ad(s), max. 206 Tage

- **Ad-IDs:** 74481256, 74485763, 107108723, 110088159, 119048629, 119048627, 119048715, 119048616, 119048717, 119048623, 119048709, 119048620, 119048711, 119048704
- **share_url (Rep. 74485763):** https://app.gethookd.ai/share/ad/74485763?signature=445d441d4f97c39e641c6c8dee7be327243afc43c3723eecf3f5ebf9d029f7a7
- **Länge:** 466 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „So hört schnarchen sofort auf. (schwarzer Balken, „schnarchen“ rot hinterlegt)“ — Bild: Nacken-Nahaufnahme, Hände, rotes Glühen → gleiches Bild grün (Vorher/Nachher) → 3D-Atemweg verengt → schnarchender Mann auf Sofa → 3D-Rachen kollabiert
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 74485763 / Medium 245033961
- **Volltranskript:** = Referenz der Body-Variante **K05-B1** (oben vollständig).

### K05-188 – Winner – 12 Ad(s), max. 164 Tage

- **Ad-IDs:** 74485761, 74485759, 107108718, 119048691, 119048638, 119048634, 119048701, 119048698, 119048693, 119048699, 119048695, 119048688
- **share_url (Rep. 74485761):** https://app.gethookd.ai/share/ad/74485761?signature=5d8069d6b21559c98f250540e5c10887c2c81e11dabcc510112ebf1f34e0cf89
- **Länge:** 466 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „So hört schnarchen sofort auf.“ — Bild: Mann liegt, rot glühender Hals/Atemweg, roter Pfeil
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 74485761 / Medium 245034009
- **Body-Variante:** K05-B1 (Wortübereinstimmung 100 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
(kein eigener Vorspann – startet direkt wortgleich)
```
- **Übergang:** ab [00:00] wortgleich mit K05-B1 ab [00:00].

### K05-189 – Winner – 3 Ad(s), max. 67 Tage

- **Ad-IDs:** 87782140, 90347406, 107108738
- **share_url (Rep. 90347406):** https://app.gethookd.ai/share/ad/90347406?signature=9843ec84451f8ab4d8f6d7c915e1eb52bb5b8d759d46b6d1eca873a92bd27c89
- **Länge:** 80 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „Wir haben einen Schlafapnoe Patienten gebeten“ — Bild: Mann mit CPAP-Maske schläft im Bett (weißes Textfeld)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 90347406 / Medium 296611384
- **Volltranskript:** = Referenz der Body-Variante **K05-B2** (oben vollständig).

### K05-190 – Kandidat – 1 Ad(s), max. 31 Tage

- **Ad-IDs:** 87782145
- **share_url (Rep. 87782145):** https://app.gethookd.ai/share/ad/87782145?signature=4088329b62e0290ec84e414f780c0c922566040a94f4413994ad70c770db6df3
- **Länge:** 79 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „Wenn ein Mann von seinem CPAP Gerät auf“ — Bild: Mann mit CPAP-Maske im Bett
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 87782145 / Medium 288517383
- **Body-Variante:** K05-B2 (Wortübereinstimmung 94 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn ein Mann von seinem CPAP-Gerät auf das Nacken-Therapie-Kissen umsteigt, passiert Folgendes.
[00:05] In der ersten Nacht reagiert sein Körper auf eine Weise, wie es keine Maschine jemals schaffen könnte.
```
- **Übergang:** ab [00:05] wortgleich mit K05-B2 ab [00:06].

### K05-191 – Kandidat – 1 Ad(s), max. 31 Tage

- **Ad-IDs:** 87782142
- **share_url (Rep. 87782142):** https://app.gethookd.ai/share/ad/87782142?signature=6628adce27805e632c3f09dae6c15fc8f06a28cf88d77f23ee8aeab897e88a68
- **Länge:** 80 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „Wir haben einen Schlafapnoe Patienten gebeten“ — Bild: Mann mit CPAP-Maske im Bett
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 87782142 / Medium 288517394
- **Body-Variante:** K05-B2 (Wortübereinstimmung 100 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
(kein eigener Vorspann – startet direkt wortgleich)
```
- **Übergang:** ab [00:00] wortgleich mit K05-B2 ab [00:00].

### K09-238 – Winner – 13 Ad(s), max. 203 Tage

- **Ad-IDs:** 74485768, 98148688, 107108736, 119048683, 119048730, 119048613, 119048666, 119048680, 119048685, 119048674, 119048615, 119048670, 119048726
- **share_url (Rep. 74485768):** https://app.gethookd.ai/share/ad/74485768?signature=b03d7e13a07ea52d0ae08ad055ded9040e093e7e6852caeb1940ba6d9a8ef3fe
- **Länge:** 401 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-das-schlaftherapie-kissen-1
- **Eingeblendeter Hook-Text (Startframe):** „Das ist die schlechteste Schlafposition (schwarzer Balken, „die schlechteste“ rot) → „und wie du stattdessen schlafen solltest““ — Bild: Beine in Seitenlage mit Muskel-Overlay → Frau schläft mit Kissen zwischen den Beinen → rotes X („Okay“)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 74485768 / Medium 245033989
- **Volltranskript:** = Referenz der Body-Variante **K09-B1** (oben vollständig).

### K11-247 – Verlierer – 1 Ad(s), max. 10 Tage

- **Ad-IDs:** 92876643
- **share_url (Rep. 92876643):** https://app.gethookd.ai/share/ad/92876643?signature=dcb43cc2149ff983bc159740405b5d73b252067a05076371cf492914d5e2612b
- **Länge:** 341 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION BEI NACKENSCHMERZEN“ — Bild: Therapeut an Mann in Seitenlage mit Muskel-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876643 / Medium 304565237
- **Volltranskript:** = Referenz der Body-Variante **K11-B1** (oben vollständig).

### K11-248 – Verlierer – 1 Ad(s), max. 9 Tage

- **Ad-IDs:** 92876647
- **share_url (Rep. 92876647):** https://app.gethookd.ai/share/ad/92876647?signature=85de9f9da5227ae61849a0ae4f10f6bab07d59775974d23520b795061e195ee1
- **Länge:** 318 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION BEI NACKENSCHMERZEN“ — Bild: Therapeut an Mann in Seitenlage mit Muskel-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876647 / Medium 304565229
- **Body-Variante:** K11-B1 (Wortübereinstimmung 93 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist die schlechteste Schlafposition bei Nackenschmerzen und wie du stattdessen schlafen
[00:04] solltest.
[00:05] Und viele Betroffene versuchen dann, die Beschwerden mit Schmerzmitteln zu betäuben.
[00:08] Aber diese beheben nicht die Ursache, sie überdecken nur die Schmerzen im Nacken.
[00:12] Oder sie probieren Physiotherapie und Dehnübungen aus.
[00:15] Aber das ist nicht nur zeitaufwendig, sondern es bringt oft nur kurzzeitige Linderung.
[00:19] Mach stattdessen das hier.
[00:20] Die traurige Wahrheit ist, die meisten Menschen achten auf ihre Haltung beim Sitzen, vermeiden
```
- **Übergang:** ab [00:20] wortgleich mit K11-B1 ab [00:43].

### K11-249 – Verlierer – 1 Ad(s), max. 8 Tage

- **Ad-IDs:** 92876646
- **share_url (Rep. 92876646):** https://app.gethookd.ai/share/ad/92876646?signature=e42574025330951175bdc4b904a205eab5d63ec7ef58129939852037b82a0c1d
- **Länge:** 342 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „NACKENSCHMERZEN DIE TROTZ BEHANDLUNGEN NICHT VERSCHWINDEN“ — Bild: Frau im Bett greift sich an den Nacken (rot markiert)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876646 / Medium 304565235
- **Body-Variante:** K11-B1 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Nackenschmerzen, die trotz Behandlungen nicht verschwinden, sind keine Verspannung, sondern
[00:04] ein Schlafpositionsproblem.
[00:05] Was diese zwei MRT-Bilder aus Österreich aufgedeckt haben, hat alles verändert, was
```
- **Übergang:** ab [00:05] wortgleich mit K11-B1 ab [00:04].

### K11-250 – Verlierer – 1 Ad(s), max. 7 Tage

- **Ad-IDs:** 92876652
- **share_url (Rep. 92876652):** https://app.gethookd.ai/share/ad/92876652?signature=28898ddf76fe072e83777ed9bf63f5c138ebb5261fd66694b6d5016aeb133167
- **Länge:** 320 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DER GRÖßTE FEHLER BEI NACKENSCHMERZEN IST ZU DENKEN“ — Bild: Split: Frau mit Laptop hält Nacken / 3D-Wirbel
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876652 / Medium 304565254
- **Body-Variante:** K11-B1 (Wortübereinstimmung 92 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der größte Fehler bei Nackenschmerzen ist zu denken, dass es ein Haltungsproblem ist.
[00:04] Dabei liegt die wahre Ursache in der Schlafposition.
[00:06] Und viele Betroffene versuchen dann, die Beschwerden mit Schmerzmittel zu betäuben.
[00:10] Aber diese beheben nicht die Ursache, sie überdecken nur die Schmerzen im Nacken.
[00:14] Oder sie probieren Physiotherapie und Dehnübungen aus.
[00:17] Aber das ist nicht nur zeitaufwendig, sondern es bringt oft nur kurzzeitige Linderung.
[00:21] Mach stattdessen das hier.
[00:23] Die traurige Wahrheit ist, die meisten Menschen achten auf ihre Haltung beim Sitzen,
```
- **Übergang:** ab [00:23] wortgleich mit K11-B1 ab [00:43].

### K11-251 – Verlierer – 1 Ad(s), max. 7 Tage

- **Ad-IDs:** 92876648
- **share_url (Rep. 92876648):** https://app.gethookd.ai/share/ad/92876648?signature=c0d3d82165da6470b37a4ef7fbb9c8b5571129db0de92b445bf04ae5719df5b7
- **Länge:** 318 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST ZERSTÖRST DU LANGSAM DEINE HALSWIRBELSÄULE“ — Bild: Therapeut an Person mit Muskel-Overlay
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876648 / Medium 304565256
- **Body-Variante:** K11-B1 (Wortübereinstimmung 93 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn Du so schläfst, zerstörst Du langsam Deine Halswirbelsäule, besonders C5 und C6.
[00:05] Und viele Betroffene versuchen dann, die Beschwerden mit Schmerzmitteln zu betäuben.
[00:09] Aber diese beheben nicht die Ursache, sie überdecken nur die Schmerzen im Nacken.
[00:13] Oder sie probieren Physiotherapie und Dehnübungen aus.
[00:16] Aber das ist nicht nur zeitaufwendig, sondern es bringt oft nur kurzzeitige Linderung.
[00:20] Mach stattdessen das hier.
[00:21] Die traurige Wahrheit ist, die meisten Menschen achten auf ihre Haltung beim Sitzen,
```
- **Übergang:** ab [00:21] wortgleich mit K11-B1 ab [00:43].

### K11-252 – Verlierer – 1 Ad(s), max. 7 Tage

- **Ad-IDs:** 92876644
- **share_url (Rep. 92876644):** https://app.gethookd.ai/share/ad/92876644?signature=6e43011f3dd9c7fc937ab3e6a9067037c9422c9e6edae92ae7db78daf390652c
- **Länge:** 318 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION BEI NACKENSCHMERZEN“ — Bild: Muskel-Overlay Nacken, Kreis-Einblendung Bandscheibe
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876644 / Medium 304565230
- **Body-Variante:** K11-B1 (Wortübereinstimmung 94 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist die schlechteste Schlafposition bei Nackenschmerzen und wie du stattdessen schlafen solltest.
[00:04] Und viele Betroffene versuchen dann, die Beschwerden mit Schmerzmittel zu betäuben.
[00:08] Aber diese beheben nicht die Ursache, sie überdecken nur die Schmerzen im Nacken.
[00:12] Oder sie probieren Physiotherapie und Dehnübungen aus.
[00:15] Aber das ist nicht nur zeitaufwendig, sondern es bringt oft nur kurzzeitige Linderung.
[00:19] Mach stattdessen das hier.
[00:20] Die traurige Wahrheit ist, die meisten Menschen achten auf ihre Haltung beim Sitzen,
```
- **Übergang:** ab [00:20] wortgleich mit K11-B1 ab [00:43].

### K11-253 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 92876649
- **share_url (Rep. 92876649):** https://app.gethookd.ai/share/ad/92876649?signature=fa54d6e90a551c63087a1bc97a54ab53c7bba67a74223ed84c8aef8ee123dc33
- **Länge:** 320 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DER GRÖßTE FEHLER BEI NACKENSCHMERZEN IST ZU DENKEN“ — Bild: Frau im Bett hält Nacken (rot markiert)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876649 / Medium 304565247
- **Body-Variante:** K11-B1 (Wortübereinstimmung 92 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der größte Fehler bei Nackenschmerzen ist zu denken, dass es ein Haltungsproblem ist.
[00:04] Dabei liegt die wahre Ursache in der Schlafposition.
[00:06] Und viele Betroffene versuchen dann, die Beschwerden mit Schmerzmittel zu betäuben.
[00:10] Aber diese beheben nicht die Ursache, sie überdecken nur die Schmerzen im Nacken.
[00:14] Oder sie probieren Physiotherapie und Dehnübungen aus.
[00:17] Aber das ist nicht nur zeitaufwendig, sondern es bringt oft nur kurzzeitige Linderung.
[00:21] Mach stattdessen das hier.
[00:23] Die traurige Wahrheit ist, die meisten Menschen achten auf ihre Haltung beim Sitzen,
```
- **Übergang:** ab [00:23] wortgleich mit K11-B1 ab [00:43].

### K11-254 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 92876653
- **share_url (Rep. 92876653):** https://app.gethookd.ai/share/ad/92876653?signature=9792c0be93191eaa25d029beafac6979dac7dedaaa920baa6b5000c256d2a37a
- **Länge:** 319 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „NACKENSCHMERZEN DIE TROTZ BEHANDLUNGEN NICHT VERSCHWINDEN“ — Bild: Frau im Bett hält Nacken
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876653 / Medium 304565245
- **Body-Variante:** K11-B1 (Wortübereinstimmung 91 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Nackenschmerzen, die trotz Behandlungen nicht verschwinden, sind keine Verspannung, sondern
[00:04] ein Schlafpositionsproblem.
[00:06] Und viele Betroffene versuchen dann, die Beschwerden mit Schmerzmitteln zu betäuben.
[00:09] Aber diese beheben nicht die Ursache, sie überdecken nur die Schmerzen im Nacken.
[00:13] Oder sie probieren Physiotherapie und Dehnübungen aus.
[00:16] Aber das ist nicht nur zeitaufwendig, sondern es bringt oft nur kurzzeitige Linderung.
[00:21] Mach stattdessen das hier.
[00:22] Die traurige Wahrheit ist, die meisten Menschen achten auf ihre Haltung beim Sitzen, vermeiden
```
- **Übergang:** ab [00:22] wortgleich mit K11-B1 ab [00:43].

### K11-255 – Verlierer – 1 Ad(s), max. 5 Tage

- **Ad-IDs:** 92876645
- **share_url (Rep. 92876645):** https://app.gethookd.ai/share/ad/92876645?signature=d50f787b5a5ffd413c1c75a9efee1f9b8c39df8652d30807fa7bdb05a08adbc5
- **Länge:** 343 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DER GRÖßTE FEHLER BEI NACKENSCHMERZEN IST ZU DENKEN“ — Bild: Split: Frau mit Laptop / 3D-Wirbel
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876645 / Medium 304565233
- **Body-Variante:** K11-B1 (Wortübereinstimmung 95 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Der größte Fehler bei Nackenschmerzen ist zu denken, dass es ein Haltungsproblem ist.
[00:04] Dabei liegt die wahre Ursache in der Schlafposition.
[00:06] Was diese zwei MRT-Bilder aus Österreich aufgedeckt haben, hat alles verändert, was
```
- **Übergang:** ab [00:06] wortgleich mit K11-B1 ab [00:04].

### K11-256 – Verlierer – 1 Ad(s), max. 4 Tage

- **Ad-IDs:** 92876650
- **share_url (Rep. 92876650):** https://app.gethookd.ai/share/ad/92876650?signature=a182dc7da165f5cb9fe83eec53ad8921c5cc4c5c76e92895b581c769cfae3e5c
- **Länge:** 319 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „NACKENSCHMERZEN DIE TROTZ BEHANDLUNGEN NICHT VERSCHWINDEN“ — Bild: Frau am Laptop hält Nacken, Kreis-Einblendung Entzündung
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 92876650 / Medium 304565251
- **Body-Variante:** K11-B1 (Wortübereinstimmung 91 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Nackenschmerzen, die trotz Behandlungen nicht verschwinden, sind keine Verspannung, sondern
[00:04] ein Schlafpositionsproblem.
[00:06] Und viele Betroffene versuchen dann, die Beschwerden mit Schmerzmittel zu betäuben.
[00:09] Aber diese beheben nicht die Ursache, sie überdecken nur die Schmerzen im Nacken.
[00:13] Oder sie probieren Physiotherapie und Dehnübungen aus.
[00:16] Aber das ist nicht nur zeitaufwendig, sondern es bringt oft nur kurzzeitige Linderung.
[00:21] Mach stattdessen das hier.
[00:22] Die traurige Wahrheit ist, die meisten Menschen achten auf ihre Haltung beim Sitzen, vermeiden
```
- **Übergang:** ab [00:22] wortgleich mit K11-B1 ab [00:43].

### K15-284 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 184804208
- **share_url (Rep. 184804208):** https://app.gethookd.ai/share/ad/184804208?signature=7d33e0dc073a963320e547b052d17f23860b2c558e0e3b2648c57f0081fa2eae
- **Länge:** 422 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „MITTEN IN“ — Bild: 3D-Animation (Pixar-Stil): Frau präsentiert im Meeting vor Kollegen
- **Transkript-Quelle:** lokal, faster-whisper „small“ (Volltranskript) · Ad 184804208 / Medium 491328737
- **Volltranskript:** = Referenz der Body-Variante **K15-B1** (oben vollständig).

### K15-285 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 184804204
- **share_url (Rep. 184804204):** https://app.gethookd.ai/share/ad/184804204?signature=5ded3bda0c932cd306c79f67efc49dc343d3c9727d553eea2b6615fcdce53d2c
- **Länge:** 423 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation: ältere Frau mit Strickjacke, verunsichert
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K15-286 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 184804201
- **share_url (Rep. 184804201):** https://app.gethookd.ai/share/ad/184804201?signature=ad17e24c5bbea8ee7e294e708fb230d6f80bf28906f416e0352d5b1f9b2131ff
- **Länge:** 436 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation: Frau im Krankenhausflur mit Befund in der Hand
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K15-287 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 184804209
- **share_url (Rep. 184804209):** https://app.gethookd.ai/share/ad/184804209?signature=9552176a2d7a2f59583209fbeb7af7bf38f55e8c5095ba70940a4b865e67a23c
- **Länge:** 427 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation: Frau im Klinikflur (Neurologie) mit Befund
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K15-288 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 184804212
- **share_url (Rep. 184804212):** https://app.gethookd.ai/share/ad/184804212?signature=dd471a562f4b4be60558dc9a3c35ebe67fdfce2a1039912db63f5a62500f87ee
- **Länge:** 423 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation: Frau vor MRT-Bildern im Arztzimmer
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K15-289 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 184804207
- **share_url (Rep. 184804207):** https://app.gethookd.ai/share/ad/184804207?signature=ab8a28bccf8ba9128d55f22774408025662a6e8df46af9ade6e91577a63206b0
- **Länge:** 420 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation: Frau beim Abendessen mit Freunden, verwirrt
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K15-290 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 184804198
- **share_url (Rep. 184804198):** https://app.gethookd.ai/share/ad/184804198?signature=4bad4671637bfcaf76bc60c06ffcd58ebbe7733ff1f464012f4d77b6bfdac311
- **Länge:** 423 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation Split: junge Frau im Büro / ältere Frau im Sessel mit Nebel um den Kopf (Brain Fog)
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K16-291 – Kandidat – 2 Ad(s), max. 18 Tage – aktiv

- **Ad-IDs:** 180754310, 181171395
- **share_url (Rep. 181171395):** https://app.gethookd.ai/share/ad/181171395?signature=ab762f76ef1747b82a49586e253e210d67822676e368f492a4c9012b530ebabf
- **Länge:** 377 s · **Landingpage:** https://shop.pillowdaddy.de/das-nacken-therapiekissen-6-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL AUFWACHST“ — Bild: 3D-Animation (Pixar-Stil): ältere Frau sitzt im Bett, Hand an der Stirn, Wecker
- **Transkript-Quelle:** lokal, faster-whisper „small“ (Volltranskript) · Ad 181171395 / Medium 485086559
- **Volltranskript:** = Referenz der Body-Variante **K16-B1** (oben vollständig).

### K16-292 – Kandidat – 1 Ad(s), max. 18 Tage – aktiv

- **Ad-IDs:** 181171404
- **share_url (Rep. 181171404):** https://app.gethookd.ai/share/ad/181171404?signature=c72c9a0f00abafc24f4b37c51558ac315f8a89ba132773e70ddab9d48b59c2c9
- **Länge:** 380 s · **Landingpage:** https://shop.pillowdaddy.de/das-nacken-therapiekissen-6-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MEIN NEUROLOGE MEINTE, ES SEI STRESS“ — Bild: 3D-Animation: ältere Frau beim Neurologen
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K16-293 – Kandidat – 1 Ad(s), max. 18 Tage – aktiv

- **Ad-IDs:** 181171399
- **share_url (Rep. 181171399):** https://app.gethookd.ai/share/ad/181171399?signature=c13872b42f2fe04a95aefbb18125b96c20483d79fe1525075d308eb59fee37e9
- **Länge:** 370 s · **Landingpage:** https://shop.pillowdaddy.de/das-nacken-therapiekissen-6-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WARUM SCHWINDEL IMMER WIEDERKOMMT“ — Bild: 3D-Animation: ältere Frau am Tisch mit Unterlagen
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K16-294 – Verlierer – 1 Ad(s), max. 6 Tage

- **Ad-IDs:** 180754287
- **share_url (Rep. 180754287):** https://app.gethookd.ai/share/ad/180754287?signature=fd418adad6c054a8949e80dd9be81c7296b153fe760b59d4e0381ff4e1ed04ba
- **Länge:** 370 s · **Landingpage:** https://shop.pillowdaddy.de/das-nacken-therapiekissen-6-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „(erstes Bild schwarz)“ — Bild: schwarzer Startframe
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K16-295 – Verlierer – 1 Ad(s), max. 5 Tage

- **Ad-IDs:** 180754305
- **share_url (Rep. 180754305):** https://app.gethookd.ai/share/ad/180754305?signature=e31db6f238623eaa1acbf01aa573f1d5c970c29c517bb734e0ec4f6e5bcfbbd9
- **Länge:** 380 s · **Landingpage:** https://shop.pillowdaddy.de/das-nacken-therapiekissen-6-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MEIN NEUROLOGE“ — Bild: schwarzer Bildschirm mit weißem Text
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K17-296 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 184804213
- **share_url (Rep. 184804213):** https://app.gethookd.ai/share/ad/184804213?signature=05a7eb19d98fabd498b00d09faf6ca88390bc70df071f46880b135361e089e39
- **Länge:** 436 s · **Landingpage:** https://shop.pillowdaddy.de/advert-schnarchen-A391
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation: Frau im Klinikflur mit Befund, Hand am Ohr
- **Transkript-Quelle:** lokal, faster-whisper „small“ (Volltranskript) · Ad 184804213 / Medium 491328734
- **Volltranskript:** = Referenz der Body-Variante **K17-B1** (oben vollständig).

### K17-297 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 184804200
- **share_url (Rep. 184804200):** https://app.gethookd.ai/share/ad/184804200?signature=47149ae83188ba1c9fcb64e9f190c61e798b00378e841cbd98e0824a23df2468
- **Länge:** 419 s · **Landingpage:** https://shop.pillowdaddy.de/advert-schnarchen-A391
- **Eingeblendeter Hook-Text (Startframe):** „UM 2 UHR“ — Bild: 3D-Animation: ältere Frau nachts im Bett greift sich an die Brust, Wecker 2:00 AM
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K17-298 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 184804206
- **share_url (Rep. 184804206):** https://app.gethookd.ai/share/ad/184804206?signature=4a61cbb11cf7e8bb185088534196c41032335667139ccded0f1ad43d6b52ad9e
- **Länge:** 422 s · **Landingpage:** https://shop.pillowdaddy.de/advert-schnarchen-A391
- **Eingeblendeter Hook-Text (Startframe):** „MITTEN IN“ — Bild: 3D-Animation: Frau präsentiert im Meeting
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K17-299 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 184804205
- **share_url (Rep. 184804205):** https://app.gethookd.ai/share/ad/184804205?signature=cbb0753461a03c9b103f3015a253efb67e2dd1863c88dd120fbbd2af021402aa
- **Länge:** 423 s · **Landingpage:** https://shop.pillowdaddy.de/advert-schnarchen-A391
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation Split: Frau im Büro / ältere Frau mit Nebel um den Kopf
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K17-300 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 184804214
- **share_url (Rep. 184804214):** https://app.gethookd.ai/share/ad/184804214?signature=3604a1e93bc0b61b8b119aa8256ef6c077f8267bcb581b5d185a871d6f996d10
- **Länge:** 427 s · **Landingpage:** https://shop.pillowdaddy.de/advert-schnarchen-A391
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation: Frau im Klinikflur mit Befund
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K17-301 – Verlierer – 1 Ad(s), max. 1 Tage

- **Ad-IDs:** 184804210
- **share_url (Rep. 184804210):** https://app.gethookd.ai/share/ad/184804210?signature=1f44ea405906b630c6f7ecc130ebf25f14f6f31ef59416065e3aa28a29b25e33
- **Länge:** 423 s · **Landingpage:** https://shop.pillowdaddy.de/advert-schnarchen-A391
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation: Frau vor MRT-Bildern im Arztzimmer
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K18-302 – Test – 1 Ad(s), max. 4 Tage – aktiv

- **Ad-IDs:** 198476496
- **share_url (Rep. 198476496):** https://app.gethookd.ai/share/ad/198476496?signature=4702e084fbbc1c2d02748dc5a56b96b98d11d0ea230da75a124e49defe04acb9
- **Länge:** 372 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „14 JAHRE LANG HABEN MIR ÄRZTE GESAGT, ICH HÄTTE EINE ANGSTSTÖRUNG“ — Bild: 3D-Animation: Frau mit Brille beim Arzt
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K18-303 – Test – 1 Ad(s), max. 4 Tage – aktiv

- **Ad-IDs:** 198476188
- **share_url (Rep. 198476188):** https://app.gethookd.ai/share/ad/198476188?signature=ab8d6534311d94c74882c45c6bf2412937d25eda46348bf292b473054503270d
- **Länge:** 372 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „DURCH DEINEN NACKEN LAUFEN NERVEN“ — Bild: 3D-Animation: Frau am Schreibtisch, Hologramm Gehirn+Wirbelsäule
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K18-304 – Test – 1 Ad(s), max. 4 Tage – aktiv

- **Ad-IDs:** 198475399
- **share_url (Rep. 198475399):** https://app.gethookd.ai/share/ad/198475399?signature=c1b988b6da9541fd44dc2667f0cbec1364301d59f55b6d3273ee34b622beb666
- **Länge:** 377 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MIT 34 BEKAM ICH DIE DIAGNOSE: ANGSTSTÖRUNG“ — Bild: 3D-Animation: Frau im Supermarkt mit Herzrasen (glühendes Herz)
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K18-305 – Test – 1 Ad(s), max. 4 Tage – aktiv

- **Ad-IDs:** 198476640
- **share_url (Rep. 198476640):** https://app.gethookd.ai/share/ad/198476640?signature=a953689e992daa2ddfb760d2422af4ff51d5808fecbd5b733eef7f0c11662eac
- **Länge:** 373 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „(kein Text im Startframe)“ — Bild: 3D-Animation: Frau mit Einkaufswagen im Supermarkt, panisch
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K18-306 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 198476799
- **share_url (Rep. 198476799):** https://app.gethookd.ai/share/ad/198476799?signature=fc2d0709086f24cb4acf2a134a16e91d9f84b4bdd656deb8c35fefb277e569b6
- **Länge:** 372 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MRT: NORMAL / BLUTBILD: NORMAL / EKG: NORMAL“ — Bild: 3D-Animation Collage: MRT, Blutabnahme, EKG
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K22-322 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 91377966
- **share_url (Rep. 91377966):** https://app.gethookd.ai/share/ad/91377966?signature=a680de7ec44af071f84a780a9cb04871f923563a650c8c3ca21aada76f51df7d
- **Länge:** 372 s · **Landingpage:** https://shop.pillowdaddy.de/advert-4-das-nacken-therapiekissen-headache
- **Eingeblendeter Hook-Text (Startframe):** „WARUM SEITENSCHLÄFER MIT MIGRÄNE“ — Bild: 3D-Animation: Mann schläft in Seitenlage, glühender Nacken
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 91377966 / Medium 299814732
- **Volltranskript:** = Referenz der Body-Variante **K22-B1** (oben vollständig).

### K22-323 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 91377963
- **share_url (Rep. 91377963):** https://app.gethookd.ai/share/ad/91377963?signature=69ad4d811f542ae5cef961d0051e4731e572c2d3213f2da8c8754718db15389d
- **Länge:** 371 s · **Landingpage:** https://shop.pillowdaddy.de/advert-4-das-nacken-therapiekissen-headache
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Muskel-Overlay Rücken/Nacken, Kreis-Einblendung Gehirn
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 91377963 / Medium 299814726
- **Body-Variante:** K22-B1 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist die schlechteste Schlafposition bei Migräne und wie du stattdessen schlafen solltest.
[00:04] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule.
```
- **Übergang:** ab [00:04] wortgleich mit K22-B1 ab [00:05].

### K22-324 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 91377961
- **share_url (Rep. 91377961):** https://app.gethookd.ai/share/ad/91377961?signature=167c8bde6bf7d204f3bee1427557382d769fee9410e2ade9b492092a2586dcc2
- **Länge:** 372 s · **Landingpage:** https://shop.pillowdaddy.de/advert-4-das-nacken-therapiekissen-headache
- **Eingeblendeter Hook-Text (Startframe):** „SEITENSCHLÄFER: DU KLEMMST DEINEN TRIGEMINUSNERV EIN“ — Bild: Therapeut an Person mit Muskel-Overlay in Seitenlage
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 91377961 / Medium 299814719
- **Body-Variante:** K22-B1 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Seitenschläfer. Du klemmst deinen Trigeminusnerv ein, während du schläfst und genau das führt zu deinen Migräneattacken.
[00:06] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule.
```
- **Übergang:** ab [00:06] wortgleich mit K22-B1 ab [00:05].

### K22-325 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 91377965
- **share_url (Rep. 91377965):** https://app.gethookd.ai/share/ad/91377965?signature=4ad195f3ec65f14d9461f17837db9b620b1e7f30161a821980e946c0a96c497e
- **Länge:** 372 s · **Landingpage:** https://shop.pillowdaddy.de/advert-4-das-nacken-therapiekissen-headache
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DER GRUND WARUM SEITENSCHLÄFER UNTER MIGRÄNE“ — Bild: Therapeut an Frau mit Muskel-Overlay in Seitenlage
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 91377965 / Medium 299814724
- **Body-Variante:** K22-B1 (Wortübereinstimmung 96 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Das ist der Grund, warum Seitenschläfer unter Migräne oder starken Kopfschmerzen leiden
[00:04] und was du dagegen tun kannst.
[00:05] Wenn du so schläfst, arbeitest du gegen die natürliche Krümmung deiner Halswirbelsäule.
```
- **Übergang:** ab [00:05] wortgleich mit K22-B1 ab [00:05].

### K23-326 – Verlierer – 1 Ad(s), max. 7 Tage

- **Ad-IDs:** 89547484
- **share_url (Rep. 89547484):** https://app.gethookd.ai/share/ad/89547484?signature=61bc0c0a30ef5b93bab7fc624404a4bf9b7d409fce74872b931362d2c976da44
- **Länge:** 106 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „warum du“ — Bild: 3D-Animation: Mann im Bett mit Nackenschmerz, gelbe Kissen-Figur (Comic)
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 89547484 / Medium 294257385
- **Volltranskript:** = Referenz der Body-Variante **K23-B1** (oben vollständig).

### K23-327 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 90347400
- **share_url (Rep. 90347400):** https://app.gethookd.ai/share/ad/90347400?signature=db388ed6ceb597aeeb957f2c1e57a21bcb9212297aedd2cdff652b837904a414
- **Länge:** 110 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „Wenn du“ — Bild: 3D-Animation: älterer Mann im Bett, glühender Nacken
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 90347400 / Medium 296611437
- **Volltranskript:** = Referenz der Body-Variante **K23-B2** (oben vollständig).

### K23-328 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 90347404
- **share_url (Rep. 90347404):** https://app.gethookd.ai/share/ad/90347404?signature=1b7824dfb77aec9bdb79a31590d23c547c5790dd3934100e98ce3d69fd8e25a2
- **Länge:** 103 s · **Landingpage:** https://shop.pillowdaddy.de/advert-2-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „Das hier“ — Bild: 3D-Animation: Mann schläft auf dem Bauch/Seite, Untertitel
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 90347404 / Medium 296611440
- **Body-Variante:** K23-B2 (Wortübereinstimmung 99 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
(kein eigener Vorspann – startet direkt wortgleich)
```
- **Übergang:** ab [00:00] wortgleich mit K23-B2 ab [00:07].

### K24-329 – Kandidat – 1 Ad(s), max. 18 Tage – aktiv

- **Ad-IDs:** 181171358
- **share_url (Rep. 181171358):** https://app.gethookd.ai/share/ad/181171358?signature=f0b874ca1b3d859da2e4d12b33057e24942adfaee672070dd7623b5c5e05c8a4
- **Länge:** 380 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „MEIN NEUROLOGE MEINTE, ES SEI STRESS“ — Bild: 3D-Animation: ältere Frau beim Neurologen
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K24-330 – Kandidat – 1 Ad(s), max. 18 Tage – aktiv

- **Ad-IDs:** 181171371
- **share_url (Rep. 181171371):** https://app.gethookd.ai/share/ad/181171371?signature=bd66b402a71b2f1a839a794c69a35c0c92812801851c956728acc849e01827d6
- **Länge:** 370 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WARUM SCHWINDEL IMMER WIEDERKOMMT“ — Bild: 3D-Animation: ältere Frau am Tisch mit Unterlagen
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K24-331 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 181171355
- **share_url (Rep. 181171355):** https://app.gethookd.ai/share/ad/181171355?signature=d1fc744149c2e7b56f4aca2f2247ed7aba99bb830be391a30081433e437fba33
- **Länge:** 377 s · **Landingpage:** https://shop.pillowdaddy.de/advert-6-das-nacken-therapiekissen-schwindel
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU MORGENS MIT SCHWINDEL AUFWACHST“ — Bild: 3D-Animation: ältere Frau im Bett, Wecker
- **Transkript:** nicht verfügbar – GetHooked-Transkription noch „processing“, lokale Transkription nicht abgeschlossen (Lücke).

### K25-332 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 110088145
- **share_url (Rep. 110088145):** https://app.gethookd.ai/share/ad/110088145?signature=1ce40812a17e23a01c84ae871652249a4d9bb6903008591ffb02e18ba312b7f3
- **Länge:** 399 s · **Landingpage:** https://shop.pillowdaddy.de/advert-3-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „DAS IST DIE SCHLECHTESTE SCHLAFPOSITION“ — Bild: Röntgen-/Glüh-Skelett in Seitenlage
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 110088145 / Medium 359778277
- **Volltranskript:** = Referenz der Body-Variante **K25-B1** (oben vollständig).

### K25-333 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 110088138
- **share_url (Rep. 110088138):** https://app.gethookd.ai/share/ad/110088138?signature=bba8ec763dcd7d68c3f43d004ead5d566e2d3f45cdccd7c4fb2f6bc88cfbdc46
- **Länge:** 398 s · **Landingpage:** https://shop.pillowdaddy.de/advert-3-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „WENN DU SO SCHLÄFST,“ — Bild: Röntgen-Glüh-Skelett auf Kissen
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 110088138 / Medium 359778268
- **Body-Variante:** K25-B1 (Wortübereinstimmung 97 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Wenn du so schläfst, zerstörst du langsam deine Halswirbelsäule, besonders C5 und C6.
[00:05] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Halswirbelsäule
```
- **Übergang:** ab [00:05] wortgleich mit K25-B1 ab [00:06].

### K25-334 – Verlierer – 1 Ad(s), max. 2 Tage

- **Ad-IDs:** 110088153
- **share_url (Rep. 110088153):** https://app.gethookd.ai/share/ad/110088153?signature=8845905ac187c5717a7ed6c9e460b87279c07fcd2960c055b85aee7ba1c4dda4
- **Länge:** 398 s · **Landingpage:** https://shop.pillowdaddy.de/advert-3-das-nacken-therapiekissen-1
- **Eingeblendeter Hook-Text (Startframe):** „TAUBHEITSGEFÜHLE IN DEN HÄNDEN“ — Bild: Frau im Bett mit kribbelnder/glühender Hand
- **Transkript-Quelle:** GetHooked (Whisper, get_transcription_status) · Ad 110088153 / Medium 359778305
- **Body-Variante:** K25-B1 (Wortübereinstimmung 98 %)
- **Hook-/Abweichungsteil wörtlich ([00:00] bis Übergang):**

```text
[00:00] Taubheitsgefühle in den Händen kommen nicht von einer schlechten Durchblutung, sondern
[00:03] von einem eingeklemmten Nerv im Nacken.
[00:05] Wenn du so schläfst, arbeitest du gegen die natürliche Ausrichtung deiner Halswirbelsäule
```
- **Übergang:** ab [00:05] wortgleich mit K25-B1 ab [00:06].

### K27-336 – Verlierer – 1 Ad(s), max. 3 Tage

- **Ad-IDs:** 96006707
- **share_url (Rep. 96006707):** https://app.gethookd.ai/share/ad/96006707?signature=121af1e3ace3c62da09c58ea9af0ee93a5a54481e4fd812a791d9b72f73892c6
- **Länge:** 496 s · **Landingpage:** https://shop.pillowdaddy.de/advert-1-schnarchen-das-nacken-therapiekissen
- **Eingeblendeter Hook-Text (Startframe):** „MEINE FRAU WOLLTE SICH WEGEN MEINES SCHNARCHENS VON MIR SCHEIDEN LASSEN. KLINGT EIGENTLICH LÄCHERLICH, ODER? ABER NACH SIEBEN JAHREN HÖLLE STREIT UM 2 UHR NACHTS, GETRENNTE SCHLAFZIMMER UND DIE ENTDECKUNG, DASS SIE HEIMLICH BEI IMMOSCOUT24 NACH WOHNUNGEN IN HAMBURG SUCHTE“ — Bild: älterer Mann mit Brille, dunkles Selfie-Video (Ich-Story), langer Text-Overlay
- **Transkript:** **kein gesprochener Text.** GetHooked lieferte nur „of a“, lokale Volltranskription (faster-whisper) nur „Musik“. Das Video (496 s) ist ein **Laufschrift-Video**: weißer Versaltext scrollt über ein abgedunkeltes Standbild (Mann mit dem Kissen im Arm), dazu Musik. Der eingeblendete Text ist wortgleich der Primärtext von §K27 (Frames 0–66 s geprüft: „MEINE FRAU WOLLTE SICH WEGEN MEINES SCHNARCHENS VON MIR SCHEIDEN LASSEN. KLINGT EIGENTLICH LÄCHERLICH, ODER? ABER NACH SIEBEN JAHREN HÖLLE STREIT UM 2 UHR NACHTS, GETRENNTE SCHLAFZIMMER UND DIE ENTDECKUNG, DASS SIE HEIMLICH BEI IMMOSCOUT24 NACH WOHNUNGEN IN HAMBURG SUCHTE WURDE MIR KLAR, DASS ES IHR VERDAMMTER ERNST WAR. …“) – vollständiger Text siehe copy-Datei §K27.
