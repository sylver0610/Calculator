import tkinter as tk
from tkinter import*
import string
import sys
from tkinter import messagebox


def main():
    Root=Tk()
    gui=windown(Root)
    Root.mainloop()
    return None

class windown:
    def __init__(self,window):
        self.window=window
        self.window.geometry('350x200')
        self.result_to_call=''
        self.result=StringVar()
        self.ktdb=['AC','C','.','=']
        self.ktdb1=['+','%','x','-',':']
        self.number= string.digits + '.'
        #add textbox
        self.txt = Entry(self.window,width=50,textvariable=self.result)
        self.txt.grid(column=0,row=0,columnspan=4,padx=2,pady=2)

        #row 1
        btnAC=Button(self.window,text='AC',command=lambda:self.handlebutton('AC')).grid(column=0,row=1,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btnC=Button(self.window,text='C',command=lambda:self.handlebutton('C')).grid(column=1,row=1,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btnpercent=Button(self.window,text='%',command=lambda:self.handlebutton('%')).grid(column=2,row=1,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btndiv=Button(self.window,text=':',command=lambda:self.handlebutton(':')).grid(column=3,row=1,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)

        #row 2
        btn7=Button(self.window,text='7',command=lambda:self.handlebutton('7')).grid(column=0,row=2,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btn8=Button(self.window,text='8',command=lambda:self.handlebutton('8')).grid(column=1,row=2,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btn9=Button(self.window,text='9',command=lambda:self.handlebutton('9')).grid(column=2,row=2,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btnmul=Button(self.window,text='x',command=lambda:self.handlebutton('x')).grid(column=3,row=2,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)

        #row 3
        btn4=Button(self.window,text='4',command=lambda:self.handlebutton('4')).grid(column=0,row=3,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btn5=Button(self.window,text='5',command=lambda:self.handlebutton('5')).grid(column=1,row=3,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btn6=Button(self.window,text='6',command=lambda:self.handlebutton('6')).grid(column=2,row=3,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btnsub=Button(self.window,text='-',command=lambda:self.handlebutton('-')).grid(column=3,row=3,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)

        #row 4
        btn1=Button(self.window,text='1',command=lambda:self.handlebutton('1')).grid(column=0,row=4,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btn2=Button(self.window,text='2',command=lambda:self.handlebutton('2')).grid(column=1,row=4,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btn3=Button(self.window,text='3',command=lambda:self.handlebutton('3')).grid(column=2,row=4,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btnadd=Button(self.window,text='+',command=lambda:self.handlebutton('+')).grid(column=3,row=4,columnspan=1,rowspan=2,sticky=N+E+S+W,padx=2,pady=2)

        #row 5
        btn0=Button(self.window,text='0',command=lambda:self.handlebutton('0')).grid(column=0,row=5,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btndot=Button(self.window,text='.',command=lambda:self.handlebutton('.')).grid(column=1,row=5,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)
        btnequal=Button(self.window,text='=',command=lambda:self.handlebutton('=')).grid(column=2,row=5,columnspan=1,sticky=N+E+S+W,padx=2,pady=2)

                                                
    def handlebutton(self,requirement):
        prior1 = ["x",":"]
        prior2 = ["=",'-']
        prior3 = ['+','-']
        flag = True
        if requirement not in self.ktdb:
            self.result_to_call += requirement
            self.result.set(self.result_to_call)
            self.txt.icursor(len(self.result_to_call))
        elif requirement == 'AC':
            self.result_to_call=''
            self.result.set(self.result_to_call)
            self.txt.icursor(len(self.result_to_call))
        elif requirement == 'C':
            self.result_to_call=self.result_to_call[:len(self.result_to_call)-1]
            self.result.set(self.result_to_call) 
            self.txt.icursor(len(self.result_to_call))
        elif requirement == '.':
            self.result_to_call += requirement
            self.result.set(self.result_to_call) 
            self.txt.icursor(len(self.result_to_call))
        elif requirement == '=':
            n = 0
            while n < len(self.result_to_call) - 2:           
                self.result_to_call = list(self.result_to_call)
                if self.result_to_call[n] in prior3 and self.result_to_call[n+1] in prior3:
                    if self.result_to_call[n] == '+' and self.result_to_call[n+1] == '-' or self.result_to_call[n] == '-' and self.result_to_call[n+1] == '+':
                        self.result_to_call[n] = '-'
                    else:
                        self.result_to_call[n] = '+'
                    self.result_to_call.pop(n+1)
                elif self.result_to_call[n] in prior1 and self.result_to_call[n+1] in prior1:
                        messagebox.showerror("Error", "Nhập ngu như con bò!!!!")
                        self.result_to_call = ''
                        flag = False
                        break
                else:
                    n += 1
            if flag:  
                #print(self.result_to_call,'0')        
                self.result_to_call = ''.join(self.result_to_call)  
                #print(self.result_to_call,'000') 
                self.list_so = self.result_to_call
                #print(self.list_so,'1') # String

                for r in self.ktdb1:
                    self.list_so=self.list_so.replace(r,' ')  
                self.list_so=self.list_so.split() # Trả về list
                #print(self.list_so,'2')
                self.list_dau=self.result_to_call

                for r in self.number:
                    self.list_dau=self.list_dau.replace(r,' ')
                #print(self.list_dau,'3')
                self.list_dau=self.list_dau.split()
                #print(self.list_dau,'4')

                while (self.list_dau.count('x')!=0) or (self.list_dau.count(':')!=0) or (self.list_dau.count('%')!=0):
                    try:
                        pos_1=self.list_dau.index('x')
                    except Exception: 
                        pos_1=sys.maxsize
                    try:
                        pos_2=self.list_dau.index(':')
                    except Exception:
                        pos_2=sys.maxsize
                    try:
                        pos_3=self.list_dau.index('%')
                    except Exception:
                        pos_3=sys.maxsize
                    minn = min(pos_1,pos_2,pos_3)
                    if minn == pos_1:
                        self.list_so[pos_1]=float(self.list_so[pos_1])*float(self.list_so[pos_1+1])
                        self.list_so.pop(pos_1+1)
                        self.list_dau.pop(pos_1)
                    elif minn == pos_2:
                        self.list_so[pos_2]=float(self.list_so[pos_2])/float(self.list_so[pos_2+1])
                        self.list_so.pop(pos_2+1)
                        self.list_dau.pop(pos_2)
                    elif minn == pos_3:
                        self.list_so[pos_3]=float(self.list_so[pos_3])%float(self.list_so[pos_3+1])
                        self.list_so.pop(pos_3+1)
                        self.list_dau.pop(pos_3)
                        #print(self.list_so[vtr1],' ',vtr2)
                while 1:
                    try:
                        if self.list_dau[0] == "+":
                            self.list_so[0] = float(self.list_so[0])+float(self.list_so[1])
                        elif self.list_dau[0] == "-":
                            self.list_so[0] = float(self.list_so[0])-float(self.list_so[1])
                        self.list_so.pop(1)
                        self.list_dau.pop(0)
                    except IndexError:
                        break
                self.result_to_call = self.list_so[0]
                self.result.set(self.result_to_call)
                self.txt.icursor(len(list(str(self.result_to_call))))
                self.result_to_call = ''

main()



























































