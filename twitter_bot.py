from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
import pyautogui
from tkinter import *

window = Tk()
window.geometry("700X600")

emails = Label(window, text="Enter your email here", font = "times 24 bold")
emails.grid(row=0, column=0)
entry_email = Entry(window)
entry_email.grid(row=0, column=6)