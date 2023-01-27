import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from tkinter import *
from tkinter import messagebox
import time
import datetime as dt
root=Tk()

def msgbox():
    messagebox.showinfo("안내","아직 지원하지 않습니다.")

def quit():
    root.destroy()
    root.quit()
def round():
    def process():
        driver=webdriver.Chrome('./chromedriver.exe')
        #구글링으로  검색
        words = []
        googleURL = 'https://www.google.com/search?q='
        driver.get(googleURL + e1.get())
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        temp = str(soup.find_all('h3',{'class': 'LC20lb DKV0Md'})).split(',')
        for i in temp:
            words.append(i.replace('<h3 class="LC20lb DKV0Md">','').replace('</h3>','').replace('[','').replace(']',''))
        temp = str(soup.find_all('span', {'class': 'st'})).replace('<span class="st"><span class="f">','').replace(', <span class="st"','').replace('...','').replace(']','').split('</span>')
        for i in range(0,len(temp)):
            if temp[i].find('-') == -1 and len(temp[i]) != 0 :
                words.append(temp[i].replace('>',''))

        #네이버로 검색 
        naverURL = 'https://search.naver.com/search.naver?query='
        driver.get(naverURL + e1.get())
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        temp = str(soup.find_all('dd',{'class':'sh_web_passage'})).replace('<dd class="sh_web_passage">','').replace('...</dd>','').split(',')
        words += temp

        temp = str(soup.find_all('dd',{'class':'sh_blog_passage'})).replace('<dd class="sh_blog_passage">','').split('</dd>')
        for i in range(0, len(temp)):
            temp[i] = temp[i].replace('<strong class="hl">','').replace('</dd>','')
        words += temp

        temp = str(soup.find_all('dd',{'class':'answer'})).replace('<dd class="answer"> <strong class="spkn">답변</strong> ','').split('</strong>')
        for i in range(0, len(temp)):
            temp[i] = temp[i].replace('<strong class="hl">','').replace('</dd>','')
        words += temp

        temp = str(soup.find_all('dd',{'class':'sh_cafe_passage'})).split('</strong>')
        for i in range(0, len(temp)):
            temp[i] = temp[i].replace('<strong class="hl">','').replace('</dd>','')
        words += temp

        for i in range(0,len(words)):
            print(str(i) + ' : ' + str(words[i]))
        
            
    def reset():
        e1.delete(0, END)
    def close():
        window.destroy()
    window=Tk()
    l1=Label(window, text="아이디", font="helvetica 10 italic")
    l1.grid(row=0, column=0)
    e1=Entry(window, bg="white", fg="green")
    e1.grid(row=0, column=1)

    b1=Button(window, text="검색", command=process)
    b2=Button(window, text="초기화", command=reset)
    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3=Button(window, text="종료", command=close)
    b3.grid(row=2, column=2)
    window.mainloop()

menubar=Menu(root)

f1=Menu(menubar, tearoff=0)
f1.add_command(label="크롤링", command=round)
f1.add_command(label="현재시간", command=msgbox)
f1.add_command(label="저장", command=msgbox)
f1.add_separator()
f1.add_command(label="Exit", command=quit)

menubar.add_cascade(label="프로그램", menu=f1)
root.config(menu=menubar)
root.mainloop()
