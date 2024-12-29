import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
import wordsAndDefinitions

# this class is responsible for the main logic of the app
class Quiz_HomonymMode(GridLayout):
    def __init__(self):
        super(Quiz_HomonymMode, self).__init__()
        self.cols = 1
        self.homonyms1 = wordsAndDefinitions.homonyms1
        self.homonyms2 = wordsAndDefinitions.homonyms2
        self.homonyms1_def = wordsAndDefinitions.homonyms1_def
        self.homonyms2_def = wordsAndDefinitions.homonyms2_def
        self.reviewed_words = [] # will store all words player reviews
        self.missed_words = [] # space that will hold all words player gets incorrect
        self.missed_words_bool = [] # will store if review_word was missed or correct
        self.totalScore = 0 # initiates user total score
        self.generate_question()
        self.start_timer() # this mode will be timed by default 

    # function is called when user selects timed mode
    def start_timer(self): 
        self.remaining_time = 30 # Amount of time user has
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
    ## will generate a spanish word, and generate two english definitions
    ## user to select the correct answer
    def generate_question(self):
        self.clear_widgets()  # Clear previous widgets

        i = random.randint(0, len(self.homonyms1) - 1)  # This determines the index of the spanish word in our array
        array_selection = random.randint(0,1) # randomly selects if picking from homonym1 array or homonym2 array
        if array_selection == 0:
            word = self.homonyms1[i] # Assign the indexed word from first array to a variable
            # Assign each definition which will show up as a choice for the user to select
            correctChoice = self.homonyms1_def[i] # assigns correct translation to variable
            wrongChoice = self.homonyms2_def[i] # assigns incorrect translation to variable
        elif array_selection == 1: 
            word = self.homonyms2[i] # Assign the indexed word from second array to a variable
            # Assign each definition which will show up as a choice for the user to select
            correctChoice = self.homonyms2_def[i] # assigns correct translation to variable
            wrongChoice = self.homonyms1_def[i] # assigns incorrect translation to variable


        # Randomly select the letter option to put answers in a randomly generated order
        options = ['a', 'b']
        letter = random.choice(options)

        bold_word = "[color=#7E8CBD][b]" + word + "[/b][/color]" # formats word to stand out when printed
        self.add_widget(Label(text="What is the correct translation? \n \n" + bold_word, halign='center', markup=True)) # label prints question to user
        ##self.layout.add_widget(Label(text=word)) # prints the spanish word user needs to translate

        # Add buttons for the answer choices
        if letter == 'a': # sets correct answer as first widget
            self.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice, word))) # a
            self.add_widget(Button(text=wrongChoice, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
        elif letter == 'b': # sets correct answer as second widget
            self.add_widget(Button(text=wrongChoice, on_press=lambda instance: self.check_answer(instance, correctChoice, word)))
            self.add_widget(Button(text=correctChoice, on_press=lambda instance: self.check_answer(instance, correctChoice, word))) # b


    ## This function is called when an answer is selected by the user. 
    ## takes button press and correctChoice as arguments
    def check_answer(self, instance, correctAnswer, word):
        userAnswer = instance.text.lower()  # gets text from button pressed. Converts text to lowercase
        if correctAnswer.lower() != userAnswer: # compares the correct answer to answer user selected
            print("INCORRECT")
            self.reviewed_words.append(word + " - " + correctAnswer)
            self.missed_words_bool.append("true")
            self.missed_words.append(correctAnswer)
        elif correctAnswer.lower() == userAnswer:
            print("CORRECT")
            self.totalScore += 1 # adds point to total user score
            self.reviewed_words.append(word + " - " + correctAnswer)
            self.missed_words_bool.append("false")
        self.generate_question()  # Regenerate a new question
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
        self.clear_widgets()  # clears screen

        # Create a ScrollView to hold the list of missed words
        scroll_view = ScrollView()
        words_layout = GridLayout(cols=1, size_hint_y=None)
        words_layout.bind(minimum_height=words_layout.setter('height'))  # Adjust height based on content

        # Title for the missed words screen
        missed_word_text = "[color=#7E8CBD][b]Missed Words Will Show in Red:[/b][/color]"
        title_label = Label(text=missed_word_text, halign='center', markup=True, size_hint_y=None, height=50)
        self.add_widget(title_label)

        # Add each reviewed word to the layout
        for i in range(len(self.missed_words_bool)):
            if self.missed_words_bool[i] == "true":
                label = Label(text=self.reviewed_words[i], color=(0.7, 0, 0, 1), size_hint_y=None, height=40)
            else:
                label = Label(text=self.reviewed_words[i], size_hint_y=None, height=40)
            words_layout.add_widget(label)

        # Add the layout with words to the scroll view
        scroll_view.add_widget(words_layout)
        self.add_widget(scroll_view)