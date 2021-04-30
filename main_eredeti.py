import  time
from blinkt import set_pixel, set_brightness, show, clear, set_all

set_brightness(0.5)

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-',' ':'_'}
#print(MORSE_CODE_DICT)





def morse_code_translater (word1, MORSE_CODE_DICT):
  word = word1.upper()
  morse_code_list = []
  words_letters = list(word)
  for letter in words_letters:
    morse_code_list.append(MORSE_CODE_DICT[letter])

  return morse_code_list

#print(morse_code_translater('ALMA', MORSE_CODE_DICT))

def blinkt_morse(morse_code_list):
  for morse_code in morse_code_list:
    time.sleep(2)
    listed_morse_code = list(morse_code)
    for symbol in listed_morse_code:
      if symbol == '.':
        clear()
        set_all(255, 255, 255)
        show()
        time.sleep(1)
        clear()
        set_all(0, 0, 0)
        show()
        time.sleep(0.5)
      elif symbol == '_':
        clear()
        show()
        time.sleep(7)
      else:
        clear()
        set_all(255, 255, 255)
        show()
        time.sleep(3)
        clear()
        set_all(0, 0, 0)
        show()
        time.sleep(0.5)

blinkt_morse(morse_code_translater('alma alma', MORSE_CODE_DICT))
