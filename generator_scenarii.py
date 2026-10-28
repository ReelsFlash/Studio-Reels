import os

def genereaza_scenariu_pro(tema):
    scenariu = f"""==================================================
🎬 SCENARIU UNIC & ORIGINAL
TEMA: {tema.upper()}
==================================================

[00:00 - 00:03] HOOK DE IMPACT
- BĂDGE SUS: "ATENȚIE MARE!"
- TEXT PE ECRAN: "{tema.upper()}?!"
- VIZUAL: Personaj principal dinamic, cadre rapide.
- VOCE: "Bă, frate, fii atent aici că nu știai chestia asta și te fură peisajul!"

[00:03 - 00:20] DEZVOLTAREA IDEII
- BĂDGE SUS: "FAZA REALĂ"
- VIZUAL: Tranziții moderne, elemente grafice aerisite.
- VOCE: "Stai a ajuți mintea să proceseze: totul pleacă de la o bază simplă, dar nimeni nu se uită unde trebuie..."

[00:20 - 00:45] PUNCTUL MAXIM
- BĂDGE SUS: "SECRETELE"
- VIZUAL: Schimbare de cadru la fiecare 2 secunde, dinamică maximă.
- VOCE: "Și când crezi că le-ai văzut pe toate, bam! Apare adevărul gol-goluț!"

[00:45 - 01:00] FINAL & CTA
- BĂDGE SUS: "HAI NOROC!"
- VIZUAL: Cadru relaxat, branding personal.
- VOCE: "Dacă ți-a plăcut cum stă treaba, dă un follow și lasă un comentariu. Atât am avut de zis, hai pa!"
"""
    cale = os.path.join("scenarii", f"{tema.lower().replace(' ', '_')}.txt")
    os.makedirs("scenarii", exist_ok=True)
    with open(cale, "w", encoding="utf-8") as f:
        f.write(scenariu)
    return scenariu
