score = 0
print ("Hello")
#Question of User's Name and the code remembering the answer
name= input("What is your name?")
#Greeting the User and introducing the quiz
print("Welcome to the Quiz", name)
print("This quiz is a 5 question quiz and it's about General Knowledge")
print("Write the capital letter of the correct answer")
#Question
question = "What is the chemical symbol for Gold?"
a = "Gd"
b = "Go"
c = "Ag"
d = "Au"
Answer = input("{}\nA.{} B.{} C.{} D.{}}".format(question, a, b, c, d)).lower()

#Answer
if Answer == a or Answer == "a":
    print("Correct!")
    score += 100
elif Answer == "":
    print("Not sure?")
elif Answer != a and Answer != "a" and Answer != b and Answer != "b" and Answer != c and Answer != "c":
     print("That wasn't an answer")
else:
    print("Wrong answer")
    print("The answer is Au")
#Ending
print("Your score is", score)
print("Now for the next question")
#Question
answer=input("what is the closest planet to the sun? \nA.Mercury B. Venus C Pluto D. Earth \nAnswer:") .upper()
#Answer
if answer == " A" .upper():
    print("Correct! The answer is A")
    score += 100
elif answer == "":
    print("Hahaha")
    print("The answer is A")
else:
    print("Wrong answer")
    print("The answer is A")
print("Your score is", score)
print("Great Job!")
#Question
answer=input("Who came up with the theory of relativity? \nA. Edgar Allan Poe B. Albert Einstein C Galileo Galilei D. Louis Pasteur \nAnswer:") .upper()
#Answer
if answer == " B" .upper():
    print("Correct! The answer is B")
    score += 100
elif answer == "":
    print("Hahaha")
    print("The answer is B")
else:
    print("Wrong answer")
    print("The answer is B")
print("Your score is", score)
#Question
answer=input("How many players are there in a soccer team? \nA. 6 B. 11 C. 10 D. 9 \nAnswer:") .upper()
#Answer
if answer == " B" .upper():
    print("Correct! The answer is B")
    score += 100
elif answer == "":
    print("Hahaha")
    print("The answer is B")
else:
    print("Wrong answer")
    print("The answer is B")
print("Your score is", score)
#Question
answer=input("What language is spoken in Brazil? \nA. Spanish B. Portuguese C. English D. French \nAnswer:") .upper()
#Answer
if answer == " B" .upper():
    print("Correct! The answer is B")
    score += 100
elif answer == "":
    print("Hahaha")
    print("The answer is B")
else:
    print("Wrong answer")
    print("The answer is B")
print("Your score is", score)
print("Thank you for answering the quiz")
print("With the final score of", score)