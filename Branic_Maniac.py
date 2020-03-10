#!/usr/bin/python3
#Tyler Hockenberry & Rob Blocker
#03-10-2020

''' This is the Braniac Maniac trivia quiz game. '''

#Imports
import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as tkst
from tkinter import messagebox as tkmb

#Globals
FONT = ("Courier", 18)
TITLE_FONT = ("Comic Sans", 34)

#Classes
class Screen(tk.Frame):
    current = 0 
    def __init__(self):
        tk.Frame.__init__(self)
    
    def switch_frame():
        screens[Screen.current].tkraise()

class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Braniac Maniac", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_geoquiz = tk.Button(self, text = "Geography Quiz", font = FONT)
        self.btn_geoquiz.grid(row = 1, column = 0)
        
        self.btn_historyquiz = tk.Button(self, text = "History Quiz", font = FONT)
        self.btn_historyquiz.grid(row = 2, column = 0)
        
        self.btn_music_quiz = tk.Button(self, text = "Music Quiz", font = FONT)
        self.btn_music_quiz.grid(row = 3, column = 0)
    
        self.btn_vidgamquiz = tk.Button(self, text = "Video Game Quiz", font = FONT)
        self.btn_vidgamquiz.grid(row = 4, column = 0)
        
        self.btn_mixquiz = tk.Button(self, text = "Mixed Quiz", font = FONT,
                                     command = self.go_mixed)
        self.btn_mixquiz.grid(row = 5, column = 0)
        
        self.btn_scores = tk.Button(self, text = "Highscores", font = FONT)
        self.btn_scores.grid(row = 6, column = 0)        
        
        self.btn_quit = tk.Button(self, text = "Quit", font = FONT)
        self.btn_quit.grid(row = 7, column = 0)

    def go_mixed(self):
        Screen.current = 1
        Screen.switch_frame()
        
class MixedQuiz(Screen):
    def __init___(self):
        Screen.__init__(self)
        self.scr_question = tkst.scrolledtext(self, text = "Question 1", font = TITLE_FONT)
        self.scr_question.grid(row = 0, column = 0, columnspan = 4, sticky = "news")
        
        self.btn_answera = tk.Button(self, text = "a", font = FONT)
        self.btn_answera.grid(row = 1, column = 0)
        
        self.ent_answera = tk.Entry(self, text = "aa", font = FONT)
        self.ent_answera.grid(row = 1, column = 1)
        
        self.btn_answerb = tk.Button(self, text = "b", font = FONT)
        self.btn_answerb.grid(row = 2, column = 0)

        self.ent_answerb = tk.Entry(self, text = "bb", font = FONT)
        self.ent_answerb.grid(row = 2, column = 1)
        
        self.btn_answerc = tk.Button(self, text = "c", font = FONT)
        self.btn_answerc.grid(row = 1, column = 2)

        self.ent_answerc = tk.Entry(self, text = "cc", font = FONT)
        self.ent_answerc.grid(row = 1, column = 3)

        self.btn_answerd = tk.Button(self, text = "d", font = FONT)
        self.btn_answerd.grid(row = 2, column = 2)
                                              
        self.ent_answerd = tk.Entry(self, text = "dd", font = FONT)
        self.ent_answerd.grid(row = 1, column = 3)


#Main
if __name__ == "__main__":
    mix = {}
    datafile = open("mix_questions.pickle", "rb")
    games = pickle.load(datafile)
    datafile.close()
    
    root = tk.Tk()
    root.title("Braniac Maniac")
    root.geometry("900x700") 
                
    screens = [MainMenu(), MixedQuiz()]
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    
                
    screens[0].tkraise()
    root.grid_columnconfigure(0, weight = 1)
    root.mainloop()   