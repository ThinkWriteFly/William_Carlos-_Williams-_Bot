import random
from Lists import Past_Simple_Verb
from Lists import Meal_Occasion
from Lists import Noun_Object_plural
from Lists import Direction
from Lists import Container
from Lists import Adjective

# this is william carlos williams bot
# infinite nonsense variations of 'this is just to say'
# this generator forms the poem from the options in the file wordlists.py 

# line structure
Line_1 = "\t I have " + random.choice(wordslist.Past_Simple_Verb) + "\n"
Line_2 = "\t the " + random.choice(wordslist.Noun_Object_Plural) + "\n"
Line_3 = "\t that were " + random.choice(wordslist.Direction) +"\n"
Line_4 = "\t the " + random.choice(wordslist.Container) + "\n" 
Line_5 = "\t and which \n"
Line_6 = "\t you were probably\n"
Line_7 = "\t saving\n"
Line_8 = "\t for " + random.choice(wordslist.Meal_Occasion) + "\n"
Line_9 = "\t Forgive me \n"
Line_10 = "\t they were " + random.choice(wordslist.Adjective) + "\n"
Line_11 = "\t so " + random.choice(wordslist.Adjective) + "\n"
Line_12 = "\t and so " + random.choice(wordslist.Adjective) + "\n"

# poem structure
Poem = Line_1 + Line_2 + Line_3 + Line_4 + "\n" + Line_5 + Line_6 + Line_7 +  Line_8 + "\n" + Line_9 + Line_10 + Line_11 + Line_12


# Output structure
print ("ThIs Is JuSt To SaY \n\n\n\n")
print (Poem)
print ("\n\n\t\t\t - WcWBot")