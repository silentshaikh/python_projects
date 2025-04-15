# ​Yes, Mad Libs is indeed a game where players fill in blanks within a story to create humorous and often nonsensical narratives. One player prompts others to provide words corresponding to specific parts of speech—such as nouns, verbs, adjectives, or exclamations—without revealing the story's context. Once all the blanks are filled, the completed story is read aloud, often resulting in amusing and unexpected outcomes. 

# The game was invented in 1953 by Leonard Stern and Roger Price, and the first Mad Libs book was published in 1958. Since then, over 110 million copies have been sold. Mad Libs has been adapted into various formats, including a television game show on the Disney Channel in 1998 and a card game released by Looney Labs in 2016.
# Wikipedia

# The enduring popularity of Mad Libs lies in its simplicity and the endless possibilities for creativity and laughter it offers to players of all ages.

import pyttsx3

#container of stories
mad_libs_templates = {
    ("A Day at the Zoo".lower().replace(" ",'')): (
        "Today, I went to the zoo. I saw a(n) {adjective1} {animal1} jumping up and down in its tree. "
        "It {verb_past_tense1} {adverb1} through the large tunnel that led to its {adjective2} {noun1}. "
        "I got some peanuts and passed them through the cage to a gigantic gray {animal2} towering above my head. "
        "Feeding that animal made me hungry. I went to get a {adjective3} scoop of ice cream. It filled my stomach. "
        "Afterwards, I had to {verb1} {adverb2} to catch our bus. When I got home, I {verb_past_tense2} my mom for a {adjective4} day at the zoo."
    ),
    ("The Fun Park Adventure".lower().replace(" ",'')): (
        "Today, my fabulous camp group went to a(n) {adjective1} amusement park. It was a fun park with lots of cool {plural_noun1} and enjoyable play structures. "
        "When we got there, my kind counselor shouted loudly, 'Everybody off the {noun1}!' We all pushed out in a terrible hurry. "
        "My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. "
        "I saw a scary roller coaster I really liked, so I {adverb1} ran over to get in the long line that had about {number1} people in it. "
        "When I finally got on the roller coaster, it climbed slowly up the steep {noun2} and then raced down the other side at {number2} miles per hour. "
        "I screamed {adverb2}. After the ride, I was a bit {adjective2}, but I was proud of myself."
    ),
    ("My Dream Vacation".lower().replace(" ",'')): (
        "Last summer, my family and I went on a(n) {adjective1} vacation to {place1}. The weather was {adjective2}, and the beaches were {adjective3}. "
        "Every day, we would {verb1} along the shoreline and collect {plural_noun1}. One afternoon, I decided to try {verb_ing1} for the first time. "
        "It was {adjective4}! In the evenings, we enjoyed {plural_noun2} at a local restaurant. I can't wait to go back next year!"
    ),
    ("The Mysterious Island".lower().replace(" ",'')): (
        "During our voyage across the {adjective1} sea, we encountered a {adjective2} storm that left us stranded on a(n) {adjective3} island. "
        "The island was filled with {plural_noun1} and the sounds of {plural_noun2} echoed through the air. "
        "As we explored, we discovered a hidden {noun1} that contained a map leading to a(n) {adjective4} treasure. "
        "With our hearts full of {noun2}, we set out to find it. Little did we know, the island was also home to a group of {adjective5} {plural_noun3} who would challenge our quest."
    )
}

# Dictionary mapping story identifiers to their respective input prompts
mad_libs_inputs = {
    "adayatthezoo": {
       "adjective1" :"Enter an adjective: ",        # {adjective1}
        "animal1":"Enter an animal: ",           # {animal1}
        "verb_past_tense1":"Enter a verb (past tense): ", # {verb_past_tense1}
        "adverb1":"Enter an adverb: ",           # {adverb1}
        "adjective2":"Enter an adjective: ",        # {adjective2}
        "noun1":"Enter a noun: ",              # {noun1}
        "animal2":"Enter an animal: ",           # {animal2}
        "adjective3":"Enter an adjective: ",        # {adjective3}
        "verb1":"Enter a verb: ",              # {verb1}
        "adverb2":"Enter an adverb: ",           # {adverb2}
        "verb_past_tense2":"Enter a verb (past tense): ", # {verb_past_tense2}
        "adjective4":"Enter an adjective: "         # {adjective4}
    },
    "thefunparkadventure": {
        "adjective1":"Enter an adjective: ",        # {adjective1}
        "plural_noun1":"Enter a plural noun: ",       # {plural_noun1}
        "noun1":"Enter a noun: ",              # {noun1}
        "adverb1":"Enter an adverb: ",           # {adverb1}
        "number1":"Enter a number: ",            # {number1}
        "noun2":"Enter a noun: ",              # {noun2}
        "number2":"Enter a number: ",            # {number2}
        "adverb2":"Enter an adverb: ",           # {adverb2}
        "adjective2":"Enter an adjective: "         # {adjective2}
    },
    "mydreamvacation": {
        "adjective1":"Enter an adjective: ",        # {adjective1}
        "place1":"Enter a place: ",             # {place1}
        "adjective2":"Enter an adjective: ",        # {adjective2}
        "adjective3":"Enter an adjective: ",        # {adjective3}
        "verb1":"Enter a verb: ",              # {verb1}
        "plural_noun1":"Enter a plural noun: ",       # {plural_noun1}
        "verb_ing1":"Enter a verb ending in 'ing': ", # {verb_ing1}
        "adjective4":"Enter an adjective: ",        # {adjective4}
        "plural_noun2":"Enter a plural noun: "        # {plural_noun2}
    },
    "themysteriousisland": {
        "adjective1":"Enter an adjective: ",        # {adjective1}
        "adjective2":"Enter an adjective: ",        # {adjective2}
        "adjective3":"Enter an adjective: ",        # {adjective3}
        "plural_noun1":"Enter a plural noun: ",       # {plural_noun1}
        "plural_noun2":"Enter a plural noun: ",       # {plural_noun2}
        "noun1":"Enter a noun: ",              # {noun1}
        "adjective4":"Enter an adjective: ",        # {adjective4}
        "noun2":"Enter a noun: ",              # {noun2}
        "adjective5":"Enter an adjective: ",        # {adjective5}
        "plural_noun3":"Enter a plural noun: "        # {plural_noun3}
    }
}

#function allow user to add their custom stories

#function to tell what's written in the story
def sayStory(story):
    voiceEngine = pyttsx3.init()
    voiceEngine.say(story)
    voiceEngine.runAndWait()

# function to show the story with fill value

def show_fulfil_story(storyObj:dict,story:str):
    # check the story is in the object
    if story.lower() in storyObj:
        # get the story
        the_story:str = storyObj[story.lower()]

        # global mad_libs_inputs
        listofPrompts = mad_libs_inputs[story.lower()]

       # Collect user inputs
    user_inputs = {}
    # use for loop to collect input in user_inputs
    for key,prompt in listofPrompts.items():
        # add the input with their value in user_inputs
        user_inputs[key] = input(prompt)
    # now fill the story with the adjective noun pluralnoun animal etc
    fill_the_story = the_story.format(**user_inputs)
    print(fill_the_story)
    # you want to listen story or not
    listenStory = input("Do you want to listen the story (yes | no) : ")
    if listenStory.lower() == "yes":
        sayStory(fill_the_story)



def mad_libs_game():
    print("\n ###  MADLIBS GAME ### \n")
    print("""
   - A Day at the Zoo
   - The Fun Park Adventure
   - My Dream Vacation  
   - The Mysterious Island              
 """)

    #select an option
    selectOption = input("Enter an Option : ").replace(" ",'')
    if not selectOption:
        print("Please Enter an option")    
    elif selectOption.lower() == "A Day at the Zoo".lower().replace(" ",''):
        show_fulfil_story(mad_libs_templates,selectOption)
    elif selectOption.lower() == "The Fun Park Adventure".lower().replace(" ",''):
        show_fulfil_story(mad_libs_templates,selectOption)
    elif selectOption.lower() == "My Dream Vacation".lower().replace(" ",''):
        show_fulfil_story(mad_libs_templates,selectOption)
    elif selectOption.lower() == "The Mysterious Island ".lower().replace(" ",''):
        show_fulfil_story(mad_libs_templates,selectOption)
    else:
        print("Invalid Option")


mad_libs_game()