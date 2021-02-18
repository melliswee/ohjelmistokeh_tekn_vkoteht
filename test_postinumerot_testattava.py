import postinumerot_testattava
import json

POSTINUMEROT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}

ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST",
    "90210": "BEVERLY HILLS"
}

TYHJA = {

}


def test_testidatalla_syntyy_kolme_ryhmaa():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(POSTINUMEROT)
    assert len(tulos) == 3


def test_erikoistapauksilla_syntyy_nelja_ryhmaa():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(
        ERIKOISTAPAUKSET)
    assert len(tulos) == 4


def test_tyhjan_totuusarvo_on_false():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(TYHJA)
    assert bool(tulos) == False


def test_juupajoella_on_yksi_nro():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(POSTINUMEROT)
    juupajoen_nrot = tulos.get('JUUPAJOKI')
    assert len(juupajoen_nrot) == 1


def test_kiuruvedella_on_kaksi_nroa():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(POSTINUMEROT)
    kiuruveden_nrot = tulos.get('KIURUVESI')
    assert len(kiuruveden_nrot) == 2


def test_juupajoen_nro_on_35540():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(POSTINUMEROT)
    juupajoen_nrot = tulos.get('JUUPAJOKI')
    assert juupajoen_nrot[0] == '35540'


def test_kiuruveden_nrot_ovat_oikein():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(POSTINUMEROT)
    kiuruveden_nrot = tulos.get('KIURUVESI')
    assert kiuruveden_nrot[0] == '74701' and kiuruveden_nrot[1] == '74700'

########################################################

# apufunktio tiedoston lukemiseksi


def lue_tiedosto():
    with open('postinumerot.json') as f:
        tiedoston_sisalto = f.read()
    postinumerot_jsonista = json.loads(tiedoston_sisalto)
    return postinumerot_jsonista

# tämä testaa vain osasinko lukea json-tiedoston: osasin!


def test_json_loytyy_korvatunturi():
    postinumerot_json = lue_tiedosto()
    assert postinumerot_json.get('99999') == 'KORVATUNTURI'

# osoitus että eri kirjoitusasut tuovat eri tulokset
# löytyykö eri määrä tuloksia eri kirjoitusasuille
# huom: tämä testi ei mene läpi, jos tekee korjauksen koodiin, jossa välilyönti poistetaan


def test_smartpost_ja_smart_post_tulosten_lkm_ero():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(lue_tiedosto())
    smartpost_nrot = tulos.get('SMARTPOST')
    smart_post_nrot = tulos.get('SMART POST')
    # testaa onko saatuja tuloksia eri määrä
    assert len(smart_post_nrot) != len(smartpost_nrot)

# osoitus että eri kirjoitusasut tuovat eri tulokset
# huom: tämä testi ei mene läpi, jos tekee korjauksen koodiin, jossa välilyönti poistetaan


def test_smart_post_nro_ei_loydy_smartpost_nroista():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(lue_tiedosto())
    smartpost_nrot = tulos.get('SMARTPOST')

    loytyy = True  # lippu, nollahypoteesi: smart_post_esim_nro löytyy smartpost_nrot:sta. Jos ei löydy, nollahypoteesi hylätään
    smart_post_esim_nro = '40934'

    if smart_post_esim_nro not in smartpost_nrot:
        loytyy = False  # ei löytynyt, nollahypoteesi hylätään

    assert loytyy == False

#######################################################
# välilyönnin poiston jälkeen nämä testit toimivat
# smartpost-muotoisia löytyy 809 kpl, smart post-muotoisia 4 kpl
# tämä testi ei toimi kun on tehty korjaus smartpsot-muodolle


def test_valilyonnin_poisto_tuottaa_odotetun_lkmn():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(lue_tiedosto())
    smartpost_nrot = tulos.get('SMARTPOST')
    assert len(smartpost_nrot) == 813


def test_entinen_smart_post_nro_loytyy_smartpost_nroista():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(lue_tiedosto())
    smartpost_nrot = tulos.get('SMARTPOST')

    loytyy = False  # lippu, nollahypoteesi: ent_smart_post_esim_nro ei löydy smartpost_nrot:sta. Jos löytyy, nollahypoteesi hylätään
    ent_smart_post_esim_nro = '40934'

    if ent_smart_post_esim_nro in smartpost_nrot:
        loytyy = True  # löytyi, nollahypoteesi hylätään

    assert loytyy == True

# smart-alkuisia tuloksia on 816 kpl, smartpsot-muotoisia on 3 kpl
# toimiiko koodiin tehty korjaus kirjoitusvirheelle smartpsot?


def test_smart_korjaus_tuottaa_odotetun_lkmn():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(lue_tiedosto())
    smartpost_nrot = tulos.get('SMARTPOST')
    assert len(smartpost_nrot) == 816

# entinen smartpsot numero löytyy smartpostnumeroista


def test_entinen_smartpsot_nro_loytyy_smartpost_nroista():
    tulos = postinumerot_testattava.ryhmittele_toimipaikoittain(lue_tiedosto())
    smartpost_nrot = tulos.get('SMARTPOST')

    loytyy = False  # lippu, nollahypoteesi: ent_smartpsot_esim_nro ei löydy smartpost_nrot:sta. Jos löytyy, nollahypoteesi hylätään
    ent_smartpsot_esim_nro = '08504'

    if ent_smartpsot_esim_nro in smartpost_nrot:
        loytyy = True  # löytyi, nollahypoteesi hylätään

    assert loytyy == True
