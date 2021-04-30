import unittest
import typing

# text = '1717 embert teszteltek a Tiszaújváros határában épülő poliol gyár építői közül! Ebből 242 lett pozitív, és további 173 embert minősítettek szoros kontaktnak, mondta Müller Cecília az operatív törzs tájékoztatóján? Egy ember van. kórházban, de a tisztifőorvos szerint felkészültek arra, ha többen szorulnának ellátásra.'


def split_text_into_sentences(text, separators):

  text_is_already_a_list_of_sentences = isinstance(text, typing.List)

  if text_is_already_a_list_of_sentences:
    sentences = text
  else:
    # A 'text' objektum az nem egy lista, hanem csak egy sima string.
    # Ezért beletesszük a 'text' objektumot egy listába,
    # mert a program többi, lenti része azt várja el,
    # hogy a 'sentences' objektum az egy lista legyen.
    # A 'sentences' objektum az tehát egy egyelemű lista lesz.
    sentences = [text]

  # A "sentences" objektum az itt már egy lista.

  if len(separators) > 0:
    # Forrás: https://stackoverflow.com/a/10532492
    first_separator, *rest_of_the_separators = separators
    
    new_sentences = []

    # Egy példa:
    # sentences == ['alma. bela.', 'hopp! kopp.']
    for sentence in sentences:
      # sentence == 'alma. bela.'
      # splitted_sentences == ['alma', ' bela', '']
      splitted_sentences = sentence.split(first_separator)

      # A 'splitted_sentences' objektum az most így néz ki:
      # ['alma', ' bela', '']
      # Távolítsuk el belőle azt az üres stringet:
      if '' in splitted_sentences:
        splitted_sentences.remove('')
      # A 'splitted_sentences' objektum az most így néz ki:
      # ['alma', ' bela']

      # Távolítsuk el a szavak elejéről a felesleges szóközt:
      splitted_sentences = list(map(str.strip, splitted_sentences))
      # A 'splitted_sentences' objektum most végül így néz ki:
      # ['alma', 'bela']
      
      new_sentences = new_sentences + splitted_sentences
      # Rövidebben írva:
      # new_sentences += splitted_sentences
  
    return split_text_into_sentences(new_sentences, rest_of_the_separators)

  else:
    return sentences


class TestTextSplitter(unittest.TestCase):

  def can_split_text_into_sentences(self):
    text = 'asd. dfg! fgh? wer!'
    separators = ['!', '?', '.']
    
    actual_sentences = split_text_into_sentences(text, separators)

    expected_sentences = ['asd', 'dfg', 'fgh', 'wer']
    self.assertEqual(actual_sentences, expected_sentences)

  def does_not_modify_the_original_separators_object(self):
    original_separators = ['!', '?', '.']
    
    split_text_into_sentences('text', original_separators)

    # A "separators" objektumnak nem szabad megváltoznia:
    self.assertEqual(original_separators, ['!', '?', '.'])


akarod_lefuttatni_a_teszteket = False

if akarod_lefuttatni_a_teszteket:
  # unittest.main(exit=False)
  runner = unittest.TextTestRunner(verbosity=2)
  runner.run(TestTextSplitter('can_split_text_into_sentences'))
  runner.run(TestTextSplitter('does_not_modify_the_original_separators_object'))
