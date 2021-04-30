import re
import pickle
import os.path
from text_splitter import split_text_into_sentences



# Sok a koronavírussal fertőzött beteg.

def keress_szavakat(szavak_listája_amiket_keresünk, szöveg_amiben_szavakat_keresünk):
  szavak_amiket_megtaláltunk_a_szövegben = []

  for szó_amit_keresünk in szavak_listája_amiket_keresünk:
    találat_objektum = re.search(szó_amit_keresünk, szöveg_amiben_szavakat_keresünk) # TalalatObjektum / None

    if találat_objektum is not None:
      szavak_amiket_megtaláltunk_a_szövegben.append(szó_amit_keresünk)
  
  return szavak_amiket_megtaláltunk_a_szövegben


def főprogram():
    elmentett_értékeket_tároló_fájl_neve = 'elmentett_értékek.dat'
    elmentett_értékek = töltsd_be_a_korábban_elmentett_értékeket(elmentett_értékeket_tároló_fájl_neve)

    helyes_következtetések_száma, összesen_elemzett_újságcikkek_száma = elmentett_értékek

    most_elemzendő_újságcikkek_száma = 3
    akarod_e_elíndítani_a_gyorstalpalót = input('Akarod-e elindítani a gyorstalpalót? [igen/nem] ')
    if akarod_e_elíndítani_a_gyorstalpalót == 'igen':
      bekért_szöveg = '1717 embert teszteltek a Tiszaújváros határában épülő poliol gyár építői közül! Ebből 242 lett pozitív, és további 173 embert minősítettek szoros kontaktnak, mondta Müller Cecília az operatív törzs tájékoztatóján? Egy ember van. kórházban, de a tisztifőorvos szerint felkészültek arra, ha többen szorulnának ellátásra.'
      separators = ['.', '?', '!']
      bekért_szöveg_mondatai = split_text_into_sentences(bekért_szöveg, separators)

      for újságcikk_szövege in bekért_szöveg_mondatai:
        újságcikket_elemez(újságcikk_szövege)
        
    else:
      újságcikk_szövege = input("\nÚjságcikk szövege: ")
      újságcikket_elemez(újságcikk_szövege)


    összesen_elemzett_újságcikkek_száma += most_elemzendő_újságcikkek_száma
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

def újságcikket_elemez(újságcikk_szövege):
  megtalált_kulcsszavak = keress_szavakat(['fertőzött' , 'koronavírus'], újságcikk_szövege)
  hány_koronavírusos_szót_talált_a_program = len(megtalált_kulcsszavak) # True / False
  a_program_szerint_ez_egy_koronavírusos_cikk = hány_koronavírusos_szót_talált_a_program != 0  # True / False

  if a_program_szerint_ez_egy_koronavírusos_cikk:
    print('A program szerint ez egy koronavírusos cikk/mondat.')
  else:
    print('A program szerint ez nem egy koronavírusos cikk/mondat.')

  valóban_koronavírusos_cikk = koronavírussal_kapcsolatos_e_a_cikk()  # True / False

  if valóban_koronavírusos_cikk:
    print('A felhasználó szerint ez a mondat koronavírussal kapcsolatos.')
  else:
    print('A felhasználó szerint ez a mondat nem koronavírussal kapcsolatos.')

  if valóban_koronavírusos_cikk == a_program_szerint_ez_egy_koronavírusos_cikk:
      helyes_következtetések_száma += 1
      #helyes_következtetések_száma = helyes_következtetések_száma + 1

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


# Start!
főprogram()