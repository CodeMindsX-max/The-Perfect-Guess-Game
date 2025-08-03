from random import randint
class A:
    history="history.txt"
    def log_file(self,guess):
        with open(self.history,"a") as f:
            f.write(str(guess)+"\n")
    def show_file(self):
        with open(self.history,"r") as f:
            a=f.read()
            print(a)
    def clear_log(self):
        with open(self.history,"w") as f:
            f.write("")

class B(A):
    def __init__(self):
        self.num=randint(1,100)
        self.score=0
    def get_num(self,num):
        if num==self.num:
            self.score+=1
            return True
        elif num<self.num:
            super().log_file(num)
            return False
        elif num>self.num:
            super().log_file(num)
            return False
        else: 
            
            return False
    
    def get_score(self):
        return self.score
    def reset_number(self):
        self.num=randint(1,100)
        


        
print("_"*15+"Welcome Number guess Game"+"_"*15+"\n")
g=B()
while True:
    
    print("(You have to guess the number and if it matche with the computer then you'll WIN)\n")
    try:
        num=int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    c=g.get_num(num)
    if c:
        print(f"\n🎉 Congrats! You guessed the right number: {g.num}\n")
        print(f"Your score: {g.get_score()}\n")
        print("Your Previous guess are...\n")
        g.show_file()
        choice=input("Press Y to play again or N to Exit: ")
        if choice.lower()=="y":
            g.clear_log()
            g.reset_number()
            continue
        else:
            print("Exiting...")
            break
    elif not c:
        if num>g.num:
            print(f"Try to guess number less then {num}\n")
        elif num<g.num:
            print(f"Try to guess number greater then {num}\n")
        else:
            print("Invalid input, Try again\n")