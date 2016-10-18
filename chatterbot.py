import random 
import time
text_file = open("stopwords.txt", "r")
stopwords = text_file.read()
text_file.close()

greetings = ['hello', 'hey', 'hi' , 'Hi', 'Hello', 'hey!', 'hola', 'sup']
#this searches through the sequence and choose a random greeting
random_greeting = random.choice(greetings)

#respond straight after greeting with a 
responses = ['How be you? ', 'Are you okie? ', 'How are you doing? ', 'Whats been happening ']
random_response = random.choice(responses)

#user input for the question the bot asks 

happy_answer = ['okie', "I'm fine thanks", 'not much']
answer_response = ['that is good to hear', 'I am glad']
random_answer_response = random.choice(answer_response)

sad_answer = ['not great', 'feeling a bit down', 'not very well']
sad_response = ['I am sorry to hear that', 'Awwh how come', 'thats sad']
random_sad_response = random.choice(sad_response)

user_question = ['how are you', 'are you okie', 'how be you']
bot_response = ['Im good', 'Never been better', 'On top of the world', 'I have had better days', 'feeling a bit blue']
random_bot_response = random.choice(bot_response)

user_question1 = ['whats your name']
bot_response_name = ('My name is Hal')
random_name_response = random.choice(bot_response_name)

def getMeTheFirstInterestingWord(words):
    for word in words:
        if word.lower() not in stopwords: return word


#stopword for loop
bot_user_response = raw_input("Hi What is your name ?")
wordlist = bot_user_response.split(" ")
interestingWord = getMeTheFirstInterestingWord(wordlist)
print (random_greeting + " " + interestingWord)
time.sleep(1)
print(random_response)
        
#everything       
while True: 
    interestingWord = getMeTheFirstInterestingWord(wordlist)
    userInput = raw_input(">> ")
        #the in tests for collection memberships 
    if userInput in greetings:
        #prints and random greeting from the greetings sequence
        print(random_greeting + " " + interestingWord)
        time.sleep(1)
        print(random_response + " " + interestingWord)
    elif userInput in happy_answer:
        time.sleep(1)
        print(random_answer_response)
    elif userInput in sad_answer:
        time.sleep(1)
        print(random_sad_response)
    elif userInput in user_question:
        time.sleep(1)
        print(random_bot_response)
    elif userInput in user_question1:
        print(bot_response_name)
    
    else:
        print("Sorry can you say that again")
        