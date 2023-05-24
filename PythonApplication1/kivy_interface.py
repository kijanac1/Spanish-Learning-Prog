import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import wordsAndDefinitions


# this class is responsible for the main logic of the app
class QuizApp(App):
    def build(self):
        self.spanish_words = wordsAndDefinitions.spanish_words
        self.definitions = wordsAndDefinitions.definitions

        self.layout = GridLayout(cols=1)  # Layout to hold the widgets
        self.remaining_time = 30  # Amount of time user has
        self.totalScore = 0 # initiates user total score
        self.time_label = Label(text="Remaining Time: " + str(self.remaining_time))
        self.layout.add_widget(self.time_label)
        Clock.schedule_interval(self.update_time, 1)  # Call update_time every second
        self.generate_menu()  # Generate the initial menu
        return self.layout

    # this function is called when game starts. Generates menu
    def generate_menu(self): 
        self.layout.clear_widgets()  # Clear previous widgets
        start_button = Button(text="Start Quiz", on_press=self.start_quiz)
        self.layout.add_widget(start_button)

    # function is called when user selects to start quiz
    def start_quiz(self, instance): 
        self.layout.clear_widgets() # clears screen to generate updated screen
        self.generate_question() # generates first question

    ## this function responsible for generating a each question for user
    ## will generate a spanish word, and generate four options for the
    ## user to select the correct answer
    def generate_question(self):
        self.layout.clear_widgets()  # Clear previous widgets

        i = random.randint(0, len(self.spanish_words) - 1)  # This determines the index of the spanish word in our array
        word = self.spanish_words[i]  # Assign the indexed word to a variable that user will need to translate

        # Randomly select three other indexes
        x = random.randint(0, len(self.spanish_words) - 1)
        y = random.randint(0, len(self.spanish_words) - 1)
        z = random.randint(0, len(self.spanish_words) - 1)

        # these while loops are to make sure the correct definition doesn't appear more than once
        while x == i:
            x = random.randint(0, len(self.spanish_words) - 1)
        while y == i or y == x:
            y = random.randint(0, len(self.spanish_words) - 1)
        while z == i or z == x or z == y:
            z = random.randint(0, len(self.spanish_words) - 1)


        # Assign each definition which will show up as a choice for the user to select
        correctChoice = self.definitions[i]  # This is the correct definition
        wrongChoice1 = self.definitions[x]  # Incorrect definition #1
        wrongChoice2 = self.definitions[y]  # Incorrect definition #2
        wrongChoice3 = self.definitions[z]  # Incorrect definition #3

        # Randomly select the letter option to put answers in a randomly generated order
        options = ['a', 'b', 'c', 'd']
        letter = random.choice(options)

        word = "[color=#7E8CBD][b]" + word + "[/b][/color]" # formats word to stand out when printed
        self.layout.add_widget(Label(text="What is the correct definition? \n \n" + word, halign='center', markup=True)) # label prints question to user
        ##self.layout.add_widget(Label(text=word)) # prints the spanish word user needs to translate

        # Add buttons for the answer choices
        if letter == 'a': # sets correct answer as first widget
            self.layout.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice))) # a
            self.layout.add_widget(Button(text=wrongChoice1, on_press=lambda instance: self.check_answer(instance, correctChoice)))
            self.layout.add_widget(Button(text=wrongChoice2, on_press=lambda instance: self.check_answer(instance, correctChoice)))
            self.layout.add_widget(Button(text=wrongChoice3, on_press=lambda instance: self.check_answer(instance, correctChoice)))
        elif letter == 'b': # sets correct answer as second widget
            self.layout.add_widget(Button(text=wrongChoice1, on_press=lambda instance: self.check_answer(instance, correctChoice)))
            self.layout.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice))) # b
            self.layout.add_widget(Button(text=wrongChoice2, on_press=lambda instance: self.check_answer(instance, correctChoice)))
            self.layout.add_widget(Button(text=wrongChoice3, on_press=lambda instance: self.check_answer(instance, correctChoice)))
        elif letter == 'c': # sets correct answer as third widget
            self.layout.add_widget(Button(text=wrongChoice1, on_press=lambda instance: self.check_answer(instance, correctChoice)))
            self.layout.add_widget(Button(text=wrongChoice2, on_press=lambda instance: self.check_answer(instance, correctChoice)))
            self.layout.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice))) # c
            self.layout.add_widget(Button(text=wrongChoice3, on_press=lambda instance: self.check_answer(instance, correctChoice)))
        elif letter == 'd': # sets correct answer as fourth widget
            self.layout.add_widget(Button(text=wrongChoice1, on_press=lambda instance: self.check_answer(instance, correctChoice)))
            self.layout.add_widget(Button(text=wrongChoice2, on_press=lambda instance: self.check_answer(instance, correctChoice)))
            self.layout.add_widget(Button(text=wrongChoice3, on_press=lambda instance: self.check_answer(instance, correctChoice)))
            self.layout.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice))) # d

    ## This function is called when an answer is selected by the user. 
    ## takes button press and correctChoice as arguments
    def check_answer(self, instance, correctAnswer): 
        userAnswer = instance.text.lower()  # gets text from button pressed. Converts text to lowercase
        if correctAnswer != userAnswer: # compares the correct answer to answer user selected
            print("INCORRECT")
        elif correctAnswer == userAnswer:
            print("CORRECT")
            self.totalScore += 1 # adds point to total user score
        self.generate_question()  # Regenerate a new question

    # this function is responsible for updating game timer every second
    def update_time(self, dt):
        self.remaining_time -= 1
        self.time_label.text = "Remaining Time: " + str(self.remaining_time)
        if self.remaining_time == 0:
            self.end_game()

    ## this function prints end screen when called. Prints "Game Over" and player final score
    def end_game(self): 
        self.layout.clear_widgets()
        # assigns "Game Over" text and final score to a label
        game_over_label = Label(text="Time's Up \n \n Total Correct Words: " + str(self.totalScore), halign='center') # assigns label text to variable
        self.layout.add_widget(game_over_label) # prints final game over screen text

### will have timed mode
### unlimited mode
### add more words
### conjugation mode
### homonym mode