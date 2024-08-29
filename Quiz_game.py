"""
EASY CHALLENGE
"""
print("Welcome to my quiz game!")
playing = input("Would like to play my Quiz game? answer 'yes' or 'no'")
if playing != 'yes': 
    print("GET THE FUCK OUT OF HERE THEN!")
    quit()
else: 
    print("OK, Let's get started!")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit": 
    print("Correct!")
    score += 1
else: print("Incorrect answer. Try again!")

answer2 = input("What does GPU stand for? ").lower()
if answer2 == "graphics processing unit": 
    print("Correct!")
    score += 1 
else: print("Incorrect answer. Try the next question!")

answer3 = input("What does RAM stand for? ").lower()
if answer3 == "ramification artificial memory": 
    print("correto!")
    score += 1
else: print("Incorrect!")

if score == 0: 
    print('Very bad, your score was ' + str(score) + ' points')
if score > 1 & score < 3: 
    print("Not bad, but you could do better... Your score is " + str(score / 3 * 100) + "%")
else: 
    print('Oh yeah! congrats, you did ' + str(score / 3 * 100) + '%.')
