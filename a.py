def addQuestions(question_list):
    return question_list

def addOptions(options):
    return options

def correctAnswer(solution_list):
    return solution_list
    

question_list=["How many continents are there?",
"What is the capital of India?", "NG mei kaun se course padhaya jaata hai?"]

questions = addQuestions(question_list)
options_list = [
    ["1.Four", "2.Nine", "3.Seven", "4.Eight"],
    ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
    ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]

options = addOptions(options_list)

solution_list = ["3","4","1"]

solutions = correctAnswer(solution_list)


i = 0
while(i < len(questions)):
    print(i+1, questions[i])
    print("Select your Option")
    j = 0
    while(j <= len(options)):
        print(options[i][j])
        j = j + 1
    choice = input("Please tell the your Finale Answer to move next question")
    if choice in solution_list:
        print("You win level of This Stage")
        print("Your Next Question Display on Your Screen")
    else:
        print("You Loose the Game")

i = i + 1