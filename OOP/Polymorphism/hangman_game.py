import random


# Abstract Game class
class Game:
    def __init__(self, name):
        self._name = name

    def play():
        pass  # Abstract method to be implemented by subclasses

    def check_correct_answer():
        pass


# Hangman game
class Hangman(Game):
    def __init__(self):
        super().__init__("Hangman")
        self._word_list = [
            "python", "hangman", "game"
            , "programming", "challenge",
            "polymorphism","abstraction"
            ]
        self._attempts = 2
        self._word = random.choice(self._word_list) #select randomly from word_list
        self._guessed_letters=set() # ?
        self._check = False # returns True if your answer is correct
        
    def play(self):
        print(f"Welcome to {self._name}!")
        while self._attempts > 0 and set(self._word) != self._guessed_letters :
            self.display_word()
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha() : #enter just one letter
                if guess in self._guessed_letters :
                    print('you have already guessed the letter')
                elif guess in self._word :
                    self._guessed_letters.add(guess)
                    print('Good guess !')
                else :
                    self._attempts -= 1
                    print(f"Incorrect guess. {self._attempts} attempts left.")
                    
            else:
                print("Invalid input. Please guess a single letter.")
        self.display_result()
         
            
    def display_word(self):
        display =""
        for letter in self._word :
            if letter in self._guessed_letters :
                display += letter
            else :
                display += '_'
        print(display)

#display_word = map(lambda i : i if in self._guessed_letters else '_' ,self._word)
       
    def display_result(self):
        if set(self._word) == self._guessed_letters :
            self._check = True
            print(f"Congratulations! You've guessed the word: {self._word}")
        else : 
            print(f"Game over! The word was: {self._word}")
            
    def check_correct_answer(self):
        return self._check


# Math Games
class MathGame(Game):
    def __init__(self):
        super().__init__('Math Game')    
        self._check = False
        
    def play(self):
        print(f"Welcome to {self._name}!")
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        answer = num1 + num2
        user_input = int(input(f"What is {num1} + {num2}? "))            
        if user_input == answer :
            self._check = True
            print("Correct answer! Well done.")
        else :
            print(f"Incorrect. The correct answer is {answer}.")
            
    def check_correct_answer(self):
        return self._check


# Main program

list_of_games=[]

for _ in range(5): 
    list_of_games.append(Hangman())
for _ in range(5):
    list_of_games.append(MathGame())
    
random.shuffle(list_of_games) #we shuffle the list of games
your_score = 0
for game in list_of_games:
    game.play()
    if game.check_correct_answer() :
        your_score += 1
print(f'Your score is {your_score}/10')