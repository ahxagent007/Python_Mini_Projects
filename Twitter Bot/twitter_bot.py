from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *

class twitter_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)

        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')

        email.clear()
        password.clear()

        email.send_keys(self.username)
        password.send_keys(self.password)

        password.send_keys(Keys.RETURN)

        time.sleep(10)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+str(hashtag)+'&src=typed_query')

        for i in range(0,30):

            print('Window Scrolling')
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')

            print('sleeping.')
            time.sleep(1)
            print('sleeping..')
            time.sleep(1)

            print('pyautogui ...')
            pyautogui.click(pyautogui.locateCenterOnScreen('1.png'), duration=2)

            print('sleeping.')
            time.sleep(1)
            print('sleeping..')
            time.sleep(1)
            print('sleeping...')
            time.sleep(1)



window = Tk()
window.geometry("700x600")

emails = Label(window, text="Enter your email here", font = "times 24 bold")
emails.grid(row=0, column=0)
entry_email = Entry(window)
entry_email.grid(row=0, column=6)

password = Label(window, text="Enter your password here", font = "times 24 bold")
password.grid(row=2, column=0)
entry_pass = Entry(window)
entry_pass.grid(row=2, column=6)

hashtag = Label(window, text="Enter #hashtag here", font = "times 24 bold")
hashtag.grid(row=4, column=0)
entry_hash = Entry(window)
entry_hash.grid(row=4, column=6)

def execute():
    log = twitter_bot(str(entry_email.get()), str(entry_pass.get()))
    log.login()
    log.like_tweet(str(entry_hash.get()))


button = Button(window, text= "GO", command=execute, width=12, bg='gray')
button.grid(row=7, column=6)

window.mainloop()




















