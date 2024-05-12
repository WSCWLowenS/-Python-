score = 0
print ("Hello")
#Question of User's Name and the code remembering the answer
name= input("What is your name?")
#Greeting the User and introducing the quiz
print("Welcome to the Quiz", name)
print("This quiz is a 10 question quiz and it's about General Knowledge")
print("Write the capital letter of the correct answer")
#Asking the user a question

questionanswer=input("What is the chemical symbol for Gold? \nA.Gd B.Go C.Ag D.Au \nAnswer:")
#Telling the user the correct answer
if answer == " D":
    print("Correct!")
    score += 100
elif answer == "":
    print("Hahaha")
    print("The answer is D")
else:
    print("Wrong answer")
    print("The answer is D")
#Ending the Quiz
print("Your final score is", score)
print("Thank you for answering the quiz")
