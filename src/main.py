from languages.english import english
from languages.spanish import spanish
from languages.german import german
from languages.portuguese import portuguese
from languages.italian import italian

def main():
    while True:
        try:
            language = int(input("Choice the language \n 1. English \n 2. Spanish \n 3. German \n 4. Portuguese \n 5. Italian \n Just insert the correspondent number: "))
        except:
            print("Error! Invalid value. Try again.")
        else:
            if language != 1 and language != 2 and language != 3 and language != 4 and language != 5:
                print("Error! Invalid value. Try again.")
            else:
                break

    if language == 1:
        english()
    elif language == 2:
        spanish()
    elif language == 3:
        german()
    elif language == 4:
        portuguese()
    else:
        italian()

main() 