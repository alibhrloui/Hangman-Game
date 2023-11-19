    # Hangman game
    #### Video Demo:  <https://youtu.be/vf36DJKqTJw>
    #### Description:
    The program starts by importing the choice function from the random module, which will be used to randomly select a word from a predefined list.

Next, there is a list called charactor which contains ASCII art representations of different situations. These are used to display a hanging man or rabbit character based on the player's mistakes.

The word_list is a list of words that can be chosen for the player to guess. Each word is in lowercase.

The variable hearts represents the number of lives the player has, while word is initialized with a randomly selected word from word_list. The chosen word is converted to uppercase.

The variable miss keeps track of the player's mistakes, and used is a list that stores the letters the player has already guessed.

The main() function is the entry point of the program. It calls three other functions: ready_player(), gaming(), and game_over().

The ready_player() function prompts the player to enter their name and checks if it is a valid name (consisting of alphabetic characters, between 3 and 15 characters long). Once a valid name is entered, a welcome message is displayed along with the number of lives the player has.

The gaming() function is the main game loop. It continues until the player runs out of lives (miss equals hearts) or guesses the word correctly (so_far equals word). In each iteration, it displays the current state of the hanging character, the letters the player has guessed, and the partially revealed word. The player is prompted to enter a guess, and the input is validated to be a single alphabetical character. If the guess has already been used,it prompts the player to guess again. If the guess is a new letter, it is added to the used list. If the guess is correct (found in the word), the program reveals the positions of the guessed letter in the word by updating the so_far variable. If the guess is incorrect, the program increments the miss variable and displays a message indicating that the letter is not in the word.

The game_over() function is called after the game loop ends. If the player has run out of lives (miss equals hearts), it displays the final state of the hanging character and a message indicating that the player lost. If the player has guessed the word correctly, it displays a message indicating that the player won. In both cases, it also reveals the word.

Finally, the program is executed by calling main().

Overall, this program is a simple word-guessing game where the player tries to guess a randomly chosen word within a limited number of attempts. The game provides visual feedback using ASCII art to represent the hanging character and displays the current state of the word being guessed.
