from platform import system
import requests
import os

def main():
    choice = "y"
    index = int(input("Input starting index: "))
    while choice != "n":
        google_link = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl="
        print("Language Codes (ISO-639-1): https://cloud.google.com/translate/docs/languages")
        lang = input("Input language code: ")
        google_link += lang + "&q="
        text = input("Input text: ")
        text = text.split()

        for i, word in enumerate(text):
            if i != len(text) - 1:
                google_link += f"{word}+"
            else:
                google_link += f"{word}"

        print("URL:")
        print(google_link)

        myfile = requests.get(google_link)

        if system() == "Windows":
            path = f"{os.getcwd()}\\"
        else:
            path = f"{os.getcwd()}/"
            
        if index <= 9:
            open(f'{path}000{index}.mp3', 'wb').write(myfile.content)
        elif index <= 99:
            open(f'{path}00{index}.mp3', 'wb').write(myfile.content)
        elif index <= 999:
            open(f'{path}0{index}.mp3', 'wb').write(myfile.content)
        elif index <= 9999:
            open(f'{path}{index}.mp3', 'wb').write(myfile.content)
        
        index += 1

        choice = input("Again? (y / n): ")
        print("\n")

if __name__ == "__main__":
    main()
