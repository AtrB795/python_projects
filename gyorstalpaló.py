from text_splitter import split_text_into_sentences
from koronavirus_elemzo import jol_dontott_e_a_program

text = '1717 embert teszteltek a Tiszaújváros határában épülő poliol gyár építői közül! Ebből 242 lett pozitív, és további 173 embert minősítettek szoros kontaktnak, mondta Müller Cecília az operatív törzs tájékoztatóján? Egy ember van. kórházban, de a tisztifőorvos szerint felkészültek arra, ha többen szorulnának ellátásra.'

sentences_of_the_text = split_text_into_sentences(text, ['?', '.', '!'])

for one_sentence in sentences_of_the_text:

  a_program_jol_dontott = jol_dontott_e_a_program(one_sentence)

  if a_program_jol_dontott:
    print('A program helyesen döntött.')
  else:
    print('A program rosszul döntött.')

