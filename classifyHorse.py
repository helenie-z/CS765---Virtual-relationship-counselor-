import json

def main():
    advice_dict = build_advice_dict()
    horsemen_dict = readPhrases()
    
    horseman_result = initiate_agent(horsemen_dict)
    give_advice(horseman_result, advice_dict)

#reading the dictionary of the four horsemen
def readPhrases():
    filename = input("please enter filename: ")
    with open(filename+'.json', 'r') as f:
        try:
            data = json.load(f)
        # if the file is empty the ValueError will be thrown
        except ValueError:
            data = {}
    data = dict(data)
    print(data)
    return data

def build_advice_dict():
    #{0: general advice etc etc
    # 1: blahblah
    #}
    return []

#classify the text
#iterate through the dictionary of horsemen. return the horseman if it has a
#phrase that matches the sentence as substring
def classify_text(sentence):
    return 0
    
def classify_horseman(person_speech_list):
    return

def initiate_agent(horsemen_dict):
    #agent talks to user. "please enter your name and your partner's name" "ask for convo log"
    userName = input("Hi there, what's your name?")
    partnerName = input("Nice to meet you " + userName + ". What is your partner's name? ")
    convoFileName = input("Please enter the filename for the conversation log between you and " + partnerName + " you would like me to analyse. ")
    with open(convoFileName + '.txt', 'r') as f:
        convo = f.readlines()
        print(convo)



        #initiate a list for each person based on user input
    #read convo log and put each sentence into corresponding person's list (based on first character/word)
    #go through each list and use classify_text() gets us a number for each phrase (number representing the horseman)
    #find the horseman with highest frequency and set that as the result for that person. also calculate the percentage

    #classify_horseman()
    
    #result: return a list of lists for each couple, and their horseman result, their percentage of that horseman,
    #and sentences that follow that horseman
    # [("Name", int, float, []),("Name", int, float, [])]

#POTENTIALLY: we can ask more questions here
#use the advice dictionary and print out advices
def give_advice(result, advice_dict):
    return

main()
