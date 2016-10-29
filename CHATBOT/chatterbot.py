import random 
import time
import wikipedia

#STOPWORDS ********************************
text_file = open("stopwords.txt", "r+")
stopwords = text_file.read()
text_file.close()

happy_words = open("happywords.txt", "r+")
PostiveWords = happy_words.read()
happy_words.close()

sad_words = open("sadwords.txt", "r+")
NegativeWords = sad_words.read()
sad_words.close()

end_words = open("endwords.txt", "r+")
EndWords = end_words.read()
end_words.close()


#******************************************


#********RESPONSES*******************************
greetings = ['hello', 'hey', 'hi' , 'Hi', 'Hello', 'hey!', 'hola', 'sup']
#this searches through the sequence and choose a random greeting
random_greeting = random.choice(greetings)

gratitude = ['thanks', 'cheers']
random_gratitude = random.choice(gratitude)

#respond straight after greeting with a 
responses = ['How be you? ', 'Are you okie? ', 'How are you doing? ', 'Whats been happening ']
random_response = random.choice(responses)

#user input for the question the bot asks 

happy_answer = ['okie', "I'm fine thanks",'im good thank you', 'not much']
answer_response = ['that is good to hear', 'I am glad', 'thats good to hear', 'awesome', 'magic']
random_answer_response = random.choice(answer_response)

sad_answer = ['not great', 'feeling a bit down', 'not very well']
sad_response = ['I am sorry to hear that', 'Awwh how come', 'thats sad', 'how come', 'that sucks']
random_sad_response = random.choice(sad_response)

user_question = ['how are you', 'are you okie', 'how be you']
bot_response = ['Im good', 'Never been better', 'On top of the world', 'I have had better days', 'feeling a bit blue']
random_bot_response = random.choice(bot_response)

user_question1 = ['whats your name']
bot_response_name = ('My name is Hal', 'you dont need to know my name', 'my name is unimportant')
random_name_response = random.choice(bot_response_name)

userEnd = ['no thanks im off', 'nah bye', 'no', 'im off', 'not today', 'not now']
botEndResponse = ['Okie bye']


#****************************************************************************

#****************FUNCTIONS************************************

def getMeTheFirstInterestingWord(words):
    for word in words:
        if word.lower() not in stopwords: return word

def getPostiveWord(postive):
    for word in postive:
        if word.lower() in PostiveWords:
            print(random_answer_response)

def getNegativeWord(negative):
    for word in negative:
        if word.lower() in NegativeWords:
            print(random_sad_response)

def getEndWord(End):
    for word in End:
        if word.lower() in EndWords:
            print(botEndResponse)


def getWikipediaSummary(Wiki):
    for word in Wiki:
        if word.lower() not in stopwords:
            print wikipedia.summary(word)
    

#***************************************************************

#*****************STOPWORD LISTS**********************************
    
    
#stopword for loop
bot_user_response = raw_input("My name is Hal, what is your name ? : ")
wordlist = bot_user_response.split(" ")
interestingWord = getMeTheFirstInterestingWord(wordlist)
print (random_greeting + " " + interestingWord)
time.sleep(1)


bot_emotion = raw_input("how are you today? : ")
wordlist = bot_emotion.split(" ")
emotion_word = [getPostiveWord(wordlist), getNegativeWord(wordlist)]
time.sleep(2)
#print(random_name_response)

bot_intel = raw_input("have you got any questions ? : ")
wordlist = bot_intel.split(" ")
quesiton_word = getWikipediaSummary(wordlist)
time.sleep(1)

bot_loop = raw_input("anything else i can help you with ? : ")
wordlist = bot_loop.split(" ")
loop_word = [getWikipediaSummary(wordlist), userEnd]
time.sleep(2)





#******************************************************************
"""
while True:
    if getPostiveWord in emotion_word:
        print(random_answer_response)
    elif getNegativeWord in emotion_word:
        print(random_sad_response)
        """

        
#**************WHILE LOOP ***************************************       
while True:    
    interestingWord = getMeTheFirstInterestingWord(wordlist)
    userInput = raw_input(">> ")
        #the in tests for collection memberships     
    if userInput in happy_answer:
        time.sleep(1)
        print(random_answer_response)
    elif userInput in sad_answer:
        time.sleep(1)
        print(random_sad_response)
    elif userInput in user_question:
        time.sleep(1)
        print(random_bot_response)
    elif userInput in user_question1:
        time.sleep(1)
        print(random_name_response)
        print wikipedia.summary(anotherInterestingWord)
    elif userInput in answer_response:
        time.sleep(1)
        print(random_gratitude)
        print wikipedia.summary(anotherInterestingWord)
    elif userInput in sad_response:
        print(random_gratitude)
        print wikipedia.summary("wikipedia")
    
    else:
        print("Sorry can you say that again")
    #*****************************************************