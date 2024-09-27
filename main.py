
import pandas
nato_data=pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict={rows.letter:rows.code for (index,rows) in nato_data.iterrows()}
is_ok=True
while is_ok:
    user_word = list(input("Enter a word: ").upper())
    try:
        word_code=[nato_dict[letter] for letter in user_word]
    except KeyError:
        print("sorry, only letters in the alphabet please.")
    else:
        print(word_code)
        is_ok = False
