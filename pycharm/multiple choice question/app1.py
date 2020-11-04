from question import Question

question_prompts=[
    "what is 1+2 ?\n(a) 3 \n(b) 2 \n(c) 6\n\n",
    "what is 1+1 ?\n(a) 3 \n(b) 2 \n(c) 6\n\n",
    "what is 4+2 ?\n(a) 3 \n(b) 2 \n(c) 6\n\n"
]


questions=[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]



def run_test(questions):
    score = 0
    for qstn in questions:
        ans=input(qstn.prompt)
        if ans==qstn.answer:
            score+=1
    print("you got "+ str(score)+"/" +str(len(questions))+"correct" )

run_test(questions)
