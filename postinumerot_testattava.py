import http_pyynto

# rivillä 10 poistetaan välilyönnit jotta smart post- muotoiset merkinnät menevät smartpost-muotoisten kanssa samaan paikkaan listassa


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        # allaolevalla poistetaan välilyönti tutkittavasta nimestä smart post --> smartpost
        nimi = nimi.replace(' ', '')
        # muokattu lisäämään kaikki smart-sanan sisältävien nimien numerot smartpost numeroiksi
        if 'SMART' in nimi:
            if 'SMARTPOST' not in paikat:
                paikat['SMARTPOST'] = []
            paikat['SMARTPOST'].append(numero)
        else:
            if nimi not in paikat:
                paikat[nimi] = []

            paikat[nimi].append(numero)

    return paikat


postinumerot = http_pyynto.hae_postinumerot()

toimipaikat = ryhmittele_toimipaikoittain(postinumerot)


def main():
    toimipaikka = input('Kirjoita postitoimipaikka: ').strip().upper()

    if toimipaikka in toimipaikat:
        toimipaikat[toimipaikka].sort()

        loydetyt_str = ', '.join(toimipaikat[toimipaikka])
        print('Postinumerot: ' + loydetyt_str)
    else:
        print('Toimipaikkaa ei löytynyt')


if __name__ == '__main__':
    main()
