def tarkista_tilinumero():
    tilinumero = input("Syötä tilinumero: ")

    # Poista välilyönnit ja tarkista pituus
    tilinumero = tilinumero.replace(" ", "")
    if len(tilinumero) != 18:
        print("False")
        return

    # Siirrä maatunnus ja tarkistenumero tilinumeron loppuun
    tilinumero = tilinumero[4:] + tilinumero[:4]

    # Korvaa kirjaimet numeroilla
    tilinumero = tilinumero.upper()
    for kirjain in tilinumero:
        if not kirjain.isdigit():
            tilinumero = tilinumero.replace(kirjain, str(ord(kirjain) - 55))

    # Laske jakojäännös ja tarkista tulos
    if int(tilinumero) % 97 == 1:
        print("True")
    else:
        print("False")

tarkista_tilinumero()
