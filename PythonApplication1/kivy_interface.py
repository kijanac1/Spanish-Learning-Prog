import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock


class QuizApp(App):
    def build(self):
        self.remaining_time = 30  # Amount of time user has
        self.layout = GridLayout(cols=1)  # Layout to hold the widgets
        self.spanish_words = ["el / la", "de", "que", "y", "a", "en", "un", "ser", "se", "no", 
        "haber", "por", "con", "su", "para", "como", "estar", "tener", "le", "lo", \
        "lo", "todo", "pero", "más", "hacer", "o", "poder", "decir", "este / esta", "ir", \
        "otro", "ese", "la", "si", "me", "ya", "ver", "porque", "dar", "cuando", \
        "él", "muy", "sin", "vez", "mucho", "saber", "qué", "sobre", "mi", "alguno", \
        "mismo", "yo", "también", "hasta", "año", "dos", "querer", "entre", "así", 'primero', \
        "desde", "grande", "eso", "ni", "nos", "llegar", "pasar", "tiempo", "ella", "sí", \
        "día", "uno", "bien", "poco", "deber", "entonces", "poner", "cosa", "tanto", "hombre", \
        "parecer", "nuestro", "tan", "donde", "ahora", "parte", "después", "vida", "quedar", "siempre", \
        "creer", "hablar", "llevar", "dejar", "nada", "cada", "seguir", "menos", "nuevo", "encontrar" ]

        self.definitions = ["the", "of, from", "that, which", "and", "to, at", "in, on", "a, an", "to be", "-self, oneself", "no", \
        "to have", "by, for, through", "with", "his, her, their, your", "for, to, in order to", "like, as", "to be", "to have", \
        "[3rd pers. indirect object pronoun]", "the", \
        "[3rd pers. masc. direct object pronoun]", "all, every", "but, yet, except", "more", "to do, make", "or", "to be able to, can", \
        "to tell, say", "this", "to go", \
        "other, another", "that", "[3rd pers. fem. direct object pronoun]", "if, whether", "me", "already, still", "to see", \
        "because", "to give", "when", "he", "very, really", "without", "time, occurrence", "much, many", "to know", \
        "what?, which?, how?", "on top of, over, about", "my", "some, someone", "same", "I", "also", "until, up to", "year", \
        "two", "to want, love", "between", "like that", "first", "from, since", "large, great, big", "that", "not even, neither, nor", \
        "us", "to arrive", "to pass, spend (time)", "time, weather", "she", "yes", "day", "one", "well", "little, few", \
        "should, out to, to owe", "so, then", "to put, get", "thing", "much", "man, mankind, husband", "to seem, look like", "our", \
        "such, too, so", "where", "now", "part, portion", "after", "life", "to remain, stay", "always", "to believe", "to speak, talk", \
        "to take, carry", "to let, leave", "nothing", "each, every", "to follow", "less, fewer", "new", "to find" ]

        self.generate_question()
        return self.layout

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

        self.layout.add_widget(Label(text="What is the correct definition?")) # label prints question to user
        self.layout.add_widget(Label(text=word)) # prints the spanish word user needs to translate

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
        self.generate_question()  # Regenerate a new question

QuizApp().run()

### will have timed mode
### unlimited mode
### add more words
### conjugation mode
### homonym mode