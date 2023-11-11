import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self,root):
          self.root = root
          self.root.title("Password Generator")
          self.root.geometry("400x300")
          self.root.configure(bg="lightgray")

          self.title_label = tk.Label(root,text="Password Generator by Arshika",bg="lightgray",font=("Helvetica",14,"bold"))
          self.title_label.pack(pady=10)

          self.label = tk.Label(root,text="Enter password length:",bg="lightgray")
          self.label.pack(pady=20)

          self.length_entry = tk.Entry(root)
          self.length_entry.pack()

          self.generate_button = tk.Button(root,text="Generate Password",command=self.generate_password,bg="pink",fg="white")
          self.generate_button.pack(pady=20)

          self.result_label = tk.Label(root,text="",bg="yellow")
          self.result_label.pack()
    def generate_password(self):
          try:
                password_length = int(self.length_entry.get())
                if password_length <= 0:
                     self.result_label.config(text="Invalid length",fg="red")
                else:
                     password = self.generate_random_password(password_length)
                     self.result_label.config(text=f"Generated Password:{password}",fg="blue")
          except ValueError:
                self.result_label.config(text="Invalid input",fg="red")

    def generate_random_password(self, Length):
          characters = string.ascii_letters + string.digits + string.punctuation
          password = ' ' . join(random.choice(characters) for _ in range(Length))
          return password
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
                
                    

          
          
