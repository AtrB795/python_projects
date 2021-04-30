from pynput.keyboard import Listener
from pynput import keyboard
import pandas as pd
import matplotlib.pyplot as plt

list_of_letters = []


def plot_list_of_letters(list_of_letters):
    df = pd.DataFrame(list_of_letters, columns=['letters'])
    value_counts = df['letters'].value_counts()
    value_counts.plot(kind='bar')
    plt.show()


def count_the_keys(key):
    global list_of_letters

    list_of_letters.append(key)
    if key == keyboard.Key.esc:
        plot_list_of_letters(list_of_letters)
        return False
    else:
        return list_of_letters


with Listener(on_press=count_the_keys) as listener:
    listener.join()

