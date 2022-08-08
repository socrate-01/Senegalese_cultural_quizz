from Questions import Questions
print("This is a multiple choice quizz!")
question_prompts = [
    "Who is the richest man in Senegal?\na-) Serigne Mboup\nb-) Babacar Ngom\nc-) Thione Niang\n\n",
    "Who built the slaves house in Goree island?\na-) Dutch\nb-) Americans\nc-) French\n\n",
    "Who is the first president in Senega?\na-) Leopold Sedhar Senghor\nb-) Abdoulaye Wade\nc-) Abdou Diouf\n\n "
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "a"),
    Questions(question_prompts[2], "a"),
]

def run_program(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
        print("You got "+ str(score)+ "/"+str(len(questions))+" correct")
    

run_program(questions)