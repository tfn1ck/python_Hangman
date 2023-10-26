import random


class HangmanGame:
    def __init__(self, words, max_lives=6):
        self.words = words
        self.max_lives = max_lives
        self.reset()

    def reset(self):
        self.c_word = random.choice(self.words).lower()
        self.size = len(self.c_word)
        self.hidden_word = ['_' for _ in range(self.size)]
        self.lives = self.max_lives

    def display_hidden_word(self):
        return ' '.join(self.hidden_word)

    def make_guess(self, guess):
        if guess == '0':
            print("Thank you for playing!")
            return False
        elif guess in self.hidden_word:
            print("You've already guessed that letter. Try a different one.")
        else:
            correct_guess = False
            for pos in range(self.size):
                letter = self.c_word[pos]
                if letter == guess:
                    self.hidden_word[pos] = letter
                    correct_guess = True

            if not correct_guess:
                self.lives -= 1
                self.display_hangman()

            if "_" not in self.hidden_word:
                print(f"Congratulations! You've won. The word was '{self.c_word}'.")
                return False
            elif self.lives == 0:
                print(f"You lose! The word was '{self.c_word}'. Try again.")
                return False
        return True

    def display_hangman(self):
        stages = ['''
        +--+
        |  |
           |
           |
           |
           |
       =====''',
                  '''
        +--+
        |  |
        O  |
           |
           |
           |
       =====''',
                  '''
        +--+
        |  |
        O  |
        |  |
           |
           |
       =====''',
                  '''
        +--+
        |  |
        O  |
       /|  |
           |
           |
       =====''',
                  '''
        +--+
        |  |
        O  |
       /|\\ |
           |
           |
       =====''',
                  '''
        +--+
        |  |
        O  |
       /|\\ |
       /   |
           |
       =====''',
                  '''
        +--+
        |  |
        O  |
       /|\\ |
       / \\ |
           |
       =====''']

        print(stages[self.max_lives - self.lives])

    def play(self):
        print("Welcome to Hangman!")
        while self.lives > 0:
            print(f"Hidden Word: {self.display_hidden_word()}")
            print(f"Lives left: {self.lives}")
            guess = input("Make a guess (Press 0 to stop): ").lower()
            if not self.make_guess(guess):
                break


if __name__ == "__main__":
    words = [
        "Apple", "Banana", "Chair", "Dance", "Elephant", "Flower", "Guitar", "Happy", "Igloo", "Juggle",
        "Kite", "Lemon", "Mouse", "Number", "Orange", "Pizza", "Quilt", "Rabbit", "Soccer", "Turtle",
        "Umbrella", "Violin", "Water", "Xylophone", "Yellow", "Zebra", "Bear", "Cat", "Dog", "Egg",
        "Fish", "Grapes", "Hat", "Ice", "Jelly", "Key", "Lollipop", "Moon", "Nest", "Owl", "Penguin",
        "Quack", "Rainbow", "Sun", "Tiger", "Unicorn", "Vase", "Watch", "X-ray", "Yacht", "Zipper",
        "Bag", "Car", "Dinosaur", "Elephant", "Fire", "Gorilla", "House", "Ice Cream", "Jellyfish",
        "Kangaroo", "Lizard", "Monkey", "Notebook", "Octopus", "Parrot", "Queen", "Rainbow", "Snake",
        "Train", "Umbrella", "Volcano", "Watermelon", "Xylophone", "Yak", "Zebra", "Airplane", "Boat",
        "Cupcake", "Duck", "Football", "Giraffe", "Helicopter", "Iguana", "Jellybean", "Kangaroo",
        "Lighthouse", "Motorcycle", "Narwhal", "Octagon", "Penguin", "Rainbow", "Seahorse", "Turtle",
        "Unicorn", "Violin", "Waterfall", "X-ray", "Yak", "Zucchini"
    ]
    game = HangmanGame(words)
    game.play()
