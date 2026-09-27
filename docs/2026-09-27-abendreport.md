# Paw Friends — Abend-Report 27.09.2026

**Stand:** 27.09.2026, 19:15 UTC · **Branch:** `claude/paw-friends-support-bot-fa27s0`
**Quelle:** `docs/2026-09-27-backlog-triage.md` (Läufe 00:20 – 18:20 UTC)

---

## 1. Überblick

### Anzahl nach Kategorie (27.09.)

| Kategorie | Anzahl |
|---|---|
| `Bot/Escalated - Owner Attention` | **3** |
| `Bot/Needs Approval` | **1** |
| `Bot/Draft Ready` | 0 |
| `Bot/No Action` | 0 |
| **Kundenvorgänge gesamt** | **4** |

**Vier Vorgänge, aber drei davon decken Fehler auf, die älter sind als der
Tag.** Zwei davon sind **Vorlagenfehler**, die mehr als einen Kunden betreffen.

### Was Kunden gefragt haben, nach Thema

| Thema | Anzahl | Wer |
|---|---|---|
| **Zugesagtes Geld ist nie angekommen** | **1** | #4055 |
| **Die 30-Tage-Garantie wird ausdrücklich angerufen** | **2** | #8431, #7898 |
| **Die Werbung bzw. Haltbarkeitszusage wird bestritten** | **2** | #8431, #7898 |
| **Direkte Frage nach dem Weg zur Erstattung** | **2** | #8431, #8568 |
| **Unbenutzte Ware liegt beim Kunden** | **1** | #8431 |
| **Schlechte Bewertung angekündigt** | **1** | #7898 |

**Die Zahl der unabhängigen Kundenaussagen zur Werbung bleibt bei
einundsiebzig** — **#4055 und #7898 wurden bereits früher gezählt und werden
nicht doppelt gezählt; #8568 erwähnt die Werbung nicht.**

### Wie geantwortet wurde, pro Thema

**Nicht ausgeführte Geldzusage (1):** **#4055** wurde offen bestätigt, dass die
am 19.09. als *„processed"* gemeldete 60 %-Erstattung im Datensatz nicht
existiert. **Keine zweite Zusage.** **Nicht behauptet, das Geld sei bei der
Bank.**

**Garantie (2):** In beiden Entwürfen wird **weder behauptet, die Garantie
decke den Kauschaden, noch, sie decke ihn nicht.** Stattdessen steht dort nur,
**was im eigenen Material überprüfbar ist** — und bei **#7898** zusätzlich,
dass die Bedingung, auf die sich die Absage vom 24.09. stützte, **in keinem
der zwölf Produkttexte und nicht im eigenen Marketing steht.**

**Werbung (2):** Nur der wörtliche eigene Text, **ohne Auslegung**. **Keine
Anzeige rekonstruiert.** **Nicht behauptet, „indestructible" existiere
nicht** — nur, dass es in den zwölf Texten nicht steht. **Bei #8431 wird der
von ihr zitierte Produkttitel als richtig bestätigt**, weil er überprüfbar
ist, **ohne daraus etwas über Haltbarkeit abzuleiten.**

**Rückgabeweg (2):** Beide Male die Wahrheit an erster Stelle: **es gibt
keine Rücksendeadresse**, mit Warnung, nichts abzuschicken — aus Australien
und aus Florida jeweils ausdrücklich.

**Angekündigte Bewertung (1):** **Nichts daran geknüpft**, nicht um Änderung
oder Rücknahme gebeten, und **nicht versucht, sie zum Wiederkauf zu bewegen.**

### 🟦 Drei Befunde des Tages, die über den Tag hinausgehen

**A. Die Rücksendeadresse, die es nie gab, wurde nachweislich an mindestens
zwei Kundinnen schriftlich angekündigt.** **#5148** am **25.08.** und
**#4055** am **23.08.** — **derselbe Satz**: *„they will provide you with the
return address and further instructions."* **Gestern stand hier noch, es
„könne weitere Empfänger geben". Es gibt sie, belegt.** **Das ist ein
Vorlagenfehler und gehört im Admin geprüft.**

**B. Der 60/50-Widerspruch im Angebotsschreiben ist nicht auf #4940
beschränkt.** Die Mail an **#4055** vom **17.09. 10:37:14** nennt in der
Überschrift **60 %** und in der Schlusszeile **„the 50% partial refund"** —
**dieselbe Fehlkonstruktion wie in Rena Barnes' sechs Schreiben.** Hier fiel
es auf: **elf Sekunden später** ging dieselbe Mail korrigiert hinaus.
**Damit ist auch das ein Vorlagenfehler.**

**C. #4055 wurde gesagt, ihre Bestellung sei nicht auffindbar — nachdem drei
Angebote darauf gemacht worden waren.** Am **15.09.**: *„we're currently
unable to locate an order under the details provided."* **Sie hat den
Widerspruch selbst benannt.** **Shopify findet #4055 sofort.** **Im Entwurf
wird das unaufgefordert richtiggestellt.**

### 🟥 Der Serienversand vom 24.09. wirkt weiter

**#7898 Tammy Brentlinger** ist der nächste dokumentierte Fall: Erstkontakt am
**21.09.**, ein Entwurf wurde geschrieben und **nie gesendet**, und am
**24.09. 12:26:45** ging stattdessen die Kauschaden-Vorlage mit klarer Absage
an sie hinaus. **Ihr Entwurf vom 21.09. ist damit überholt und in der Datei
als ersetzt gekennzeichnet.**

---

## 2. 📤 HEUTE ZU SENDEN

**Vier Entwürfe, alle von heute.** **Die acht Entwürfe aus dem gestrigen
Abendreport** (#8228, #8559, #8573, #8781, #7034, #5148, #8574, #7559)
**sind unverändert offen und stehen dort im Volltext** —
`docs/2026-09-26-abendreport.md`.

**⚠️ Alle liegen ausschließlich als Text in diesem Repo. Keiner ist ein
Gmail-Entwurf** — `create_draft` ist seit dem 21.08. gesperrt. **Zum Senden
musst du sie aus der Datei kopieren.**

**⚠️ Zwei Entwürfe in der Datei sind als ERSETZT gekennzeichnet und dürfen
nicht zusätzlich gesendet werden:** der erste für **#8577** (12:20-Lauf vom
25.09.) und der vom **21.09. für #7898**.

---

## #8431 — Sarah Williams (`slw72@tpg.com.au`) — **AU**, Erstkontakt, **verlangt ausdrücklich eine Erstattung unter der 30-Tage-Garantie**

**Betreff:** `Re: Refund Request – Order #8431 – Donkey Plush Destroyed Within 10 Minutes`

> Dear Sarah,
>
> Thank you for writing, and for setting the dates out so clearly. You asked
> one direct question — how to proceed with a refund under the 30-day
> guarantee — and I would rather answer it honestly than send you a policy
> paragraph.
>
> **The honest answer has two parts, and the first one is uncomfortable.**
>
> **There is no returns process and no returns address.** We do not have one
> to give you. **So please do not post anything back to us** — from Australia
> that would be expensive, and you would lose the toy on top of the postage.
> **That is not a refusal of your claim. It is simply where things stand, and
> you were entitled to hear it in the first reply rather than the fifth.**
>
> **On the refund itself: I cannot approve it from this desk, and I am not
> going to refuse it either.** That decision belongs to the shop owner. **Your
> message goes to him today, in your own words, unedited, as a refund request
> under the guarantee** — which is exactly what you called it.
>
> **I am not going to tell you whether the guarantee covers what happened, in
> either direction.** That is his call and not mine, and guessing at it would
> not help you.
>
> **What I can check, and you can hold me to it:**
>
> - **The product is indeed listed under the title "Plushies – Designed for
>   Furry Friends Who Destroy Everything."** You quoted it accurately; that is
>   our own wording on our own page.
> - Where a **30-day money-back guarantee** appears in our own marketing
>   material, **it appears without any condition attached to it.**
> - **Our published refund policy contains a section headed "Australia —
>   Consumer Guarantees"**, which states that rights under it **"are not
>   limited by the requirement that an item be unused or in its original
>   packaging."** **That is our own wording, quoted as it stands. I am not a
>   lawyer, I am not going to tell you what it means for your order, and I am
>   not going to use it to promise you anything** — but you are entitled to
>   know it is there, and it goes to him with your message.
>
> **You offered photographs, proof of purchase and anything else required.
> Please do not go to the trouble.** **Nothing here is conditional on you
> proving what happened**, and asking you for evidence would only put another
> step between you and an answer.
>
> **You have said you are now reluctant to give the elephant to your dog.**
> **That is recorded as you wrote it, and I am not going to tell you what to
> do with it in either direction** — not to try it, and not to keep it sealed.
> **The fact that it is unopened goes to him with the rest.**
>
> **I am not going to make a claim about the toy itself**, and **I am drawing
> no conclusion from your dog's breed or from the fact that it was a birthday
> present.**
>
> **What is on the order:** #8431, placed **9 September**, despatched
> **14 September**, two toys, **A$53.53 recorded on the order, nothing
> refunded to date.** **You say it reached you on 26 September; our own record
> carries no update after despatch, so I am recording your date rather than
> contradicting it.**
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **ehrliche Beantwortung ihrer Frage** — es gibt keinen
Rückgabeweg —, die Weitergabe ihrer Forderung **unverändert und ausdrücklich
als Garantieanspruch**, die überprüfbare Bestätigung des **eigenen
Produkttitels**, und die **wörtliche Wiedergabe des eigenen AU-Abschnitts der
Refund Policy, ausdrücklich ohne Auslegung.** **Keine Erstattung zugesagt, kein
Betrag, kein Termin — und keine Absage.** **Nicht behauptet, die Garantie decke
den Kauschaden, und nicht behauptet, sie decke ihn nicht.** **Keine Frist
genannt und nicht berechnet, ob sie in der Frist liegt** — weder die 30 Tage ab
Kauf noch ab Erhalt. **Keine rechtliche Bewertung.** **Fotos, Kaufbeleg und
alles weitere ausdrücklich abbestellt** — nichts zur Bedingung gemacht.
**Keine Rücksendeadresse erfunden**, mit Warnung vor einer Sendung aus
Australien. **Keine Aussage zur Haltbarkeit oder Qualität, in keine Richtung.**
**Nichts aus Rasse des Hundes oder dem Anlass gefolgert.** **Ihre Angabe
„$50+" nicht gegen den Bestellsatz gerechnet.** **Ihr Zustelldatum
übernommen, ohne ihr zu widersprechen und ohne die Sendungsnummer als
Zustellbeleg zu benutzen.** **Ihre Telefonnummer aus der Signatur nicht benutzt
und nicht erwähnt.** **Keine Kauschaden-Vorlage.** **Kein Prozentangebot.**
**Keine Anweisung, was sie mit dem ungeöffneten Elefanten tun soll.**

---

## #8568 — Allen Irvin (`allenirvin@aol.com`) — US, Erstkontakt, **fragt direkt nach dem Weg zur Erstattung**

**Betreff:** `Re: How do I get my money back`

> Dear Allen,
>
> You asked a direct question, so here is a direct answer rather than a page
> of policy.
>
> **The first part is not the answer you want.** **There is no returns process
> and no returns address.** We do not have one to give you. **So please do not
> post anything back** — from Florida that would cost you the postage and the
> item both. **That is not a refusal of your request; it is simply where
> things stand, and you should not have to find it out the hard way.**
>
> **On the money itself: I cannot approve a refund from this desk, and I am
> not going to refuse you one either.** That decision belongs to the shop
> owner. **Your message goes to him today, in your own words, as a request for
> your money back** — which is exactly what you asked for.
>
> **I am not going to promise you an answer or a date, because I do not
> control either.**
>
> **You attached a photograph. I have not opened it, and I am not asking you
> for any.** No photograph is a condition of anything here.
>
> **I am not going to make a claim about the toy in either direction** — not
> to defend it and not to agree with you about it. **You told us what happened
> and it is recorded exactly as you wrote it.** **I am also drawing no
> conclusion whatsoever from your dog's breed or his weight. You mentioned
> them; I am not going to use them.**
>
> **One question, because I would rather ask than assume.** Your order has two
> toys on it, and you wrote about one. **If the second is still unopened, tell
> me and I will say so when I pass this on**, because that is a different
> situation and he should know which he is deciding. **If you have given him
> both, that is fine too — I am not going to guess either way.**
>
> **What is on the order:** #8568, placed **16 September**, despatched
> **17 September**, two toys, **$38.41 recorded on the order, nothing refunded
> to date.**
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **direkte Beantwortung seiner Frage** — es gibt keinen
Rückgabeweg —, die Weitergabe seiner Forderung **unverändert**, und **eine
Rückfrage statt einer Annahme** zum zweiten Artikel. **Keine Erstattung
zugesagt, kein Betrag, kein Termin — und keine Absage.** **Keine
Kauschaden-Vorlage.** **Kein Prozentangebot.** **Keine Aussage zur Haltbarkeit
oder Qualität, in keine Richtung.** **Ausdrücklich nichts aus Rasse oder
Gewicht seines Hundes gefolgert** — und ihm das auch so gesagt. **Nicht
angenommen, der zweite Artikel sei unbenutzt** — danach wird gefragt.
**Kein Foto verlangt**, das beigefügte **nicht geöffnet**. **Nichts über die
Werbung behauptet** — er hat sie nicht erwähnt. **Nichts über die Garantie
behauptet** — er hat sie nicht angerufen. **Keine Rücksendeadresse erfunden**,
mit Warnung vor einer Sendung. **Die Sendungsnummer nicht als Zustellbeleg
benutzt.** Kein Eskalationsmarker im Text.

---

## #4055 — Kimberley Shenton (`kim.shenton@me.com`, Bestellung auf `kim.ierston@googlemail.com`) — **60 % am 19.09. als „processed" bestätigt, `refunds` leer**

**Betreff:** `Re: Refund request`

> Dear Kimberley,
>
> You wrote one line and it deserves a straight answer rather than another
> reassurance.
>
> **As far as our own order record goes, the refund was never issued.** Order
> #4055 shows **£0.00 refunded and no refund entries against it at all.**
>
> **You were told on 19 September that the 60 % had been "processed to your
> original payment method" and asked to allow a few business days.** **That
> was eight days ago, and I am not going to repeat that sentence to you.** **I
> am not going to tell you it is sitting with your bank either. I have no
> basis for saying so, and you have already been told once.**
>
> **There are two other things in this thread that were our doing, and you
> should not have to raise them yourself.**
>
> **First, on 15 September you were told we could not locate an order under
> your details — after the order had already been found and three separate
> offers had been made against it.** **You were right to say that made no
> sense.** **The order is on our system, under your maiden name and the
> address you gave us, exactly where you said it would be. It was never
> missing.**
>
> **Second, on 23 August you were told your return request had been forwarded
> and that a team would provide you with a return address and further
> instructions.** **No return address was ever sent, because there is no
> returns address to send.** **You waited on that for nearly two weeks before
> the first partial offer arrived.** **That is our failure, not yours.**
>
> **So where this stands: you accepted 60 % on 17 September, you were told on
> 19 September it had been paid, and our record shows nothing paid.**
>
> **I cannot issue it from this desk — that is the limit of what support can
> do here, not a deflection — and I am not going to make you a second
> promise.** **What I have done today is put the whole sequence in front of
> the shop owner, with the dates on it, as an outstanding payment that was
> confirmed in writing and not made.** **He is the only person who can release
> it.**
>
> **What is on the order:** #4055, placed **31 July**, despatched **5 August**,
> one toy, **£19.95 recorded on the order, £0.00 refunded.**
>
> I am sorry you have had to chase this.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Feststellung, dass die am 19.09. bestätigte
Erstattung im Bestelldatensatz nicht existiert** (`totalRefundedSet` 0,00 £,
`refunds` leer), die **ausdrückliche Weigerung, eine zweite Zusage zu machen**,
die **unaufgeforderte Richtigstellung der Auskunft vom 15.09.**, die Bestellung
sei nicht auffindbar — **sie war es**, und die **unaufgeforderte Anerkennung,
dass ihr am 23.08. eine Rücksendeadresse angekündigt und nie geschickt wurde.**
**Keine Erstattung zugesagt, kein Termin, keine Absage.** **Nicht behauptet,
das Geld sei unterwegs, bei der Bank oder in Bearbeitung.** **Der Betrag
£11,97 wird ihr gegenüber nicht genannt** — nur der Bestellbetrag und die
0,00 £. **Nichts zur Herkunft der Ware gesagt, in keine Richtung** — sie hat
sie erwähnt, fragt aber nicht danach, und es wird nicht wiederholt.
**Nichts über die Abbildungen oder die Größe des Artikels gesagt.** **Keine
Aussage zur Qualität, in keine Richtung.** **Ihre eigene Preisrechnung nicht
korrigiert.** **Die Rückgabe wird nicht wieder gegen sie aufgemacht** — sie
hat die 60 % angenommen. Kein Eskalationsmarker im Text.

---

## #7898 — Tammy Brentlinger (`pitbulladvocate@live.com`) — US, **zweiter Kontakt nach der Vorlage vom 24.09.** · **ERSETZT den Entwurf vom 21.09.**

**⚠️ Der Entwurf vom 21.09. ist überholt und darf nicht mehr gesendet
werden.** Er entstand, bevor sie am 24.09. die Kauschaden-Vorlage erhielt, und
kennt diese Absage nicht.

**Betreff:** `Re: Dog Toys`

> Dear Tammy,
>
> You said you bought them because of the 30-day guarantee. **That deserves a
> straight answer about what our own material actually says, rather than
> another paragraph of policy.**
>
> **The reply you received on 24 September told you the guarantee "applies to
> items returned unused and in their original condition."** **I have checked
> where that condition comes from, and I am going to tell you what I found
> rather than defend it.**
>
> - I have read all twelve of our current product descriptions. **That
>   condition is in none of them.**
> - **The description of the toys you bought carries no guarantee wording at
>   all.**
> - Where a **30-day money-back guarantee** does appear in our own marketing
>   material, **it appears without any condition attached to it.**
> - **The word "indestructible" is not in any of the twelve descriptions
>   either.** **I cannot see the advertisement you actually read, so I am not
>   going to tell you what it said, and I am certainly not going to suggest
>   you misread it.**
>
> **What I am not going to do is tell you the guarantee covers what happened,
> or that it does not.** **That is the shop owner's decision and not mine, and
> I will not pretend otherwise in either direction.**
>
> **What I can tell you honestly: I cannot reverse the 24 September reply from
> this desk, and I am not going to tell you it has been reversed.** **What I
> have done is put your message in front of the shop owner today, in your own
> words, together with the fact that the condition the refusal relied on does
> not appear in our own product descriptions or marketing.** **He is the only
> person who can change the answer.**
>
> **On the review: that is entirely your business.** **I am not going to ask
> you to reconsider it, I am not going to ask you to change or remove
> anything, and nothing here depends on what you write or do not write.**
> **The same goes for not buying from us again.**
>
> **I am not going to make a claim about the toys themselves in either
> direction**, and **I am drawing no conclusion from your dogs' size or from
> how they play.** **You described what happened and it is recorded exactly as
> you wrote it.** **Your photograph from 21 September is on the file and you
> do not need to send anything further.**
>
> **One practical thing, in case it is on your mind: there is no returns
> address.** **We do not have one to give you, so please do not post anything
> back from Arizona** — it would cost you the postage and the items.
>
> **What is on the order:** #7898, placed **27 August**, not handed over for
> despatch until **3 September — seven days** — two toys, **$42.61 recorded on
> the order, nothing refunded to date.**
>
> I am sorry this is not a better answer today.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **überprüfbare Auskunft, dass die Bedingung, auf die
sich die Absage vom 24.09. stützt, in keinem der zwölf Produkttexte und nicht
im eigenen Marketing steht**, und die Weitergabe genau dieses Umstands an den
Owner zusammen mit ihrer Nachricht. **Keine Erstattung zugesagt, kein Ersatz,
kein Betrag, kein Termin.** **Nicht behauptet, die Absage vom 24.09. sei
aufgehoben oder sei keine Entscheidung gewesen** — sie wurde tatsächlich
gesendet, und das wird nicht beschönigt. **Nicht behauptet, die Garantie decke
den Kauschaden, und nicht behauptet, sie decke ihn nicht.** **Nicht behauptet,
„indestructible" existiere nicht** — nur, dass es in den zwölf Texten nicht
steht. **Keine Rekonstruktion der Anzeige.** **Nichts an ihre Bewertung
geknüpft**, nicht um Änderung oder Rücknahme gebeten, und **nicht versucht,
sie zum Wiederkauf zu bewegen.** **Keine Aussage zur Haltbarkeit oder
Qualität, in keine Richtung.** **Nichts aus Größe oder Verhalten ihrer Hunde
gefolgert.** **Kein Foto verlangt.** **Ihre Preisangabe nicht gegen den
Bestellsatz gerechnet.** **Keine Rücksendeadresse erfunden.** **Die
Trinkgeld-Position der Bestellung wird nicht erwähnt.** Kein
Eskalationsmarker im Text.

---

## 3. ⬛ HEUTE ZU ERSTATTEN

**Kauschäden stehen hier grundsätzlich nicht.** Das betrifft heute **#8568**
und **#7898** — **#7898 steht deshalb nicht hier, obwohl die Absage vom
24.09. sich auf eine Bedingung stützte, die im eigenen Material nicht
existiert.** **Ob die Garantie greift, ist eine Owner-Entscheidung und wird
von hier nicht vorweggenommen.** **Ebenso #8431**, soweit es den zerstörten
Donkey betrifft — **der ungeöffnete Elefant steht dagegen unten.**

### Schriftlich zugesagt — braucht keine neue Entscheidung, nur die Ausführung

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#4055** | **£11,97** (60 % von 19,95 £) | **Kimberley Shenton** | **HEUTE BELEGT.** 60 % am **17.09.** angenommen, am **19.09.** als „processed to your original payment method" bestätigt; `totalRefundedSet` **0,00 £**, `refunds` **leer**. **Acht Tage.** |
| **#5148** | **£13,98** (50 % von 27,95 £) | Trudi Wright | **VIERMAL** als „processed" bestätigt — 07./16./18./22.09.; `refunds` leer |
| **#5973** | **£14,98** (50 % von 29,95 £) | Stephen Cooil | am 17.09. „processed"; `refunds` leer |
| **#4919** | **£11,18** (40 % von 27,95 £) | Em Gregory | zweimal „processed"; `refunds` leer |
| **#4812** | **86,89 £ / 116,92 $** | Carolyn Marmalejo | volle Erstattung 21.09. „processed" |
| **#7884** | **8,30 $** | Logan Bishop | 30 % 22.09. „processed" — **er hatte keine verlangt** |
| **#7179** | **24,32 $** | Keith Crane | 50 % 22.09. angenommen |
| **#6546** | **41,55 $** | Vik Jehdian | 50 %, 09.09. „processed" |
| **#6583** | **30,54 £** | Ken Beville | zugesagt 03.09., wortgleich erneut 21.09. |
| **#6259** | **offen** | Nick Tarrant | Trading Standards, Frist abgelaufen |
| **#4998** | **19,95 £** | — | zugesagt, nicht ausgeführt |
| **#6528** | **22,93 £** | Tommy Johnson | 50 % 19.09. angenommen |
| **#6159** | **9,17 £** | Mary Linan | 30 % 19.09. angenommen |
| **#6936** | **8,39 £** | — | angenommen, nicht ausgeführt |
| **#7060** | **offen** | — | 30 % angenommen |

**⚠️ #4940 Rena Barnes steht hier NICHT** — sie hat **keines** der sechs
Angebote angenommen. **Es besteht keine Zusage, und es wird keine unterstellt.**

### ⏰ Vor Versand storniert — zeitkritisch

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#8781** | **37,69 $** | **Glenn Yarbrough** | **21 Minuten nach der Bestellung storniert (24.09.)**, **DREIMAL gebeten**; `cancelledAt: null`, **`updatedAt` unverändert seit vierzehn Sekunden nach der Bestellung** |
| **#8669** | **38,19 $** | Chad Lovell | **elf Minuten nach der Bestellung storniert (19.09.)**; **die Ablehnung vom 22.09. („already been shipped") ist durch nichts gedeckt** |
| **#8605** | **£27,95** | Gurvinder Ghattaura | seit 17.09. nicht versandt |

### Nie angekommen / defekt angekommen / Ersatz nie versandt

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#5036** | **27,95 £** | Lynette Lumley | Zustellmeldung vom 08.09. steht gegen den eigenen Datensatz (**seit 22.08. keine Aktualisierung**). **Bewertung bereits abgegeben.** |
| **#8079** | **19,95 £** | Nick Wright | nie angekommen; Versand 08.09., **seither neunzehn Tage ohne Aktualisierung** |
| **#2894** | **19,95 £** | Jeff Hughes | defekt angekommen 23.07.; **Ersatz am 24.07. wörtlich zugesagt, nie versandt** |
| **#3089** | **27,95 £** | Sue Steer | nie zugestellt seit 28.07., vier Nachfassungen, null Antworten |
| **#5905** | **27,95 £** | Kate Stephens | nicht erhalten seit 01.09. |
| **#8295** | **27,95 £** | Ivan Griffen | **nicht erhalten** — steht hier wegen der Nichtlieferung |
| **#7459** | **19,95 £** | Sarah Taylor | nicht erhalten |
| **#4604** | **28,51 £** | Nicholas Kloepfer | an die falsche Adresse versandt |
| **#8081** | **20,35 £** | Matthew Pierce | APO-Adresse, liegt seit über drei Wochen |
| **#7970** | **offen** | Melissa Harris | nicht erhalten; Betrag ungeklärt |

### Unbenutzte Ware — erfüllt die veröffentlichte Garantie, kein Rückgabeweg vorhanden

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#8431** | **offen** (von A$53,53) | **Sarah Williams** | **NEU 27.09.** — **der Elefant ist ungeöffnet**, sie traut sich nicht, ihn zu geben. **AU.** |
| **#7034** | **offen** (von 27,95 £) | Sarah Checksfield | zweiter Artikel ungeöffnet — erfüllt **genau die Bedingung, die ihr am 15.09. entgegengehalten wurde** |
| **#5148** | s. o. | Trudi Wright | **beide Spielzeuge einen Monat ungeöffnet aufbewahrt** — wegen der angekündigten Adresse, die es nie gab |
| **#4055** | s. o. | Kimberley Shenton | **wollte von Anfang an zurückgeben**; ihr wurde am **23.08.** dieselbe Adress-Ankündigung geschickt wie #5148 |
| **#8312** | **offen** (von 27,95 £) | Paul Beaver | ein Artikel unbenutzt in Originalverpackung; **dritte Bitte um Rückgabe** |
| **#5973** | **offen** (von 29,95 £) | Stephen Cooil | der **Donkey ist unbenutzt**; seine Frage vom **11.09.** ist **sechzehn Tage unbeantwortet** |
| **#7048** | **offen** (von 27,95 £) | Josephine Carr | fünfter Kontakt; **kündigte am 23.09. ein Paket an eine „UK department" an, die es nicht gibt — vier Tage ohne Antwort** |
| **#8484** | **offen** (von 19,95 £) | Sue Quick | fragt nur nach dem Rückgabeweg |
| **#8372** | **96,89 $** | Kerri Forbey | alle Artikel unbenutzt in Originalverpackung; **dritte Kauschaden-Absage ohne Kauschaden** |
| **#7347** | **offen** (von 29,95 £) | Jill Hibbs | ein Artikel unbeschädigt; **30 % zweimal abgelehnt** |
| **#8456** | **offen** (von 34,95 £) | Cath Livesey | Rückgabe und volle Erstattung verlangt |
| **#8577** | **offen** (von 49,90 £) | Shirley McCutcheon | Rückgabe verlangt, kein Rückgabeweg vorhanden |
| **#6254** | **offen** | David Hickman | zwei von vier ungeöffnet |
| **#7479** | **offen** (von 29,95 £) | Richard Bellamy-Williams | ungeöffnet, in der Frist gemeldet; 30 % am 22.09. abgelehnt |
| **#4812** | s. o. | Carolyn Marmalejo | alles außer einem Stück ungeöffnet |
| **#7555** | **34,95 £** | Steve Kerr | zwei von drei Stücken unbenutzt |
| **#7119** | **28,50 £** | Susan McGee | ein Stück unberührt, **AU** |
| **#7179** | s. o. | Keith Crane | zwei von drei Stücken ungeöffnet |

**⚠️ #8568 Allen Irvin steht hier bewusst NICHT.** Auf seiner Bestellung
stehen zwei Artikel, er schreibt aber nur von einem. **Ob der zweite
unbenutzt ist, wurde nicht unterstellt — im Entwurf wird danach gefragt.**

### Fehlmenge / fehlender Artikel

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#7989** | **offen** (von A$53,87) | Karen Reynolds | bezahlt für 2, erhalten 1 — **und die am 30.08. schriftlich zugesagte Variante „Frog" kam nie auf die Bestellung** |
| **#6656** | **offen** | Jesse Sida | bezahlt für 4, erhalten 2; Bank-Claim angekündigt |
| **#7608** | **offen** | Patricia Arenella | beworbener Gratisartikel nie erhalten |

### Summe

**Summe der bezifferten Beträge in GBP: 466,97 £.**

Aufschlüsselung: **155,06 £** zugesagt · **27,95 £** vor Versand storniert ·
**220,51 £** nie angekommen/defekt · **63,45 £** unbenutzt.

**Gegenüber gestern +11,97 £** — **kein neuer Fall, sondern #4055**, die
gestern noch unbeziffert war. **60 % von 19,95 £ sind ein glatter Prozentsatz
des Bestellbetrags einer Einzelposition, keine Schätzung aus einem
Bündelpreis** — deshalb ist die Zahl jetzt nennbar.

**Zusätzlich in USD/AUD, nicht umgerechnet:** **116,92 $** (#4812) ·
**96,89 $** (#8372) · **42,61 $** (#7898, nichts erstattet — **keine
Erstattungsposition**, nur zur Information) · **41,55 $** (#6546) ·
**38,41 $** (#8568, **keine Erstattungsposition**) · **38,19 $** (#8669) ·
**37,69 $** (#8781) · **24,32 $** (#7179) · **8,30 $** (#7884).

**Fünfzehn Positionen sind weiterhin nicht beziffert** (#6259, #7060, #7970,
#7048, #8456, #7347, #8312, #8577, #6254, #7479, #7989, #6656, #7608, #8484,
#5973 und **neu #8431** in der Rubrik „unbenutzt"), weil der Anteil je
Position aus den **Kaching-Bundle-Preisen nicht errechenbar** ist: die
Listenpreise summieren sich nicht auf den gezahlten Gesamtbetrag. **Diese
Anteile müssen im Shopify-Admin bestimmt werden; hier wird nichts geschätzt.
Es wird nichts zwischen Währungen umgerechnet.**

### Nicht hier aufgeführt, aber zu beobachten

**🟨 Die Google-Sicherheitswarnung vom 26.09. 10:23 UTC** (neuer Passkey auf
`support.pawfriends.uk@gmail.com`) **ist von hier aus nicht prüfbar und
weiterhin offen. Das bleibt der dringendste Punkt überhaupt** — es ist das
Konto, über das der gesamte Kundenverkehr läuft.

**🟨 Kaltakquise vom 26.09.** (`permitshopify@gmail.com`) — nicht beantwortet,
nichts herausgegeben.

**Fünf Sendungen ohne jede Aktualisierung seit dem Versand:** #8080, #8079,
#8483, #8432, #8476.

**Elf Bestellungen haben eine unausgelieferte E-Book-Position:** #8372, #7555,
#6592, #6254, #6546, #2852, #7831, #8456, #8476, #8577, #8550. **⚠️ #7898
trägt eine offene Trinkgeld-Position — das ist keine Ware und wird hier nicht
mitgezählt.**

**Sechster Kunde, dessen frühere Nachricht hier nicht auffindbar ist**
(#7401) — **der zweite Posteingang `paw-friends.uk@paw-friends.uk` bleibt ein
blinder Fleck.**

**Drei Adressabweichungen zwischen Absender und Bestelldatensatz:** **#8574**
(ungeklärt, keine Bestelldaten herausgegeben), **#8431** und **#4055**
(beide von den Kundinnen selbst aufgelöst).

**Zu prüfen, unverändert:** Shopify ordnet **#7813** `tpayne743@gmail.com` /
Tasha Payne zu; im Protokoll vom 18.09. steht #7813 für Maria Carter.
**Welche Zuordnung stimmt, wird von hier aus nicht entschieden.**

---

## Was dieser Report bewusst NICHT tut

- **Er erfindet keinen Entwurfstext.** Alle vier Volltexte oben stehen so in
  `docs/entwuerfe-zum-kopieren.md`.
- **Er führt keinen Kauschaden in Teil 3.**
- **Er rechnet nichts zwischen Währungen um** und **schätzt keinen Anteil aus
  einem Bündelpreis.**
- **Er behauptet keine Erstattung und keine Stornierung als ausgeführt.**
  `refundCreate` und `orderCancel` sind gesperrt; **heute wurde keine einzige
  Erstattung und keine einzige Stornierung ausgeführt.**
