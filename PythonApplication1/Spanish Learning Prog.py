import random

def main():
    generate_question()

    ## random select a spanish_words[i]
    ## randomly select three definitions
    ## correct answer equals definitons[i]
    ## options of a, b, c, d
       # make something to place in random order
    ## if inputted answer does not equal definitons[i], then wrong answer

def generate_question():
    spanish_words = ["el / la", "de", "que", "y", "a", "en", "un", "ser", "se", "no", 
        "haber", "por", "con", "su", "para", "como", "estar", "tener", "le", "lo", \
        "lo", "todo", "pero", "más", "hacer", "o", "poder", "decir", "este / esta", "ir", \
        "otro", "ese", "la", "si", "me", "ya", "ver", "porque", "dar", "cuando", \
        "él", "muy", "sin", "vez", "mucho", "saber", "qué", "sobre", "mi", "alguno", \
        "mismo", "yo", "también", "hasta", "año", "dos", "querer", "entre", "así", 'primero', \
        "desde", "grande", "eso", "ni", "nos", "llegar", "pasar", "tiempo", "ella", "sí", \
        "día", "uno", "bien", "poco", "deber", "entonces", "poner", "cosa", "tanto", "hombre", \
        "parecer", "nuestro", "tan", "donde", "ahora", "parte", "después", "vida", "quedar", "siempre", \
        "creer", "hablar", "llevar", "dejar", "nada", "cada", "seguir", "menos", "nuevo", "encontrar" ] 

    definitions = ["the", "of, from", "that, which", "and", "to, at", "in, on", "a, an", "to be", "-self, oneself", "no", \
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

    i = random.randint(0, len(spanish_words) - 1)  # this determines index item in our array
    word = spanish_words[i] # assigns our indexed item to a variable

    # this code randomly selects three other indexes
    x = random.randint(0, len(spanish_words) - 1)
    y = random.randint(0, len(spanish_words) - 1)
    z = random.randint(0, len(spanish_words) - 1)

    # these while loops are to make sure the correct definition doesn't appear more than once
    while x == i:
        x = random.randint(0, len(spanish_words) - 1)
    while y == i or y == x:
        y = random.randint(0, len(spanish_words) - 1)
    while z == i or z == x or z == y:
        z = random.randint(0, len(spanish_words) - 1)

    # these assign each definition which will show up as a choice for the user to select
    correctChoice = definitions[i] # this definition will be the correct definition
    wrongChoice1 = definitions[x] # incorrect definition #1
    wrongChoice2 = definitions[y] # incorrect definition #2
    wrongChoice3 = definitions[z] # incorrect definition #3

    # this code randomly selects the letter option the correct answer will be assigned to
    options = ['a', 'b', 'c', 'd']
    letter = random.choice(options)

    print

    # else/if prints to user the list of answers to choose from
    if letter == 'a':
        print("a. " + correctChoice)
        print("b. " + wrongChoice1)
        print("c. " + wrongChoice2)
        print("d. " + wrongChoice3)
    elif letter == 'b':
        print("a. " + wrongChoice1)
        print("b. " + correctChoice)
        print("c. " + wrongChoice2)
        print("d. " + wrongChoice3)
    elif letter == 'b':
        print("a. " + wrongChoice1)
        print("b. " + wrongChoice2)
        print("c. " + correctChoice)
        print("d. " + wrongChoice3)
    elif letter == 'd':
        print("a. " + wrongChoice1)
        print("b. " + wrongChoice2)
        print("c. " + wrongChoice3)
        print("d. " + correctChoice)

main()
