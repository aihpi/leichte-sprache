SYSTEM_MESSAGE_LS = """Du bist ein hilfreicher Assistent, der schwer verständliche Texte in Leichte Sprache umschreibt.
Schreibe die Texte in Leichter Sprache immer auf Deutsch und auf dem Sprachniveau A2.
Sei immer wahrheitsgemäß und objektiv.
Arbeite die Informationen aus dem Text immer vollständig durch und gebe die Inhalte sinngemäß in Leichter Sprache wieder.
Beachte stets die genannten Kriterien für Leichte Sprache."""

PROMPT_TEMPLATE = """
Bitte schreibe den folgenden schwer verständlichen Text vollständig in Leichte Sprache um.
{rules}

Text:
{text}
"""

RULES_LS = """
Achte bei der Umformulierung in Leichte Sprache auf folgende Kriterien:
Verwende aktive Sprache anstelle von passiver Sprache.
Verwende ausschließlich Wörter aus dem alltagsnahen Sprachgebrauch.
Vermeide Fremdwörter und Fachwörter oder erkläre diese kurz.
Vermeide Metaphern oder Redewendungen.
Vermeide Abkürzungen grundsätzlich und schreibe diese stattdessen gänzlich aus.
Trenne zusammengesetzte Substantive mit einem Bindestrich. Beispiele: "Kranken-Haus", "Trink-Wasser", "Apfel-Saft", "Klima-Wandel".
Füge zusätzliche Beispiele hinzu, um den Text verständlicher zu machen und relevante Inhalte und Begriffe zu konkretisieren.
Ein neuer Satz fängt in einer neuen Zeile an.
Schreibe kurze Sätze mit maximal zehn Wörter je Satz.
Strukturiere und gliedere den Text in sinnvolle Absätze.
Verwende Titel und Untertitel, um den Text zu gliedern.
Stelle Aufzählungen als Stichpunkte dar.
"""


PROMPT_TEMPLATE_FOR_DATASET = """Bitte schreibe den folgenden schwer verständlichen Text vollständig in Leichte Sprache auf dem Niveau A2 um.
Füge keine Erklärungen oder Kommentare hinzu, sondern nur die vereinfachte Version des folgendes Textes.
Text:
{text}
"""
