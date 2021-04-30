text = '1717 embert teszteltek a Tiszaújváros határában épülő poliol gyár építői közül! Ebből 242 lett pozitív, és további 173 embert minősítettek szoros kontaktnak, mondta Müller Cecília az operatív törzs tájékoztatóján? Egy ember van. kórházban, de a tisztifőorvos szerint felkészültek arra, ha többen szorulnának ellátásra.'

separators = ['!', '?', '.']


def split_text_into_sentences(sentences):
  global separators

  if len(separators) > 0:
    separator = separators.pop()
    
    new_sentences = []

    for sentence in sentences:
      almondatok_listaja = sentence.split(separator)

      for almondat in almondatok_listaja:
        new_sentences.append(almondat)
  
    sentences = new_sentences
    
    split_text_into_sentences(sentences)
    return sentences
    

  else:
    return # semmit nem adunk vissza
    

# Start, itt indul a program:
#a = split_text_into_sentences([text])

#print(a)



























#def szöveg_darabolása_mondatokra(karakterek_listája_amit_keresünk, szöveg_amiben_karaktereket_keresünk):
  
 # for karakter_amit_keresünk in karakterek_listája_amit_keresünk:
  #  találat_objektum = szöveg_amiben_karaktereket_keresünk.split(karakter_amit_keresünk)

   