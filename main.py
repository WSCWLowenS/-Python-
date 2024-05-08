score = 0
print ("Hello")
#Question of User's Name and the code remembering the answer
name= input("What is your name?")
#Greeting the User and introducing the quiz
print("Welcome to the Quiz", name)
print("This quiz is about General Knowledge")
print("Write the capital letter of the correct answer")
#Asking the user a question
answer=input("What is the chemical symbol for Gold?") 
answer=print("A.Gd B.Go C.Ag D.Au")
#Telling the user the correct answer
if answer == " D":
    print("Correct!")
elif answer == "":
    print("Hahaha")
    print("The answer is D")
else:
    print("Wrong answer")
    print("The answer is D")

if answer == " D":
    score =+ 100
#Ending the Quiz
print("Your final score is", score)
print("Thank you for answering the quiz")