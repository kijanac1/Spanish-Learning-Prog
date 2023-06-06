# The purpose of this file is to store all the words and definitions into arrays
# for organization purposes. Other files that need these arrays will call them

from re import L
from tkinter import N


common_words = ["el / la", "de", "que", "y", "a", "en", "un", "ser", "se", "no", 
        "haber", "por", "con", "su", "para", "como", "estar", "tener", "le", "lo", \
        "lo", "todo", "pero", "más", "hacer", "o", "poder", "decir", "este / esta", "ir", \
        "otro", "ese", "la", "si", "me", "ya", "ver", "porque", "dar", "cuando", \
        "él", "muy", "sin", "vez", "mucho", "saber", "qué", "sobre", "mi", "alguno", \
        "mismo", "yo", "también", "hasta", "año", "dos", "querer", "entre", "así", 'primero', \
        "desde", "grande", "eso", "ni", "nos", "llegar", "pasar", "tiempo", "ella", "sí", \
        "día", "uno", "bien", "poco", "deber", "entonces", "poner", "cosa", "tanto", "hombre", \
        "parecer", "nuestro", "tan", "donde", "ahora", "parte", "después", "vida", "quedar", "siempre", \
        "creer", "hablar", "llevar", "dejar", "nada", "cada", "seguir", "menos", "nuevo", "encontrar" ]

common_definitions = ["the", "of, from", "that, which", "and", "to, at", "in, on", "a, an", "to be", "-self, oneself", "no", \
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

household_words = ["fregadero", "grifo", "estufa", "horno", "refrigerador", "congelador", "lavaplatos", "electrodomésticos", "tostadora", \
        "cafetera", "licuadora", "batidora", "mezcladora", "mostrador", "encimera", "despensa", "alacena", "piso", "suelo", \
        "protector contra salpicaduras", "limpiar", "lavar", "barrer", "preparar", "fregar", "restregar", "cocinar", "hervir", \
        "freír", "hornear", "sala", "silla", "sillón", "reloj", "mesa de centro", "lámpara", "mesa auxiliar", "florero", "alfombra", \
        "fútbol", "telenovelas", "televisión", "televisor", "libro", "baraja", "juegos de mesa", "ver", "jugar", "descansar", \
        "estar alborotado", "dormitorio", "cama", "tapete", "lamparilla", "ventana", "cortinas", "armario", "ropero", "cómoda", \
        "despertador", "dormir", "despertar", "levantar", "desvestir", "leer en voz alta", "bañar", "desnudar", "cepillar", "acicalar", \
        "duchar", "afeitar", "pasta de dientes", "cepillo de dientes", "champú", "jabón", "toalla", "peine", "cepillo", "maquinilla de afeitar", \
        "crema de afeitar", "loción",]

household_definitions = ["sink", "faucet", "stove", "oven", "refrigerator", "freezer", "dishwasher", "appliances", "toaster", "coffee maker", \
        "blender", "mixer", "mixer", "counter", "counter", "pantry", "cupboard", "floor", "floor", "backsplash", "to clean", "to wash", "to sweep", \
        "to prepare", "to mop", "to scrub", "to cook", "to boil", "to fry", "to bake", "living room", "chair", "armchair", "clock", "coffee table", \
        "lamp", "end table", "vase", "carpet", "soccer", "soap operas", "television", "television", "book", "deck of cards", "board games", "watch", \
        "to play", "to relax", "to be excited", "bedroom", "bed", "rug", "nightlight", "window", "curtains", "wardrobe", "closet", "dresser", \
        "alarm clock", "to sleep", "to wake up", "to get up", "to undress", "to read aloud", "to give a bath to", "to undress", "to brush", "to groom", \
        "to shower", "to shave", "toothpaste", "toothbrush", "shampoo", "soap", "towel", "comb", "brush", "razor", "shaving cream", "lotion" ]

sentences = ['¿entiende(s)?', 'no entiendo', 'no (lo) sé', 'no tengo ni idea', 'no hablo español', 'estoy perdido(a)', "¿cómo te llamas?", \
    '¿cómo está usted?', '¿cómo estás?', '¿qué tal?', '¿cómo te va?', '¿qué haces?', '¿qué pasa?']
sentence_definitions = ['do you understand?', 'i don’t understand', 'i don’t know', 'i have no idea', 'i don’t speak spanish', 'i’m lost', \
    "what is your name?", 'how are you? (formal)', 'how are you? (informal)', 'how are you? (informal)', 'how‘s it going?', 'what are you doing?', \
    'what‘s happening?']

spanish_words2 = ['así', 'de nada!', 'por favor', '¡perdón!', '¡disculpe!', '¡lo siento!', 'gracias', 'salud', 'Yo', 'tú (informal)',\
    'usted (formal)', 'él', 'ella', 'nosotros/nosotras', 'ustedes', 'ellos', 'ellas (females)', 'hola', 'buenos días', 'buenas tardes', \
    'buenas noches', 'old', 'young', 'middle-aged', 'youthful', 'nuevo/a', '¡feliz cumpleaños!', '¡felicitaciones!', '¡diviértete!', \
    '¡buen provecho!', '¡bienvenidos!/¡bienvenidas!', 'salud!', 'adiós', 'chao', 'domingo', 'lunes', 'martes', 'miércoles', 'jueves', \
    'viernes', 'sábado', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', \
    'diciembre', 'anteayer', 'ayer', 'el año', 'el día', 'el mes', 'el siglo', 'la hora', 'hoy', 'la semana', 'madrugada', 'mañana', 'mañana', \
    'medianoche', 'mediodía', 'el minuto', 'la noche', 'el pasado mañana', 'los segundos', 'la tarde', 'el padre', 'el papá', 'la madre', \
    'la mamá', 'el hermano', 'la hermana', 'el hijo', 'la hija', 'la familia cercana', 'el abuelo', 'la abuela', 'el bisabuelo', 'la bisabuela', \
    'la nieta', 'el nieto', 'el tío', 'la tía', 'el tío abuelo', 'la tía abuela', 'el primo', 'la prima', 'mis parientes', 'abrazar', 'amar', \
    'reír', 'perdonar', 'empezar', 'seguir', 'abrir', 'buscar', 'cantar', 'cerrar', 'destruir', 'dormir', 'encontrar', 'esconder', 'esperar',  \
    'faltar', 'hacer', 'intentar', 'llamar', 'llevar', 'llorar', 'luchar', 'mentir', 'odiar', 'recibir', 'reconocer', 'robar', 'salvar', 'sonreír', \
    'soñar', 'tomar', 'vivir', 'tranquilo/a', 'ruidoso/a', 'gritar', 'escuchar', 'silencio', 'alto', 'bajo', 'ensordecedor', 'agudo', 'grave', \
    'melodioso', 'armónico', 'zumbido', 'sordo', 'duro de oído', 'oído fino', 'problemas de audición', 'fuera de alcance', 'ver', 'mirar',  \
    'de colores', 'blanco y negro', 'brillante', 'apagado', 'claro', 'oscuro', 'ciego', 'mirar fijamente', 'echar un vistazo', 'bizquear', 'guiñar', \
    'parpadear', 'tocar', 'agarrar', 'suave', 'áspero(a)', 'liso(a)', 'rugoso(a)', 'pegajoso(a)', 'punzante', 'sedoso(a)', 'esponjoso(a)', \
    'mullido(a)', 'hormigueo', 'entumecido(a)', 'rozar', 'acariciar', 'agarrar', 'olor', 'el perfume', 'la fragancia', 'el hedor', 'apestoso(a)', \
    'fresco(a)', 'acre', 'húmedo(a)', 'podrido(a)', 'ahumado(a)', 'apestar', 'gusto', 'sabor', 'probar', 'sabroso', 'delicioso', 'perfecto',\
    'apetitoso', 'dulce', 'dulzón', 'soso', 'abierto/a', 'ancho/a', 'estrecho/a', 'lejano/a', 'cercano/a', 'alegre', 'gracioso/a', 'serio/a', \
    'tímido/a', 'valiente', 'loco/a', 'contento(a)', 'feliz', 'preocupado(a)', 'nervioso(a)', 'tranquilo(a)', 'calmado(a)', 'emocionado(a)', \
    'largo/a', 'corto/a', 'liso/a', 'rizado/a', 'ondulado/a', 'castaño/a', 'rubio/a', 'pelirrojo/a', 'negro/a', 'canoso/a', 'abundante', 'fino/a', \
    'escalado/a', 'teñido/a', 'saludable', 'claro/a', 'encrespado/a', 'brillante', 'calvo/a', 'hasta luego', 'hasta mañana', 'nos vemos', \
    '¡cuídate mucho!', '¡tenga un buen día!', '¡hasta luego!', '¡buen viaje!', 'como siempre', 'muy bien', "grande", "pequeño/a", "enorme", \
    "delgado/a", "esbelto/a", "flaco/a", "menudo/a", "alto/a", "bajo/a", "hermoso/a", "guapo/a", "feo/a", "adorable", "bonita", "impresionante", \
    "poco atractivo/a", "promedio/a", "atractivo/a", "negro", "marrón / café", "gris", "blanco", "amarillo", "anaranjado", "rojo", "rosado", \
    "morado / púrpura", "azul", "verde", "colorear", "construir", "cortar", "coser", "dibujar", "pintar", "el gato", "el perro", "el conejo", \
    "el pollo", "la gallina", "el gallo", "la vaca", "el toro", "la oveja", "el caballo", "el cerdo", "la cabra", "el burro", "el ratón", "el ciervo", \
    "el mapache", "la ardilla", "el búho", "el zorro", "el lobo", "el oso", "el cangrejo", "la medusa", "el delfín", "la ballena", "el tiburón", \
    "la foca", "el lobo marino", "la morsa", "el pingüino", "el viaje", "el equipaje", "la salida", "la llegada", "los documentos de identidad", \
    "el billete de avión", "el hotel", "el permiso de conducir", "echar gasolina", "viajar", "volver", "ir", "salir", "parar", "partir", "porter(a)", \
    "hostia", "botones", "anfitriona", "el avión", "el coche", "la bicicleta", "la motocicleta", "el tren", "el metro/subte", "el autobús", "el barco", \
    "taxista", "revisor(a)", "dependiente de gas", "conductor(a)", "camionero(a)", "el sol", "las nubes", "la niebla", "la neblina", "la lluvia", \
    "la llovizna", "la tormenta", "el tornado", "el trueno", "el relámpago", "el rayo", "el viento", "la brisa", "el granizo", "el hielo", "la nieve", \
    "el calor", "el frío", "la humedad", "la temperatura", "el pronóstico", "llover", "lloviznar", "diluviar", "granizar", "nevar", "el invierno", \
    "la primavera", "el verano", "el otoño", "carta de motivación", "el cv", "la firma", "el negocio", "la compañía", "el jefe", "el empleado", \
    "trabajar", "negociar", "consultor(a)", "dueño(a)", "abogado(a)", "arquitecto(a)", "bombero(a)", "campesino(a)", "carpintero(a)", "cartero(a)", \
    "casero(a)", "científico(a)", "cocinero(a)", "consejero(a)", "constructor(a)", "contador(a)", "doméstico(a)", "detective", "director", "electricista", \
    "escritor", "vaquero", "manejador(a)", "granjero(a)", "ingeniero(a)", "jardinero(a)", "jefe", "juez", "lavandero(a)", "marinero(a)", "mecánico(a)", \
    "camarero(a)", "padre", "panadero(a)", "pastor(a)", "periodista", "pescador(a)", "pintor(a)", "plomero(a)", "Policía", "programador(a)", "dueño(a)", \
    "químico(a)", "ranchero(a)", "rebuscador(a)", "reparador(a)", "técnico(a) de laboratorio", "trabajador(a) de fábrica", "veterinario(a)", "ir al gimnasio", \
    "ir de caminata", "levantar pesas", "mantenerse en forma", "practicar", "nadar", "el yoga", "el fútbol", "el fútbol americano", "el béisbol", \
    "el baloncesto", "el golf", "el hockey", "el tenis", "el voleibol", "luchar", "correr", "esquiar", "el partido", "la carrera", "el torneo", "patear", \
    "saltar", "parar", "balancear", "servir", "rematar", "pegar", "driblar", "tirar", "agarrar", "ganar", "perder", "empatar", "caminar", "bailar", "jugar", \
    "competir", "la comida", "las bebidas", "las verduras", "las frutas", "cocinar", "tengo hambre", "tengo sed", "la res", "el pollo", "la gallina", \
    "el cordero", "la barbacoa", "el cerdo", "el perrito caliente", "el jamón", "la hamburguesa", "el tocino", "el pescado", "la zanahoria", "la lechuga", \
    "el tomate", "la maíz", "la papa", "la patata", "las papas", "las patatas fritas", "el brócoli", "la espinaca", "la cebolla", "la col", "la ensalada", \
    "la aceituna", "las calabacitas", "el hongo", "el pepino", "la manzana", "la pera", "la fresa", "la frambuesa", "la zarzamora", "el arándano", \
    "el arándano rojo", "la naranja", "la mandarina", "la toronja", "el limón", "la lima", "el plátano", "la piña", "el coco", "el mango", "la papaya", \
    "la cerveza", "el refresco", "el té", "el té helado", "el café", "la leche", "el agua", "el jugo", "el batido", "el chocolate", "los dulces", "el pastel", \
    "las galletas", "el helado", "el churros con chocolate", "el basque cheesecake", "el plato", "el plato hondo", "el vaso", "la copa", "el tenedor", \
    "la cuchara", "el cuchillo", "la servilleta", "dulce", "salado(a)", "rico(a)"
]

english_translations = ['so, so', 'you’re welcome! / no problem!', 'please', 'excuse me!', 'excuse me!', 'sorry!', 'thank you', 'bless you', 'I', \
    'you (informal)', 'you (formal)', 'he', 'she', 'we', 'you all', 'they', 'they (females)', 'hello', 'good morning', 'good afternoon', \
    'good evening / good night', 'old', 'young', 'middle-aged', 'youthful', 'new', 'happy birthday!', 'congratulations!', 'have fun!',  \
    'bon appetit!', 'welcome!', 'cheers!', 'goodbye', 'goodbye', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', \
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'day before yesterday', \
    'yesterday', 'year', 'day', 'month', 'century', 'hour', 'today', 'week', 'dawn, very early in the morning', 'tomorrow', 'morning', 'midnight', \
    'noon', 'minute', 'night', 'day after tomorrow', 'seconds', 'afternoon', 'father', 'dad', 'mother', 'mom', 'brother', 'sister', 'son', 'daughter', \
    'close family', 'grandfather', 'grandmother', 'great-grandfather', 'great-grandmother', 'granddaughter', 'grandson', 'uncle', 'aunt', 'great-uncle', \
    'great-aunt', 'cousin (male)', 'cousin (female)', 'my relatives', 'to hug', 'to love', 'to laugh', 'to forgive', 'to start', 'to follow', \
    'to open', 'to search', 'to sing', 'to close', 'to destroy', 'to sleep', 'to find', 'to hide', 'to wait', 'to miss', 'to do', 'to try', 'to call', \
    'to take', 'to cry', 'to fight', 'to lie', 'to hate', 'to receive', 'to recognize', 'to steal', 'to save', 'to smile', 'to dream', 'to take', \
    'to live', 'quiet', 'loud', 'to shout', 'to hear', 'silence', 'loud', 'soft', 'deafening', 'sharp, high-pitched', 'low-pitched', 'melodious', \
    'harmonic', 'buzz', 'deaf', 'hard of hearing', 'acute hearing', 'hearing-impaired', 'out of earshot', 'to see', 'to look', 'colorful', 'black and white', \
    'bright', 'dim', 'light', 'dark', 'blind', 'to stare', 'to glance', 'to squint', 'to wink', 'to blink', 'to touch', 'to grab', 'soft', 'rough', \
    'smooth', 'wrinkled', 'sticky', 'sharp', 'silky', 'spongy', 'fluffy', 'tingle', 'numb', 'to touch gently', 'to caress', 'to grab', 'smell', 'scent',\
    'fragrance', 'stench', 'smelly', 'fresh', 'pungent', 'musty', 'rotten', 'smoky', 'to stink', 'taste', 'flavor', 'try', 'tasty', 'delicious', 'perfect', \
    'appetizing', 'sweet', 'sugary', 'bland', 'open', 'wide', 'narrow', 'far', 'close', 'joyful', 'funny, amusing', 'serious', 'shy', 'brave', 'crazy', \
    'content', 'happy', 'worried', 'nervous', 'tranquil', 'calm', 'excited', 'long', 'short', 'straight', 'curly', 'wavy', 'brown', 'blonde', 'red', 
    'black', 'grey', 'thick', 'thin', 'layered', 'dyed', 'healthy', 'light', 'frizzy', 'shiny', 'bald', 'see you later (most likely today)', \
    'see you tomorrow', 'see you (informal)', 'take care!', 'have a nice day!', 'see you soon!', 'have a good trip!', 'as always', 'very well', "big", \
    "small", "huge", "lean", "slender", "skinny", "petite", "tall", "short", "beautiful", "handsome", "ugly", "cute", "pretty", "stunning", "plain",  \
    "average", "attractive", "black", "brown", "grey", "white", "yellow", "orange", "red", "pink", "purple", "blue", "green", "to color", "to construct", \
    "to cut", "to sew", "to draw", "to paint", "cat", "dog", "rabbit", "chicken", "hen", "rooster", "cow", "bull", "sheep", "horse", "pig", "goat", "donkey", \
    "mouse", "deer", "raccoon", "squirrel", "owl", "fox", "wolf", "bear", "crab", "jellyfish", "dolphin", "whale", "shark", "seal", "sea lion", "walrus", \
    "penguin", "trip", "bags", "exit", "arrival", "id papers", "boarding pass", "hotel", "driver's license", "to get gas", "to travel", "to return", "to go", \
    "to leave", "to stop", "to depart", "doorman", "hostess", "bellhop", "airline hostess", "airplane", "car", "bicycle", "motorcycle", "train", "subway", "bus", \
    "ship", "taxi driver", "train conductor", "gas station attendant", "driver, chauffeur", "truck driver", "the sun", "the clouds", "the fog", "the mist", \
    "the rain", "the drizzle", "the storm", "the tornado", "the thunder", "the lightning strike", "the lightning bolt", "the wind", "the breeze", "the hail", \
    "the ice", "the snow", "the heat", "the cold", "the humidity", "the temperature", "the forecast", "to rain", "to drizzle", "to pour down", "to hail", "to snow", \
    "winter", "spring", "summer", "fall", "cover letter", "resume", "firm", "business", "company", "boss", "employee", "to work", "to negotiate", "consultant", "owner", \
    "lawyer", "architect", "fireman", "farm worker", "carpenter", "postal worker", "landlord", "scientist", "cook, chef", "counselor", "construction worker", \
    "accountant/bookkeeper", "maid", "detective", "editor", "electrician", "writer/author", "cowboy", "manager", "farmer", "engineer", "gardener", "boss", "judge", \
    "laundry person", "merchant marine", "mechanic", "waiter", "priest", "baker", "pastor/minister", "reporter/journalist", "fisherman", "painter", "plumber", \
    "policeman", "computer programmer", "owner", "chemist", "rancher", "researcher", "repairman", "lab technician", "factory worker", "veterinarian", "go to the gym", \
    "go hiking", "lift weight", "to stay in shape", "to practice", "to swim", "yoga", "soccer", "football", "baseball", "basketball", "golf", "hockey", "tennis", \
    "volleyball", "to wrestle/to fight", "to run", "to ski", "game/match", "race", "tournament", "to kick", "to jump", "to stop/to block", "to swing", "to serve", \
    "to spike", "to hit", "to dribble", "to throw", "to catch", "to win", "to lose", "to tie", "to walk", "to dance", "to play", "to compete", "food", "drinks",  \
    "vegetables", "fruits", "to cook", "I'm hungry", "I'm thirsty", "beef", "chicken", "chicken", "lamb", "grilled", "pork", "hot dog", "ham", "hamburger", "bacon", \
    "fish", "carrot", "lettuce", "tomato", "corn", "potato", "potato", "french fries", "french fries", "broccoli", "spinach", "onion", "cabbage", "salad", "olive", \
    "squash", "mushroom", "cucumber", "apple", "pear", "strawberry", "raspberry", "blackberry", "blueberry", "cranberry", "orange", "tangerine", "grapefruit", "lemon", \
    "lime", "banana", "pineapple", "coconut", "mango", "papaya", "beer", "pop, soft drink", "tea", "iced tea", "coffee", "milk", "water", "juice", "milkshake",  \
    "chocolate", "candy", "cake", "cookies", "ice cream", "chocolate churros", "cheesecake", "plate", "bowl", "glass", "cup", "fork", "spoon", "knife", "napkin", \
    "sweet", "savory", "delicious"]


homonyms1 = ['a', 'arrollo', 'asar', 'Asia', 'asta', 'barón', 'basta', 'bienes', 'calló', 'cerrar', 'cien', 'ciento', 'cocer', 'halla', 'hierba', 'hierro', \
    'hola', 'honda', 'mas', 'rallar', 'rebelarse', 'solo', 'si', 'sumo', 'tasa', 'tu', 'tubo']
homonyms2 = ['ha', 'arroyo', 'azar', 'hacia', 'hasta', 'varón', 'vasta', 'vienes', 'cayó', 'serrar', 'sien', 'siento', 'coser', 'haya', 'hierva', 'yerro', \
    'ola', 'onda', 'más', 'rayar', 'revelarse', 'sólo', 'sí', 'zumo', 'taza', 'tú', 'tuvo']


homonyms1_def = ['to', 'conjugated form, to roll up', 'to roast', 'Asia', 'pole', 'baron', 'enough', 'property', 'conjugated form, to silence', 'to close', \
    'hunderd', 'hundred', 'to cook', 'conjugated form, to find', 'herb', 'iron', 'hello', 'deep', 'but', 'to grate', 'to rebel', 'alone', 'if', 'supreme', 'rate', \
    'your', 'pipe']

homonyms2_def = ['conjugated form of haber', 'stream', 'chance, fate', 'toward', 'until', 'man', 'vast', 'conjugated form, to come', 'conjugated form, to fall', 'to saw', \
    'temple', 'conjugated form, to feel', 'to sew', 'conjugated form, to have', 'conjugated form, to boil', 'mistake', 'wave', 'wave', 'more', 'to make lines on', \
    'to reveal oneself', 'only', 'yes', 'juice', 'cup', 'you', 'conjugated form, to have']


#https://www.grittyspanish.com/2019/01/12/household-items-in-spanish/

    # pick homo1[i] & homo2[i]
    # randomly pick def one
    # if player answer matches correct answer win