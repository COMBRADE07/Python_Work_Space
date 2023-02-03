from question_model import question
from data import question_data
from quiz_brain import quizbrain
question_bank = []
for q in question_data:
    q_text = q['text']
    q_ans = q['answer']
    new_que = dict(text=q_text, answer=q_ans)
    question_bank.append(new_que)

# print(q['text'],"\nnew qqqq is ",q_text)

# print(question_bank)
quiz = quizbrain(question_bank)
quiz.next_question()
quiz.still_have_a_question()
