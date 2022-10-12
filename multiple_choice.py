from question import question

question_prompts = [
    "what color are apples?\n(a) Red\Greeen\n(b) Blue\n(c) Orange\n\n",
    "what is 5 + 5?\n(a) Five\n(b) Zero\n(c) Ten\n\n",
    "what is 5 + 5 * 5 + 5?\n(a) 55\n(b) 35\n(c) 75\n\n"
]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print ("you got " + str(score) + "/" + str (len(questions)) + " correct")

run_test(questions)
