"""Search musics with lyrics
Codded by ALIREZA RAHIMI
import usable libraries"""

# import libraries
import tkinter
from tkinter import Label, StringVar, messagebox
from typing import Text
import requests
from bs4 import BeautifulSoup

# define function to scraping on datasets
def Click():
    Name_info = Name.get()
    messagebox.askquestion("Confirm", "Search Result About: " + Name_info + "\nAre You Sure?")
    Response = requests.get("https://songsear.ch/q/" + Name_info)
    Soup = BeautifulSoup(Response.content, "html.parser")
    try:
        My_Class = Soup.ul.strings
        Soup.prettify()

        My_file = open("Music Searcher.txt", "w+")
        for item in My_Class:
            My_file.write(item)
        My_file.close()
    except:
        print("OOPS! Can't Find Any Results :(")

# work with TKinter to use GUI
root = tkinter.Tk()
root.title("Music Searcher")
tkinter.Label(root, text="Welcome to Music Searcher\nPlease Enter Your Music Name :", font=("calibri", 12)).pack()
Name = StringVar()
tkinter.Entry(root, font=("arial", 12, "bold"), insertwidth=4, bg="powder blue", textvariable=Name).pack()
tkinter.Button(root, padx=13,bd=5, text="Search", command=Click).pack()
lab = tkinter.Label(root, text="Alireza Rahimi", foreground="red")
tkinter.Label(root, text=(r"|Powered By Alireza Rahimi|") ,font=("Algerian", 10), foreground="red").pack()

# show graphical box
root.mainloop()