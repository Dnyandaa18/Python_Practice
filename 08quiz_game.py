# Python Quiz Game

questions = ("Which Planet in Solar System is known as Red Planet?: ",
             "What is the capital city of France?: ",
             "Which popular animated Disney movie features a cheerful snowman named Olaf?: ",
             "What is the largest living animal on Earth?: ")

options = (("A. Venus", "B. Mars","C. Jupiter","D. Mercury"),
           ("A. London", "B. Berlin", "C. Paris", "D. Madrid"),
           ("A. Moana", "B. Toy Story", "C. Shrek", "D. Frozen"),
           ("A. Blue Whale", "B. African Elephant", "C. Giraffe", "D. Great White Shark"),
           ("A. Egypt", "B. India", "C. China", "D. Brazil"))

answers = ("B", "C", "D", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-"*70)
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
     score+=1
     print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

print("------------------------------------------------------")
print("                       Results                        ")
print("------------------------------------------------------")

print("answers:", end="")
for answer in answers:
   print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
   print(guess, end=" ")
print()


score = (score/ len(questions) * 100)
print(f"Your score is {score}%")