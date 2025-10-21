print("Welcome to my computer.. ")
playing = input("Do you wanna play game? [Yes] or [No] ")

if playing.lower() == "yes":
    print("Okh lets play :) ")
else:
    quit()

score = 0

quiz = input("What does cpu stand for ?\n")
if quiz.lower() != "central processing unit":
    print("incorrect ")
else:
    print("correct")
    score += 1
quiz = input("What does gpu stand for ?\n")
if quiz.lower() != "graphic processing unit":
    print("incorrect ")
else:
    print("correct")
    score += 1
quiz = input("What does RAM stand for ?\n")
if quiz.lower() != "random access memory":
    print("incorrect ")
else:
    print("correct")
    score += 1
quiz = input("What does psu stand for ?\n")
if quiz.lower() != "power supply":
    print("incorrect ")
else:
    print("correct")
    score += 1

print(f"You got {score} question correct.")
print(f"You got the {(score/4)*100}%.")
