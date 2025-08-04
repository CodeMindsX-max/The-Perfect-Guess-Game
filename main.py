# from random import randint
# import os
# class A:
#     history="history.txt"
#     def log_file(self,guess,name):
#         with open(self.history,"a") as f:
#             f.write(f"Guess by {name} : ")
#             f.write(str(guess)+"\n")
#     def show_file(self):
#         with open(self.history,"r") as f:
#             a=f.read()
#             print(a)
#     def clear_log(self):
#         with open(self.history,"w") as f:
#             f.write("")
#     def log_bestScore(self,score,name):
#         with open("bestScore.txt","w") as f:
#             f.write(str(score)+f" by {name}")

#     def read_score(self,score,name):
#         try:
#             with open("bestScore.txt","r") as f:
#                 content=f.read().strip()
#                 scores=int(content.split()[0])
#         except (FileNotFoundError,ValueError,IndexError):
#             scores=0
#         if scores<score:
#                 self.log_bestScore(score,name)
#     def show_bestScore(self):
#         with open("bestScore.txt","r") as f:
#             print(f.read())

# class B(A):
#     def __init__(self):
#         self.num=randint(1,100)
#         self.score=0
#         self.bestscore=0
#         self.name=""
#     def get_num(self,num):
#         if num==self.num:
#             self.score+=1
#             self.check_score(self.name)
#             return True
#         elif num<self.num:
#             super().log_file(num,self.name)
#             return False
#         elif num>self.num:
#             super().log_file(num,self.name)
#             return False
        
#     def check_score(self,name):
#         if self.bestscore<self.score:
#             self.bestscore=self.score
#             super().read_score(self.bestscore,name)

#     def get_bestscore(self):
#         return self.bestscore
#     def get_score(self):
#         return self.score
#     def reset_number(self):
#         self.num=randint(1,100)
#     def reset_score(self):
#         self.score=0
        


        
# print("_"*15+"Welcome Number guess Game"+"_"*15+"\n")
# g=B()

# while True:
#     playerName=input("Enter Player name: ")
#     g.name=playerName
#     for attempts in range(5):
#         print(f"(You have to guess number in 5 attempts, Remaining {5-attempts})\n")
#         try:
#             num=int(input("Your guess: "))
#         except ValueError:
#             print("Please enter a valid number")
#             continue
#         c=g.get_num(num)
#         if c:
#             print(f"\n🎉 Congrats {playerName}! You guessed the right number: {g.num}\n")
#             print(f"Your score: {g.get_score()}\tHigh Score is ",end="")
#             g.show_bestScore()
#             print("Your Previous guess are...\n")
#             g.show_file()
#             choice=input("Press Y to play again or N to Exit: ")
#             if choice.lower()=="y":
#                 g.clear_log()
#                 g.reset_number()
#                 g.read_score()
#                 continue
#             else:
#                 print("Exiting...")
#                 break
#         elif not c:
#             if num>g.num:
#                 print(f"Try to guess number less then {num}\n")
#             elif num<g.num:
#                 print(f"Try to guess number greater then {num}\n")
#             else:
#                 print("Invalid input, Try again\n")
#     else:
#         print("\n❌ You Lose! Out of attempts.")
#         print(f"The correct number was: {g.num}")
#         print(f"Your score: {g.get_score()}\n")
#         print("Your Previous guess are...\n")
#         g.show_file()
#         choice=input("Press Y to play again or N to Exit: ")
#         if choice.lower()=="y":
#             attempts=0
#             g.clear_log()
#             g.reset_number()
#             continue
#         else:
#             print("Exiting...")
#             break

# # ================================================================================================================================

from random import randint

class A:
    history = "history.txt"

    def log_file(self, guess, name):
        with open(self.history, "a") as f:
            f.write(f"Scored by {name} : {guess}\n")

    def show_file(self):
        with open(self.history, "r") as f:
            print(f.read())

    def clear_log(self):
        with open(self.history, "w") as f:
            f.write("")

    def log_bestScore(self, score, name):
        with open("bestScore.txt", "w") as f:
            f.write(f"{score} by {name}")

    def read_score(self, score, name):
        try:
            with open("bestScore.txt", "r") as f:
                content = f.read().strip()
                best = int(content.split()[0])
        except (FileNotFoundError, ValueError, IndexError):
            best = 0
        if score > best:
            self.log_bestScore(score, name)

    def show_bestScore(self):
        try:
            with open("bestScore.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No high score yet.")

class B(A):
    def __init__(self):
        self.num = randint(1, 100)
        self.score = 0
        self.bestscore = 0
        self.name = ""

    def get_num(self, num):
        if num == self.num:
            self.score += 1
            self.check_score()
            return True
        elif num < self.num:
            self.log_file(num, self.name)
            return False
        elif num > self.num:
            self.log_file(num, self.name)
            return False

    def check_score(self):
        if self.bestscore < self.score:
            self.bestscore = self.score
            self.read_score(self.bestscore, self.name)

    def get_score(self):
        return self.score

    def reset_number(self):
        self.num = randint(1, 100)

    def reset_score(self):
        self.score = 0

# ------------------ Game Starts ------------------

print("_" * 15 + " Welcome Number Guess Game " + "_" * 15 + "\n")
g = B()

while True:
    playerName = input("Enter Player name: ")
    g.name = playerName

    for attempts in range(5):
        print(f"(You have to guess number in 5 attempts, Remaining {5 - attempts})\n")
        try:
            num = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if g.get_num(num):
            print(f"\n🎉 Congrats {playerName}! You guessed the right number: {g.num}\n")
            print(f"Your score: {g.get_score()} \tHigh Score: ", end="")
            g.show_bestScore()
            print("Your previous guesses are:\n")
            g.show_file()
            choice = input("Press Y to play again or N to Exit: ")
            if choice.lower() == "y":
                g.clear_log()
                g.reset_number()
                g.reset_score()  # reset only the score, not bestscore
                break
            else:
                print("Exiting...")
                exit()

        elif num > g.num:
            print(f"Try guessing a number less than {num}\n")
        elif num < g.num:
            print(f"Try guessing a number greater than {num}\n")

    else:
        print("\n❌ You Lose! Out of attempts.")
        print(f"The correct number was: {g.num}")
        print(f"Your score: {g.get_score()} \tHigh Score: ", end="")
        g.show_bestScore()
        print("Your previous guesses are:\n")
        g.show_file()
        choice = input("Press Y to play again or N to Exit: ")
        if choice.lower() == "y":
            g.clear_log()
            g.reset_number()
            g.reset_score()
            continue
        else:
            print("Exiting...")
            break
