import random

name = "Dude"
question = "Is Python your favorite programming language?"
answer = ""

randomNumber = random.randint(1, 10)

if randomNumber == 1:
    answer = "Yes - definitely"
elif randomNumber == 2:
    answer = "It is decidedly so"
elif randomNumber == 3:
    answer = "Without a doubt"
elif randomNumber == 4:
    answer = "Reply hazy, try again"
elif randomNumber == 5:
    answer = "Ask again later"
elif randomNumber == 6:
    answer = "Better not tell you now"
elif randomNumber == 7:
    answer = "My sources say no"
elif randomNumber == 8:
    answer = "Outlook not so good"
elif randomNumber == 9:
    answer = "Very doubtful"
elif randomNumber == 10:
    answer = "fuck off, quit bothering me with stupid questions"
else:
    answer = "Error"

if question == "":
    print("I guess you dont have any questions!")
else:
    if name == "":
        print(f"{question}")
    else:
        print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")