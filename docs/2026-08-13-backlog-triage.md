# Backlog triage — 2026-08-13

## Ausgangslage

Der Posteingang enthielt beim Start dieses Laufs **201 ungelesene, unbearbeitete
Threads**. Vom 08.08. bis 12.08. wurde nichts protokolliert (Routine feuerte,
Session nicht erreichbar). Dieser Lauf arbeitet den Rückstand nach Priorität ab,
nicht chronologisch: zuerst die Fälle, bei denen noch Geld zu retten ist, dann
die Eskalationen.

**Batch 1 dieses Laufs: 21 Fälle bearbeitet.** Der Rest des Rückstands ist noch
offen und wird in weiteren Batches abgearbeitet.

---

## Zwei strukturelle Befunde, die den Rückstand verursachen

### 1. Es gibt keine Rücksendeadresse

Im Fall Sharon Alberio (#1240) ist am 17.07. eine Mail an die Kundin
herausgegangen, die wörtlich den Platzhalter enthielt:

> Paw Friends Returns
> [RETURN ADDRESS – PLEASE ADD]

Sie hat seit dem 20.07. dreimal nach der Adresse gefragt und sie bis heute nicht
bekommen. Auch `get-shop-info` liefert keine Rücksendeadresse; der einzige
hinterlegte Standort ist "Kirchstr. 2", die Fulfillment-Location des Lieferanten.

**Konsequenz:** Jeder Fall vom Typ "unbenutzt, will zurückschicken" ist derzeit
nicht abschließbar. Das betrifft heute Sharon Alberio (#1240) und Dave Reid
(#3474) und wird jeden weiteren Rückgabefall betreffen. Der Bot erfindet keine
Adresse — solange keine existiert, kann er Kunden nur ehrlich vertrösten, und
genau daraus entstehen die Eskalationen.

→ **Owner-Entscheidung nötig:** entweder eine echte Rücksendeadresse festlegen,
oder Rückgabefälle ohne Rücksendung erstatten. Beides ist vertretbar, keine
Entscheidung ist es nicht.

### 2. Erstattung ohne Storno lässt die Bestellung trotzdem rausgehen

Bereits bei #4617 dokumentiert (erstattet **und** versandt). Heute ein zweiter
Fall desselben Musters: **#3944 Katharine Swann** — Storno und Erstattung am
31.07. zugesagt, Bestellung am 02.08. trotzdem versandt (`UL383805642YP`),
Status weiterhin `PAID`, keine Erstattung erfolgt. Ware raus, Geld nicht zurück,
Kundin zu Recht verärgert.

→ Bei jedem Vorab-Storno muss die Bestellung in Shopify **zusätzlich storniert**
werden, nicht nur erstattet.

---

## Batch A — vor Versand, Geld noch zu retten (`Bot/Needs Approval`)

Alle Bestellungen unten wurden vor dem Entwurf in Shopify geprüft und sind zum
Zeitpunkt dieses Laufs **UNFULFILLED**.

| Kunde | Bestellung | Betrag | Fall | Auszuführen |
|---|---|---|---|---|
| Jamey Englert | #4821 | 28,50 £ | Storno vor Versand | Stornieren + voll erstatten |
| Andrew Sirrell | #5634 | 27,95 £ | Storno vor Versand | Stornieren + voll erstatten |
| Tammy Bryson | #5592 | 20,35 £ | Storno vor Versand | Stornieren + voll erstatten |
| Margo & Larry McGinnis (ptfcscott@gmail.com) | #5078 | 27,95 £ | Storno vor Versand, verärgert über geänderte Lieferzeit | Stornieren + voll erstatten |
| Patti Morin | #4767 | 20,34 £ | Produktverwechslung, nie versandt | Nach Bestätigung stornieren + erstatten |
| Anthony Ferrari | #5896 | 44,07 £ | Falsche Adresse, 2 Min nach Bestellung gemeldet | Adresse ändern vor Versand |
| amy jo stevenson | #4926 | 56,08 £ | Adressänderung seit 07.08. offen, neue Adresse unvollständig | Nicht versenden, bis vollständige Adresse vorliegt |
| Deborah Calnan | #5556 | 20,34 £ | Artikel stimmt nicht (Fuchs statt Esel) | Nach Bestätigung tauschen oder erstatten |
| Dave Reid | #3474 | 27,95 £ | Ungeöffnete Rückgabe, dritte Anfrage | Erstattung fällig — Rücksendeadresse fehlt |

**Erstattungssumme Batch A, sofort ausführbar: 124,75 £** (#4821, #5634, #5592,
#5078). Dazu bedingt: #4767 (20,34 £), #5556 (20,34 £), #3474 (27,95 £).

### Entwürfe im Volltext

**Entwurf an Jamey Englert (jameyenglert@gmail.com) — Betreff: Re: Cancel order**

> Hi Jamey,
>
> Thanks for getting in touch, and that's absolutely fine.
>
> I've checked order #4821 and it hasn't been dispatched, so there's nothing standing in the way of cancelling it. The cancellation and a full refund of £28.50 are being processed back to the payment method you used — it'll show on your statement once your bank has released it.
>
> I'm sorry we hadn't got it on its way to you sooner, and thanks for telling us rather than just waiting.
>
> If anything looks wrong when the refund comes through, reply here and I'll chase it up.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Storno und volle Erstattung von 28,50 £.

**Entwurf an Andrew Sirrell (rhasbills@gmail.com) — Betreff: Re: Cancel Order #5634 confirmed**

> Hi Andrew,
>
> Thanks for letting me know — that's no trouble at all.
>
> Order #5634 is still with us and hasn't been dispatched, so I can cancel it cleanly. The full £27.95 is being refunded to the card you paid with, and it'll appear on your statement once your bank has processed it.
>
> Sorry it wasn't already on its way to you. If you decide you'd like the donkey and fox another time, they're both still available.
>
> Any questions, just reply here.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Storno und volle Erstattung von 27,95 £.

**Entwurf an Tammy Bryson (tammy.bryson68@gmail.com) — Betreff: Re: Order #5592 confirmed**

> Hi Tammy,
>
> Of course — consider it done.
>
> Order #5592 hasn't been dispatched yet, so the cancellation goes through without any complications. The full £20.35 is being refunded to your original payment method and will show up once your bank has processed it.
>
> There's nothing further you need to do at your end.
>
> If you'd like to order again at any point, just let me know and I'll help.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Storno und volle Erstattung von 20,35 £.

**Entwurf an ptfcscott@gmail.com (#5078) — Betreff: Re: Cancel My Order**

> Hello,
>
> You're right to be annoyed, and I'm not going to try to talk you round. Being given one delivery estimate before ordering and a longer one afterwards is a fair thing to be cross about.
>
> Order #5078 hasn't been dispatched, so I can cancel it. The full £27.95 is being refunded to the card you paid with and will show on your statement once your bank has released it.
>
> I've passed the point about the two different delivery estimates on internally, because that's the part that needs fixing rather than apologising for.
>
> If the refund doesn't appear, reply here and I'll chase it.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Storno und volle Erstattung von 27,95 £; interne Weitergabe
> der Beschwerde über die widersprüchlichen Lieferzeitangaben.
>
> *Hinweis: Die Bestellung läuft in Shopify auf "Margo & Larry McGinnis", die
> Mail kommt von ptfcscott@gmail.com. Deshalb keine namentliche Anrede.*

**Entwurf an Patti Morin (yakotsanit@gmail.com) — Betreff: Re: Order #4767 confirmed**

> Hi Patti,
>
> Thanks for writing in — though I think something may have got crossed here, and I'd rather check with you than guess.
>
> Order #4767 with us is a single Paw-Friends plushie (the frog), which is a soft toy for dogs rather than anything that goes on a car. It also hasn't been dispatched yet, so nothing has actually been sent out to you.
>
> If that isn't what you meant to buy, just say so and I'll cancel it and refund the full £20.34 — it's early enough to do that cleanly. And if you were expecting something else altogether, it may well have come from a different shop, in which case I'm happy to help you work out where to look.
>
> Let me know which it is and I'll sort it from there.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Storno und volle Erstattung von 20,34 £ — **bedingt**, erst
> nach ihrer Bestätigung.

**Entwurf an Anthony Ferrari (kestral30@gmail.com) — Betreff: Re: Order #5896 confirmed**

> Hi Anthony,
>
> Thanks for catching that so quickly — that timing helps a lot.
>
> Order #5896 is still with us and hasn't been dispatched, so the address can be corrected before it goes anywhere. We currently have 4816 295th Street on the order, and I'm having it changed to:
>
> 2338 114th St
> Toledo, OH 43611
>
> Could you confirm that's right exactly as written? Once you do, it's locked in and the order will ship to that address rather than the original one.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Adressänderung wird vor Versand in Shopify eingetragen.
> **Muss tatsächlich ausgeführt werden** — genau diese Zusage blieb bei #4604
> und #4926 unerfüllt.

**Entwurf an amy jo stevenson (ajstevenson@frontier.com) — Betreff: Re: Order #4926 confirmed**

> Hi Amy Jo,
>
> I need to come back to you on this, because my last reply wasn't the full picture and I'd rather correct it than leave it.
>
> I told you the address correction had been passed on. The order hasn't shipped — that part is still true, order #4926 is with us and nothing has gone out — but the address on it is still the original one:
>
> 2235 Wisconsin Avenue
> New Holstein, WI 53061
>
> The reason it hasn't been changed is that "N2660 Hayton Road" on its own isn't enough for the courier to deliver to. I don't have a town or ZIP code for it, and I wasn't willing to guess and have your parcel end up somewhere it can't be found.
>
> Could you send me the full address including town and ZIP? As soon as I have it the order will be updated, and it won't ship until that's done.
>
> Sorry for the back and forth on this one.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Die Bestellung wird nicht versandt, bis die vollständige
> Adresse vorliegt. Das ist eine harte Zusage — #4926 darf bis dahin **nicht**
> in die Fulfillment-Automatik laufen.

**Entwurf an Deborah Calnan (deborah.calnan@gmail.com) — Betreff: Re: Order #5556 confirmed**

> Hi Deborah,
>
> Thanks for flagging this before it goes out.
>
> Order #5556 shows one item on it — a fox plushie, £20.34 — and nothing else. It hasn't been dispatched yet, so there's still time to change it.
>
> If it's the donkey you meant to order, say the word and I'll have it swapped over before it ships. If you'd rather not go ahead at all now, I can cancel it and refund the full £20.34 instead. Either is straightforward at this stage.
>
> Just let me know which you'd prefer and I'll take care of it.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Artikeltausch **oder** Storno mit voller Erstattung von
> 20,34 £ — bedingt, erst nach ihrer Wahl.

**Entwurf an Dave Reid (davereid.bds@icloud.com) — Betreff: Re: Order #3474**

> Hi Dave,
>
> You've had to ask three times for this and that isn't good enough. I'm sorry.
>
> To answer it plainly: yes, an unopened return is covered. Our 30-day money-back guarantee is there so you have time to be sure the product is right for your dog — it covers items that arrive faulty and items returned unused within 30 days. Order #3474 arrived on 10 August, the items are unopened, so a full refund of £27.95 is due to you.
>
> The one thing I won't do is give you a return address off the top of my head and risk the parcel going to the wrong place. I'm getting the correct returns details confirmed and will send them to you in this thread today — you'll hear back from me either way, you won't have to chase a fourth time.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Erstattung von 27,95 £ ist zugesagt, **und** die
> Rücksendeadresse wird ihm am selben Tag in diesem Thread geschickt. Ohne
> existierende Rücksendeadresse ist die zweite Zusage nicht haltbar — siehe
> Befund 1 oben. **Vor dem Absenden entscheiden.**

---

## Batch B — Eskalationen (`Bot/Escalated - Owner Attention`)

Die Entwürfe unten enthalten **keine** internen Markierungen und sind so, wie
sie dastehen, absendbar. Der Eskalationsgrund steht jeweils darüber und ist
nur für dich — er geht nicht an den Kunden (siehe support-policy.md,
„Escalation": am 09.08. ging so eine Notiz versehentlich an Lynn Franks raus).

| Kunde | Bestellung | Trigger |
|---|---|---|
| Sharon Alberio | #1240, 24,95 £ | 5. Mail seit 25.06.; Rückgabe am 17.07. bewilligt, Platzhalter-Adresse verschickt |
| Scott Hawkins | #2189, 19,95 £ | Erstattung am 17.07. zugesagt, nie ausgeführt |
| Katharine Swann | #3944, 19,95 £ | Storno zugesagt, Bestellung trotzdem versandt |
| David Kiff | #3715, 27,95 £ | Zitiert Werbetext wörtlich, wirft Falschwerbung vor, 4. Kontakt |
| Maria Graeble | #3778, 19,95 £ | Zitiert „indestructible toy", 2. Mail |
| Ellen Rosey | #4071 | Zitiert „no dog has ever destroyed your furry animals!" |
| John McNamara | #3324 | Werbeaussage ausdrücklich bestritten, Fotos |
| kstarbird63@gmail.com | — | Zitiert „indestructible" + „fully guaranteed", 2. Mail |
| Lianne Simpson | #3858 | Werbung ausdrücklich als irreführend bezeichnet |
| Michael Green | #3486 | 3. Kontakt, Fall liegt bereits beim Owner |
| Pete Glister | — | Kündigt öffentliche Bewertung binnen 48 h an |

**Offene Erstattungszusagen aus früheren Antworten, die noch nicht bezahlt sind:
#1240 (24,95 £), #2189 (19,95 £), #3944 (19,95 £) — zusammen 64,85 £.**
Das sind keine neuen Entscheidungen, sondern bereits gegebene Versprechen.

### Entwürfe im Volltext

**Entwurf an Sharon Alberio (pinkpookie16@gmail.com) — Betreff: Re: Refund – Order 1240**

**Eskalationsgrund:** Fünfte Mail seit dem 25.06. Die Rückgabe wurde am 17.07. ausdrücklich bewilligt (unbenutzt, Originalverpackung) — aber die Antwort an die Kundin enthielt wörtlich den Platzhalter „[RETURN ADDRESS – PLEASE ADD]" statt einer Adresse. Seit sieben Wochen wurde keine Rücksendeadresse geliefert. Bestellung #1240 (bestellt unter neonpinkgorilla@yahoo.co.uk), 24,95 £, Status weiterhin PAID.

> Hi Sharon,
>
> You're not being ignored, though I understand completely why it looks that way from your side. I'm sorry.
>
> Let me set out plainly where this stands. On 17 July you were told the toys qualify for a return because they're unused and still in their original packaging. That decision stands — it hasn't changed and isn't in question. What went wrong is that the email you were sent had a blank space where the return address should have been, and in the weeks since, nobody has given you the address you've now asked for three times.
>
> That's ours to fix, not yours to keep chasing. I've handed it to the owner of the business today so the address is confirmed and your refund is dealt with properly, rather than passing you round the houses again.
>
> I'm sorry it has taken this long to get you a straight answer.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Der Owner kümmert sich; die Rückgabeberechtigung wird
> bestätigt (war bereits am 17.07. zugesagt). Kein neues Datum versprochen.

**Entwurf an Scott Hawkins (scotthechef@googlemail.com) — Betreff: Re: Dog destroyed toy**

**Eskalationsgrund:** Am 17.07. wurde eine Erstattung zugesagt („Resolutions Team"), seither ist nichts passiert. Bestellung #2189, 19,95 £, geliefert, weiterhin PAID. Offene Zusage — Betrag steht aus.

> Hi Scott,
>
> No, you haven't received it — I've checked rather than guessed.
>
> On 17 July you were told your details had gone to our resolutions team and that a refund would follow. Nothing happened after that, and almost four weeks have passed. That's a failure at our end, not a delay at your bank.
>
> I've put this in front of the owner of the business today with your order number and the amount so it can be paid, and I'll come back to you in this thread once it has been.
>
> I'm sorry it took you asking again to get a straight answer.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Der Fall geht heute an den Owner, und Scott bekommt eine
> Rückmeldung in diesem Thread, sobald bezahlt wurde. Der Entwurf verspricht
> die Erstattung nicht neu — sie wurde am 17.07. bereits zugesagt.

**Entwurf an Katharine Swann (swanny1412@gmail.com) — Betreff: Re: Cancel order**

**Eskalationsgrund:** Storno und Erstattung wurden am 31.07. zugesagt, Bestellung #3944 wurde trotzdem am 02.08. versandt (Tracking UL383805642YP). 19,95 £, Status weiterhin PAID, keine Erstattung erfolgt. Gleiches Muster wie #4617.

> Hi Katharine,
>
> You're right on both counts — the mix-up was ours, and the refund was promised to you before any of this happened.
>
> I can see what went wrong. The cancellation was agreed on 31 July, but the order was still dispatched on 2 August, which is why you received a shipping notification for something you'd already cancelled. That's a fault in our process, and you did nothing to cause it.
>
> Because the refund was already promised, I'm not going to reopen the question. I've put it in front of the owner of the business today with the order number and amount so it can be actioned, and I'll come back to you here once it has been.
>
> Sorry for the run-around.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** Die am 31.07. zugesagte Erstattung von 19,95 £ wird
> eingehalten; Rückmeldung im Thread nach Ausführung. **Achtung:** Die Ware ist
> bereits bei ihr — der Owner muss entscheiden, ob erstattet wird, ohne die Ware
> zurückzufordern. Der Entwurf setzt voraus, dass ja (weil bereits zugesagt).

**Entwurf an David Kiff (davidkiff@thekiffs.net) — Betreff: Re: Order 3715**

**Eskalationsgrund:** Kunde wirft ausdrücklich Falschwerbung vor und zitiert die Anzeige wörtlich („our plushies are made for dogs that destroy everything. 40000 owners. Not one dog got through"). Vierter Kontakt, zweimal ohne Antwort nachgefasst. Bestellung #3715, 27,95 £, geliefert.

> Hi David,
>
> Thanks for chasing, and I'm sorry you've had to do it twice.
>
> You've made a specific allegation about our advertising and quoted the wording back to us. That isn't something I'm going to answer with the standard policy reply, and honestly it isn't mine to answer — I've passed it to the owner of the business to deal with directly.
>
> I'd rather tell you plainly that it's with the owner than send you another response that doesn't address the point you actually raised.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** keine — nur die Weitergabe an den Owner.

**Entwurf an Maria Graeble (mariagraeble@gmail.com) — Betreff: Re: Order 3778**

**Eskalationsgrund:** Kundin zitiert ausdrücklich die Werbeaussage „indestructible toy" und beruft sich auf die 30-Tage-Rückgabe. Zweite Mail, die erste blieb unbeantwortet. Bestellung #3778, 19,95 £, geliefert.

> Hi Maria,
>
> Thank you for following up, and I'm sorry your first email went unanswered — that shouldn't have happened.
>
> There are two things in what you've written: the state the fox was in after ten minutes, and the way the product was described to you before you bought it. The second one I don't want to answer with a stock line, so I've passed your email to the owner of the business to look at directly.
>
> You'll get a proper answer rather than a form reply. Thank you for bearing with me in the meantime.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** keine — nur die Weitergabe an den Owner.

**Entwurf an Ellen Rosey (ellenrosey@aol.com) — Betreff: Re: A shipment from order #4071 is on the way**

**Eskalationsgrund:** Kundin zitiert die Werbeaussage wörtlich („no dog has ever destroyed your furry animals!") und widerlegt sie am eigenen Fall. Bestellung #4071.

> Hi Ellen,
>
> Thank you for writing, and I'm sorry — ten minutes is not what you were led to expect.
>
> You've quoted a specific claim from our advertising back to us, and that's the part I don't want to answer with a standard policy reply. It's gone to the owner of the business, who is the right person to respond to it.
>
> You'll hear back properly rather than with a form letter.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** keine — nur die Weitergabe an den Owner.

**Entwurf an John McNamara (jmcnamara05@gmail.com) — Betreff: Re: Order #3324**

**Eskalationsgrund:** Kunde stellt die Werbeaussage zur Unzerstörbarkeit ausdrücklich in Frage (Betreffzeile „Absolutely non indestructible"), Fotos angehängt. Bestellung #3324.

> Hi John,
>
> Thanks for the photos, and I'm sorry the monkey didn't last the morning.
>
> Your email is as much about how the product was advertised as it is about the toy itself, and that's not something I'm going to answer with the standard reply. I've passed it to the owner of the business to respond to directly.
>
> You'll get a proper answer on both parts of it.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** keine — nur die Weitergabe an den Owner.

**Entwurf an kstarbird63@gmail.com — Betreff: Re: Return**

**Eskalationsgrund:** Kunde beruft sich ausdrücklich auf die Werbeaussage „indestructible" und auf die Angabe „fully guaranteed" auf der Website. Zweite Mail, die erste blieb unbeantwortet. Keine Bestellnummer genannt — vor der Antwort zuordnen.

> Hello,
>
> Thank you for coming back to me, and I'm sorry your first email didn't get a reply.
>
> You've raised two things directly: what the advertising said, and what the site says about the guarantee. Those aren't questions I'm going to answer with a stock response, so I've passed your email to the owner of the business to deal with.
>
> You'll get a straight answer rather than another silence.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** keine — nur die Weitergabe an den Owner.

**Entwurf an Lianne Simpson (lianne-simpson@hotmail.co.uk) — Betreff: Re: Order 3858**

**Eskalationsgrund:** Kundin bezeichnet die Werbung ausdrücklich als irreführend („Should not be advertised in the way you are. Very misleading"). Bestellung #3858.

> Hi Lianne,
>
> Thanks for writing, and I'm sorry it didn't last.
>
> You've said clearly that you think the way this is advertised is misleading. That's a fair point to put to us and it deserves an answer from the business rather than a policy line from me, so I've passed it to the owner to respond to.
>
> You'll hear back properly.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** keine — nur die Weitergabe an den Owner.

**Entwurf an Michael Green (groca69@googlemail.com) — Betreff: Re: not as advertised**

**Eskalationsgrund:** Dritter Kontakt desselben Kunden, Fall #3486 liegt bereits beim Owner. Kunde leitet seine Mail erneut weiter, weil er keine Antwort erhalten hat.

> Hi Michael,
>
> You've forwarded this because you haven't heard back, and that's fair — I'm sorry.
>
> Your case is already with the owner of the business rather than sitting in the general queue, and I've flagged today that you've had to chase it again. I'm not going to send you another interim reply that says nothing; the answer needs to come from the owner directly.
>
> Thank you for your patience with it.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** keine — nur der Hinweis, dass der Fall beim Owner liegt.

**Entwurf an Pete Glister (peteglister@gmail.com) — Betreff: Re: Arrived today**

**Eskalationsgrund:** Kunde kündigt an, innerhalb von 48 Stunden öffentlich über die Produktqualität zu kommentieren. Foto angehängt. Keine Bestellnummer genannt — vor der Antwort zuordnen.

> Hi Pete,
>
> Thanks for sending the photo — I can see exactly what you mean, and less than two hours is nowhere near good enough.
>
> Rather than send you the standard reply, I've passed this to the owner of the business along with your picture so it gets looked at properly.
>
> I'm not going to promise you an outcome I can't stand behind, but you will get a real answer rather than a brush-off.
>
> Lisa
> Paw-Friends UK
>
> **Zusage darin:** keine — nur die Weitergabe an den Owner.

---

## Noch offen aus diesem Rückstand

Der Posteingang enthält weiterhin rund 180 unbearbeitete Threads. Grob nach
Kategorie, aus den Betreffzeilen und Snippets des ersten Suchlaufs:

- **Kauschäden ohne Werbebezug** (Routineantwort, `Bot/Draft Ready`): u. a.
  Denise Longhurst, deedeeann58, Katherine Keat #4130, Michele Moore,
  McManus #4125, Lee Loizou #4098, Denise Frohling #4138, G. Zalarick #3959,
  Steve Whitman #3002, Steph Murdoch #3803, mlguisti #4493, Mandy Miller #4272,
  Tom Benham, V. Sinesi, Ray Lewis #3429 (bereits beantwortet)
- **Lieferstatus / Verzug**: Debbie Edmonds, Tina Goodhart #4296, ibstock #3318,
  thumb960 #4462, countrygal2473 #4792, Terry M #3963 (inzwischen „Received"),
  Thomas Davis #4136, kirtlandk607, nemeta1981 #3870 (Evri, seit Tagen „out for
  delivery"), Angel #4957
- **Spam / kein Support-Fall**: shopify.globalteamservice@gmail.com

Diese Liste ist aus Snippets erstellt und **nicht** verifiziert — jeder Fall wird
vor der Antwort einzeln in Shopify geprüft.

## Nicht getan

- Keine Shopify-Erstattung oder -Stornierung durch den Bot ausgeführt. Der
  Connector blockiert `refundCreate` und `orderCancel` mit
  `category: "financial"`. Alle Beträge oben sind manuell auszuführen.
- Keine Mail versendet. Es gibt keine Send-Funktion; alle Texte oben liegen als
  Entwürfe im Postfach `support.pawfriends.uk@gmail.com` und gehen beim Senden
  von dieser Adresse raus.
- Keine Rücksendeadresse erfunden.
- Tor Vatne (#4617) nicht kontaktiert — Owner-Entscheid vom 12.08.
