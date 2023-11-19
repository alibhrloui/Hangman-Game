# importing random module to use random choice
from random import choice


# our charactor and different situations
charactor = [
    """
                                      (\_/)
                                      (ಠ_ಠ)
                                  ＿ノヽ ノ＼＿
                                /`/ ⌒  Ｙ⌒Ｙ   )
                              ( (三ヽ 人  /    |
                              | ﾉ⌒＼ ￣￣ヽ   ノ
▬▬ι═══════ﺤ                    ヽ＿＿＿＞､＿＿／
                                    |( 王 ﾉ〈
                                    /ﾐ`ー―彡
                                  |╰        ╯|
                                  |    /\    |
                                  |   /  \   |
                                  |  /    \  |
""",
    """
                                      (\_/)
                                      (ಠ_ಠ)
                                  ＿ノヽ ノ＼＿
                                /`/ ⌒  Ｙ⌒Ｙ   )
                              ( (三ヽ 人  /    |
                              | ﾉ⌒＼ ￣￣ヽ   ノ
       ▬▬ι═══════ﺤ             ヽ＿＿＿＞､＿＿／
                                    |( 王 ﾉ〈
                                    /ﾐ`ー―彡
                                  |╰        ╯|
                                  |    /\    |
                                  |   /  \   |
                                  |  /    \  |
""",
    """
                                      (\_/)
                                      (ಠ_ಠ)
                                  ＿ノヽ ノ＼＿
                                /`/ ⌒  Ｙ⌒Ｙ   )
                              ( (三ヽ 人  /    |
                              | ﾉ⌒＼ ￣￣ヽ   ノ
               ▬▬ι═══════ﺤ     ヽ＿＿＿＞､＿＿／
                                    |( 王 ﾉ〈
                                    /ﾐ`ー―彡
                                  |╰        ╯|
                                  |    /\    |
                                  |   /  \   |
                                  |  /    \  |
""",
    """
                                      (\_/)
                                      (ಠ_ಠ)
                                  ＿ノヽ ノ＼＿
                                /`/ ⌒  Ｙ⌒Ｙ   )
                              ( (三ヽ 人  /    |
                              | ﾉ⌒＼ ￣￣ヽ   ノ
                   ▬▬ι═══════ﺤ ヽ＿＿＿＞､＿＿／
                                    |( 王 ﾉ〈
                                    /ﾐ`ー―彡
                                  |╰        ╯|
                                  |    /\    |
                                  |   /  \   |
                                  |  /    \  |
""",
    """
                                      (\_/)
                                      (ಥ_ಥ)
                                  ＿ノヽ ノ＼＿
                                /`/ ⌒  Ｙ⌒Ｙ   )
                              ( (三ヽ 人  /    |
                              | ﾉ⌒＼ ￣￣ヽ   ノ
                          ▬▬ι═══════ﺤ 🩸＿＞､＿＿／
                                    |( 王 ﾉ〈
                                    /ﾐ`ー―彡
                                  |╰        ╯|
                                  |    /\    |
                                  |   /  \   |
                                  |  /    \  |
""",
]

word_list = [
    "apple",
    "banana",
    "carrot",
    "dog",
    "elephant",
    "fish",
    "grape",
    "horse",
    "ice cream",
    "jellyfish",
    "kiwi",
    "lemon",
    "monkey",
    "nut",
    "orange",
    "pear",
    "quail",
    "rabbit",
    "strawberry",
    "turtle",
    "umbrella",
    "violet",
    "watermelon",
    "xylophone",
    "yogurt",
    "zebra",
]

# player lives
hearts = 5

# the word to be guessed
word = choice(word_list).upper()

# player's mistakes
miss = 0

# list to keep track of letters already guessed
used = []


def main():
    ready_player()
    gaming()
    game_over()


def ready_player():
    # to keep asking player and player put a valid name
    while True:
        a = input("Wellcome To My Little Game\nWhat Is Your Name Soldier? ")
        if a.isalpha() and len(a) > 2 and len(a) < 15:
            print(f"Hello {a}! You Have 5 Lives, Use It Wisely...\nEnjoy :))")
            break
        else:
            print("\nWrite a proper Name Son! \n")
            continue


def gaming():
    global miss

    so_far = "-" * len(word)

    while miss < hearts and so_far != word:
        print(charactor[miss])
        print("\nYou've used the following letters:\n", used)
        print("\nSo far, you have guessed:\t", so_far)

        while True:
            guess = input("Enter your guess:\t")
            if guess.isalpha() and len(guess) == 1:
                guess = guess.upper()
                break
            else:
                continue

        try:
            if guess in used:
                print("You already guessed the letter:", guess)
                while True:
                    guess = input("Guess again:\t")
                    if guess.isalpha() and len(guess) == 1:
                        guess = guess.upper()
                        break
                    else:
                        continue

            used.append(guess)

            if guess in word:
                print(f"The letter {guess} is in the word")
                new = ""
                for x in range(len(word)):
                    if guess == word[x]:
                        new += guess
                    else:
                        new += so_far[x]
                so_far = new
            else:
                print("\nSorry, {} isn't in the word".format(guess))
                miss += 1

        except (TypeError, ValueError):
            continue

        continue


def game_over():
    global miss
    # when player lost
    if miss == hearts:
        print(charactor[4] + "OH NO! so close Sorry...RIP")

    else:
        # when player wins
        print("\nWinner Winner Chicken Dinner!")

    print("\nThe word was", word.lower())

    input("\nPress Enter key to exit")


if __name__ == "__main__":
    main()
