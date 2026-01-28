
def get_char_index(char, word):
    indexes = []
    for index, c in enumerate(word):
        if char == c:
            indexes.append(index)

    return indexes

words = {"apple", "banana", "cherry", "kiwi"}
name = input("Please enter your name:  ")
print(f"----- Welcome {name} to HangMan ----")
# get word that I need to play
selected_word = words.pop()
guessed_word = len(selected_word)* "-"
print(f"try to guess this word {guessed_word}")
guessed_word = list(guessed_word)
selected_word = list(selected_word)
for i in range(0,7):
    char = input("Please enter your guess: ")
    if len(char) ==1 and char in selected_word:
        char_index = get_char_index(char, selected_word)
        for j in char_index:
            guessed_word[j] = char
        if guessed_word == selected_word:
            print(f"You won the game! The word was {''.join(guessed_word)}")
            break
        print(''.join(guessed_word))
    else:
        print("-----You can only enter one char at time ----")

else:
    print("-----You have lost the game! -----")
