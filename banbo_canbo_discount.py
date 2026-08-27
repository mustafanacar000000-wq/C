MIN_TUTAR = 2000
UYE_INDIRIM = 50
UYE_OLMAYAN_INDIRIM = 25


def indirim_hesapla(tutar, banbo_canbo_uyesi):
    if tutar < MIN_TUTAR:
        return 0
    return UYE_INDIRIM if banbo_canbo_uyesi else UYE_OLMAYAN_INDIRIM


def odenecek_tutar(tutar, banbo_canbo_uyesi):
    return tutar - indirim_hesapla(tutar, banbo_canbo_uyesi)


if __name__ == "__main__":
    tutar = float(input("Alışveriş tutarını girin (TL): "))
    cevap = input("Banbo Canbo üyeliğiniz var mı? (e/h): ").strip().lower()
    uye = cevap == "e"

    indirim = indirim_hesapla(tutar, uye)
    net_tutar = odenecek_tutar(tutar, uye)

    if indirim > 0:
        print(f"Uygulanan indirim: {indirim} TL")
    else:
        print("Bu alışveriş indirim için gerekli minimum tutara ulaşmıyor.")

    print(f"Ödenecek tutar: {net_tutar} TL")
