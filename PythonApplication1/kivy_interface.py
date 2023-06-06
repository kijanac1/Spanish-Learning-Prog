import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import wordsAndDefinitions
import Homonym_Mode

# Menu class responsible for generating the initial menu
class Menu(GridLayout):
    def __init__(self):
        super(Menu, self).__init__()
        self.cols = 1
        unlimited_button = Button(text="Unlimited Mode", on_press=self.unlimited_quiz) # calls unlimited_quiz function when called
        self.add_widget(unlimited_button) # creates button for unlimited mode
        timed_button = Button(text="Timed Mode", on_press=self.timed_quiz) # calls timed_quiz function when called
        self.add_widget(timed_button) # creates button for timed mode
        homonym_button = Button(text="Homonym Challenge", on_press=self.homonym_mode) # calls homonym_mode function when called
        self.add_widget(homonym_button) # creates button for homonym mode

    def unlimited_quiz(self, instance): # function call to start quiz
        self.clear_widgets()  # Clears the menu
        self.quiz = Quiz("unlimited") # calls the Quiz class
        self.add_widget(self.quiz) # Quiz class replaces menu in GUI

    def timed_quiz(self, instance): # function call to start quiz
        self.clear_widgets()  # Clears the menu
        self.quiz = Quiz("timed") # calls the Quiz class
        self.add_widget(self.quiz) # Quiz class replaces menu in GUI

    def homonym_mode(self, instance):
        self.clear_widgets()
        self.quiz = Homonym_Mode.Quiz_HomonymMode()
        self.add_widget(self.quiz)



# this class is responsible for the main logic of the app
class Quiz(GridLayout):
    def __init__(self, mode):
        super(Quiz, self).__init__()
        self.cols = 1
        self.spanish_words = wordsAndDefinitions.spanish_words2 # combines all word arrays
        self.definitions = wordsAndDefinitions.english_translations # combines all definition arrays
        self.reviewed_words = [] # will store all words player reviews
        self.missed_words = [] # space that will hold all words player gets incorrect
        self.missed_words_bool = [] # will store if review_word was missed or correct
        self.totalScore = 0 # initiates user total score
        self.mode = mode
        if mode == "timed":
            self.generate_question()
            self.start_timer()
        else: 
            self.generate_question()
    

    # function is called when user selects timed mode
    def start_timer(self): 
        self.remaining_time = 7 # Amount of time user has
        Clock.schedule_interval(self.update_time, 1)  # Call update_time every second
        self.time_label = Label(text="Remaining Time: " + str(self.remaining_time))
        self.add_widget(self.time_label)

    # this function is responsible for updating game timer every second
    def update_time(self, dt):
        self.remaining_time -= 1
        self.time_label.text = "Remaining Time: " + str(self.remaining_time)
        if self.remaining_time == 0:
            self.end_game()
        

    ## this function responsible for generating a each question for user
    ## will generate a spanish word, and generate four options for the
    ## user to select the correct answer
    def generate_question(self):
        self.clear_widgets()  # Clear previous widgets

        i = random.randint(0, len(self.spanish_words) - 1)  # This determines the index of the spanish word in our array
        word = self.spanish_words[i]  # Assign the indexed word to a variable that user will need to translate

        # Randomly select three other indexes
        x = random.randint(0, len(self.spanish_words) - 1)
        y = random.randint(0, len(self.spanish_words) - 1)
        z = random.randint(0, len(self.spanish_words) - 1)

        # these while loops are to make sure the correct definition doesn't appear more than once
        # if a definition equals another definition, it loops until the definition isn't repeated
        while self.definitions[x] == self.definitions[i]:
            x = random.randint(0, len(self.spanish_words) - 1)
        while self.definitions[y] == self.definitions[i] or self.definitions[y] == self.definitions[x]:
            y = random.randint(0, len(self.spanish_words) - 1)
        while self.definitions[z] == self.definitions[i] or self.definitions[z] == self.definitions[x] or self.definitions[z] == self.definitions[y]:
            z = random.randint(0, len(self.spanish_words) - 1)


        # Assign each definition which will show up as a choice for the user to select
        correctChoice = self.definitions[i]  # This is the correct definition
        wrongChoice1 = self.definitions[x]  # Incorrect definition #1
        wrongChoice2 = self.definitions[y]  # Incorrect definition #2
        wrongChoice3 = self.definitions[z]  # Incorrect definition #3

        # Randomly select the letter option to put answers in a randomly generated order
        options = ['a', 'b', 'c', 'd']
        letter = random.choice(options)

        bold_word = "[color=#7E8CBD][b]" + word + "[/b][/color]" # formats word to stand out when printed
        self.add_widget(Label(text="What is the correct definition? \n \n" + bold_word, halign='center', markup=True)) # label prints question to user
        ##self.layout.add_widget(Label(text=word)) # prints the spanish word user needs to translate

        # Add buttons for the answer choices
        if letter == 'a': # sets correct answer as first widget
            self.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice, word))) # a
            self.add_widget(Button(text=wrongChoice1, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=wrongChoice2, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=wrongChoice3, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
        elif letter == 'b': # sets correct answer as second widget
            self.add_widget(Button(text=wrongChoice1, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice, word))) # b
            self.add_widget(Button(text=wrongChoice2, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=wrongChoice3, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
        elif letter == 'c': # sets correct answer as third widget
            self.add_widget(Button(text=wrongChoice1, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=wrongChoice2, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice, word))) # c
            self.add_widget(Button(text=wrongChoice3, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
        elif letter == 'd': # sets correct answer as fourth widget
            self.add_widget(Button(text=wrongChoice1, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=wrongChoice2, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=wrongChoice3, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice, word))) # d
        if self.mode == "unlimited":
            # this line of code will create a button to exit unlimited mode when the user wishes
            # will take to screen to review missed words
            button = Button(text="Exit Session", on_press=lambda instance: self.review_missed_words())
            button.background_color = get_color_from_hex("#0000FF")
            self.add_widget(button)


    ## This function is called when an answer is selected by the user. 
    ## takes button press and correctChoice as arguments
    def check_answer(self, instance, correctAnswer, word):
        userAnswer = instance.text.lower()  # gets text from button pressed. Converts text to lowercase
        if correctAnswer != userAnswer: # compares the correct answer to answer user selected
            print("INCORRECT")
            self.reviewed_words.append(word + " - " + correctAnswer)
            self.missed_words_bool.append("true")
            self.missed_words.append(correctAnswer)
        elif correctAnswer == userAnswer:
            print("CORRECT")
            self.totalScore += 1 # adds point to total user score
            self.reviewed_words.append(word + " - " + correctAnswer)
            self.missed_words_bool.append("false")
        self.generate_question()  # Regenerate a new question
        if self.mode == "timed":
            self.time_label = Label(text="Remaining Time: " + str(self.remaining_time)) 
            self.add_widget(self.time_label) # regenerating time label since the app screen is cleared

    ## this function prints end screen when called. Prints "Game Over" and player final score
    def end_game(self): 
        self.clear_widgets()
        # assigns "Game Over" text and final score to a label
        total_amt_words = len(self.missed_words_bool) # tally of total amount of questions user had
        game_over_label = Label(text="Time's Up \n \n Total Correct Words: " + str(self.totalScore) + "/" + str(total_amt_words),\
           halign='center') # assigns label text to variable
        self.add_widget(game_over_label) # prints final game over screen text

        self.add_widget(Button(text="Review Missed Words", on_press=lambda instance: self.review_missed_words()))
    
    def review_missed_words(self):
        self.clear_widgets() # clears screen
        missed_word_text = "[color=#7E8CBD][b] Missed Words Will Show in Red: [/color][/b]"
        missed_words_label = Label(text=missed_word_text, halign='center', markup=True)
        missed_words_label.size_hint = (None, None)  # Disable automatic size adjustment
        missed_words_label.size = (2000, 350)  # Set the size manually (width, height)
        self.add_widget(missed_words_label) # prints text to screen

        # updated this function so it shows all reviewed words, not just missed words. Will show missed words in red text.
        for i in range(len(self.missed_words_bool)): # loops through each word and prints to screen
            if self.missed_words_bool[i] == "true":
                label = Label(text=self.reviewed_words[i], color=(0.7, 0, 0, 1))  # Prints red if word was missed
            else:
                label = Label(text=self.reviewed_words[i]) # word prints white otherwise
            label.size_hint = (None, None)  # Disable automatic size adjustment
            label.size = (2000, 50)  # Set the size manually (width, height)

            self.add_widget(label) # prints final list of words to screen

class QuizApp(App):
    def build(self):
        self.layout = Menu()  # Initial menu screen
        return self.layout



### will have timed mode
### unlimited mode
### add more words
### conjugation mode
### homonym mode