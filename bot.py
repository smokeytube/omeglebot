#bot for making a bit of money from sad people on the internet
#coded completely by smokeytube, you are allowed to edit and redistribute as you like.
import pyautogui
import time
from selenium import webdriver
import win32api, win32con
from tkinter import *
import random
from datetime import datetime


win = Tk()
win.title("OmegleBot")
win.geometry("300x250")
heading = Label(win, text="Input into the feilds")

Label(win, text="Made by Zach").place(x=200, y=10)
Label(win, text="Make money!").place(x=200, y=30)

Label(win, text="Enter adfly link:").place(x=10, y=10)
linkcontent = StringVar()
Entry(win, textvariable=linkcontent, width=25, bg="gray").place(x=10, y=30)
def link():
    print (str(linkcontent.get()))
Button(win, text="Submit", width=5, height=1, bg="gray", command=link).place(x=10, y=50)

var1 = IntVar()
def ratcheck():
    print (int(var1.get()))
Checkbutton(win, text="Timeout", variable=var1, command=ratcheck).place(x=200, y=150)

Label(win, text="Enter timeout time (I reccomend ~1 hour):").place(x=10, y=100)
Label(win, text="24 hour, no colon (ex. 15:40 would be 1540)").place(x=10, y=120)
timeoutvar = IntVar()
Entry(win, textvariable=timeoutvar, width=25, bg="gray").place(x=10, y=150)
def timeout():
    print (int(timeoutvar.get()))
Button(win, text="Submit", width=5, height=1, bg="gray", command=timeout).place(x=10, y=170)

Button(win, text="Start", bg="red", command=win.quit).place(x=10, y=220)

win.mainloop()

now = datetime.now()

current_time = now.strftime("%H%M")
print("Current Time =", current_time)
print("Current Time in 1 hour =", current_time)

timeoutchat = int(timeoutvar.get())
linkcontent = str(linkcontent.get())
timetimeout = int(var1.get())
print (timeoutchat)
# http://criarysm.com/3yeg my adfly link
if linkcontent == '':
    linkcontent = 'http://criarysm.com/3yeg'


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTIF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTIF_LEFTUP, 0, 0)

chromedriverdir = 'C:\webdrivers\chromedriver.exe'
driver = webdriver.Chrome(chromedriverdir)
driver.implicitly_wait(5)

driver.get('https://chatserv.omegle.com/?from=www.xiaodiaomao.com')
driver.implicitly_wait(5)

starttext = driver.find_element_by_xpath('//*[@id="textbtn"]')
starttext.click()


conf01 = confidence=0.01
conf5 = confidence=0.5

def click(image):
        start = pyautogui.locateOnScreen(image, conf01)
        print (image)
        pyautogui.moveTo(start)
        pyautogui.click()
        time.sleep(0.001)

def imageProcess(image):
        print ("imageProcess")
        return pyautogui.locateOnScreen(image, conf5)


while True:
    current_time = now.strftime("%H%M")
    age = ''

    shortrand = random.randint(1, 4)
    medrand = random.randint(4, 7)
    longrand = random.randint(6, 10)
    age = random.randint(17, 25)

    rand = random.randint(1, 3)
    rand2 = random.randint(1, 3)
    rand3 = random.randint(1, 3)

    time.sleep(shortrand)
    if rand == 1:
        pyautogui.typewrite("hey")
    elif rand == 2:
        pyautogui.typewrite("hello")
    elif rand == 3:
        pyautogui.typewrite("hi ")
    time.sleep(shortrand)
    pyautogui.press('enter')
    time.sleep(shortrand)
    pyautogui.typewrite("f. " + age)
    time.sleep(shortrand)
    pyautogui.press('enter')
    if rand2 == 1:
        pyautogui.typewrite("you?")
    else:
        pyautogui.typewrite("hbu?")
    time.sleep(shortrand)
    pyautogui.press('enter')
    time.sleep(shortrand)
    if rand3 == 1:
        pyautogui.typewrite("nice lol. If you wanna get together contact me: " + linkcontent)
    elif rand3 == 2:
        pyautogui.typewrite("lol if you want to add me we can chat in private " + linkcontent)
    elif rand3 == 3:
        pyautogui.typewrite("hey why dont we ditch omegle and chat here " + linkcontent)
    time.sleep(longrand)
    pyautogui.press('enter')
    time.sleep(medrand)
    if imageProcess('newchat.png'):
            click('newchat.png')
    else:
        pyautogui.press('escape')
        time.sleep(0.2)
        pyautogui.press('escape')
        time.sleep(0.2)
        pyautogui.press('escape')
    if timeoutchat == 1 and timetimeout == 1:
        driver.close()
        time.sleep(2175984000)