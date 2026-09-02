# Backlog-Triage 2026-09-02

## ⛔ Die Warnung von gestern ist heute Morgen eingetreten

Shopify, geprüft 02.09. 21:2x UTC:

| Bestellung | Kunde | Betrag | Stand jetzt | Versandt am |
|---|---|---|---|---|
| **#6870** | Mary Jacobs | 45,95 £ | `PAID` / **`FULFILLED`** | **02.09. 10:36 UTC**, JQ Express US, `JCHSG0000004362592` |
| **#6905** | Wendy Higgins | 28,52 £ | `REFUNDED` / **`FULFILLED`** | **02.09. 10:38 UTC**, JQ Express US, `JCHSG0000004362798` |

Beide sind heute Vormittag im selben Fulfilment-Lauf rausgegangen, zwei Minuten
auseinander.

**#6905 ist damit der zweite #4617:** erstattet **und** versandt. 28,52 £ sind
zurückgezahlt und die Ware ist trotzdem unterwegs nach Florida. Geld und Ware
beide weg. Genau davor stand gestern im Log und im Abend-Report: *„Solange sie
auf `UNFULFILLED` steht, kann die Fulfilment-Automatik sie ziehen."* Zwischen
der Warnung und dem Versand lagen fünfzehn Stunden.

**#6870 ist der sechste Fall des Musters:** Todd Jacobs hat am **20.08. 21:51**
um Storno gebeten. Die Bestellung war bis heute Vormittag `UNFULFILLED` und
damit dreizehn Tage lang stornierbar. Statt zu stornieren wurde ihm am 22.08.
eine Rückfrage nach dem Grund geschickt. Heute ist sie versandt worden, und der
Betrag steht weiterhin auf `PAID` — **keine Erstattung**.

Die Reihe ist damit: #4617 (Vatne), #3944 (Swann), #4212 (Baker), #5474
(Kirtland), #6173 (Myers), #6870 (Jacobs), #6905 (Higgins).

### Was daraus folgt

Das Zeitfenster ist keine Formalie. Beide Fälle standen seit dem 21.08. im Log
mit Bestellnummer, Betrag und der ausdrücklichen Anweisung „erst stornieren,
dann erstatten". Ausgeführt wurde in dreizehn Tagen weder das eine noch das
andere; bei #6905 wurde erstattet, ohne zu stornieren, und genau das hat den
Verlust erzeugt.

**Der Bot kann das nicht abfangen** — der Shopify-Connector blockiert
`orderCancel` und `refundCreate` auf Serverebene (`category: "financial"`).
Die Ausführung liegt zu 100 % beim Owner, und die Laufzeit zwischen Meldung und
Ausführung ist die eigentliche Fehlerquelle.

## Beide Entwurfstexte sind damit falsch geworden

`docs/entwuerfe-zum-kopieren.md` enthielt für beide Fälle Sätze wie „nothing has
been dispatched" bzw. „Order #6905 hasn't been dispatched". Das stimmt seit
heute Vormittag nicht mehr. **Beide Texte sind in derselben Datei ersetzt
worden** — die alten Fassungen dürfen nicht mehr abgeschickt werden, sie würden
dem Kunden etwas Unwahres schreiben.

Das ist zum zweiten Mal derselbe Mechanismus wie bei #5634: ein Entwurf, der
liegen bleibt, wird nicht nur nicht gelesen — er wird falsch. Runbook 6a hält
das fest; hier ist es innerhalb von 24 Stunden passiert.

## Zu erledigen

1. **#6870 erstatten** — 45,95 £, volle Summe, ohne Rücksendung. Der Kunde hat
   rechtzeitig storniert; dass die Ware trotzdem rausging, ist nicht sein
   Fehler.
2. **#6905** — Geld ist zurück, Ware unterwegs. Nichts mehr auszuführen; die
   Kundin muss nur erfahren, dass ein Paket kommt, für das sie erstattet wurde.
   Ob es zurückgefordert wird, ist eine Owner-Entscheidung — nach dem Muster
   von #5474 (Kirtland) wird nicht zurückgefordert, wenn der Fehler bei uns lag.
3. **Die Storno-Rückfrage aus den Vorlagen entfernen.** Sie hat in beiden
   Fällen den entscheidenden Tag gekostet und widerspricht Regel 3 ausdrücklich
   („no argument, no attempt to talk them out of it").
4. **Prüfen, ob weitere `PAID`/`UNFULFILLED`-Stornofälle offen sind**, bevor der
   nächste Fulfilment-Lauf sie zieht. Offen bekannt: #6126 Alex Marris
   (29,95 £), #5841 Alexander Tyrrell (Betrag aus Shopify holen).

## Nicht getan

- Keine Entwürfe angelegt, keine Labels gesetzt — der Gmail-Schreibpfad bricht
  seit dem 21.08. bei jedem Versuch ab (inzwischen über zwanzig Versuche).
- Keine Erstattung, kein Storno in Shopify ausgeführt — Connector blockiert
  beides.
- Kein Entwurfstext rekonstruiert; die zwei ersetzten Texte sind neu
  geschrieben und als solche gekennzeichnet.
