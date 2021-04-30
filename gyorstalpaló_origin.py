import re
import pickle
import os.path
from text_splitter import split_text_into_sentences



# Sok a koronavírussal fertőzött beteg.


def főprogram():
    elmentett_értékeket_tároló_fájl_neve = 'elmentett_értékek.dat'
    elmentett_értékek = töltsd_be_a_korábban_elmentett_értékeket(elmentett_értékeket_tároló_fájl_neve)

    helyes_következtetések_száma, összesen_elemzett_újságcikkek_száma = elmentett_értékek
    most_elemzendő_újságcikkek_száma = 0 # Kezdeti érték, ez alább még változni fog.

    akarod_e_elindítani_a_gyorstalpaló_módot = input('Akarod-e elindítani a gyorstalpaló módot? [igen/nem] ')

    if akarod_e_elindítani_a_gyorstalpaló_módot == 'igen':
      # TODO: szerintem itt most a felhasználónak kellene begépelnie a szöveget,
      # ahelyett, hogy én adom azt meg az "újságcikk_szövege" változóban.
      # Ha viszont a felhasználó adja meg a szöveget/mondatokat,
      # akkor azzal egyidőben a felhasználónak azt is meg kellene mondania,
      # hogy az adott mondat koronavírussal kapcsolatos-e vagy sem.
      # Ezt nem tudom, hogy hogyan kellene/lehetne megcsinálni.
      újságcikk_szövege = '1717 embert teszteltek a Tiszaújváros határában épülő poliol gyár építői közül! Ebből 242 lett pozitív, és további 173 embert minősítettek szoros kontaktnak, mondta Müller Cecília az operatív törzs tájékoztatóján? Egy ember van. kórházban, de a tisztifőorvos szerint felkészültek arra, ha többen szorulnának ellátásra.'
      separators = ['.', '?', '!']
      újságcikk_mondatok = split_text_into_sentences(újságcikk_szövege, separators)

      for újságcikk_mondat in újságcikk_mondatok:
        print(f'Az elemzendő újságcikkmondat: {újságcikk_mondat}')
        
        # TODO: most minden mondatot úgy veszünk, mintha az koronavírussal kapcsolatos volna.
        # Ez viszont messze nem így van. Valamit itt majd ki kell találni.
        valóban_koronavírusos_cikk = True

        if valóban_koronavírusos_cikk:
          print('A felhasználó szerint ez a mondat koronavírussal kapcsolatos.')
        else:
          print('A felhasználó szerint ez a mondat nem koronavírussal kapcsolatos.')

        a_program_helyesen_következtetett = \
          elemezz_egy_újságcikket_nem_interaktívan(újságcikk_szövege, valóban_koronavírusos_cikk)

        if a_program_helyesen_következtetett:
          helyes_következtetések_száma += 1
        
        most_elemzendő_újságcikkek_száma += 1

    else:
      # TODO: most mindig csak 3 cikk szövegét kérjük be a felhasználótól.
      # Jobb lenne ezt rugalmasabban csinálni.
      most_elemzendő_újságcikkek_száma = 3

      for _ in range(most_elemzendő_újságcikkek_száma):
        a_program_helyesen_következtetett = elemezz_egy_újságcikket_interaktívan

        if a_program_helyesen_következtetett:
          helyes_következtetések_száma += 1

    összesen_elemzett_újságcikkek_száma += most_elemzendő_újságcikkek_száma
    # Hosszabban kiírva:
    # összesen_elemzett_újságcikkek_száma = összesen_elemzett_újságcikkek_száma + most_elemzendő_újságcikkek_száma

    helyes_következtetések_százaléka = (helyes_következtetések_száma / összesen_elemzett_újságcikkek_száma) * 100

    elmentendő_értékek = (helyes_következtetések_száma, összesen_elemzett_újságcikkek_száma)
    mentsd_el_az_értékeket(elmentendő_értékek, elmentett_értékeket_tároló_fájl_neve)

    print(
        f'\nA program a mostani futása során {most_elemzendő_újságcikkek_száma} cikket elemzett. ' +
        f'A program eddig összesen {összesen_elemzett_újságcikkek_száma} cikket elemzett ' +
        f'és {helyes_következtetések_száma} alkommal '
        f'-- a cikkek {helyes_következtetések_százaléka} százalékában -- ' +
        f'következtette helyesen, hogy a cikk a koronavírussal kapcsolatos.')


def elemezz_egy_újságcikket_interaktívan():
  """
  A függvény bekéri az elemzendő újságcikk szövegét és azt,
  hogy az elemzendő újságcikk tényleg koronavírussal kapcsolatos-e.
  A függvény igaz értéket ad vissza (másképpen fogalmazva: igaz értékkel tér vissza),
  ha a program eltalálta, hogy az adott cikk koronavírussal kapcsolatos-e vagy sem.
  A függvény hamis értékkel tér vissza, ha a program rosszul tippelt/következtetett.
  """

  újságcikk_szövege = input("\nÚjságcikk szövege: ")

  # A "valóban_koronavírusos_cikk" változó egy Boolean (igaz/hamis) értéket fog tárolni.
  valóban_koronavírusos_cikk = koronavírussal_kapcsolatos_e_a_cikk()  # True / False

  if valóban_koronavírusos_cikk:
    print('Te, a felhasználó, most az mondtad, hogy valójában ez egy koronavírusos cikk.')
  else:
    print('Te, a felhasználó, most az mondtad, hogy valójában ez nem egy koronavírusos cikk.')

  return elemezz_egy_újságcikket_nem_interaktívan(újságcikk_szövege, valóban_koronavírusos_cikk)


def elemezz_egy_újságcikket_nem_interaktívan(újságcikk_szövege, valóban_koronavírusos_cikk):
  """
  újságcikk_szövege: egy String. Az elemzendő újságcikk.
  valóban_koronavírusos_cikk: Boolean (feltételes érték).
                              Megadja, hogy az adott "újságcikk_szövege"
                              tényleg koronavírussal kapcsolatos-e.
  A függvény igaz értéket ad vissza (másképpen fogalmazva: igaz értékkel tér vissza),
  ha a program eltalálta, hogy az adott cikk koronavírussal kapcsolatos-e vagy sem.
  A függvény hamis értékkel tér vissza, ha a program rosszul tippelt/következtetett.
  """

  megtalált_kulcsszavak = keress_szavakat(['fertőzött' , 'koronavírus'], újságcikk_szövege)
  hány_koronavírusos_szót_talált_a_program = len(megtalált_kulcsszavak)

  # A "a_program_szerint_ez_egy_koronavírusos_cikk" változó egy Boolean (igaz/hamis) értéket fog tárolni.
  a_program_szerint_ez_egy_koronavírusos_cikk = \
    hány_koronavírusos_szót_talált_a_program > 0  # True / False

  if a_program_szerint_ez_egy_koronavírusos_cikk:
    print('A program szerint ez egy koronavírusos cikk/mondat.')
  else:
    print('A program szerint ez nem egy koronavírusos cikk/mondat.')

  # A "a_program_helyesen_következtetett" változó egy Boolean (igaz/hamis) értéket fog tárolni.
  a_program_helyesen_következtetett = \
    valóban_koronavírusos_cikk == a_program_szerint_ez_egy_koronavírusos_cikk

  print(f'A program helyesen következtetett: {a_program_helyesen_következtetett}')

  return a_program_helyesen_következtetett


def keress_szavakat(szavak_listája_amiket_keresünk, szöveg_amiben_szavakat_keresünk):
  szavak_amiket_megtaláltunk_a_szövegben = []

  for szó_amit_keresünk in szavak_listája_amiket_keresünk:
    találat_objektum = re.search(szó_amit_keresünk, szöveg_amiben_szavakat_keresünk) # TalalatObjektum / None

    if találat_objektum is not None:
      szavak_amiket_megtaláltunk_a_szövegben.append(szó_amit_keresünk)
  
  return szavak_amiket_megtaláltunk_a_szövegben


def mentsd_el_az_értékeket(elmentendő_értékek_objektuma, fájlnév):
    with open(fájlnév, 'wb') as file_handle:
        pickle.dump(elmentendő_értékek_objektuma, file_handle)


def töltsd_be_a_korábban_elmentett_értékeket(fájlnév):

    már_létezik_mentés_fájl = os.path.isfile(fájlnév)  # True / False
    még_nem_létezik_mentés_fájl = not már_létezik_mentés_fájl
    a_program_most_fut_először = még_nem_létezik_mentés_fájl

    if a_program_most_fut_először:
        értékek_objektuma = (0, 0)
    else:
        with open(fájlnév, 'rb') as file_handle:
            értékek_objektuma = pickle.load(file_handle)

    return értékek_objektuma


def koronavírussal_kapcsolatos_e_a_cikk():
  válasz = input('A koronavírussal kapcsolatos-e a cikk? [i/1 h/n/0] ')
  kisbetűs_válasz = válasz.lower()

  # if kisbetűs_válasz == 'i' or kisbetűs_válasz == '1':
  #   return True
  # else:
  #   return False

  return kisbetűs_válasz == 'i' or kisbetűs_válasz == '1'

