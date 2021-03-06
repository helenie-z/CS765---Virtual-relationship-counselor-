import json

def main():
    advice_dict = build_advice_dict()
    horsemen_dict = readPhrases()

    response = "yes"
    while (response == "yes"):
        horseman_result = initiate_agent(horsemen_dict)
        response = give_advice(horseman_result, advice_dict)

    print("Thank you for using the program!")




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
def classify_text(sentence, horsemen_dict):
    for key in horsemen_dict.keys():
        for phrase in horsemen_dict[key]:
            #print(phrase)
            if phrase in sentence:
                return int(key)
    return 0

#find the highest horseman in the user list, and also their percentage
def classify_horseman(horsemen_list):
    #[0, 2, 1, ...]
    freqDict = {0:0, 1:0, 2:0, 3:0, 4:0}

    #print (horsemen_list)
    for num in horsemen_list:
        if num == 0:
            freqDict[0] = freqDict[0] + 1
        elif num == 1:
            freqDict[1] = freqDict[1] + 1
        elif num == 2:
            freqDict[2] = freqDict[2] + 1
        elif num == 3:
            freqDict[3] = freqDict[3] + 1
        elif num == 4:
            freqDict[4] = freqDict[4] + 1

    horsemanResult = 0
    maxFreq = 0
    #print (freqDict)

    for horseman, freq in freqDict.items():
        if freq >= maxFreq:
            maxFreq = freq
            horsemanResult = horseman

    #if max horseman has freq 0, then make it 0

    #if maxFreq == 0:
    #    horsemanResult = 0

    length = len(horsemen_list)

    percentage = maxFreq/length

    #print(horsemanResult)
    #print(percentage)
    return [horsemanResult, percentage]
def get_sentences_for_horseman(userList, userHorsemen, horseman):
    result = []

    for i in range(0, len(userHorsemen)):
        if userHorsemen[i] == horseman:
            result.append(userList[i])

    #print(result)
    return result


def initiate_agent(horsemen_dict):
    #agent talks to user. "please enter your name and your partner's name" "ask for convo log"
    userName = input("Hi there, what's your name? ")
    partnerName = input("Nice to meet you " + userName + ". What is your partner's name? ")
    convoFileName = input("Please enter the filename for the conversation log between you and " + partnerName + " you would like me to analyse: ")

    # initiate a list for each person based on user input
    userList = []
    partnerList = []

    #read convo log and put each sentence into corresponding person's list (based on first character/word)
    with open(convoFileName + '.txt', 'r') as f:
        convo = f.readlines()
        for sentence in convo:
            name = sentence.split(":")[0]
            if (name == userName):
                userList.append(sentence.split(":")[1].strip())
            else:
                partnerList.append(sentence.split(":")[1].strip())


    #print(userList)
    #print(partnerList)
        #print(convo)

    #initiate a list for each user, where each item corresponds to the horseman in that sentence at that index
    userHorsemen = []
    partnerHorsemen = []

    #go through each list and use classify_text() gets us a number for each phrase (number representing the horseman)
    for sentence in userList:
        userHorsemen.append(classify_text(sentence, horsemen_dict))

    for sentence in partnerList:
        partnerHorsemen.append(classify_text(sentence, horsemen_dict))

    #print("user horseman: ")
    #print (userHorsemen)
    #print (partnerHorsemen)

    #find the horseman with highest frequency and set that as the result for that person. also calculate the percentage
    userResult = classify_horseman(userHorsemen)
    partnerResult = classify_horseman(partnerHorsemen)

    userHorsemanSentence = get_sentences_for_horseman(userList, userHorsemen, userResult[0])
    partnerHorsemanSentence = get_sentences_for_horseman(partnerList, partnerHorsemen, partnerResult[0])

    userResult.append(userHorsemanSentence)
    partnerResult.append(partnerHorsemanSentence)
    userResult.append(userName)
    partnerResult.append(partnerName)

    #print(userResult)
    #print(partnerResult)
    #result: return a list of lists for each couple, and their horseman result, their percentage of that horseman,
    return (userResult, partnerResult)
    # ((int, float, []),(int, float, [])]

#POTENTIALLY: we can ask more questions here
#use the advice dictionary and print out advices
def give_advice(result, advice_dict):
    user_result = result[0]
    partner_result = result[1]

    horseman_dict = {0: "no horseman", 1: "criticism", 2: "contempt", 3: "defensiveness", 4: "stonewalling"}

    user_horseman = horseman_dict[user_result[0]]
    user_percentage = str(user_result[1] * 100)
    user_sentences = user_result[2]
    user_name = user_result[3]

    partner_horseman = horseman_dict[partner_result[0]]
    partner_percentage = str(partner_result[1] * 100)
    partner_sentences = partner_result[2]
    partner_name = partner_result[3]
    print()
    print("Hi " + user_name + ", it seems that your most prominent horseman is " + user_horseman + " with a percentage of " + user_percentage + "%")
    print()

    print("Some of the examples are : ")

    for sentence in user_sentences:
        print("\"" + sentence + "\"")

    #give advice
    print("Here are some advice blahblahblah")
    print()


    print("As for your partner " + partner_name + ", it seems that their most prominent horseman is " + partner_horseman + " with a percentage of " + partner_percentage + "%")
    print()

    print("Some of the examples are : ")
    for sentence in partner_sentences:
        print("\"" + sentence + "\"")
        print()

    print("Here are some advice blahblahblah")

    response = input("Would you like to analyse another dialogue?")




    #print (user_result)
    #print(partner_result)

    return response

main()
