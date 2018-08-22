def checkAnswer(userAnswer,acceptedValues):
    temp = False
    for i in range(5):
        if userAnswer == acceptedValues[i]:
            temp = True
    return temp

def askQuestion(questionString,acceptedValues,errorMessage):
    while True:
        userAnswer = input(questionString)
        if userAnswer in acceptedValues:
            break
        print(errorMessage)
    return(checkAnswer(userAnswer,acceptedValues))

print(askQuestion("Is the animal a mammal?: ",["y","Y","yes","Yes","YES","n","N","no","No","NO"],"Please enter Yes or No"))