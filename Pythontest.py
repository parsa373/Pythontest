import random
import tkinter as tk
from tkinter import messagebox

class PythonTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Test")
        self.root.geometry("600x400")
        
        # دیکشنری سوالات
        self.questions = {
            1: ("خروجی دستور `print(3 + 5)` چیست؟", ["6", "8", "35", "15"], "8"),
            2: ("کدام کلمه کلیدی برای تعریف تابع در پایتون استفاده می‌شود؟", ["function", "def", "define", "func"], "def"),
            3: ("نوع داده `3.14` چیست؟", ["int", "str", "float", "bool"], "float"),
            4: ("دستور `input()` چه نوع داده‌ای برمی‌گرداند؟", ["int", "float", "str", "bool"], "str"),
            5: ("برای بررسی شرط در پایتون از چه کلمه‌ای استفاده می‌کنیم؟", ["if", "for", "while", "try"], "if"),
            6: ("خروجی `len('سلام')` چیست؟", ["4", "5", "3", "6"], "4"),
            7: ("کدام عملگر برای تقسیم صحیح استفاده می‌شود؟", ["%", "/", "//", "*"], "//"),
            8: ("برای ایجاد لیست خالی چه می‌نویسیم؟", ["[]", "{}", "()", "<>"], "[]"),
            9: ("خروجی `2 ** 3` چیست؟", ["6", "9", "8", "5"], "8"),
            10: ("کدام گزینه یک متغیر معتبر است؟", ["1var", "var_1", "var-1", "var 1"], "var_1"),
            11: ("برای تکرار ۵ بار از چه حلقه‌ای استفاده می‌کنیم؟", ["if", "while", "for", "try"], "for"),
            12: ("خروجی `print('Hi' * 2)` چیست؟", ["HiHi", "Hi2", "2Hi", "Hi Hi"], "HiHi"),
            13: ("کدام نوع داده برای `True` است؟", ["int", "str", "bool", "float"], "bool"),
            14: ("برای اضافه کردن به لیست از چه متدی استفاده می‌کنیم؟", ["add()", "append()", "insert()", "push()"], "append()"),
            15: ("خروجی `5 % 2` چیست؟", ["2", "1", "3", "0"], "1"),
            16: ("کدام عملگر برای مقایسه برابری است؟", ["=", "==", "!=", "<="], "=="),
            17: ("برای تبدیل '5' به عدد از چه تابع استفاده می‌کنیم؟", ["str()", "float()", "int()", "bool()"], "int()"),
            18: ("خروجی `type(42)` چیست؟", ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"], "<class 'int'>"),
            19: ("برای توقف حلقه از چه کلمه‌ای استفاده می‌کنیم؟", ["stop", "break", "exit", "end"], "break"),
            20: ("کدام گزینه یک حلقه است؟", ["if", "elif", "while", "else"], "while"),
            21: ("خروجی `list(range(3))` چیست؟", ["[0, 1, 2]", "[1, 2, 3]", "[0, 1, 2, 3]", "[1, 2]"], "[0, 1, 2]"),
            22: ("برای دسترسی به اولین عنصر لیست چه می‌نویسیم؟", ["list[1]", "list[0]", "list[-1]", "list[2]"], "list[0]"),
            23: ("خروجی `'hello'.upper()` چیست؟", ["HELLO", "hello", "Hello", "hELLO"], "HELLO"),
            24: ("کدام کلمه برای مدیریت خطا استفاده می‌شود؟", ["if", "try", "for", "def"], "try"),
            25: ("خروجی `10 // 3` چیست؟", ["3", "4", "3.33", "1"], "3"),
            26: ("برای بررسی عضویت در لیست از چه عملگری استفاده می‌کنیم؟", ["is", "in", "not", "and"], "in"),
            27: ("خروجی `'python'[1]` چیست؟", ["p", "y", "t", "h"], "y"),
            28: ("کدام گزینه یک رشته است؟", ["[1, 2]", "'سلام'", "42", "True"], "'سلام'"),
            29: ("برای تعریف متغیر از چه چیزی استفاده نمی‌کنیم؟", ["=", "==", ":=", ":="], "=="),
            30: ("خروجی `len([1, 2, 3, 4])` چیست؟", ["3", "4", "5", "2"], "4")
        }
        
        # انتخاب تصادفی سوالات
        self.question_keys = list(self.questions.keys())
        random.shuffle(self.question_keys)
        self.current_question = 0
        self.score = 0
        
        # رابط کاربری
        self.label = tk.Label(root, text="به آزمون پایتون خوش اومدید!", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.question_label = tk.Label(root, text="", font=("Arial", 12), wraplength=500)
        self.question_label.pack(pady=10)
        
        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value=str(i+1), font=("Arial", 10))
            rb.pack(anchor="w", padx=20)
            self.radio_buttons.append(rb)
        
        self.submit_button = tk.Button(root, text="ثبت پاسخ", command=self.check_answer)
        self.submit_button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        
        # نمایش سوال اول
        self.show_question()
    
    def show_question(self):
        if self.current_question < 30:
            key = self.question_keys[self.current_question]
            question, options, _ = self.questions[key]
            self.question_label.config(text=f"سوال {self.current_question + 1}: {question}")
            
            # به‌روزرسانی گزینه‌ها
            for i, rb in enumerate(self.radio_buttons):
                rb.config(text=f"{i+1}. {options[i]}")
            
            self.radio_var.set("")  # ریست انتخاب
            self.result_label.config(text="")
        else:
            # پایان آزمون
            percentage = (self.score / 30) * 100
            result = f"آزمون تموم شد!\nامتیاز: {self.score} از ۳۰\nدرصد موفقیت: {percentage:.1f}%"
            if percentage >= 80:
                result += "\nعالی! شما پایتون رو خوب بلدی! 😎"
            elif percentage >= 50:
                result += "\nخوبه، ولی یه کم تمرین بیشتر لازم داری! 📚"
            else:
                result += "\nنیاز به مطالعه بیشتر داری! نگران نباش، ادامه بده! 💪"
            
            self.question_label.config(text="")
            for rb in self.radio_buttons:
                rb.config(text="")
            self.submit_button.config(state="disabled")
            self.result_label.config(text=result)
    
    def check_answer(self):
        if self.current_question >= 30:
            return
        
        try:
            user_answer = int(self.radio_var.get())
            key = self.question_keys[self.current_question]
            _, options, correct_answer = self.questions[key]
            
            if 1 <= user_answer <= 4:
                if options[user_answer - 1] == correct_answer:
                    self.score += 1
                    messagebox.showinfo("نتیجه", "درست! ✅")
                else:
                    messagebox.showerror("نتیجه", f"غلط! پاسخ درست: {correct_answer} ❌")
            else:
                messagebox.showwarning("خطا", "لطفاً یک گزینه انتخاب کنید!")
                return
        except ValueError:
            messagebox.showwarning("خطا", "لطفاً یک گزینه انتخاب کنید!")
            return
        
        self.current_question += 1
        self.show_question()

# اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = PythonTest(root)
    root.mainloop()
    
