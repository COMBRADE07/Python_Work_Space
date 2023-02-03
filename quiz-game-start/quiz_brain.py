class quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        print(f"Q.1]{self.question_list[self.question_number]['text']}?(True/False)")
        ans = input("Make your choice")
        ans_l = self.question_list[self.question_number]['answer']
        if ans == ans_l:
            print("Congrats :D")
            # print(len(self.question_list))

        else:
            print(":(")

    def still_have_a_question(self):
        i = 2
        while (i < len(self.question_list)):
            print(f"Q.{i}]{self.question_list[i]['text']}?(True/False)")
            ans = input("Make your choice")
            ans_l = self.question_list[self.question_number]['answer']
            if ans == ans_l:
                print("Congrats :D")
            i +=1
