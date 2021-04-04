import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
import heapq
import heapq 
nltk.download ('punkt')
def nltk_summarizer(raw_text):
    sentence_scores={}
    stopwords=nltk.corpus.stopwords.words("english")
    word_frequencies={}
    for word in nltk.word_tokenize(raw_text):
           if word not in stopwords:
                if word not in word_frequencies.keys(): 
                    word_frequencies[word]=1
                else:
                    word_frequencies[word] +=1 
    maximum_frequency=max(word_frequencies.values()) 
    for word in word_frequencies.keys():
           word_frequencies[word]=(word_frequencies[word]/maximum_frequency) 
    sentence_list=nltk.sent_tokenize(raw_text)
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                      if sent not in sentence_scores.keys():
                              sentence_scores[sent] = word_frequencies[word] 
                      else:
                              sentence_scores[sent] +=word_frequencies[word]

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ''.join(summary_sentences) 
    return (summary)
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
import time

timestr=time.strftime("%Y%m%d-%H%M%S") 
from bs4 import BeautifulSoup
import requests
from gtts import gTTS 
import os
from rake_nltk import Rake 
window=Tk()
window.title("Summaryzer GUI")
window.geometry("700x500")
style=ttk.Style(window) 
style.configure('lefttab.TNotebook',tabposition='wn')
def clear_text():
    entry.delete('1.0',END) 
def clear_display_result():
    tab1_display.delete('1.0',END) 
def save_summary(): 
    raw_text=entry.get('1.0',tk.END)
    final_text=nltk_summarizer(raw_text) 
    file_name='yoursummary'+timestr+'.txt' 
    with open(file_name,'w') as f:
        f.write(final_text)
    result='\nNAme of file: {},\nSummary: {}'.format(file_name,final_text) 
    tab1_display.insert(tk.END,result)
def clear_text_file(): 
    displayed_file.delete('1.0',END)
def clear_text_result(): 
    tab2_display_text.delete('1.0',END)
def clear_url_entry(): 
    url_entry.delete(0,END)
def clear_url_display(): 
    tab3_display_text.delete('1.0',END)
def clear_compare_text(): 
    entry1.delete('1.0',END)
def clear_compare_display_result(): 
    tab4_display_text.delete('1.0',END)
def sound(): 
    text=tab1_display.get('1.0',tk.END) 
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save("Downloads/summary.mp3")
def keyword(): 
    text=entry.get('1.0',tk.END) 
    r=Rake()
    r.extract_keywords_from_text(text) 
    s=""
    l=r.get_ranked_phrases() 
    for i in l:
        s=s+"\n"+i 
    tab1_display.insert(tk.END,s)
tab_control=ttk.Notebook(window,style='lefttab.TNotebook')
tab1=ttk.Frame(tab_control) 
tab2=ttk.Frame(tab_control) 
tab3=ttk.Frame(tab_control)
tab_control.add(tab1,text=f' {"Home":^20s}') 
tab_control.add(tab2,text=f' {"File":20s}') 
tab_control.add(tab3,text=f' {"URL":20s}')
label1=Label(tab1,text='Summaryzer',padx=5,pady=5) 
label1.grid(column=0,row=0) 
label2=Label(tab2,text='File Processing',padx=5,pady=5) 
label2.grid(column=0,row=0) 
label3=Label(tab3,text='URL',padx=5,pady=5) 
label3.grid(column=0,row=0)
tab_control.pack(expand=1,fill='both')
l1=Label(tab1,text='Enter text to Summarize',padx=5,pady=5) 
l1.grid(column=0,row=1)
entry=ScrolledText(tab1,height=10) 
entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)
tab1_display=ScrolledText(tab1,height=10) 
tab1_display.grid(row=9,column=0,columnspan=2,padx=5,pady=5)
button1=Button(tab1,text='Reset',command=clear_text,width=12,bg='#A569BD',fg='#fff') 
button1.grid(row=4,column=0,pady=10,padx=10)
button2=Button(tab1,text='Summarize',command=save_summary,width=12,bg='#85C1E9',fg='#fff')
button2.grid(row=4,column=1,pady=10,padx=10)
button3=Button(tab1,text='Clear Result',command=clear_display_result,width=12,bg='#E67E22',fg='#fff')
button3.grid(row=4,column=2,pady=10,padx=10)
button4=Button(tab1,text='Audio FIle',command=sound,width=12,bg='#0E6655',fg='#fff') 
button4.grid(row=4,column=3,pady=10,padx=10) 
button5=Button(tab1,text='Keywords',command=keyword,width=12,bg='#F1C40F',fg='#fff') 
button5.grid(row=4,column=4,pady=10,padx=10)
def openfiles():
    file1=tkinter.filedialog.askopenfilename(filetype=(('text files',".txt"),("All files","*"))) 
    read_text=open(file1).read()
    displayed_file.insert(tk.END,read_text)




def save_summary2():
    raw_text=displayed_file.get('1.0',tk.END) 
    final_text=nltk_summarizer(raw_text) 
    file_name='yoursummary'+timestr+'.txt' 
    with open(file_name,'w') as f:
        f.write(final_text)
    result='\nNAme of file: {},\nSummary: {}'.format(file_name,final_text) 
    tab2_display_text.insert(tk.END,final_text)


def sound1(): 
    text=tab2_display_text.get('1.0',tk.END) 
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save("Downloads/summary.mp3")


def keyword1(): 
    text=displayed_file.get('1.0',tk.END) 
    r=Rake() 
    r.extract_keywords_from_text(text) 
    s=""
    l=r.get_ranked_phrases() 
    for i in l:
        s=s+"\n"+i 
        tab2_display_text.insert(tk.END,s)
displayed_file=ScrolledText(tab2,height=10) 
displayed_file.grid(row=1,column=0,columnspan=3,padx=5,pady=5)
tab2_display_text=ScrolledText(tab2,height=10) 
tab2_display_text.grid(row=7,column=0,columnspan=3,padx=5,pady=5) 
tab2_display_text.config(state=NORMAL)
b0=Button(tab2,text='Open file',command=openfiles,width=12,bg='#A93226',fg='#fff') 
b0.grid(row=4,column=0,pady=10,padx=10)
b1=Button(tab2,text='Reset',command=clear_text_file,width=12,bg='#5DADE2',fg='#fff') 
b1.grid(row=4,column=1,pady=10,padx=10)
b2=Button(tab2,text='Summarize',command=save_summary2,width=12,bg='#F1C40F',fg='#fff') 
b2.grid(row=4,column=2,pady=10,padx=10)
b3=Button(tab2,text='Clear Result',command=clear_text_result,width=12,bg='#DC7633',fg='#fff')
b3.grid(row=4,column=3,pady=10,padx=10)
b4=Button(tab2,text='Close',command=window.destroy,width=12,bg='#D7BDE2',fg='#fff') 
b4.grid(row=4,column=4,pady=10,padx=10)
button4=Button(tab2,text='Audio FIle',command=sound1,width=12,bg='#0E6655',fg='#fff') 
button4.grid(row=4,column=5,pady=10,padx=10) 
bb6=Button(tab2,text='Keyword',command=keyword1,width=12,bg='#85C1E9',fg='#fff') 
bb6.grid(row=4,column=6,pady=10,padx=10)
def url_save(): 
    URL=url_entry.get()
    r=requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser') 
    l=soup.find_all('p')
    s=""
    for i in range(len(l)):
       s=s+l[i].get_text() 
       url_display.insert(tk.END,s)
def save_summary3(): 
    raw_text=url_display.get('1.0',tk.END) 
    final_text=nltk_summarizer(raw_text) 
    file_name='yoursummary'+timestr+'.txt'
    with open(file_name,'w') as f:
        f.write(final_text)
    result='\nNAme of file: {},\nSummary: {}'.format(file_name,final_text) 
    tab3_display_text.insert(tk.END,final_text)
def sound3(): 
    text=tab3_display_text.get('1.0',tk.END) 
    language = 'en'  #
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save("Downloads/Summary.mp3")
def keyword3(): 
    text=url_display.get('1.0',tk.END) 
    r=Rake() 
    r.extract_keywords_from_text(text)
    s=""
    l=r.get_ranked_phrases() 
    for i in l:
        s=s+"\n"+i 
        tab3_display_text.insert(tk.END,s) 
def clear_display_result1():
    url_display.delete('1.0',END) 
ll1=Label(tab3,text="Enter URL To Summarize") 
ll1.grid(row=1,column=0)
raw_entry=StringVar() 
url_entry=Entry(tab3,textvariable=raw_entry,width=50) 
url_entry.grid(row=1,column=1)
bb1=Button(tab3,text='Reset',command=clear_url_entry,width=12,bg='#7D6608',fg='#fff') 
bb1.grid(row=4,column=0,pady=10,padx=10)
bb2=Button(tab3,text='Get Text',command=url_save,width=12,bg='#641E16',fg='#fff') 
bb2.grid(row=4,column=1,pady=10,padx=10)
bb3=Button(tab3,text='clear Result',command=clear_url_display,width=12,bg='#1B2631',fg='#fff')
bb3.grid(row=4,column=2,pady=10,padx=10)
bb4=Button(tab3,text='Summarize',command=save_summary3,width=12,bg='#4A235A',fg='#fff')
bb4.grid(row=4,column=3,pady=10,padx=10)
bb5=Button(tab3,text='clear Text',command=clear_display_result1,width=12,bg='#641E16',fg='#fff')
bb5.grid(row=4,column=4,pady=10,padx=10)
bb6=Button(tab3,text='Audio File',command=sound3,width=12,bg='#0E6655',fg='#fff') 
bb6.grid(row=4,column=5,pady=10,padx=10)
bb7=Button(tab3,text='keywords',command=keyword3,width=12,bg='#F1C40F',fg='#fff') 
bb7.grid(row=4,column=6,pady=10,padx=10)
url_display=ScrolledText(tab3,height=10) 
url_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)
tab3_display_text=ScrolledText(tab3,height=10) 
tab3_display_text.grid(row=8,column=0,columnspan=3,padx=5,pady=5) 
window.mainloop()
 
