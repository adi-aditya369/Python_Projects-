# python quiz game

questions =("how many element are in the periodic table?: ",
           "which animal lays the largest eggs? ",
           "how many bones are in humman body?: ")

options = (("a.116","b.117","c.118","d.119"),
            ("a.whale","b.crocodile","c.elephant","d.ostrich"),
            ("a.206","b.207","c208","d.210"))
answer =("c","d","a")
guesses = []
score = 0
question_num =0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess =input("enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score == 1
        print("correct!")
    else:
        print("incorrect!")
        print(f"{answer[question_num]} is the correct answer")    

    question_num += 1  

print("----------------")
print("      result    ")
print("----------------")

print("answers:,end=")
for answer in answer:
    print(answer,end=" ")
print()    

print("guesses:,end=")
for guess in guess:
    print(guess,end=" ")
print()    
      
 
 
 
        
               
