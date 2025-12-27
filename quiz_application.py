questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit",
                    "C. Computer Personal Unit", "D. Central Program Unit"],
        "answer": "B"
    }
]

score = 0

print("Welcome to the Quiz Application\n")

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print("Quiz Completed!")
print("Your Score:", score, "/", len(questions))
