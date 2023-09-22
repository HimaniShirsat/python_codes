import random

questions = ["How many elements are in the periodic table?",
             "Which animal lays the largest eggs?",
             "What is the most abundant gas in Earth's atmosphere?",
             "How many bones are in the human body?",
             "Which planet in the solar system is the hottest?",
             "Who Invented the 3-D printer?",
             "What is the maximum number of Members in Lok Sabha?",
             "Which of the following is known as the Diamond City of India?",
             "In which year Forest Conservation Act was passed?",
             "What does Triratna mean in Buddhism?"]

options = [["A. 116", "B. 117", "C. 118", "D. 119"],
           ["A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"],
           ["A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"],
           ["A. 206", "B. 207", "C. 208", "D. 209"],
           ["A. Mercury", "B. Venus", "C. Earth", "D. Mars"],
           ["A. Nick Holonyak", "B. Elias Howe", "C. Chuck Hull", "D. Christiaan Huygens"],
           ["A. 512", "B. 542", "C. 552", "D. 532"],
           ["A. Mumbai", "B. Jaipur", "C. Surat", "D. Panna"],
           ["A. 1980", "B. 1988", "C. 1986", "D. 1990"],
           ["A. Satya, Ahimsa, Karuna", "B. Sheel, Samadhi, Sangha", "C. Tripitaka", "D. Buddha, Dhamma (dharma), Sangha"]]

answers = ["C", "D", "A", "A", "B", "C", "C", "D", "A", "D"]

# Create a list of question indices to shuffle them.
question_indices = list(range(len(questions)))
random.shuffle(question_indices)

guesses = []
score = 0

for question_num in question_indices:
    print("----------------------")
    print(questions[question_num])
    shuffled_options = options[question_num][:]
    # random.shuffle(shuffled_options)
    
    for option in shuffled_options:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    if(guess=='A' or guess=='B' or guess=='C' or guess=='D'):
        guesses.append(guess)
    else:
        print("invalid alphabet")    

    
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")