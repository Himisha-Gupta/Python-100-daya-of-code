class Question:
    def __init__(self, text , answer):
        self.q_text = text
        self.q_answer = answer


q1 = Question("WHAT IS YOUR NAME"  , "Himishsa")
print(q1.q_text)
print(q1.q_answer)
