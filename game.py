from random import choice
from unicodedata import normalize
import os


def play():
    clear_console()
    welcome()

    difficulty = choose_difficulty()

    [tip, secret_word] = random_word(difficulty)
    correct_letters = ["_" for letter in secret_word]
    letters_used = []
    hanged = False
    hit = False
    errors = 0

    while not hanged and not hit:
        display_information(correct_letters, tip)

        choice = remove_accents(str(input("Digite uma letra: ")).strip().upper())
        clear_console()

        if choice in remove_accents(secret_word):
            correct_choice_mark(secret_word, choice, correct_letters)
            draw_hangman(errors, letters_used)
        else:
            errors += 1
            letters_used.append(choice) if choice not in letters_used else None
            draw_hangman(errors, letters_used)
            print(blue(f"\nA letra {choice} não foi encontrada na palavra secreta.\n"))

        hit = not "_" in correct_letters
        hanged = errors == 6

    if hit:
        winner()
    else:
        loser()

    print(yellow(f"\nA palavra era: {secret_word.capitalize()}"))
    print("\n", 10 * ">", " Fim do jogo! ", 10 * "<", "\n")


def welcome():
    text_welcome = "Welcome to the Hangman Game!"
    print("\n" + len(text_welcome) * "*")
    print(text_welcome)
    print(len(text_welcome) * "*" + "\n")


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def choose_difficulty():
    input_difficulty = int(
        input(
            "Qual nível de dificuldade?\n\n(1) Fácil\n(2) Médio\n(3) Difícil\n\nEscolha: "
        )
    )
    print()
    input_difficulty = 4 if input_difficulty > 3 else input_difficulty

    difficulties = ["easy_words", "medium_words", "hard_words", "words"]
    return difficulties[input_difficulty - 1]


def remove_accents(palavra):
    return normalize("NFKD", palavra).encode("ASCII", "ignore").decode("ASCII")


def random_word(file_name="words"):
    with open(f"./words/{file_name}.txt", "r") as arquivo:
        lines = arquivo.readlines()
        arquivo.close()
        lista_palavras = [list(line.split()) for line in lines]
        tip_palavra = choice(lista_palavras)
        tip_palavra[1] = tip_palavra[1].upper()
        return tip_palavra


def correct_choice_mark(secret_word, choice, correct_letters):
    index = 0
    for letter in secret_word:
        if choice == remove_accents(letter):
            correct_letters[index] = letter
        index += 1
    print(
        blue(
            f"\nA letra {choice} foi encontrada {correct_letters.count(choice)} vezes.\n"
        )
    )


def display_information(correct_letters, tip):
    print(" ".join(correct_letters) + "\n")
    print(blue("Dica: " + tip + "\n"))


def blue(text):
    return f"\033[34m{text}\033[0;0m"


def yellow(text):
    return f"\033[33m{text}\033[0;0m"


def green(text):
    return f"\033[32m{text}\033[0;0m"


def red(text):
    return f"\033[31m{text}\033[0;0m"


def winner():
    print(
        green(
            "\nParabéns, você ganhou!\n"
            + "       ___________      \n"
            + "      '._==_==_=_.'     \n"
            + "      .-\\:      /-.    \n"
            + "     | (|:.     |) |    \n"
            + "      '-|:.     |-'     \n"
            + "        \\::.    /      \n"
            + "         '::. .'        \n"
            + "           ) (          \n"
            + "         _.' '._        \n"
            + "        '-------'       \n"
        )
    )


def loser():
    print(
        red(
            "Puxa, você foi enforcado!\n"
            + "    _______________         \n"
            + "   /               \       \n"
            + "  /                 \      \n"
            + "//                   \/\  \n"
            + "\|   XXXX     XXXX   | /   \n"
            + " |   XXXX     XXXX   |/     \n"
            + " |   XXX       XXX   |      \n"
            + " |                   |      \n"
            + " \__      XXX      __/     \n"
            + "   |\     XXX     /|       \n"
            + "   | |           | |        \n"
            + "   | I I I I I I I |        \n"
            + "   |  I I I I I I  |        \n"
            + "   \_             _/       \n"
            + "     \_         _/         \n"
            + "       \_______/           \n"
        )
    )


def draw_hangman(errors, letters_used):
    if errors >= 1:
        print("  _______     ")
        print(" |/      |    ")

    if errors == 1:
        print(" |     (o_o)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |     (o_o)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |     (o_o)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |     (o_o)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |     (o_o)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 6:
        print(" |     (x_x)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    if errors >= 1:
        print(" |            ")
        print("_|___         ")
        print()
        print("  ".join(letters_used) + "\n")


if __name__ == "__main__":
    play()
