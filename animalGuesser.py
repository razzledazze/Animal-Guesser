import csv

numbers = ["0","1","2","3","4","5","6","7","8","9"]

table = open("animalTable.csv")
reader = csv.reader(table)

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

def initRowTable():
    rowTable = []
    for row in reader:
        rowTable.append(row)
    return rowTable

rowTable = initRowTable()

rowNumber = "1"
while True:
    for row in rowTable:
        if row[0] == rowNumber:
            questionRow = row

    if askQuestion(questionRow[1],["y","Y","yes","Yes","YES","n","N","no","No","NO"],"Please enter Yes or No") == True:
        rowNumber = questionRow[2]
    else:
        rowNumber = questionRow[3]
    if rowNumber not in numbers:
        print("Your animal is a",rowNumber)
        break