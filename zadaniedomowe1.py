def bmi(masa, wzrost):
    wskaznik_bmi = masa / ((wzrost / 100) ** 2)
    return round(wskaznik_bmi, 2)


def komentarz_bmi(wskaznik_bmi):
    komentarz = {
        wskaznik_bmi < 16: "wygłodzenie",
        16 <= wskaznik_bmi < 17: "wychudzenie",
        17 <= wskaznik_bmi < 18.5: "niedowaga",
        18.5 <= wskaznik_bmi < 25: "wartość prawidłowa",
        25 <= wskaznik_bmi < 30: "nadwaga",
        30 <= wskaznik_bmi < 35: "I stopień otyłości",
        35 <= wskaznik_bmi < 40: "II stopień otyłości (otyłość kliniczna)",
        wskaznik_bmi >= 40: "III stopień otyłości (otyłość skrajna)",
    }
    return komentarz[True]


for waga in range(50, 151, 5):
    print("Waga: " + str(waga) + "; Wzrost: 190; Twoje BMI: " + str(bmi(waga, 190)) + " - " + komentarz_bmi(bmi(waga, 190)))
