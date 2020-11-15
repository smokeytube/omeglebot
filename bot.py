#bot for making a bit of money from sad people on the internet
#coded completely by smokeytube, you are allowed to edit and redistribute as you like.
import pyautogui
import time
from selenium import webdriver
import win32api, win32con
from tkinter import *

win = Tk()
win.title("OmegleBot")
win.geometry("300x150")
heading = Label(win, text="Input into the feilds")

Label(win, text="Made by Zach").place(x=200, y=10)
Label(win, text="Make money!").place(x=200, y=30)

Label(win, text="Enter adfly link:").place(x=10, y=10)
linkcontent = StringVar()
Entry(win, textvariable=linkcontent, width=25, bg="gray").place(x=10, y=30)
def link():
    print (str(linkcontent.get()))
Button(win, text="Submit", width=5, height=1, bg="gray", command=link).place(x=10, y=50)

Button(win, text="Start", bg="red", command=win.quit).place(x=10, y=100)

win.mainloop()

linkcontent = str(linkcontent.get())
print ("got here")
# http://criarysm.com/3yeg my adfly link
if linkcontent == '':
    linkcontent = 'http://criarysm.com/3yeg'
else:
    linkcontent = str(linkcontent.get())

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
        #pyautogui.click()
        time.sleep(0.001)

def imageProcess(image):
        print ("imageProcess")
        return pyautogui.locateOnScreen(image, conf5)

while True:
    # msgboxcontent = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea')
    # msgboxcontent.click()
    # msgboxcontent.typewrite("hey")
    time.sleep(1)
    pyautogui.typewrite("hey")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite("f. 19")
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite("you?")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite("nice lol. If you wanna get together contact me: " + linkcontent)
    time.sleep(7)
    pyautogui.press('enter')
    time.sleep(3)
    if imageProcess('newchat.png'):
            click('newchat.png')
    else:
        pyautogui.press('escape')
        time.sleep(0.2)
        pyautogui.press('escape')
        time.sleep(0.2)
        pyautogui.press('escape')