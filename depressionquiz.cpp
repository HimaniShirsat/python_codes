import tkinter as tk
from tkinter import messagebox

class DepressionQuizApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Depression Quiz")

        self.questions = [
            "Over the past few weeks, have you experienced a persistent feeling of sadness or emptiness that doesn't seem to go away?",
            # ... Add more questions ...
        ]

        self.choices = [
            ["Not at all", "Occasionally", "Often", "Almost every day"],
            # ... Add more choices ...
        ]

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.choice_buttons = []
        for _ in range(4):
            button = tk.Button(root, text="", command=lambda: self.select_choice())
            self.choice_buttons.append(button)
            button.pack()

        self.next_button = tk.Button(root, text="Next", command=lambda: self.next_question())
        self.next_button.pack()

        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
            for i, button in enumerate(self.choice_buttons):
                button.config(text=self.choices[self.current_question][i])
            self.next_button.config(state=tk.DISABLED)
        else:
            self.show_result()

    def select_choice(self, choice):
        self.score += choice
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.update_question()

    def show_result(self):
        interpretation = self.interpret_score(self.score)
        messagebox.showinfo("Result", interpretation)
        self.root.destroy()

    def interpret_score(self, score):
        if score < 10:
            return "Your score suggests a relatively low likelihood of experiencing depressive symptoms."
        elif score >= 10 and score <= 20:
            return "Your score indicates that you may be experiencing some depressive symptoms. Consider seeking professional help."
        else:
            return "Your score suggests a higher likelihood of experiencing depressive symptoms. It's important to consult a mental health professional."

if _name_ == "_main_":
    root = tk.Tk()
    app = DepressionQuizApp(root)
    root.mainloop()

    DECLARE
 a number(3) := 100;
 b number(3) := 300;
BEGIN
 -- check the boolean condition 
 IF( a = 100 ) THEN
 -- if condition is true then check the following 
  IF( b = 200 ) THEN
   -- if condition is true then print the following 
   dbms_output.put_line('Value of a and  b is  100 and  200  respectively' );
   else
   dbms_output.put_line('Value of  b is not 200 ' );
   
   END IF;
else
dbms_output.put_line('Value of a is not 100 ' );
 END IF;
 dbms_output.put_line('Exact value of a is : ' || a );
 dbms_output.put_line('Exact value of b is : ' || b );
END;