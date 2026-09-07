# Backlog-Triage 2026-09-07

Stündliche Läufe 01:17, 02:17, 03:17 UTC: nichts Neues. Um **04:17 UTC** ist ein
Fall aufgetaucht, der im Sweep vom 06.09. nicht in den ersten 25 Treffern war
(43 geschätzt) — er ist also nicht neu eingegangen, sondern neu sichtbar.

Der Gmail-Schreibpfad bricht weiterhin ab. Keine Entwürfe, keine Labels, kein
Text rekonstruiert.

---

## #6259 — Nick Tarrant (nick.tarrant@me.com) — „replacement guarantee", jetzt auf der **Website**

- **03.09. 06:22:** zwei Plushies, „In 5 mins, my female greyhound had torn off
  an ear and exposed the stuffing. I'd like to request a refund as these are
  meant to be…"
- **04.09. 13:17 aus dem Postfach:** Vorlagen-Absage („the toy was damaged after
  your dog used it … given the durability claims")
- **05.09. 14:48 Kunde, sachlich und ohne Eskalationston:**

  > „Hi Lisa, Thanks for your reply. **Your website mentions 'With replacement
  > guarantee'.** I'm keen to hear what this means?"

**Das ist der wichtige Teil.** Bisher war der Befund: die Absolutaussagen stehen
in den **Anzeigen**, die Shopify-Produktseite ist zurückhaltend formuliert
(„reinforced double stitching **to help prevent** tearing"). Nick Tarrant nennt
die **Website** als Quelle für „With replacement guarantee" — nicht eine Anzeige.

Wenn das stimmt, verspricht der Shop selbst eine Ersatzgarantie, die in
`support-policy.md` nicht vorkommt. Der Bot kann diese Frage nicht beantworten,
ohne entweder etwas zu erfinden oder eine beworbene Zusage abzustreiten.

**Eskalationsgrund:** Zweiter Kontakt, ausdrücklich bestrittene bzw. eingeforderte
Werbeaussage, dazu eine Vorlagen-Absage, die die gestellte Frage nicht berührt.
→ `Bot/Escalated - Owner Attention`.

### Damit sind es drei Kunden zu derselben Lücke

| Kunde | Seit | Was er will |
|---|---|---|
| **Adam Sellens** (adamsellens@aol.com) | 14.08., Werbung als Beleg mitgeschickt | Ersatzlieferung; am 15.08. „an unser Team weitergegeben", seither nichts |
| **Gary Sanderson** (g.sanderson1@sky.com) | 17.08. | „How do you qualify for a replacement?" |
| **Nick Tarrant** (#6259) | 05.09. | „Your website mentions 'With replacement guarantee'. What does this mean?" |

Drei Kunden, drei Wochen, dieselbe Frage — und keine Antwort, weil die Policy
die Zusage nicht kennt. Das ist keine Klassifikationslücke mehr, sondern ein
Widerspruch zwischen dem, was verkauft wird, und dem, was der Support einlösen
darf.

→ **Owner-Entscheidung, vor jeder Antwort an diese drei:** Gibt es die
Ersatzgarantie? Wenn ja, gehört sie in die Policy und die drei bekommen Ersatz.
Wenn nein, gehört sie von Website und Anzeigen entfernt, bevor der nächste Kunde
danach fragt.

**Wo genau steht es?** Vor der Antwort sollte jemand die Produktseite auf die
Formulierung „With replacement guarantee" prüfen. Der Befund vom 13.08. besagt,
die Produktbeschreibung enthalte solche Absolutaussagen nicht — entweder ist
die Seite seither geändert worden, oder die Formulierung steht an anderer Stelle
(Badge, Banner, Checkout-Hinweis) als in der Beschreibung.

---

# Lauf 08:17 UTC

## 🚩 #8295 — Ivan Griffen: dem Kunden wurde gesagt, die Ware sei unterwegs. Sie ist es nicht.

**Shopify, geprüft 07.09. 08:2x UTC:**

- **#8295**, bestellt **31.08. 01:24 UTC**, 27,95 £, **`PAID` / `UNFULFILLED`**,
  **`fulfillments: []`** — keine Sendung, keine Sendungsnummer
- Artikel: Plushies „Elk" und „monkey", Lieferadresse Gosport PO12 4WE

**Was ihm geschrieben wurde**, 06.09. 17:04 UTC aus dem Postfach:

> „I can confirm that **your order has been shipped and is currently on the
> way**."

Das ist unwahr. Die Bestellung ist seit sieben Tagen unversandt.

**Sein Verlauf:**

| Wann | Was |
|---|---|
| 05.09. 09:35 | „When is my order going to arrive and when will I get a tracking number." |
| 06.09. 17:04 | Antwort aus dem Postfach: „shipped and currently on the way" — **ohne Nummer** |
| 06.09. 17:45 | „Have you got a tracking number" |
| **07.09. 08:01** | „Can I have a tracking number please" |
| **07.09. 08:02** | dieselbe Bitte noch einmal, in einem zweiten Thread |

**Vierter Kontakt in derselben Sache** — nach Policy ein Eskalationstrigger ab
dem dritten. Er fragt viermal nach einer Nummer, die nicht existieren kann, weil
nichts versandt wurde.

**Eskalationsgrund:** Dem Kunden wurde eine unzutreffende Auskunft gegeben, und
er hakt seitdem nach. Die Policy ist an dieser Stelle ausdrücklich
(„Bounds on the above"): *„Say what Shopify actually shows … a customer
reassured with something false comes back angrier, which is how several of this
week's escalations started."*

Das ist dasselbe Muster wie **#4212 Mandy Baker**, nur umgekehrt: dort wurde
„nicht versandt" gesagt, als die Ware raus war; hier wird „versandt" gesagt,
obwohl sie liegt.

→ **Zwei Dinge sind zu tun, und beide gehören dem Owner:**
1. Klären, warum #8295 nach sieben Tagen noch `UNFULFILLED` ist.
2. Ihm ehrlich schreiben, dass die Bestellung noch nicht raus ist — und dass die
   vorige Auskunft falsch war. Eine weitere Antwort ohne Sendungsnummer, aber
   mit derselben Behauptung, macht es schlimmer.

Der Entwurf dazu konnte nicht angelegt werden (Schreibpfad defekt). **Kein Text
rekonstruiert**, und ausdrücklich **keine Sendungsnummer genannt** — es gibt
keine.

## Zweiter Fall desselben Typs im Postfach

**Robert Gagne** (Log 06.09.) hat am 06.09. die Nummer `WNBAA0493985171YQ`
bekommen; der Zusteller sagt ihm, sie sei ungültig, die richtige beginne mit
`SWF`. Auch hier: vor der nächsten Antwort in Shopify nachsehen, was tatsächlich
hinterlegt ist, statt die Nummer noch einmal zu schicken.

---

# Lauf 10:17 UTC

## 🚩 Sue Steer — drei Mails seit dem 06.08., **null Antworten**

`suesteer@hotmail.com`, Thread „Fluffy toys" (bereits `Label_7`).

`get_thread` zeigt **zwei Kundennachrichten und keine einzige `SENT`-Nachricht**
— zusammen mit der zitierten Erstmail vom 06.08. sind das **drei Kontakte in
32 Tagen, auf die nie geantwortet wurde.**

**Ihr Fall** (Erstmail 06.08., wörtlich):

> „I ordered 3 fluffy dog toys from your company on the **20th July**. The
> courier, EVRI said they had delivered them on the 28th to my address and
> **left them in my greenhouse, but I have not received them. I do not have a
> greenhouse** and the picture showed they were left on a desk. […] I have
> contacted EVRI about this and was told to contact you. **I would still like
> these items** and would recommend you do not use this courier."

- **22.08.:** „have not received a response yet from you. Could you please
  update me on your decision."
- **07.09. 10:04:** „Could you please give an update regarding **my order
  replacement**."

**Eskalationsgrund:** Paket nie angekommen bzw. an falscher Stelle abgeliefert —
das ist ein ausdrücklicher Trigger in `support-policy.md`. Dazu dritter Kontakt
ohne jede Antwort.

### Zwei Punkte, die vor einer Antwort geklärt sein müssen

1. **Es wurde ihr nie ein Ersatz zugesagt.** Sie schreibt von „my order
   replacement", aber im Thread steht keine Zusage — es steht überhaupt nichts
   von uns darin. Vermutlich hat sie aus dem Ausbleiben einer Absage
   geschlossen, ihr Wunsch („I would still like these items") sei bewilligt.
   **Der Bot bestätigt keinen Ersatz, den niemand zugesagt hat**, und bestreitet
   ihn auch nicht — das ist eine Owner-Entscheidung.

2. **Sie wurde bereits von Evri zu uns zurückgeschickt.** Die Policy verbietet
   ohnehin, Kunden an den Zusteller zu verweisen („Never refer the customer to
   the shipping carrier"). Hier wäre es zusätzlich sinnlos: sie war schon dort.

Der Fall unterscheidet sich von der Werbewelle — es geht nicht um Haltbarkeit,
sondern um Ware, die sie bezahlt und nie bekommen hat. Nach fünf Wochen Stille
ist das der Fall mit der klarsten Anspruchslage im ganzen Postfach.

### Shopify, geprüft 07.09. 11:2x UTC

- **#3089** — Sue Steer — bestellt **19.07. 07:42 UTC** — **27,95 £** —
  `PAID` / **`FULFILLED`**, 2 Positionen

Der Status `FULFILLED` deckt sich mit der Evri-Meldung „zugestellt" — er sagt
nur, dass die Sendung rausging, nicht dass sie angekommen ist. Bei ihr ist sie
das nachweislich nicht.

*Zwei kleine Abweichungen, die keine Rolle spielen, aber nicht übergangen werden
sollten:* sie nennt den **20.07.** als Bestelldatum (Shopify: 19.07.) und
**drei** Spielzeuge (Shopify: 2 Positionen — möglicherweise 2 Positionen mit
Menge 3). Vor einer Ersatzlieferung kurz nachsehen, **was** genau zu ersetzen
ist. Ihre Schilderung deshalb nicht anzuzweifeln — die Abweichung liegt im
Bereich normaler Erinnerung.

→ **Owner-Entscheidung: Ersatz liefern oder 27,95 £ erstatten.** Beides ist
vertretbar, weiter schweigen nicht. Der Fall gehört auf die Erstattungsliste,
sobald die Entscheidung gefallen ist — als „nie angekommen", nicht als
Kauschaden.

---

# Lauf 12:21 UTC — drei neue Fälle

## 1. #5036 — Lynette Lumley — Storno nach 30 Tagen Wartezeit

**11:52:** „I think it is time to **cancel this order** please — it has been over
a month now and i still haven't received the items. I am not holding out much
hope any longer. Delivery states up to 21 days…"

**Shopify, geprüft 07.09. 12:2x UTC:**

- **#5036**, bestellt **08.08. 06:58 UTC**, **27,95 £**, `PAID` / **`FULFILLED`**
- Versandt **22.08. 01:41 UTC**, Yanwen Special Line, `UL442891848YP`
- Fuchs + Elefant, Lieferadresse Abingdon OX14 1FW

**Kein Regel-3-Fall.** Die Ware ist seit 16 Tagen unterwegs, ein Vorab-Storno ist
nicht mehr möglich. Damit fällt der Fall unter „von der Garantie nicht benannt"
→ ehrliche Zwischenantwort, `Bot/Needs Approval`, Lücke an den Owner melden.

**Wichtig zur Einordnung:** Die Antwort vom 01.09. („your order is on the way and
currently in transit") war hier **zutreffend** — anders als bei #8295. Der
Unterschied zwischen den beiden Fällen ist genau der Punkt: einmal deckte die
Auskunft sich mit Shopify, einmal nicht.

Sie beruft sich auf die zugesagte Lieferzeit („Delivery states up to 21 days") —
die ist seit dem 29.08. überschritten. Owner-Entscheidung: erstatten trotz
laufender Sendung, oder ihr die Wahl lassen (behalten oder zurückschicken, sobald
das Paket ankommt). **Der Bot sagt keine Erstattung zu**, weil der Fall nicht
unter die zwei Regelfälle fällt.

## 2. #4829 — Valerie (lemonsnawba@aol.com) — Trading Standards **und** Facebook angedroht

- 03.09.: „I've just received this indestructible toy 10 minutes ago and guess
  what? My dog has pulled a bit off of it"
- 04.09. 15:03 aus dem Postfach: **Vorlagen-Absage**
- **07.09. 11:37:** „reading the reports your are just **a big con of a
  company**, no one has a good word to say. Just to let you know **if I don't get
  a full refund I will take this matter further with fb and trading**
  [standards]"

**Eskalationsgrund:** Behörde (Trading Standards) angedroht **plus** öffentliche
Bewertung angekündigt **plus** bestrittene Werbeaussage — drei Trigger. Die
Vorlagen-Absage vom 04.09. hat die Eskalation ausgelöst; vorher stand davon
nichts in ihrer Mail.

Damit ist Jason Branch (17.08.) nicht mehr der einzige Trading-Standards-Fall.

## 3. #6606 — mpinnock@hotmail.co.uk — Werbeaussage, Fotos angeboten

**11:45:** „our dog has totally destroyed it within days **though you say they
are non destructible**. What are the next steps? **Am happy to show
photographs.**"

Bestrittene Werbeaussage → Eskalation. Ton ist sachlich, sie fragt nach dem
Verfahren und bietet Belege an. Eine Vorlagen-Absage würde hier denselben
Verlauf nehmen wie bei #4829 zwei Tage zuvor.

## Ebenfalls diese Stunde

- **seancragan@gmail.com** — zweiter Kontakt (11:14), nach „About time you pulled
  your fingers out" vom 06.09.

---

## Nicht getan

- Keine Entwürfe, keine Labels — Schreibpfad defekt seit 21.08.
- Keine Erstattung, kein Storno, keine Adressänderung.
- Keine Aussage zur Ersatzgarantie erfunden.
- Keine Sendungsnummer für #8295 genannt — es existiert keine.
- Sue Steer keinen Ersatz bestätigt — es ist keiner zugesagt worden.
