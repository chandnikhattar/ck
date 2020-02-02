#Chandni Khattar - PROJECT
#VirtualAssistant

#Importing Python Modules
import random

#Using Data Structures and Data Types for introducting Inputs and outputs 
INPUTS = ("Yo","hello", "hi", "greetings", "sup", "whatsup","hey", "yo","help")
RESPONSES = ["hi, how can I help you", "hey, how can I help you", "hi there, how can I help you", "hello, how can I help you", "I am glad! You are talking to me"]

#Defining Python Functions and Parameters
def chatbox(sentence):
 
    for word in sentence.split():
        if word.lower() in INPUTS:
            return random.choice(RESPONSES)
        
#Giving introductory Input for virtual Assistance
condition=True
print("Chatbox: My name is Chandni.I am your virtual assistant. If you want to exit, type Bye!")

#Error Handling and Debugging
#Using Control Flow 
try: 
    while(condition==True):
        user_response = input()
        user_response = user_response.lower()
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you'):
                condition=False
                print("Chatbox: You are welcome!")
            else:
                if(chatbox(user_response)!=None):
                    print("Chatbox: " + chatbox(user_response))
                else:
                    print("Chatbox: ",end="")
                    print(response(user_response))
                   
        else:
            condition=False
            print("Chatbox: Bye! take care!!")
except NameError:
    print('Sorry, I did not get that! Please try again')
