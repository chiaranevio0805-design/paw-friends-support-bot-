# Paw-Friends — Abendreport Montag, 21.09.2026

---

## 1. Überblick

### Anzahl nach Kategorie

| Kategorie | Anzahl |
|---|---|
| **Draft Ready** | **0** |
| **Needs Approval** | **0** |
| **Escalated — Owner Attention** | **19** |
| **No Action** | **0** |

**Neunzehn Kundenvorgänge, alle neunzehn eskaliert.** Kein einziger Fall war
von hier aus abschließbar. **Keine Erstattung ausgeführt** — kein Fall fiel
unter Regel 4 (bestätigte Falschlieferung).

### Was Kunden heute gefragt haben, nach Thema

| Thema | Anzahl | Bestellungen |
|---|---|---|
| **Haltbarkeit / Spielzeug zerstört** | **8** | #8171, #6804, #6384, #8406, #3387, #8002, #8003, #7898 |
| **Werbung / Garantie direkt in Frage gestellt** | **6** | #6804, #8406, #7048, #7541, #7815, #3387 |
| **Geld schon zugesagt, nicht angekommen** | **3** | #6583, #6546, #7041 |
| **Nie zugestellt / Ersatz nie versandt** | **2** | #3089, #2894 |
| **Fehlmenge** | **1** | #7989 |
| **Rückgabe unbenutzter Ware verlangt** | **1** | #6254 |
| **Frage nach dem Verfahren selbst** („war das eine automatische Antwort?") | **1** | #8002 |
| **Frist läuft** | **1** | #8295 (23.09.) |

*(Mehrfachnennung möglich — #6804, #8406 und #3387 stehen in zwei Zeilen.)*

### Wie darauf geantwortet wurde, pro Thema

- **Haltbarkeit.** Keine Kauschaden-Vorlage, in keinem einzigen Fall. Statt
  einer Absage: die Garantielage wahrheitsgemäß genannt (Plushies-Seite **ohne**
  Garantietext, Werbemails **mit** 30-Tage-Garantie **ohne** Bedingung), die
  Entscheidung ausdrücklich beim Owner verortet. **Keine Zusage, keine Absage.**
- **Werbung.** Wo Kunden „indestructible" zitieren, wird gesagt, was geprüft
  wurde (zwölf Produktbeschreibungen — das Wort steht in keiner) **und was von
  hier nicht prüfbar ist** (welche Anzeige sie gesehen haben). **Keine
  Behauptung, das Zitat existiere nicht.** Bei #7815, die Website-Text zitiert,
  wird bestätigt, dass es unser eigener Text ist.
- **Zugesagtes Geld.** Bei #6583 und #6546 wird der Datenstand offen gegen die
  eigene Zusage gestellt: **es ist nichts gebucht.** Die Zusicherung „processed"
  wird **nicht wiederholt.** Bei #7041 wird gesagt, dass **keine Zusage
  auffindbar ist** — ohne zu behaupten, es habe keine gegeben.
- **Nichtlieferung.** #2894 und #3089 bekommen zuerst die Feststellung, dass sie
  **acht bzw. vier Mal ohne Antwort geblieben sind**, dann den Datenstand. **Kein
  Verweis an den Versanddienstleister.**
- **Fehlmenge (#7989).** Die Kauschaden-Absage, die ihr geschickt wurde, wird als
  falsche Antwort benannt. **Ihr wird nicht gesagt, sie habe sich verzählt.**
- **Rückgabe (#6254).** Es wird gesagt, dass **keine Rücksendeadresse existiert**
  — und er ausdrücklich gebeten, **nichts** zu verschicken.
- **#8002.** Die Frage „war das eine automatische Antwort?" wird **mit Ja**
  beantwortet.
- **#8295.** Fünfte Fassung, ohne die Carrier-Frage wieder aufzumachen.

### Drei Befunde dieses Tages

1. **⛔ Die Kauschaden-Vorlage ist heute Vormittag erneut in Serie gegangen** —
   mindestens **fünfundzwanzig Sendungen**, vier Antworten kamen binnen
   30 Minuten zurück. Mehrere waren mit **„Dear Customer"** adressiert, an Kunden
   im dritten und fünften Kontakt. **#7989 bekam sie auf eine Fehlmenge**,
   **#6254 hat sie zu einem Rückgabewunsch veranlasst, den der Shop nicht
   erfüllen kann.**
2. **🟦 Zwei Advertorial-Seiten** (`angelina-notes-dog-toys`,
   `sophie-dog-toy-counter`) liefern über die API **keinen `body`** — der Inhalt
   kommt aus einem Page-Builder. **Was dort steht, ist von hier nicht lesbar.**
   Dazu ein **Kunden-PDF „Plushies Dog Toys Email"** (#7898), **nicht geöffnet**.
   Zusammen mit den belegten Klaviyo-Mails vom 27.08. sind das **drei mögliche
   Fundorte** der Werbeaussage — **alle drei kann nur der Owner öffnen.**
3. **🔴 #6546 ist der sechste Fall** „Erstattung als erledigt gemeldet, nicht
   ausgeführt" (nach #5148, #6583, #4998, #6259 — und #6583 heute erneut).

### Zwei eigene Richtigstellungen

- **Die Zählung der Vorlagen-Sendungen ist eine Untergrenze, kein Gesamtwert.**
  Eine gesendete Nachricht wird hier nur sichtbar, wenn im selben Thread später
  eine **ungelesene eingehende** Nachricht liegt. Threads, in denen der Kunde
  aufgegeben hat, bleiben unsichtbar. Alle Zahlen sind mit **„mindestens"** zu
  lesen.
- **Der Bestand der Entwurfsdatei wurde zuletzt mit „124 Entwürfen" angegeben.
  Das stimmt nicht.** Nachgezählt enthält `entwuerfe-zum-kopieren.md`
  **300 Entwürfe**. Die Zahl war ein fortgeschriebener Zählstand, der nicht mehr
  an der Datei geprüft worden war.

---

## 2. 📤 HEUTE ZU SENDEN

**Alle neunzehn Entwurfstexte dieses Tages im Volltext, in der Reihenfolge ihrer
Entstehung. Wortgleich aus `docs/entwuerfe-zum-kopieren.md` übernommen —
nichts gekürzt, nichts nacherzählt, nichts rekonstruiert.**

**Keiner dieser Entwürfe liegt in Gmail.** `create_draft` ist seit dem 21.08.
blockiert (21 Versuche, **kein 22.**). Zum Versenden müssen die Texte von hier
kopiert werden.

**Keine Erstattung und keine Stornierung wurde heute ausgeführt.**
`refundCreate` und `orderCancel` sind für den Bot gesperrt.

---

## #8171 — Orville Fender jr (drewdlo2000@hotmail.com) — US, Erstkontakt, verlangt nichts

**Betreff:** Re: Dissatisfied customer

> Dear Orville,
>
> Thank you for writing, and I am sorry it is about this. **The first day.**
> That is not what you paid for, and I am not going to argue with you about it or
> ask you to prove it.
>
> **You have not asked us for anything, and I am not going to put words in your
> mouth.** You told us what happened. **If what you want is your money back, say
> so in one line and it goes forward as that** — the option is open and it is not
> a trick question. Either way, what you wrote is already with the shop owner,
> with what our records show: **order #8171, one Plushies, $30.29 recorded on the
> order, nothing refunded, ordered 29 August, dispatched 8 September.**
>
> **Whether a refund is given is his decision and not mine**, so I am not going
> to promise you one and I am not going to refuse you one.
>
> **There is nothing for you to do.** You do not need to send photographs, and
> **please do not post anything back to us** — we have no returns address I can
> give you, and I would rather tell you that than have you pay postage to
> nowhere.
>
> **One thing from our own records that you did not ask about but should
> probably know.** Your order was placed on 29 August and was not handed over for
> dispatch until 8 September — **ten days.** That was at our end, and I am not
> going to explain it away.
>
> **And thank you for the tip you added to the order.** I have not forgotten that
> it is on there; I am mentioning it because it makes the rest of this worse, not
> better.
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **Weigerung, seine Meldung als Erstattungsforderung
auszulegen**, verbunden mit dem Angebot, sie auf ein Wort hin so weiterzugeben;
die Weitergabe mit allen Zahlen; die **ungefragte Offenlegung der zehn Tage bis
zum Versand**; und eine Nachfass-Zusage. **Keine Erstattung zugesagt, kein
Betrag zugesagt, kein Termin, keine Absage, keine Vorlagen-Antwort.** **Keine
Aussage, die Garantie decke Kauschaden** — die Garantie wird nicht zitiert, da
die Plushies-Beschreibung keinen Garantietext enthält. **Keine Fotobedingung.**
**Keine Rücksendeadresse erfunden.** **Keine Umrechnung** — 30,29 $ ist der
Betrag in seiner Währung auf der Bestellung; **die Trinkgeldposition wird nicht
beziffert und nicht verrechnet.** Kein Eskalationsmarker im Text.

---

## #7041 — Tim Fitton (schreibt von fittontim@gmail.com, Bestellung auf fitton@fitton.karoo.co.uk) — dritter Kontakt, **noch nie eine Antwort erhalten**

**Betreff:** Re: Order #7041 confirmed

> Dear Tim,
>
> **You have written three times — on 16 September, on 17 September and again
> this morning — and you have not had a single reply from us. Not a slow one, not
> a poor one: none at all.** That is our failure, and I am not going to open with
> anything else.
>
> **Because of that, I want to be careful about one word in your message.** You
> wrote that you are *"still awaiting a full refund"*. **I can find no reply from
> us in which a refund was agreed**, so I do not want you to be left believing
> something is already in motion when I cannot see that it is. **If someone did
> promise you one and it is not in our records, tell me and it goes straight to
> the shop owner as a broken promise rather than a new request.**
>
> **What our records do show:** **order #7041, two Paw-Friends™ Fluffys, £29.95
> recorded on the order, nothing refunded, ordered 21 August, dispatched
> 2 September** — **twelve days sitting here before it moved at all**, which is
> ours.
>
> **One administrative note, and I would rather say it than work around it.** You
> are writing from `fittontim@gmail.com`; the order is recorded against
> `fitton@fitton.karoo.co.uk`, with the billing name Bev Fitton at the same
> address. **I am not treating that as a problem — you forwarded the original
> order confirmation, so the connection is plain.** But if a refund is approved
> it would go back to **the card used on that order**, not to whoever wrote last,
> and the shop owner will check the match properly.
>
> **On "not as described".** Our Paw-Friends™ Fluffys page lists a **30-day
> money-back guarantee, and it does not attach a condition to it.** **I am not
> telling you that settles your case** — that decision is the shop owner's and
> not mine, and **I am not going to promise you a refund or refuse you one.**
> **But I am not going to keep our own published wording from you either.**
>
> **Please do not post anything back** — we have no returns address I can give
> you.
>
> **You should not have had to write three times.** If you have heard nothing in
> a few days, reply here and I will chase it again.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Feststellung, dass er auf drei Nachrichten
keine einzige Antwort erhalten hat**, die **ehrliche Klarstellung zu „still
awaiting a refund"** (es ist keine Zusage auffindbar — verbunden mit dem
Angebot, eine etwaige Zusage als gebrochenes Versprechen weiterzugeben), die
**ungefragte Offenlegung der zwölf Tage bis zum Versand**, die **offene
Benennung der Adressabweichung**, die **wahrheitsgemäße Wiedergabe des eigenen
Fluffys-Produkttexts** mit ausdrücklichem Hinweis, dass damit nichts entschieden
ist, und eine Nachfass-Zusage. **Keine Erstattung zugesagt, kein Betrag
zugesagt, kein Termin, keine Absage.** **Keine Behauptung, ihm sei eine
Erstattung versprochen oder nicht versprochen worden** — es wird nur gesagt, was
auffindbar ist. **Keine erfundene „unbenutzt"-Bedingung.** **Keine
Rücksendeadresse erfunden.** **Keine Zahlungsdaten genannt** — nur, dass eine
Erstattung auf die Karte der Bestellung ginge. Kein Eskalationsmarker im Text.

---

## #6804 — Jill Brown (jillbindewald@gmail.com) — US, zweite Fassung, 1-Stern-Bewertung abgegeben

**Betreff:** Re: Order #6804

> Dear Jill,
>
> **On 16 September you asked one question: how can you get a refund. The reply
> you got on 18 September did not answer it — it explained to you why chewing is
> not covered. I am not going to defend that, and I am not going to send you
> another one.**
>
> **So, the answer to the question you actually asked, in two parts.**
>
> **There is nowhere to send the toys back to.** We do not publish a returns
> address. There is none I can give you and I am not going to invent one.
> **Please do not post anything**, and **you do not need to send more
> photographs** — the one you sent arrived, **I have not opened it**, and nothing
> here depends on it.
>
> **And the refund decision is not mine to make.** It belongs to the shop owner.
> **I am not going to promise you a refund and I am not going to refuse you one
> for a second time.** Your case is with him as you put it: **order #6804, two
> Plushies, $41.68 recorded on the order, nothing refunded, ordered 20 August,
> dispatched 2 September, destroyed within three minutes, refund requested on
> 16 September.**
>
> **On the advertising.** You say we claim the toy is indestructible and market
> it as tough and great for strong chewers. I have read all twelve of our current
> product descriptions, and the word "indestructible" is not in any of them —
> **but the wording about strong chewers is ours**, and I am not going to pretend
> otherwise. **What I cannot see from here is the advertising that was actually
> shown to you, and I am not going to guess at it.** **Your sentence goes to the
> shop owner exactly as you wrote it**, because he is the only person who can
> look at the advertising itself and change it.
>
> **On your review.** You left one star and told other people not to shop with
> us. **I am not going to ask you to take it down, change it or soften it, and
> nothing in this email is conditional on it.** That is yours.
>
> **One thing from our records that you did not ask about.** Your order sat here
> from 20 August until 2 September before it was handed over for dispatch —
> **thirteen days.** That was at our end too.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Feststellung, dass ihre Frage vom 16.09. nicht
beantwortet wurde**, die **endliche Beantwortung in beiden Teilen**, die
**wahrheitsgemäße Bestätigung, dass die Formulierung über „strong chewers"
unsere eigene ist**, die Weitergabe mit allen Zahlen, und die **ungefragte
Offenlegung der dreizehn Tage bis zum Versand**. **Keine Erstattung zugesagt,
kein Betrag zugesagt, kein Termin, keine zweite Absage.** **Keine Bitte, die
Bewertung zu entfernen, zu ändern oder abzuschwächen**, und **nichts daran
geknüpft**. **Keine Behauptung, das Wort „indestructible" existiere nicht** —
es wird gesagt, was geprüft wurde und was nicht einsehbar ist. **Keine
Rekonstruktion der Anzeige.** **Keine Auswertung des Fotos, keins verlangt.**
**Keine Rücksendeadresse erfunden.** **Keine Umrechnung** — 41,68 $ ist der
Betrag in ihrer Währung auf der Bestellung. Kein Eskalationsmarker im Text.

---

## #2894 — Jeff Hughes (jeff.hughes@yahoo.co.uk) — ⛔ **defekt geliefert, Ersatz am 24.07. schriftlich zugesagt, nie versandt, achter Nachfasser**

**Betreff:** Re: Order Number 2894

> Dear Jeff,
>
> **You asked for an update. Here is a real one, and it is not an excuse.**
>
> **Our own records show that no replacement was ever sent.** Order #2894 has one
> despatch on it, from 14 July — the original. **There is nothing after it.** So
> when you were told on 6 August that it was being flagged to the owner "today to
> get the replacement actually dispatched", **that did not happen**, and no one
> has written to you since.
>
> **The full sequence, as it stands in our records:**
>
> - **23 July** — you reported the fox arrived with a tear and asked for a
>   replacement, offering to return the damaged one.
> - **24 July** — we agreed to a replacement in writing and told you that you
>   would **not** have to return anything at your own cost.
> - **29 July, 5 August, 13 August, 27 August, 13 September, and today** — you
>   asked for an update. **Six of those got no reply at all.**
> - **Nothing has been dispatched, and nothing has been refunded.**
>
> **That is fifty-nine days since a promise we made, not one you asked for.**
>
> **What I can do and what I cannot.** I cannot dispatch a replacement and I
> cannot issue a refund — neither is mine to do. **So I am not going to give you
> another "I'm chasing this up", because you have had three of those already and
> they were worth nothing.** What I have done is put the case in front of the
> shop owner stated plainly as **an outstanding written commitment**, not as a
> new request: **order #2894, £19.95, damaged on arrival 23 July, replacement
> agreed 24 July, never dispatched, nothing refunded, eight follow-ups from
> you.**
>
> **What has not changed in your favour:** the undertaking that you would not
> have to return the damaged item at your own cost **still stands and I am not
> withdrawing it.** **Please do not post it back** — we have no returns address
> to give you in any case.
>
> **I am not going to ask you for patience.** You have already shown more than
> this deserved.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **überprüfbare Feststellung aus unserem eigenen
Datensatz, dass nie ein Ersatz versandt wurde** (nur ein Fulfillment vom
14.07.), die **vollständige Chronologie mit den sechs unbeantworteten
Nachfragen**, die **Bestätigung, dass die Zusage vom 24.07. — keine Rücksendung
auf eigene Kosten — weiterhin gilt**, und die Weitergabe als **offene
schriftliche Zusage**, nicht als neue Bitte. **Kein Ersatz zugesagt, keine
Erstattung zugesagt, kein Betrag, kein Termin, keine Absage.** **Keine erneute
„wir kümmern uns"-Formel** — dass die drei bisherigen nichts wert waren, wird
ausdrücklich gesagt. **Keine Rücksendeadresse erfunden.** **Keine Bitte um
Geduld.** Kein Eskalationsmarker im Text.

---

## #6583 — Kenneth Beville (kenthecarman06@gmail.com) — 🔴 **dieselbe Erstattungszusage zum zweiten Mal, nichts gebucht**

**Betreff:** Re: Order 6583 return

> Dear Ken,
>
> **You are right, and I am not going to soften it.** The email you received this
> morning is the same one you received on 3 September. **Eighteen days apart, word
> for word, and no refund in between.**
>
> **I am not going to tell you a third time that your case has been "forwarded to
> our team".** That sentence has now been sent to you twice and it has bought you
> nothing.
>
> **What our own records show, so that you are not relying on my word:** against
> order #6583 there is **no refund recorded at all** — the order still shows as
> paid in full, **$41.32**, with nothing refunded against it. **It is possible a
> payment was made outside our shop system and is not recorded there; I cannot
> see your bank and I am not going to guess.** But I am not going to repeat an
> assurance I cannot stand behind.
>
> **What I have done instead:** your case has gone to the shop owner personally,
> stated as **a refund promised on 3 September, repeated on 21 September, and not
> paid** — not as a new request. **I cannot issue the refund myself; that is not
> mine to do.** **So I am not going to promise you a date, because the last two
> promises you got were worth nothing.**
>
> **You have been waiting eighteen days on a decision that was already made in
> your favour.** If you have heard nothing in a few days, reply here and I will
> chase it again.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **ausdrückliche Bestätigung seiner Beobachtung** (es ist
dieselbe Mail wie am 03.09.), die **Weigerung, die Formel „an unser Team
weitergeleitet" ein drittes Mal zu verwenden**, die **wahrheitsgemäße Auskunft
über den eigenen Datenstand** mit offener Nennung der Grenze, und die Weitergabe
**als offene Zusage, nicht als neue Bitte**. **Keine Erstattung zugesagt, kein
Termin zugesagt, keine Absage.** **Keine Behauptung, es sei nicht gezahlt
worden** — nur, dass nichts verzeichnet ist. **Keine Umrechnung** — 41,32 $ ist
der Betrag in seiner Währung auf der Bestellung. Kein Eskalationsmarker im Text.

---

## #6384 — Simon Foord (simonfoord@me.com) — GB, Consumer Rights Act + Klarna + Trading Standards

**Betreff:** Re: Order 6384

> Dear Simon,
>
> **The reply you had this morning was a standard paragraph, and it was addressed
> to "Dear Customer". You have written to us three times. I am not going to
> defend it.**
>
> **You have said the product is not fit for purpose and that a refund must
> follow under UK law. I am not going to argue with you about that, and I am not
> going to give you my assessment of it either** — I am not qualified to give one
> and it would be worth nothing. **Your position goes to the shop owner in full,
> in your words.**
>
> **What I can tell you plainly:**
>
> - **I cannot issue a refund.** That decision is the shop owner's, not mine, so
>   **I am not going to promise you one and I am not going to refuse you one for
>   a third time.**
> - **There is nowhere to send the toys back to.** We do not publish a returns
>   address, and I am not going to invent one. **Please do not post anything.**
> - Your case is with him as it stands: **order #6384, two Plushies, £27.95
>   recorded on the order, nothing refunded, ordered 16 August, dispatched
>   20 August.**
>
> **On Klarna and trading standards.** **Those are yours to contact and I am not
> going to ask you to hold off**, delay, or reconsider. **Nothing in this email
> is conditional on either.**
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Distanzierung von der Vorlagen-Absage von
09:35** samt der Anrede „Dear Customer", die Weitergabe seiner
Rechtsauffassung im Original, die klare Auskunft zur fehlenden
Rücksendeadresse, und die ausdrückliche Feststellung, dass **Klarna und Trading
Standards seine Sache sind und an nichts geknüpft werden**. **Keine Erstattung
zugesagt, kein Betrag, kein Termin, keine dritte Absage.** **Keine rechtliche
Bewertung in eine der beiden Richtungen.** **Keine Rücksendeadresse erfunden.**
Kein Eskalationsmarker im Text.

---

## #8406 — Joyce Abdalla (jva0259@gmail.com) — US, Garantiefrage, zuvor Sicherheitsmeldung

**Betreff:** Re: Order 8406

> Dear Joyce,
>
> **The reply you had this morning was a standard paragraph addressed to "Dear
> Customer", and it did not answer you. I am not going to defend it.**
>
> **On the guarantee, here is the honest picture and it is not simple.**
>
> - **The product page for the Plushies carries no guarantee text at all.** I
>   have read all twelve of our current product descriptions to check.
> - **But a "30-day money-back guarantee" does appear in our own marketing
>   emails, with no condition attached to it.** **So you did not take that from
>   nowhere, and I am not going to suggest that you did.**
>
> **You wrote that a 30-day guarantee implies we stand behind the product. I am
> not going to argue with that reading.** What I cannot do is decide your refund
> — that is the shop owner's call and not mine. **So I am not going to promise
> you one and I am not going to refuse you one.** Your case is with him as you
> put it: **order #8406, one Plushies, $27.56 recorded on the order, nothing
> refunded, ordered 8 September, dispatched 9 September.**
>
> **On sharing your experience** — that is entirely yours to do. **I am not going
> to ask you not to, and nothing here is conditional on it.**
>
> **Please do not post anything back** — we have no returns address I can give
> you.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Distanzierung von der Vorlagen-Absage von
09:36**, die **vollständige und ehrliche Auskunft zur Garantiefrage** (keine auf
der Produktseite, **aber** eine bedingungslose in den eigenen Werbemails), die
Weitergabe mit allen Zahlen, und die ausdrückliche Feststellung, dass ihre
öffentliche Weitergabe ihre Sache ist. **Keine Erstattung zugesagt, kein Betrag,
kein Termin, keine zweite Absage.** **Keine Behauptung, es gebe keine
Garantie.** **Keine Wiederaufnahme ihrer früheren Sicherheitsmeldung ohne
Anlass** — sie hat sie heute nicht erwähnt. **Keine Aussage zur
Materialsicherheit.** **Keine Rücksendeadresse erfunden.** **Keine
Umrechnung.** Kein Eskalationsmarker im Text.

---

## #3387 — Graeme Everett (graeme.everett@sky.com) — GB, Erstkontakt

**Betreff:** Re: Elephant toy

> Dear Graeme,
>
> Thank you for writing, and I am sorry it is about this. **A beagle managed it.**
> I am not going to argue with you about that, and **your photograph is with your
> message — I have not opened it**, and nothing here depends on it.
>
> **You asked what our next steps are, so here they are without decoration.**
>
> **Mine: none that will satisfy you, and I would rather say so than pretend
> otherwise.** I cannot issue a refund or send a replacement — neither is mine to
> decide. **So I am not going to promise you either, and I am not going to refuse
> you either.** **And there is nowhere to send the toys back to**: we do not
> publish a returns address, and I am not going to invent one. **Please do not
> post anything.**
>
> **What I have done:** your case is in front of the shop owner as you wrote it,
> with our records: **order #3387, two Plushies, £27.95 recorded on the order,
> nothing refunded, ordered 25 July, dispatched 29 July.**
>
> **On "advertised as indestructible".** I have read all twelve of our current
> product descriptions and that word is not in any of them. **That is not me
> telling you that you did not see it** — I cannot see the advertising you were
> shown and I am not going to guess at it. **Your sentence goes to him exactly as
> you wrote it**, because he is the only one who can look at the advertising
> itself.
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **direkte Beantwortung seiner Frage nach den nächsten
Schritten** — einschließlich der offenen Auskunft, dass es von hier aus keine
befriedigenden gibt —, die Weitergabe mit allen Zahlen, die ehrliche Auskunft
zur Werbefrage, und eine Nachfass-Zusage. **Keine Erstattung zugesagt, kein
Ersatz zugesagt, kein Betrag, kein Termin, keine Absage, keine
Vorlagen-Antwort.** **Keine Auswertung des Fotos, keins verlangt.** **Keine
Behauptung, das Wort „indestructible" existiere nicht.** **Keine Rekonstruktion
der Anzeige.** **Keine Rücksendeadresse erfunden.** Kein Eskalationsmarker im
Text.

---

## #7989 — Karen Reynolds (House54@outlook.com.au) — ⛔ **Fehlmenge, beantwortet mit einer Kauschaden-Absage**

**Betreff:** Re: Missing Item.

> Dear Karen,
>
> **You are right to be angry, and the reply you had this morning was wrong on
> its face.** You reported a **missing item**. You were answered about **damage**.
> **Nothing of yours is damaged, you said so plainly, and I am not going to
> pretend that reply made sense.**
>
> **So, your actual case, as you stated it: the hippo arrived, the frog did
> not.**
>
> **What our records show, and I am not going to dress it up:** order #7989 is
> recorded as **two Plushies on one line, both marked fulfilled, on a single
> despatch dated 8 September**. **Our system therefore shows both as sent. You
> say one arrived.** **I am not going to tell you that you miscounted** — you
> opened the parcel and I did not. **What I can say is that our record and your
> parcel do not agree, and that is something only the shop owner can resolve,
> because he can look behind the fulfilment entry and I cannot.**
>
> **It is with him now, stated as a short shipment and not as anything else:**
> **order #7989, two Plushies ordered, one received, A$53.87 recorded on the
> order, nothing refunded, ordered 28 August, despatched 8 September.**
>
> **What I cannot do is decide it** — whether you get the frog sent, or the money
> back for it, is his call and not mine, **so I am not going to promise you
> either.**
>
> **You do not need to send photographs and there is nothing to return.**
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **ausdrückliche Feststellung, dass die Antwort von
09:28 den falschen Fall beantwortet hat**, die **offene Gegenüberstellung von
Datensatz und ihrer Schilderung**, und die Weitergabe **als Fehlmenge**. **Keine
Erstattung zugesagt, keine Nachlieferung zugesagt, kein Betrag, kein Termin,
keine Absage.** **Ihr wird ausdrücklich nicht gesagt, sie habe sich verzählt.**
**Keine Fotobedingung, keine Rücksendeaufforderung.** **Keine Umrechnung** —
53,87 A$ ist der presentment-Betrag. Kein Eskalationsmarker im Text.

---

## #8002 — Thomas Robinson (thomas2788work@gmail.com) — fragt direkt, ob das eine automatische Antwort war

**Betreff:** Re: Plushies

> Dear Thomas,
>
> **You asked whether that was an automated response, and whether you had already
> been sent the same thing. The honest answer to both is yes.** It is a standard
> paragraph, you had already received it, and sending it to you a second time was
> not an answer. **I am not going to send you a third.**
>
> **What your case actually is, in our records:** **order #8002, one Plushies,
> £19.95 recorded on the order, nothing refunded, ordered 28 August, despatched
> 8 September** — **eleven days sitting here before it moved**, which is ours.
>
> **What I can and cannot do.** I cannot issue a refund or send a replacement;
> neither is mine to decide. **So I am not going to promise you either and I am
> not going to refuse you either.** Your case is in front of the shop owner as
> you described it. **And there is nowhere to send anything back to** — we do not
> publish a returns address, and I am not going to invent one.
>
> **You should have had a real answer the first time.** If you have heard nothing
> in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **direkte, bejahende Antwort auf seine Frage**, ob es
sich um eine automatische, bereits gesendete Antwort handelte; die Weitergabe
mit allen Zahlen; die **ungefragte Offenlegung der elf Tage bis zum Versand**;
und eine Nachfass-Zusage. **Keine Erstattung zugesagt, kein Ersatz zugesagt,
kein Betrag, kein Termin, keine dritte Absage.** **Keine Rücksendeadresse
erfunden.** Kein Eskalationsmarker im Text.

---

## #7048 — Jo Carr (jocarr247@yahoo.com) — 40 % angeboten, beruft sich auf „full refund"

**Betreff:** Re: #7048

> Dear Jo,
>
> **You were offered 40 per cent. You did not ask for a percentage, and I am not
> going to argue you down to one.**
>
> **On the wording you are relying on.** You say it states a full refund if you
> are not happy with the products. **You did not take that from nowhere:** a
> **30-day money-back guarantee appears in our own marketing emails, with no
> condition attached to it.** **I am not telling you that settles your case** —
> whether it is applied here is the shop owner's decision and not mine. **But I
> am not going to pretend our own wording says something narrower than it does.**
>
> **What I can and cannot do.** I cannot approve a full refund and I cannot
> approve the 40 per cent either — **neither is mine to decide.** **So I am not
> going to promise you anything, and I am not going to withdraw what you were
> already offered.** Your position goes to him exactly as you put it: **you want
> the full amount, not a percentage.** With it: **order #7048, two Plushies,
> £27.95 recorded on the order, nothing refunded, ordered 21 August, despatched
> 2 September.**
>
> **Please do not post anything back** — we have no returns address I can give
> you.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **Respektierung ihrer Ablehnung des Prozentangebots**,
die **wahrheitsgemäße Bestätigung, dass die Garantieformulierung aus unseren
eigenen Werbemails stammt** — mit ausdrücklichem Hinweis, dass damit nichts
entschieden ist —, und die Weitergabe ihrer Position im Original. **Keine
Erstattung zugesagt, kein Prozentsatz bestätigt oder zurückgenommen, kein
Betrag, kein Termin, keine Absage.** **Kein Versuch, sie zum Prozentangebot zu
überreden.** **Keine Rücksendeadresse erfunden.** Kein Eskalationsmarker im
Text.

---

## #8295 — Ivan Griffen (griffenivan@gmail.com) — fünfte Fassung, Frist 23.09.

**Betreff:** Re: Order #8295

> Dear Ivan,
>
> **Eight minutes. Thank you for telling us, and I am sorry you had to say it to
> a reply that began "Dear Customer" — after three weeks of correspondence with
> us.**
>
> **You have written to us since 6 September and the thing you asked for has
> still not happened.** I am not going to add another holding line to that.
>
> **Where it stands, in our records:** **order #8295, two Plushies, £27.95
> recorded on the order, nothing refunded, ordered 31 August, despatched
> 8 September.** Your case is with the shop owner, with your own words about the
> eight minutes and with the date you set.
>
> **What I cannot do is decide it.** A refund is his call and not mine, **so I am
> not going to promise you one and I am not going to refuse you one.**
>
> **Please do not post anything back** — we have no returns address I can give
> you.
>
> **You set a date of 23 September. He has it, and so does the fact that this is
> your fifth attempt.**
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **Benennung der unpersönlichen Anrede nach drei Wochen
Korrespondenz**, die Weitergabe mit allen Zahlen **und seiner Frist**, und die
offene Feststellung, dass es sein fünfter Anlauf ist. **Keine Erstattung
zugesagt, kein Betrag, kein Termin, keine Absage.** **Keine Wiederholung der
Carrier-Frage**, die am 18.09. bereits richtiggestellt wurde. **Keine
Rücksendeadresse erfunden.** Kein Eskalationsmarker im Text.

---

## #7541 — Lois Hertz (drlhertz@gmail.com) — US, zweite Fassung, benennt den Widerspruch der Bedingung

**Betreff:** Re: 2 days order 7541

> Dear Lois,
>
> **The reply you had this morning was a standard paragraph addressed to "Dear
> Customer". I am not going to defend it, and I am not going to send you
> another.**
>
> **You put your finger on something, and you are owed a straight answer about
> it.** You asked who would want to return an **unopened** product. **That is the
> weakness in the sentence you were sent**, and I am not going to pretend
> otherwise: a guarantee that only applies to items never taken out of the
> packaging cannot be a guarantee about how the toy performs. **Whether that
> condition applies at all is the shop owner's question to answer, not mine** —
> but I am not going to argue it at you.
>
> **And on the advertising**, which you called deceiving: I have read all twelve
> of our current product descriptions. **What I can tell you is what I checked
> and what I cannot see** — I cannot see the advertisements that were put in
> front of you, and I am not going to guess at them. **Your words go to the shop
> owner exactly as you wrote them.**
>
> **What I cannot do is decide your refund.** That is his call and not mine, **so
> I am not going to promise you one and I am not going to refuse you one for a
> second time.** Your case is with him: **order #7541, two Plushies, $38.87
> recorded on the order, nothing refunded, ordered 24 August, despatched
> 3 September.**
>
> **Please do not post anything back** — we have no returns address I can give
> you in any case.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Distanzierung von der Vorlage** samt der
Anrede „Dear Customer", die **ehrliche Anerkennung ihres Einwands** (eine
Garantie, die nur für ungeöffnete Ware gilt, sagt nichts über die Haltbarkeit),
die Auskunft zur Werbefrage, und die Weitergabe mit allen Zahlen. **Keine
Erstattung zugesagt, kein Betrag, kein Termin, keine zweite Absage.** **Keine
Aussage darüber, ob die Bedingung rechtlich haltbar ist** — nur, dass die
Entscheidung beim Owner liegt. **Keine Reaktion auf „conmen"** außer der
kommentarlosen Weitergabe. **Keine Rücksendeadresse erfunden.** **Keine
Umrechnung.** Kein Eskalationsmarker im Text.

---

## #8003 — Michelle Owen (michelle.owen2010@gmail.com) — GB, Erstkontakt

**Betreff:** Re: Refund

> Dear Michelle,
>
> Thank you for writing, and I am sorry it is about this. **An hour.** That is
> not what you paid for, and I am not going to argue with you about it. **Your
> evidence came with your message — I have not opened it**, and nothing here
> depends on it.
>
> **You asked plainly for a refund, so here is a plain answer: I cannot approve
> one.** That decision is the shop owner's, not mine. **So I am not going to
> promise you a refund and I am not going to refuse you one.** Your request is
> already in front of him exactly as you made it, with our records: **order
> #8003, one Plushies, £19.95 recorded on the order, nothing refunded, ordered
> 28 August, despatched 8 September** — **eleven days sitting here before it
> moved at all**, which is ours and which I am not going to explain away.
>
> **There is nothing for you to do.** You do not need to send anything else, and
> **please do not post the toy back** — we have no returns address I can give
> you, and I would rather say that than have you pay postage to nowhere.
>
> **On "the indestructible".** I have read all twelve of our current product
> descriptions and that word is not in any of them. **That is not me telling you
> that you did not see it** — I cannot see the advertising you were shown and I
> am not going to guess at it. **Your wording goes to him as you wrote it.**
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **direkte Antwort auf ihre Erstattungsbitte** (die
Entscheidung liegt nicht beim Bot), die Weitergabe mit allen Zahlen, die
**ungefragte Offenlegung der elf Tage bis zum Versand**, die ehrliche Auskunft
zur Werbefrage, und eine Nachfass-Zusage. **Keine Erstattung zugesagt, kein
Betrag, kein Termin, keine Absage, keine Vorlagen-Antwort.** **Keine Auswertung
des Anhangs, keiner verlangt.** **Keine Behauptung, das Wort existiere nicht.**
**Keine Rücksendeadresse erfunden.** Kein Eskalationsmarker im Text.

---

## #6254 — David Hickman (davehickman71@gmail.com) — ⛔ **zwei ungeöffnete Artikel, weil die Vorlage ihn darauf hingewiesen hat**

**Betreff:** Re: A shipment from order #6254 is on the way

> Dear Dave,
>
> **You have read the reply you were sent this morning carefully and taken it at
> its word, and I am afraid that is exactly where the problem is.**
>
> **Yes — you have two toys still in their packaging, untouched, and you are
> asking the obvious question. I cannot give you the answer it implies.** **We do
> not publish a returns address.** There is none I can give you, and I am not
> going to invent one. **So please do not post anything back yet**, because I
> cannot tell you where it would go.
>
> **I would rather say that plainly than let you parcel them up on the strength
> of a paragraph we sent you.**
>
> **What I have done:** your request is in front of the shop owner, stated as
> what it is — **two unopened, unused items that a customer has asked to return,
> and no route by which to do it.** With it: **order #6254, four Plushies plus
> the digital guide, £44.95 recorded on the order, nothing refunded, ordered
> 15 August, despatched 22 August, two items destroyed, two never opened.**
>
> **Whether you get money back for those two is his decision and not mine**, so
> **I am not going to promise you anything and I am not going to refuse you.**
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Feststellung, dass seine Frage berechtigt ist
und die Antwort darauf nicht existiert** (keine Rücksendeadresse), die
ausdrückliche Bitte, **nichts zu verschicken**, und die Weitergabe des Falls als
**unbenutzte Ware ohne Rücksendeweg**. **Keine Erstattung zugesagt, kein Betrag,
kein Termin, keine Absage.** **Keine Rücksendeadresse erfunden, kein Etikett
zugesagt.** **Keine Wiederholung der Bedingung aus der Vorlage.** Kein
Eskalationsmarker im Text.

---

## #7815 — Angela Stevens (angedave@bigpond.net.au) — AU, zitiert die Website-Versprechen

**Betreff:** Re: Re order 7815

> Dear Angela,
>
> **You quoted our own website back at us, and you were entitled to.** I am not
> going to argue with the contrast you are drawing.
>
> **What I can tell you honestly about that wording:** I have read all twelve of
> our current **product descriptions**, and the passage you quote is not in those
> — **it sits elsewhere on the site.** **I am not suggesting you invented it**;
> I am telling you the limits of what I checked. **Where exactly it appears, and
> whether it should be changed, is the shop owner's question — he is the only one
> who can look at the site as a whole and act on it.** **Your quotation goes to
> him in your words.**
>
> **On your order.** Whether you are refunded is his decision and not mine, **so
> I am not going to promise you a refund and I am not going to refuse you one.**
> It is with him as it stands: **order #7815, one Plushies, A$38.66 recorded on
> the order, nothing refunded, ordered 26 August, despatched 3 September.**
>
> **One thing you are entitled to know because your delivery address is in
> Victoria.** Our published returns policy carries a section headed **"Australia
> – Consumer Guarantees"**, stating that Australian consumer rights **"are not
> limited by the requirement that an item be unused or in its original
> packaging."** **That is our own text. I am not giving you a legal opinion on
> it** — only telling you it is there, because you should not have to find it
> yourself.
>
> **Please do not post anything back** — we have no returns address I can give
> you.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **Bestätigung, dass sie unseren eigenen Website-Text
zitiert**, die **ehrliche Eingrenzung dessen, was geprüft wurde** (zwölf
Produktbeschreibungen — die Passage steht nicht dort, sondern anderswo auf der
Seite), das **wörtliche Zitat der eigenen AU-Passage** ohne Auslegung, und die
Weitergabe mit allen Zahlen. **Keine Erstattung zugesagt, kein Betrag, kein
Termin, keine Absage.** **Keine rechtliche Bewertung.** **Keine Behauptung, die
zitierte Passage existiere nicht oder sei falsch wiedergegeben.** **Keine
Rücksendeadresse erfunden.** **Keine Umrechnung** — 38,66 A$ ist der
presentment-Betrag. Kein Eskalationsmarker im Text.

---

## #3089 — Sue Steer (suesteer@hotmail.com) — ⛔ **nie zugestellt, vier Nachfragen seit dem 06.08., keine einzige Antwort**

**Betreff:** Re: Fluffy toys

> Dear Sue,
>
> **You have written on 6 August, on 22 August, on 7 September and again today,
> and you have not had a single reply from us. Not a slow one — none.** That is
> our failure and I am going to start there rather than with your order.
>
> **What our records show, so that you are not relying on my word.** Order #3089
> was placed on **19 July** and handed over for despatch on **20 July**.
> **There is one despatch on the order and nothing after it.** **No replacement
> has ever been sent, and nothing has been refunded.**
>
> **Two things in our record do not match what you have told us, and I would
> rather set them side by side than quietly pick one.**
>
> - You say you ordered **three** fluffy toys; the order records **two
>   Plushies**. **I am not going to tell you that you misremembered your own
>   order** — I am telling you what our system holds, so that the difference is
>   visible and can be sorted out by someone who can look behind it.
> - You name **Evri**; the carrier recorded against the despatch is a different
>   one. **I cannot reconcile that from here and I am not going to guess.**
>
> **What I am not going to do is send you back to the courier.** You have already
> been to Evri, and they sent you to us. **Chasing a parcel we despatched is not
> your job**, and passing you round again would be the fourth non-answer you have
> had from this address.
>
> **What I can and cannot do.** I cannot send a replacement and I cannot issue a
> refund — neither is mine to do. **So I am not going to promise you either.**
> What I have done is put the case in front of the shop owner stated plainly:
> **order #3089, £27.95, despatched 20 July, marked delivered to a greenhouse the
> customer does not have, never received, four unanswered follow-ups, nothing
> sent, nothing refunded.**
>
> **You said you would still like the items.** That is on the record as what you
> asked for, not as a refund request — **unless you tell me otherwise, in which
> case one line back here is enough.**
>
> If you have heard nothing in a few days, reply here and I will chase it again.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Feststellung, dass vier Nachfragen
unbeantwortet blieben**, die **überprüfbare Wiedergabe des Datenstands** (ein
Versand, kein Ersatz, keine Erstattung), die **sichtbare Gegenüberstellung der
beiden Abweichungen** (drei statt zwei Artikel; anderer Versanddienstleister)
**ohne sie aufzulösen oder gegen sie zu verwenden**, und die Weitergabe mit
ihrem eigentlichen Wunsch (Ware, nicht Geld). **Keine Erstattung zugesagt, kein
Ersatz zugesagt, kein Betrag, kein Termin, keine Absage.** **Ihr wird
ausdrücklich nicht gesagt, sie habe sich in der Menge geirrt.** **Kein Verweis
an den Versanddienstleister** — im Gegenteil, es wird gesagt, dass das nicht
ihre Aufgabe ist. **Keine Aussage darüber, welcher Dienstleister das Paket
hatte.** **Keine Deutung ihrer Meldung als Erstattungsforderung.** Kein
Eskalationsmarker im Text.

---

## #7898 — Tammy Brentlinger (pitbulladvocate@live.com) — US, Erstkontakt, volle Erstattung verlangt

**Betreff:** Re: Dog Toys

> Dear Tammy,
>
> Thank you for writing, and I am sorry it is about this. **Two toys, under an
> hour, and you took the second one away before it went the same way.** That is
> not what you paid for, and I am not going to argue with you about it or ask you
> to prove it.
>
> **Your picture and your PDF arrived with the message. I have not opened
> either**, and nothing here depends on them. **You do not need to send anything
> else.**
>
> **You asked for a full refund, so here is a straight answer: I cannot approve
> one.** That decision belongs to the shop owner, not to me. **So I am not going
> to promise you a refund and I am not going to refuse you one.** Your request is
> in front of him exactly as you made it, with our records: **order #7898, two
> Plushies, $42.61 recorded on the order, nothing refunded, ordered 27 August,
> despatched 3 September, both toys destroyed within an hour, full refund
> requested.**
>
> **On the word you put in quotation marks.** I have read all twelve of our
> current product descriptions and "indestructible" is not in any of them.
> **That is not me telling you that you did not see it** — I cannot see the
> advertising that was put in front of you, and I am not going to guess at it.
> **Your words go to the shop owner as you wrote them**, because he is the only
> person who can look at the advertising itself.
>
> **And please do not post anything back** — we have no returns address I can
> give you, and I would rather say so than have you pay postage to nowhere.
>
> **One last thing.** You added a tip to the order. I am not going to pretend I
> did not notice it; it makes this worse, not better.
>
> If you have heard nothing in a few days, reply here and I will chase it.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **direkte Antwort auf ihre Erstattungsbitte** (die
Entscheidung liegt nicht beim Bot), die Weitergabe mit allen Zahlen, die
ehrliche Auskunft zur Werbefrage, und eine Nachfass-Zusage. **Keine Erstattung
zugesagt, kein Betrag zugesagt, kein Termin, keine Absage, keine
Vorlagen-Antwort.** **Weder das Foto noch das PDF geöffnet**, und das wird ihr
ungefragt gesagt. **Keine Auseinandersetzung mit ihren Preisangaben** („$20 a
piece", „$42 per your regular price") — es wird **nur der auf der Bestellung
verzeichnete Betrag genannt und nichts verrechnet oder richtiggestellt.**
**Keine Behauptung, das Wort „indestructible" existiere nicht.** **Keine
Rekonstruktion der Anzeige.** **Keine Rücksendeadresse erfunden.** Kein
Eskalationsmarker im Text.

---

## #6546 — Vik Jehdian (vjehdian1972@icloud.com) — 🔴 **angenommene 50-%-Erstattung am 09.09. als „processed" bestätigt, in Shopify nicht verzeichnet**

**Betreff:** Re: Refund

> Dear Vik,
>
> **You are right to ask, and the honest answer is not the one you were given.**
>
> **On 9 September this address told you that your 50% refund had been
> processed. I am not going to repeat that sentence to you today, because I
> cannot stand behind it.** Our own records show **no refund paid out on your
> order — not a partial one, not any.** There is nothing there that a bank could
> still be holding up.
>
> **The one limit on what I can see**, said plainly rather than left for you to
> discover: I can only see payments made through our shop system. **If money
> were sent to you some other way, it would not show here.** But nothing in our
> records suggests that happened, and after twelve days of silence on your side
> I am not going to offer you that as a comfortable explanation.
>
> **Where this stands now.** You asked for a full refund on 2 September and
> said clearly you did not want to keep the products. You were offered 30%,
> then 50%, and you accepted the 50% on 5 September and confirmed it again on
> 7 September when you were asked to. **That is a settled agreement on our side,
> not a request still waiting to be judged.** It has gone to the shop owner as
> exactly that: **an accepted offer that was confirmed to you as paid and was
> not paid.**
>
> **What I am not going to do is give you a date.** I cannot issue or release
> money myself, and you have already had one confirmation from us that did not
> hold. **You will not get a second one from me that I cannot keep.**
>
> **You do not need to do anything, and please do not post the items back** —
> we have no returns address I can give you.
>
> If you have heard nothing in a few days, reply here and I will chase it
> again.
>
> Kind regards,
> Lisa
> Paw-Friends Customer Support

⚠️ **Zusage darin:** die **offene Richtigstellung der eigenen Zusage vom
09.09.** („processed") gegen den Datenstand, die **ehrliche Nennung der Grenze**
(außerhalb von Shopify geleistete Zahlungen sind von hier nicht sichtbar) **ohne
sie als Ausrede anzubieten**, die **Einordnung als angenommene, offene
Vereinbarung — nicht als neue Forderung**, und eine Nachfass-Zusage. **Keine
neue Erstattung zugesagt, kein Betrag genannt, kein Termin, keine Absage.**
**Die Zusicherung „processed" wird ausdrücklich nicht wiederholt.** **Keine
Bestellnummer, kein Betrag und kein Bestellinhalt im Text** — er schreibt von
einer anderen Adresse als der auf der Bestellung hinterlegten (siehe Log).
**Keine Rücksendeadresse erfunden.** **Keine Deutung seiner Nachricht.** **Keine
Umrechnung** — der Bestellbetrag ist in US-Dollar verzeichnet. Kein
Eskalationsmarker im Text.
---

### Offene Entwürfe aus den Vortagen, die noch nicht gesendet sind

**Diese Texte stehen im Volltext in `docs/entwuerfe-zum-kopieren.md` und in den
Abendreports der jeweiligen Tage.** Sie werden hier **namentlich**
weitergeführt, damit keiner verlorengeht — der Volltext wird nicht ein zweites
Mal abgedruckt, sondern ist in der Datei nachzulesen.

| Bestellung | Kunde | Entstanden | Abendreport |
|---|---|---|---|
| #7479 | Richard Bellamy-Williams | 20.09. (sechste Fassung) | 20.09. |
| #7828 | Jim Edwards | 20.09. | 20.09. |
| #8221 | Beau Ricketts | 20.09. | 20.09. |
| #5086 | John Mullins | 20.09. | 20.09. |
| #5310 | Heather Taylor | 20.09. | 20.09. |
| #7560 | Samantha Vowles | 20.09. (zweite Fassung) | 20.09. |
| #7440 | Aaron Kell | 20.09. | 20.09. |
| #8053 | Angie Zgonina | 20.09. | 20.09. |
| #7975 | Carl Princehorn | 20.09. | 20.09. |
| #6592 | Andrew Rowlands | 20.09. | 20.09. |
| jscalera1@aol.com | (Bestellung nicht zuzuordnen) | 20.09. | 20.09. |
| #7749 | Adrian Vincent-Janes | 20.09. **nach** dem Report | **in keinem Report** |
| #7884 | Logan Bishop | 20.09. **nach** dem Report | **in keinem Report** |
| #7472 | Francisco Almazan | 20.09. **nach** dem Report | **in keinem Report** |
| #7885 | Rod McNess | 20.09. 21:20 | **in keinem Report** |
| #7771 | Barb Fitzgerald | 19.09. 20:20 | **in keinem Report** |

**Die letzten fünf Zeilen sind in keinem Abendreport im Volltext enthalten**,
weil sie jeweils nach dessen Erstellung entstanden sind. **Ihr Volltext steht in
`docs/entwuerfe-zum-kopieren.md`.**

---

## 3. ⬛ HEUTE ZU ERSTATTEN

**Keiner dieser Fälle ist ein Kauschaden.** Kauschäden stehen hier
grundsätzlich nicht — auch nicht die acht Haltbarkeitsfälle von heute.

### Schriftlich zugesagt — braucht keine neue Entscheidung, nur die Ausführung

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#6546** | **41,55 $** | **Vik Jehdian** | **NEU 21.09.** — 50 % am 05./07.09. von ihm angenommen, am **09.09. schriftlich als „processed" bestätigt**; `totalRefundedSet` **0,00 $**, `refunds` **leer** |
| **#6583** | **30,54 £** | Ken Beville | volle Erstattung am **03.09.** zugesagt, **am 21.09. ein zweites Mal** zugesagt, **nie ausgeführt**; Ware **nie benutzt** |
| **#5148** | **offen** | Trudi Wright | 50 % **zweimal** als „processed" bezeichnet, erstattet **0,00** |
| **#6259** | **offen** | Nick Tarrant | am **19.09.** als ausgeführt gemeldet, in Shopify **keine**; **Trading Standards**, Frist **abgelaufen** |
| **#4998** | **19,95 £** | — | zugesagt, nicht ausgeführt |
| **#4055** | **11,97 £** | Kimberley Shenton | 60 % vom Shop angeboten, von ihr am **17.09.** schriftlich angenommen |
| **#6528** | **22,93 £** | Tommy Johnson | 50 % am **19.09.** angenommen |
| **#6159** | **9,17 £** | Mary Linan | 30 % am **19.09.** angenommen |
| **#6936** | **8,39 £** | — | angenommen, nicht ausgeführt |
| **#7060** | **offen** | — | 30 % angenommen, nie ausgeführt |

### Vor Versand storniert

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#8669** | **38,19 $** | Chad Lovell | **elf Minuten nach der Bestellung storniert** (19.09.), **nicht ausgeführt**; Stornofenster **weiterhin offen** |

### Nie angekommen / Ersatz nie versandt

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#2894** | **19,95 £** | **Jeff Hughes** | **defekt angekommen 23.07.**, Ersatz am **24.07. schriftlich zugesagt**, **nie versandt**, **acht Nachfassungen**, 46 Tage Funkstille |
| **#3089** | **27,95 £** | **Sue Steer** | **nie zugestellt** seit 28.07., **vier Nachfassungen**, **null Antworten** |
| **#5036** | **27,95 £** | Lynette Lumley | nie erhalten, Erstattungsbitte seit **07.09.** unbeantwortet |
| **#5905** | **27,95 £** | Kate Stephens | nicht erhalten seit **01.09.**, zugesagte Rückmeldung ausgeblieben |
| **#8295** | **27,95 £** | Ivan Griffen | nicht erhalten, **fünf Kontakte**, **Frist 23.09.** — *die Zeile beruht auf der Nichtlieferung, nicht auf seiner heutigen Haltbarkeitsmeldung* |
| **#7459** | **19,95 £** | Sarah Taylor | nicht erhalten, elf Tage Liegezeit vor Versand |
| **#4604** | **28,51 £** | Nicholas Kloepfer | **an die falsche Adresse versandt**, nachdem er sie gemeldet hatte |
| **#8081** | **20,35 £** | Matthew Pierce | APO-Adresse, Bestellung liegt seit **21 Tagen** |
| **#7970** | **offen** | Melissa Harris | nicht erhalten; **48,46 $ gegen 35,65 £ — Betrag ungeklärt, nicht umgerechnet** |

### Unbenutzte Ware — erfüllt die veröffentlichte Garantie, kein Rückgabeweg vorhanden

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#6254** | **offen** | **David Hickman** | **NEU 21.09.** — **zwei von vier Artikeln ungeöffnet**; **der Rückgabewunsch wurde durch unsere eigene Absage ausgelöst** |
| **#7479** | **14,98 £** | Richard Bellamy-Williams | ungeöffnet, **in der Frist gemeldet**; Frist **21.09. abgelaufen** |
| **#7347** | **14,98 £** | Jill Hibbs | unbenutzt, dem Hund nie gegeben |
| **#7048** | **27,95 £** | Jo Carr | **ungeöffnet**, Rückgabe seit **15.09.** erbeten; 40 % abgelehnt |
| **#4812** | **offen** | Carolyn Marmalejo | alles außer einem Stück ungeöffnet, **fünfmal** nach der Adresse gefragt |
| **#7555** | **34,95 £** | Steve Kerr | **zwei von drei Stücken unbenutzt** |
| **#8312** | **27,95 £** | Paul Beaver | ein Stück ungeöffnet, Rückgabe von sich aus angeboten |
| **#8372** | **71,56 £** | Kerri Forbey | unbenutzt, Originalverpackung |
| **#7119** | **28,50 £** | Susan McGee | ein Stück unberührt, **AU** |

### Fehlmenge

| Bestellung | Betrag | Kunde | Grund |
|---|---|---|---|
| **#7989** | **offen** | Karen Reynolds | **bezahlt für 2, erhalten 1**; Variante am 29.08. zugesagt, nie umgesetzt; **heute erneut mit einer Kauschaden-Absage beantwortet** |

### Summe

**Summe der bezifferten Beträge in GBP: 524,38 £.**
(102,95 £ zugesagt · 200,56 £ nie angekommen · 220,87 £ unbenutzt)
**Zusätzlich in USD, nicht umgerechnet: 41,55 $ (#6546) und 38,19 $ (#8669).**

**Sieben Positionen sind nicht beziffert** (#5148, #6259, #7060, #7970, #6254,
#4812, #7989), weil der Anteil je
Position aus den **Kaching-Bundle-Preisen nicht errechenbar** ist — die
Listenpreise summieren sich nicht auf den gezahlten Gesamtbetrag. **Diese
Anteile müssen im Shopify-Admin bestimmt werden; hier wird nichts geschätzt.**
Bei **#7970** ist zusätzlich ungeklärt, ob USD oder GBP maßgeblich ist.
**Es wird nichts zwischen Währungen umgerechnet.**

### Nicht hier aufgeführt, aber zu beobachten

**Vier Sendungen stehen still** (`updatedAt == createdAt`, seit dem Versand
keine Aktualisierung): **#8080** (Texas), **#6002** (Florida), **#8221** (NSW)
und **#6546** (Kalifornien, seit dem 22.08.). **Das ist noch keine
Nichtlieferung** und steht deshalb nicht in der Erstattungsliste — aber es ist
derselbe Weg dorthin, den #5036, #5905 und #8081 gegangen sind.

**Fünf Bestellungen haben eine unausgelieferte E-Book-Position:** #8372, #7555,
#6592, #6254, #6546.

---

## Was heute NICHT in diesen Entwürfen steht

- **Keine Erstattungszusage und keine Ersatzzusage**, in keinem einzigen Text.
- **Keine Absage** — auch nicht dort, wo der Fall nicht unter die
  Erstattungsregel fällt.
- **Keine Wiederholung der Zusicherung „processed"** (#6546, #6583). Der
  Datenstand wird offen dagegengestellt.
- **Keine Behauptung, es habe nie eine Erstattungszusage gegeben** (#7041) — nur,
  dass keine auffindbar ist.
- **Keine Rücksendeadresse.** Es gibt keine. Wo Kunden zurücksenden wollen,
  werden sie ausdrücklich gebeten, nichts zu verschicken (#6254, #7815, #7898).
- **Keine Kauschaden-Vorlage**, in keinem Entwurf dieses Tages.
- **Keine rechtliche Bewertung**, in keine Richtung — weder zum Consumer Rights
  Act (#6384) noch zum australischen Verbraucherrecht (#7815).
- **Kein Versuch, einen Kunden von einer Bewertung, einem Chargeback, Klarna
  oder Trading Standards abzubringen** (#6804, #6384).
- **Keine Bitte, eine öffentliche Bewertung zu ändern oder zu löschen** (#6804),
  und keine Erstattung, die davon abhängig gemacht wird.
- **Keine Aussage zur Materialsicherheit**, in keine Richtung (#8406).
- **Die frühere Sicherheitsmeldung von #8406 wird nicht ungefragt wieder
  aufgegriffen** — sie hat sie heute nicht erwähnt.
- **Keine Auswertung von Fotos, Videos oder PDF-Anhängen.** Alle Anhänge blieben
  ungeöffnet (#3387, #8003, #7898); dass sie ungeöffnet blieben, wird den Kunden
  gesagt.
- **Keine Rekonstruktion, welche Anzeige ein Kunde gesehen hat.**
- **Keine Behauptung, ein zitierter Satz existiere nicht** (#6804, #7898, #7815)
  — gesagt wird, **was geprüft wurde und was nicht prüfbar ist.**
- **Keine Deutung einer Meldung als Erstattungsforderung**, wo der Kunde keine
  gestellt hat (#8171).
- **Keine Bestelldaten an eine Adresse, die an der Bestellung nicht hinterlegt
  ist** (#6546 — weder Bestellnummer noch Betrag noch Inhalt im Text).
- **Keine Richtigstellung einer Kundenangabe gegen den Datenstand** (#3089,
  #7989) — beides wird nebeneinandergestellt und weitergegeben.
- **Keine Währungsumrechnung.** Genannt wird jeweils der Betrag, der auf der
  Bestellung selbst steht.
- **Kein Verweis an einen Versanddienstleister** (#3089).
- **Kein Eskalationsmarker im Text.** Die Eskalationsgründe stehen ausschließlich
  im Tagesprotokoll.
