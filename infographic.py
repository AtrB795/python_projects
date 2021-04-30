import pandas as pd
import matplotlib.pyplot as plt


def plot_list_of_letters(list_of_letters):
    df = pd.DataFrame(list_of_letters, columns=['letters'])
    value_counts = df['letters'].value_counts()
    value_counts.plot(kind='bar')
    plt.show()


if __name__ == '__main__':
    list_of_letters = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
    plot_list_of_letters(list_of_letters)
