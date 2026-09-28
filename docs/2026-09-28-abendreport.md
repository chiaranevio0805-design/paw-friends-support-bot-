# Paw Friends — Abend-Report 28.09.2026

**Stand:** 28.09.2026, 19:15 UTC · **Branch:** `claude/paw-friends-support-bot-fa27s0`
**Quelle:** `docs/2026-09-28-backlog-triage.md` (Läufe 00:20 – 18:20 UTC)

---

## 1. Überblick

### Anzahl nach Kategorie (28.09.)

| Kategorie | Anzahl |
|---|---|
| `Bot/Escalated - Owner Attention` | **7** |
| `Bot/Needs Approval` | **2** |
| `Bot/Draft Ready` | 0 |
| `Bot/No Action` | 0 |
| **Kundenvorgänge gesamt** | **9** |

**Der schwerste Tag bisher — und zwei der drei wichtigsten Befunde betreffen
nicht einzelne Kunden, sondern uns.**

### Was Kunden gefragt haben, nach Thema

| Thema | Anzahl | Wer |
|---|---|---|
| **Die Werbung bzw. eine Haltbarkeitszusage wird bestritten** | **4** | #7373, #7479, #7168, #7831 |
| **Antwort auf ein Prozentangebot (abgelehnt oder Gegenvorschlag)** | **2** | #7479 (3. Ablehnung), #6254 (40 % oder Rückgabe) |
| **Versiegelte, ungeöffnete Ware — wie zurückgeben?** | **3** | #7479, #6254, #8142 |
| **Keine konkrete Forderung gestellt** | **3** | `hud@…`, #7626, #7373 |
| **Öffentliche oder externe Schritte angekündigt** | **3** | #7831 (Facebook + BBB), #8142 (Bewertung + Chargeback), #7479 (mehrere Behörden) |
| **Adressänderung** | **1** | `betsey.barton@…` |

**Die Zahl der unabhängigen Kundenaussagen zur Werbung steht bei
zweiundsiebzig** (71 → 72; **#7373** ist neu, alle anderen wurden früher
gezählt und nicht doppelt gezählt).

### Wie geantwortet wurde, pro Thema

**Werbung (4):** In allen vier Entwürfen **nur der überprüfbare eigene
Produkttext**, ohne Auslegung. **Nicht behauptet, eine zitierte Aussage
existiere nicht** — nur, was in den zwölf Produkttexten steht und was nicht.
**Keine Anzeige rekonstruiert.** **Keine Aussage darüber, ob die Werbung
irreführend war — in keine Richtung.**

**Prozentangebote (2):** **#7479 bekommt kein viertes Angebot** — seine
Ablehnung geht unverändert weiter. **#6254s Gegenvorschlag (40 % oder
Rückgabe) geht wörtlich weiter**; **keine eigene Zahl ins Spiel gebracht.**

**Versiegelte Ware (3):** Immer dieselbe ehrliche Antwort zuerst: **es gibt
keine Rücksendeadresse**, mit Warnung, kein Porto auszugeben. **Bei #8142
zusätzlich die offene Anerkennung, dass ihre Frage dreimal übergangen wurde.**

**Keine Forderung (3):** **Neutrales Angebot statt Deutung.** **Keine
Nachricht wurde in eine Erstattungsforderung umgedeutet.**

**Angekündigte externe Schritte (3):** **An keinen einzigen wurde etwas
geknüpft.** Nicht um Aufschub, Rücknahme oder Verzicht gebeten. Zu #7831
ausdrücklich: *„You do not owe us silence in exchange for an answer."*

**Adressänderung (1):** **In Shopify wurde nichts verändert.** **Weder
behauptet, es sei zu spät, noch, es sei noch möglich.**

### 🟥 Die drei Befunde des Tages

**A. Die Shopify-Verbindung zeigt seit heute früh auf einen anderen Shop.**
`shop.name` ist **„Paw-Besties.com"**, `ordersCount` **0**, die Produkte sind
Kinderkissen. **Zwischen 03:20 und 06:20 UTC gewechselt.** **Es fehlen keine
Bestellungen** — meine Einordnung von 07:20 („#7626 nicht abrufbar, im Admin
prüfen") war deshalb **falsch und ist berichtigt.** **`switch-shop` wurde
NICHT aufgerufen**: es entzieht den Token und verlangt eine interaktive
Neu-Autorisierung, die in dieser Sitzung nicht möglich ist. **Du musst die
Verbindung wiederherstellen.** **Seit 06:20 enthält kein Entwurf mehr Angaben
aus dem Bestelldatensatz.**

**B. Ein zweiter Serienversand — und beide Zahlen waren viel zu niedrig.**
Ich habe seit dem 24.09. behauptet, der Postausgang sei nur teilweise
sichtbar und die Zahl „von hier aus nicht feststellbar". **Das stimmt nur für
`in:inbox`-Suchen, die ich benutzt hatte. `in:sent` liefert ihn vollständig.**

| Datum | Zeitraum | **Gesendet** | Was ich gemeldet hatte |
|---|---|---|---|
| **24.09.** | 12:18:01 – 12:39:49 | **37** | „mindestens fünfzehn" |
| **28.09.** | 11:08:21 – 11:26:59 | **32** | „mindestens fünf" |

**Von den 32 Empfängern heute haben nur sechs geantwortet.** **Was die
übrigen sechsundzwanzig bekommen haben, ist durch keine Antwort geprüft.**
**#8605 — eines der drei offenen Stornofenster — war darunter.**

**C. Die Kauschaden-Vorlage trifft wiederholt versiegelte Ware.** **#8142 hat
dreimal nach dem ungeöffneten Artikel gefragt und dreimal eine Antwort über
den zerkauten bekommen.** **#7479 hatte am 16.09. dasselbe gefragt und bekam
heute stattdessen ein drittes Prozentangebot.**

---

## 2. 📤 HEUTE ZU SENDEN

**Neun Entwürfe, alle von heute.** **Die vier Entwürfe aus dem gestrigen
Abendreport** (#8431, #8568, #4055, #7898) **sind unverändert offen und
stehen dort im Volltext** — `docs/2026-09-27-abendreport.md`. **Achtung: der
dortige #8568-Entwurf ist inzwischen ersetzt** (siehe unten).

**⚠️ Alle liegen ausschließlich als Text in diesem Repo. Keiner ist ein
Gmail-Entwurf.**

**⚠️ VIER Entwürfe in der Datei sind als ERSETZT gekennzeichnet und dürfen
nicht zusätzlich gesendet werden:** **#8577** (25.09.), **#7898** (21.09.),
**#8568** (27.09. 03:20), **#7831** (23.09.).

**⚠️ Kein Entwurf unten enthält Angaben aus dem Bestelldatensatz** — er ist
seit heute früh nicht abrufbar, und es wird nichts behauptet, was nicht
geprüft werden konnte.

---

## #? — `hud@hildebrandt.com.au` — **AU**, Erstkontakt, **keine Bestellung auffindbar**, keine Forderung gestellt

**Betreff:** `Re: your message of 28 September`

> Hello,
>
> Thank you for writing, and for setting out plainly what happened. **You have
> asked us to work out where we go from here rather than telling us what you
> want, so I am not going to decide that on your behalf.** If you would like a
> refund, a replacement, or simply for this to be on record, say which and it
> goes on exactly as you put it.
>
> **First, something awkward that I would rather tell you than hide.** **I
> cannot find an order under the address you have written from.** **I am not
> suggesting you did not order** — **there is a second address customers write
> to, `paw-friends.uk@paw-friends.uk`, which I cannot see from this desk, and
> orders are often placed under a different email than the one people write
> from.** **If you send me the order number, or the name and address the order
> was placed under, I can look properly.** Until then I genuinely do not have
> your order in front of me, and I am not going to guess at it.
>
> **What I can tell you without it:**
>
> - **I cannot approve a refund or a replacement from this desk, and I am not
>   going to refuse you one either.** That decision belongs to the shop owner,
>   and your message goes to him today in your own words.
> - **I am not going to promise you an answer or a date, because I do not
>   control either.**
> - **There is no returns process and no returns address.** We do not have one
>   to give you. **So please do not post anything back from Australia** — the
>   postage would be significant and you would lose the items on top of it.
>   **That is not a refusal of anything; it is simply where things stand.**
> - **Our published refund policy has a section headed "Australia — Consumer
>   Guarantees."** **I am not a lawyer, I am not going to tell you what it
>   means for your case, and I am not going to use it to promise you
>   anything** — but you are in Australia and you are entitled to know it is
>   there and to read it yourself.
>
> **You attached photographs. I have not opened them, and I am not asking you
> for any.** **Nothing here is conditional on you proving what happened.**
>
> **I am not going to make a claim about the toys in either direction** — not
> to defend them and not to agree with you about them. **You described what
> happened and it is recorded exactly as you wrote it.** **I am also drawing
> no conclusion from your dog.**
>
> **You mention a fourth item you have not given him.** **That is noted as you
> wrote it, and I am not going to tell you what to do with it in either
> direction** — not to try it, and not to keep it back.
>
> Send me the order number when you can, and I will chase this properly.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Auskunft, dass unter seiner Adresse keine
Bestellung gefunden wurde — ausdrücklich ohne zu unterstellen, er habe nicht
bestellt**, mit Hinweis auf die zweite Shop-Adresse; die **klare Auskunft,
dass es keine Rücksendeadresse gibt**, mit Warnung vor einer Sendung aus
Australien; und der **bloße Hinweis auf den eigenen AU-Abschnitt der Refund
Policy, ausdrücklich ohne Auslegung und ohne daraus etwas abzuleiten.**
**Keine Erstattung zugesagt, kein Ersatz, kein Betrag, kein Termin — und keine
Absage.** **Keine Bestelldaten genannt** — es gibt keine. **Keine Deutung
seiner Nachricht als Erstattungsforderung.** **Keine Kauschaden-Vorlage, kein
Prozentangebot.** **Keine Aussage zur Haltbarkeit oder Qualität, in keine
Richtung.** **Nichts aus dem Hund gefolgert.** **Kein Foto verlangt**, die
beigefügten **nicht geöffnet**. **Keine Anweisung zum vierten, nicht
ausgegebenen Artikel.** **Kein geratener Name** — er unterschreibt nicht.
Kein Eskalationsmarker im Text.

---

## #7626 — `tonisfurryfriends@yahoo.com` — Erstkontakt, **keine Forderung gestellt** · **Bestellung von hier aus nicht abrufbar**

**Betreff:** `Re: A shipment from order #7626 is on the way`

> Hello,
>
> Thank you for writing, and I am sorry — that is not what you paid for.
>
> **You have told us what happened and you have not asked us for anything, so
> I am not going to decide on your behalf what you wanted.** **If you would
> like this passed on as a refund request, one line back here is enough. If
> you would rather it simply be recorded, that is what it stays.** **Either
> way it is with the shop owner today, in your own words.**
>
> **What I should be straight about:** I cannot approve a refund or a
> replacement from this desk, **and I am not going to refuse you one either.**
> That decision is his. **I am also not going to promise you an answer or a
> date, because I do not control either.**
>
> **One thing in case it is on your mind: there is no returns address.** **We
> do not have one to give you, so please do not post anything back** — it
> would cost you the postage for nothing. **That is not a refusal of anything;
> it is simply where things stand.**
>
> **I am not going to make a claim about the toys in either direction** — not
> to defend them and not to argue with you about them. **You described what
> happened and it is recorded exactly as you wrote it.** **I am drawing no
> conclusion from your dogs.**
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** das **neutrale Angebot statt einer Deutung** — sie fordert
nichts —, und die **klare Auskunft, dass es keine Rücksendeadresse gibt**, mit
Warnung vor einer Sendung. **Keine Erstattung zugesagt, kein Ersatz, kein
Betrag, kein Termin — und keine Absage.** **⚠️ Ausdrücklich KEINE Angaben aus
dem Bestelldatensatz** — die Bestellung ist von hier aus nicht abrufbar, und
es wird nichts behauptet, was nicht überprüft werden konnte, **auch nicht,
dass nichts erstattet sei.** **Nicht gesagt, ihre Bestellung sei nicht
auffindbar** — sie hat ihre eigene Versandbestätigung zitiert, und das wird
nicht gegen sie verwendet. **Keine Kauschaden-Vorlage, kein Prozentangebot.**
**Keine Aussage zur Haltbarkeit oder Qualität, in keine Richtung** — auch
nicht zustimmend. **Nichts aus ihren Hunden gefolgert.** **Nichts über die
Werbung behauptet** — sie erwähnt sie nicht. **Nichts über die Garantie
behauptet** — sie ruft sie nicht an. **Kein geratener Name** — sie
unterschreibt nicht. Kein Eskalationsmarker im Text.

---

## #7373 — Dom Frisina (`isdom00@gmail.com`) — Erstkontakt, **bestreitet eine Werbeaussage** · **Bestelldatensatz nicht abrufbar**

**Betreff:** `Re: Order #7373`

> Dear Dom,
>
> Thank you for writing.
>
> **You have raised something and not told me what you want from us, so I am
> not going to decide that on your behalf.** **If you would like this passed
> on as a refund request, or as a request for a replacement, one line back
> here is enough. If you would rather it simply be recorded, that is what it
> stays.** **Either way it is with the shop owner today, in your own words.**
>
> **You say it was stated that the toy was not breakable.** **Here is what I
> can tell you that is checkable, rather than my opinion:** I have read all
> twelve of our current product descriptions. **The word "indestructible" is
> not in any of them**, and **the descriptions carry no wording about the toy
> being unbreakable.** Where a **30-day money-back guarantee** appears in our
> own marketing material, **it appears without any condition attached to it.**
>
> **I cannot see the advertisement you actually read, so I am not going to
> tell you what it said, and I am certainly not going to suggest you misread
> it or imagined it.** **What you were told, and where, goes to the owner
> exactly as you put it.**
>
> **What I cannot do:** approve a refund or a replacement from this desk.
> **I am also not going to refuse you one.** That decision is his. **I am not
> going to promise you an answer or a date, because I do not control either.**
>
> **One thing in case it is on your mind: there is no returns address.** **We
> do not have one to give you, so please do not post anything back** — it
> would cost you the postage for nothing. **That is not a refusal of
> anything.**
>
> **I am not going to make a claim about the toy in either direction** — not
> to defend it and not to agree with you about it. **You described what
> happened and it is recorded exactly as you wrote it.** **Your photographs
> are on the file and you do not need to send anything further.**
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** das **neutrale Angebot statt einer Deutung** — seine
Formulierung *„Like to ask"* wird **nicht** als Erstattungsforderung gelesen —,
die **überprüfbare Auskunft über den eigenen Produkttext**, und die **klare
Auskunft, dass es keine Rücksendeadresse gibt.** **Keine Erstattung zugesagt,
kein Ersatz, kein Betrag, kein Termin — und keine Absage.** **⚠️ Ausdrücklich
KEINE Angaben aus dem Bestelldatensatz** — er ist derzeit nicht abrufbar (siehe
Protokoll), **und es wird nichts behauptet, was nicht überprüft werden konnte,
auch nicht, dass nichts erstattet sei.** **Nicht gesagt, seine Bestellung sei
nicht auffindbar.** **Nicht behauptet, die zitierte Aussage existiere nicht** —
nur, was in den zwölf Produkttexten steht und was nicht. **Keine Rekonstruktion
der Anzeige.** **Keine Aussage zur Haltbarkeit oder Qualität, in keine
Richtung.** **Kein Foto verlangt**, die beigefügten **nicht geöffnet.**
**Keine Kauschaden-Vorlage, kein Prozentangebot.** Kein Eskalationsmarker im
Text.

---

## #7479 — Richard Bellamy (`richard@brownwolf.net`) — **lehnt 50 % ab, ruft die Garantie für den ungeöffneten Artikel an** · 28.09.

**Betreff:** `RE: FW: Refund request and business address request`

> Dear Richard,
>
> **You have declined 30 % and now 50 %, and you have said plainly what you
> want instead: the guarantee applied to the unopened item.** **I am not going
> to answer that with a third percentage.** **No further offer is being made
> here.**
>
> **Your position goes to the shop owner today, in your own words and
> unedited** — including that you consider the claim to have been made inside
> the published time limit. **He is the only person who can answer it.**
>
> **What I am not going to do, in either direction:** tell you the guarantee
> applies to your unopened item, or tell you it does not. **That is his
> decision and not mine, and I will not dress up a guess as an answer.**
> **I am also not going to comment on any of the regulatory or legal points
> you have raised — not to agree with them and not to dispute them.** **They
> go forward exactly as you wrote them.**
>
> **On the address you asked for:** **our published Terms of Service do
> contain a trading address**, and that is the address we publish. **Beyond
> what is published there I am not going to confirm or deny anything about
> registrations, ownership or individuals** — not because of anything you have
> said, but because it is not mine to disclose.
>
> **One practical point I have to be honest about: there is no returns
> process and no returns address I can give you.** **So please do not post
> the unopened item back yet** — until someone gives you an address in
> writing you would simply lose it and the postage. **That is not a refusal
> of your claim.** **You asked on 15 September how to return it and you were
> entitled to that answer then.**
>
> **Nothing here depends on what you do or do not do with the complaints you
> have described.** **I am not asking you to pause anything, withdraw
> anything, or wait.**
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **ausdrückliche Feststellung, dass kein drittes
Prozentangebot gemacht wird**, die unveränderte Weitergabe seiner Position,
die **ehrliche Auskunft, dass es keinen Rückgabeweg gibt**, und der Hinweis
auf die **in den eigenen Terms of Service veröffentlichte Handelsadresse.**
**Keine Erstattung zugesagt, kein Betrag, kein Termin — und keine Absage.**
**Nicht behauptet, die Garantie greife für den ungeöffneten Artikel, und
nicht behauptet, sie greife nicht.** **Keine rechtliche Bewertung, in keine
Richtung** — weder zu Fernabsatz, Werbung, Marken, Patenten noch Betrug.
**Nichts über Registrierungen, Inhaberschaft oder Personen bestätigt oder
bestritten, über das Veröffentlichte hinaus** — und ausdrücklich gesagt,
warum nicht. **Kein Versuch, ihn von Behörden, Bank, Shopify oder Ombudsstelle
abzubringen**, nichts daran geknüpft. **Keine Rücksendeadresse erfunden.**
**Kein Foto verlangt.** **Keine Angaben aus dem Bestelldatensatz** — er ist
derzeit nicht abrufbar. Kein Eskalationsmarker im Text.

---

---

## #6254 — David Hickman (`davehickman71@gmail.com`) — **antwortet auf 30 % mit einem Gegenvorschlag** · 28.09.

**Betreff:** `Re: A shipment from order #6254 is on the way`

> Dear Dave,
>
> Thank you for coming back so clearly.
>
> **You have made a specific counter-proposal — 40 % on the total order, or
> returning the items instead — and that goes to the shop owner today in
> exactly those words.** **I am not going to name a different figure, and I am
> not going to talk you up or down from yours.**
>
> **I cannot approve either option from this desk, and I am not going to
> refuse you either.** That decision is his. **I am not going to promise you
> an answer or a date, because I do not control either.**
>
> **There is one thing I have to be straight about, because it affects the
> second half of your proposal: there is no returns process and no returns
> address I can give you.** **So please do not post the two unopened items
> back yet** — until someone sends you an address in writing you would lose
> them and the postage. **That is not a refusal; it is simply where things
> stand, and you asked for that address on 16 September.**
>
> **Your reason for not wanting to keep the two unopened toys is recorded as
> you put it, and I am not going to argue with it or agree with it.** **I am
> not going to tell you what to do with them in either direction.**
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **unveränderte Weitergabe seines Gegenvorschlags
(40 % oder Rückgabe)**, und die **ehrliche Auskunft, dass es keinen
Rückgabeweg gibt** — die zweite Hälfte seines Vorschlags ist von hier aus
nicht durchführbar. **Keine Erstattung zugesagt, kein Betrag genannt, kein
Termin, keine Absage.** **Keine eigene Zahl ins Spiel gebracht** und **nicht
versucht, ihn von seiner Zahl wegzubewegen.** **Keine Aussage zur Haltbarkeit
oder Qualität, in keine Richtung.** **Nichts aus seinen Hunden gefolgert**,
und seine Begründung nicht gegen ihn verwendet. **Keine Anweisung zu den zwei
ungeöffneten Artikeln.** **Keine Rücksendeadresse erfunden.** **Keine Angaben
aus dem Bestelldatensatz** — er ist derzeit nicht abrufbar. Kein
Eskalationsmarker im Text.

---

---

## #7168 — Phil & Sarah Hockley (`philnsarahhockley@gmail.com`) — **verlangt ausdrücklich Eskalation, wirft Irreführung vor** · 28.09.

**Betreff:** `Re: Order #7168 confirmed`

> Hello,
>
> **You asked for this to be escalated. It has been, today, and I would
> rather tell you exactly what that means than leave it as a word.**
>
> **Your message goes to the shop owner in full and unedited — including your
> statement that the advertising was misleading.** **I am not softening it,
> not summarising it, and not putting my own gloss on it.** **He is the only
> person who can answer it.**
>
> **What I am not going to do is tell you whether the advertising was
> misleading or whether it was not.** **That is not mine to rule on, and you
> would be right not to trust me if I did.** **What I can tell you is what is
> checkable:** I have read all twelve of our current product descriptions.
> **The word "indestructible" is not in any of them.** Where a **30-day
> money-back guarantee** appears in our own marketing material, **it appears
> without any condition attached to it.** **I cannot see the advertisement you
> actually saw, so I am not going to tell you what it said, and I am certainly
> not going to suggest you misread it.**
>
> **I cannot approve a refund or a replacement from this desk, and I am not
> going to refuse you one either.** **I am not going to promise you an answer
> or a date, because I do not control either.**
>
> **And nothing here depends on what you do next** — whether you take this
> further, write a review, or leave it. **I am not asking you to hold off on
> anything.**
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **Bestätigung, dass der Vorgang eskaliert ist**, und
die unveränderte Weitergabe des Vorwurfs. **Keine Erstattung zugesagt, kein
Ersatz, kein Betrag, kein Termin — und keine Absage.** **Nicht behauptet, die
Werbung sei irreführend gewesen, und nicht behauptet, sie sei es nicht** —
ausdrücklich als nicht von hier entscheidbar benannt. **Nur der überprüfbare
Produkttext-Befund.** **Keine Rekonstruktion der Anzeige.** **Nichts an eine
mögliche Bewertung oder weitere Schritte geknüpft.** **Kein Prozentangebot,
keine Kauschaden-Vorlage.** **Kein geratener Vorname** — die Adresse nennt
zwei Personen und die Nachricht ist nicht unterschrieben. **Keine Angaben aus
dem Bestelldatensatz** — er ist derzeit nicht abrufbar. Kein
Eskalationsmarker im Text.

---

## #8142 — Wendy Price (`wendyprice579@gmail.com`) — **versiegelter Artikel dreimal übergangen** · 28.09.

**Betreff:** `Re: FW: Defective`

> Dear Wendy,
>
> **You have now asked the same question three times — on 24 September, and
> twice within ten minutes today — and each time you were answered about the
> chewed toy instead of the sealed one. That is our failure, and I am going
> to answer the question you actually asked.**
>
> **Where do you send the sealed one? Nowhere — because there is no returns
> address.** **We do not have one to give you.** **So please do not post it,
> and please do not go to the post office for it** — until somebody sends you
> an address in writing you would simply lose the toy and the postage on top.
>
> **That is not a refusal of your refund.** **It is the honest state of
> things, and you were entitled to hear it on 24 September, when you first
> wrote that one toy was still in its packaging — not after asking twice
> more.**
>
> **On the refund itself — for both toys, as you asked: I cannot approve it
> from this desk, and I am not going to refuse you either.** That decision
> belongs to the shop owner. **Your messages go to him today in your own
> words, and I am flagging specifically that the sealed, unopened toy has now
> been passed over three times.**
>
> **What I am not going to do is tell you the guarantee covers the chewed toy,
> or tell you it does not.** **That is his call, not mine.** **What I am also
> not going to do is send you the same policy paragraph a third time.**
>
> **On the bank chargeback and the review: both are entirely your decision.**
> **I am not going to ask you to hold off on either, I am not going to ask you
> to take anything down, and nothing here depends on what you do.**
>
> **I am not going to make a claim about the toys in either direction.** You
> described what happened and it is recorded exactly as you wrote it. **I am
> drawing no conclusion from your dog.**
>
> I am sorry you had to ask three times to get a straight answer.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **direkte Beantwortung ihrer zweimal gestellten
Frage** — es gibt keine Rücksendeadresse —, die **offene Anerkennung, dass der
versiegelte Artikel zweimal übergangen wurde**, und die Weitergabe ihrer
Forderung **für beide Artikel** unverändert. **Keine Erstattung zugesagt, kein
Betrag, kein Termin — und keine Absage.** **Nicht behauptet, die Garantie decke
den Kauschaden, und nicht behauptet, sie decke ihn nicht.** **Keine dritte
Kauschaden-Vorlage** — und ausdrücklich gesagt, dass keine kommt. **Nichts an
den angekündigten Chargeback oder die angekündigte Bewertung geknüpft**, nicht
um Aufschub oder Rücknahme gebeten. **Keine Aussage zur Haltbarkeit oder
Qualität, in keine Richtung.** **Nichts aus ihrem Hund gefolgert.** **Keine
Rücksendeadresse erfunden**, mit ausdrücklicher Warnung, keine Postgebühr
auszugeben. **Keine Angaben aus dem Bestelldatensatz** — er ist derzeit nicht
abrufbar. **Kein Prozentangebot.** Kein Eskalationsmarker im Text.

---

## #7831 — Mary Hollerich (`mhollerich89@gmail.com`) — US, **kündigt einen öffentlichen Beitrag und eine BBB-Meldung an** · **ERSETZT den Entwurf vom 23.09.**

**⚠️ Der Entwurf vom 23.09. ist überholt und darf nicht mehr gesendet
werden.** Er entstand, bevor sie am 28.09. die Kauschaden-Vorlage erhielt, und
kennt weder die fünf Tage Schweigen noch die Ankündigung.

**Betreff:** `Re: Items`

> Dear Mary,
>
> **You wrote on 23 September and heard nothing for five days. Then what you
> did get was a policy paragraph. I am not going to defend that.**
>
> **You asked for your money back for all of it. That request goes to the
> shop owner today, in your own words, unedited.** **I cannot approve it from
> this desk and I am not going to refuse you either — that decision is his,
> and I will not dress a guess up as an answer.**
>
> **You said we told you it would hold up.** **I cannot see the advertisement
> you were shown, so I am not going to tell you what it said, and I am
> certainly not going to suggest you misread it.** **What I can tell you is
> checkable:** I have read all twelve of our current product descriptions.
> **The word "indestructible" is not in any of them.** Where a **30-day
> money-back guarantee** appears in our own marketing material, **it appears
> without any condition attached to it.** **Your wording goes to him as you
> wrote it, because he is the only one who can look at the advertising
> itself.**
>
> **What I am not going to do is tell you the guarantee covers what happened,
> or tell you it does not.** **And I am not going to send you that same
> paragraph a second time.**
>
> **About posting on Facebook, and about reporting us to the Better Business
> Bureau: both are entirely your business.** **I am not going to ask you to
> reconsider either, I am not going to ask you to wait, and nothing here
> depends on whether you do them or not.** **You do not owe us silence in
> exchange for an answer.**
>
> **I am not going to make a claim about the toys in either direction** — not
> to defend them and not to agree with you about them. **You told us what
> happened and it is recorded exactly as you wrote it.** **You threw them out
> the same night; I am not going to suggest you should have kept them, and
> nothing here depends on your still having them.**
>
> I am sorry it took five days and a form letter to get to this.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Anerkennung der fünf Tage ohne Antwort und
der Vorlage**, die unveränderte Weitergabe ihrer Forderung, und die
**überprüfbare Auskunft über den eigenen Produkttext.** **Keine Erstattung
zugesagt, kein Betrag, kein Termin — und keine Absage.** **Nicht behauptet,
die Garantie decke den Kauschaden, und nicht behauptet, sie decke ihn nicht.**
**Keine zweite Kauschaden-Vorlage** — und ausdrücklich gesagt, dass keine
kommt. **Nichts an den angekündigten Facebook-Beitrag und nichts an die angekündigte BBB-Meldung geknüpft**, nicht um
Aufschub, Verzicht oder Rücknahme gebeten, und ausdrücklich gesagt, dass sie
uns kein Schweigen schuldet. **Nicht behauptet, „indestructible" existiere
nicht** — nur, was in den zwölf Texten steht. **Keine Rekonstruktion der
Anzeige.** **Ihr wird nicht vorgehalten, die Artikel weggeworfen zu haben**,
und nichts davon abhängig gemacht. **Keine Angaben aus dem Bestelldatensatz**
— er ist derzeit nicht abrufbar. **Kein Prozentangebot.** **Sie wird mit
ihrer eigenen Unterschrift „Mary" angesprochen**, die Abweichung zum
Bestellnamen nicht thematisiert. Kein Eskalationsmarker im Text.

---

## Adressänderung — `betsey.barton@yahoo.com` — **keine Bestellnummer, Datensatz nicht prüfbar**

**Betreff:** `Re: Address change`

> Hello,
>
> Thank you for writing, and I will be straight with you about what I can and
> cannot do here.
>
> **I cannot change a delivery address from this desk** — I do not have that
> access, and I am not going to tell you it is done when it is not. **What I
> have done is pass your request on to the shop owner straight away, with the
> new address exactly as you wrote it.** He can make the change in the admin
> if the order has not yet gone out.
>
> **I also cannot tell you whether it is too late.** **I am not able to check
> your order's status from here at the moment, and I would rather say that
> than guess.** **So please do not take this as confirmation that the address
> has been changed, and please do not take it as a refusal either.**
>
> **One thing that would help: your order number.** If you send it, the change
> can be matched to the right order without anyone having to search. **If you
> do not have it to hand, the name and the original delivery address will do.**
>
> **If the parcel has already gone to the old address**, tell me and I will
> pass that on too — that is a different problem and it should not be left to
> sit.
>
> I am sorry I cannot simply confirm it for you.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **ehrliche Auskunft, dass von hier aus keine Adresse
geändert werden kann**, und die sofortige Weitergabe der neuen Adresse
**wortgetreu**. **Keine Adressänderung zugesagt und keine vorgenommen** — in
Shopify wurde nichts verändert, und das wäre auch außerhalb der Regeln.
**Nicht behauptet, es sei zu spät, und nicht behauptet, es sei noch möglich**
— **ausdrücklich gesagt, dass der Bestellstatus derzeit nicht prüfbar ist.**
**Keine Bestellnummer, kein Datensatz** — es wird nichts über die Bestellung
behauptet. **Kein Termin genannt.** **Kein geratener Name** — sie
unterschreibt nicht. **Ihre neue Adresse wird ihr gegenüber nicht wiederholt**
(sie kennt sie) **und geht ausschließlich an den Owner.** Kein
Eskalationsmarker im Text.

---

## 3. ⬛ HEUTE ZU ERSTATTEN

**Kauschäden stehen hier grundsätzlich nicht.** Das betrifft heute **#7373,
#7626, #7831, `hud@…`** — und **#7168**, soweit es den zerstörten Artikel
betrifft.

**⚠️ Alle Beträge unten stammen aus Abfragen von vor heute früh** — der
Bestelldatensatz ist seit dem Shop-Wechsel nicht mehr prüfbar. **Sie sind
nicht neu verifiziert.**

### Schriftlich zugesagt — braucht nur die Ausführung

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#4055** | **£11,97** | Kimberley Shenton | 60 % am 19.09. als „processed" bestätigt; `refunds` leer |
| **#5148** | **£13,98** | Trudi Wright | **VIERMAL** „processed" — 07./16./18./22.09. |
| **#5973** | **£14,98** | Stephen Cooil | 17.09. „processed"; `refunds` leer |
| **#4919** | **£11,18** | Em Gregory | zweimal „processed" |
| **#4812** | **86,89 £ / 116,92 $** | Carolyn Marmalejo | volle Erstattung 21.09. „processed" |
| **#6583** | **30,54 £** | Ken Beville | zugesagt 03.09., wortgleich erneut 21.09. |
| **#4998** 19,95 £ · **#6528** 22,93 £ · **#6159** 9,17 £ · **#6936** 8,39 £ | | | angenommen, nicht ausgeführt |
| **#7179** 24,32 $ · **#6546** 41,55 $ · **#7884** 8,30 $ | | | angenommen bzw. „processed" |
| **#6259** · **#7060** | offen | Nick Tarrant u. a. | Frist abgelaufen / angenommen |

**⚠️ #4940 Rena Barnes steht hier NICHT** — sie hat keines der sechs Angebote
angenommen. **⚠️ #7479 steht hier NICHT** — er hat alle drei abgelehnt.
**Es besteht in beiden Fällen keine Zusage, und es wird keine unterstellt.**

### ⏰ Vor Versand storniert — zeitkritisch

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#8781** | **37,69 $** | Glenn Yarbrough | 21 Minuten nach der Bestellung storniert, **dreimal gebeten**, Datensatz unverändert seit vierzehn Sekunden nach der Bestellung |
| **#8669** | **38,19 $** | Chad Lovell | elf Minuten nach der Bestellung; **die Ablehnung vom 22.09. ist durch nichts gedeckt** |
| **#8605** | **£27,95** | Gurvinder Ghattaura | seit 17.09. nicht versandt — **und heute 11:21:32 eine Nachricht aus dem Serienversand erhalten, Inhalt hier ungeprüft** |

### Nie angekommen / defekt angekommen / Ersatz nie versandt

#5036 27,95 £ (Lynette Lumley, Bewertung abgegeben) · #8079 19,95 £ ·
#2894 19,95 £ (**Ersatz 24.07. zugesagt, nie versandt**) · #3089 27,95 £ ·
#5905 27,95 £ · #8295 27,95 £ · #7459 19,95 £ · #4604 28,51 £ ·
#8081 20,35 £ · #7970 offen

### Unbenutzte Ware — kein Rückgabeweg vorhanden

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#8142** | **offen** (von 27,95 £) | **Wendy Price** | **ein Artikel versiegelt in Originalverpackung — dreimal danach gefragt, dreimal über den zerkauten geantwortet** |
| **#7479** | **offen** (von 29,95 £) | **Richard Bellamy** | **ein Artikel ungeöffnet; fragte am 16.09. nach dem Rückgabeweg — nie beantwortet, stattdessen drei Prozentangebote** |
| **#6254** | **offen** (von 34,95 £) | **David Hickman** | **zwei von vier ungeöffnet**; bietet ausdrücklich die Rückgabe an |
| **#8431** | **offen** (von A$53,53) | Sarah Williams | Elefant ungeöffnet, **AU** |
| **#7034** · **#5148** · **#4055** · **#8312** · **#5973** · **#7048** · **#8484** · **#8372** (96,89 $) · **#7347** · **#8456** · **#8577** · **#7555** (34,95 £) · **#7119** (28,50 £) · **#4812** · **#7179** | | | unverändert |

**⚠️ NICHT hier aufgeführt:** **#8568** (beide Artikel nachweislich benutzt),
**#7831** (alles weggeworfen), **#7626**, **#7373**, **`hud@…`** (keine
Rückgabe verlangt bzw. Zustand ungeklärt).

### Fehlmenge

#7989 (A$53,87) · #6656 · #7608

### Summe

**Summe der bezifferten Beträge in GBP: 466,97 £** — **unverändert gegenüber
gestern.** Aufschlüsselung: **155,06 £** zugesagt · **27,95 £** vor Versand
storniert · **220,51 £** nie angekommen/defekt · **63,45 £** unbenutzt.

**Kein neuer bezifferter Fall heute** — **alle neun Vorgänge des Tages sind
entweder Kauschäden, ohne Forderung, oder nicht bezifferbar**, und der
Bestelldatensatz ist ohnehin nicht abrufbar.

**Zusätzlich in USD/AUD, nicht umgerechnet:** 116,92 $ · 96,89 $ · 41,55 $ ·
38,19 $ · 37,69 $ · 24,32 $ · 8,30 $.

**Sechzehn Positionen bleiben unbeziffert**, weil der Anteil je Position aus
den Kaching-Bundle-Preisen nicht errechenbar ist. **Hier wird nichts
geschätzt und nichts umgerechnet.**

### Nicht hier aufgeführt, aber zu beobachten

**🟥 Die Shopify-Verbindung zeigt auf den falschen Shop** — **der dringendste
technische Punkt.**

**🟨 Die Google-Sicherheitswarnung vom 26.09.** (neuer Passkey auf dem
Support-Konto) **ist weiterhin ungeprüft.**

**🟨 Drei unaufgeforderte Geschäftsanbahnungen** in diesem Postfach:
`shopifystoreregulatory.center@gmail.com` (06.09.), `permitshopify@gmail.com`
(26.09.), **`emmydigital4200@gmail.com` (28.09., fragte nach einer
WhatsApp-Nummer — keine herausgegeben).**

**⚠️ Zweiundsiebzig unabhängige Kundenaussagen zur Werbung.**

---

## Was dieser Report bewusst NICHT tut

- **Er erfindet keinen Entwurfstext.** Alle neun Volltexte oben stehen so in
  `docs/entwuerfe-zum-kopieren.md`.
- **Er führt keinen Kauschaden in Teil 3.**
- **Er rechnet nichts zwischen Währungen um** und **schätzt keinen Anteil aus
  einem Bündelpreis.**
- **Er gibt keine Bestellzahlen als heute geprüft aus** — sie stammen aus
  Abfragen von vor dem Shop-Wechsel und sind so gekennzeichnet.
- **Er behauptet keine Erstattung, keine Stornierung und keine
  Adressänderung als ausgeführt.** **Heute wurde nichts davon ausgeführt.**
