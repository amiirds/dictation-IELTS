import random
import tkinter as tk
from gtts import gTTS
import pygame
from PyDictionary import PyDictionary

dictionary = PyDictionary()
words_file = "Words.txt"
corrects_file = "corrects.txt"
important_file = "importants.txt"
mistakes_file = "mistakes.txt"

def openfile(name_of_file):
    with open(name_of_file, 'r') as file:
        text = file.read().lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        words = [word.replace("â€™", "'") for word in words]
    return words

def say(text, lang='en-gb'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    pygame.mixer.init()  # Initialize Pygame mixer
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

def find_uniques(unique, corrects):
    return [word for word in unique if word not in corrects]

def spell_word(word):
    spelled_word = ' '.join(word)
    return spelled_word

def check_word(input_word, word_of_choice, unique_words, input_entry, correct_word_label):
    if input_word == word_of_choice:
        correct_word_label.config(text="Correct!")
        unique_words.remove(word_of_choice)
    else:
        correct_word_label.config(text=f"Incorrect! The correct word is {word_of_choice}")
        spelled_word = spell_word(word_of_choice)
        say(spelled_word)

def start_learning():
    words_file = "/Users/amiirds/Desktop/IELTS_dictation_Ds/Words.txt"
    corrects_file = "/Users/amiirds/Desktop/IELTS_dictation_Ds/corrects.txt"
    important_file = "/Users/amiirds/Desktop/IELTS_dictation_Ds/importants.txt"  # Add this line
    mistakes_file = "/Users/amiirds/Desktop/IELTS_dictation_Ds/mistakes.txt"  # Add this line



    words = openfile(words_file)
    corrects = openfile(corrects_file)
    important_words = openfile(important_file)
    mistakes = openfile(mistakes_file)
    unique_words = find_uniques(words, corrects)
    current_word = None

    def next_word():
        nonlocal current_word
        if len(unique_words) == 0:
            correct_word_label.config(text="You have learned all the words!")
            return

        current_word = random.choice(unique_words)
        correct_word_label.config(text="")
        say(current_word)

    def on_check():
        input_word = input_entry.get().lower()
        next_word_button.config(state=tk.NORMAL)  # Enable the next word button
        if current_word:
            check_word(input_word, current_word, unique_words, input_entry, correct_word_label)
        input_entry.delete(0, tk.END)

    def repeat_word():
        if current_word:
            say(current_word)

    root = tk.Tk()
    root.title("Word Learning App")

    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    input_label = tk.Label(input_frame, text="Enter the word you heard:")
    input_label.pack(side=tk.LEFT)

    input_entry = tk.Entry(input_frame)
    input_entry.pack(side=tk.LEFT)

    check_button = tk.Button(input_frame, text="Check Word", command=on_check)
    check_button.pack(side=tk.LEFT, padx=5)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    start_button = tk.Button(button_frame, text="Start Learning", command=next_word)
    start_button.pack(side=tk.LEFT, padx=5)

    repeat_button = tk.Button(button_frame, text="Repeat", command=repeat_word)
    repeat_button.pack(side=tk.LEFT, padx=5)

    next_word_button = tk.Button(button_frame, text="Next Word", command=next_word, state=tk.DISABLED)
    next_word_button.pack(side=tk.LEFT, padx=5)

    correct_word_label = tk.Label(root, text="")
    correct_word_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_learning()
