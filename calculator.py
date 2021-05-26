import tkinter as tk
from tkinter import*
import string
import sys

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
        self.number= string.digits
        #add textbox
        txt= Entry(self.window,width=50,textvariable=self.result ).grid(column=0,row=0,columnspan=4,padx=2,pady=2)

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
        if requirement not in self.ktdb:
            self.result_to_call += requirement
            self.result.set(self.result_to_call)
        elif requirement == 'AC':
            self.result_to_call=''
            self.result.set(self.result_to_call)
        elif requirement == 'C':
            self.result_to_call=self.result_to_call[:len(self.result_to_call)-1]
            self.result.set(self.result_to_call) 
        
        elif requirement == '=':
            self.list_so=self.result_to_call
            for r in self.ktdb1:
                self.list_so=self.list_so.replace(r,' ')  
            self.list_so=self.list_so.split(' ')
            self.list_dau=self.result_to_call
            for r in self.number:
                self.list_dau=self.list_dau.replace(r,' ')
            self.list_dau=self.list_dau.split()
            while (self.list_dau.count('x')!=0) or (self.list_dau.count(':')!=0):
                try:
                    vtr1=self.list_dau.index('x')
                except Exception: 
                    vtr1=sys.maxsize
                try:
                    vtr2=self.list_dau.index(':')
                except Exception:
                     vtr2=sys.maxsize
                if vtr1<vtr2:
                    self.list_so[vtr1]=float(self.list_so[vtr1])*float(self.list_so[vtr1+1])
                    self.list_so.pop(vtr1+1)
                    self.list_dau.pop(vtr1)
                else:
                    self.list_so[vtr2]=float(self.list_so[vtr2])/float(self.list_so[vtr2+1])
                    self.list_so.pop(vtr2+1)
                    self.list_dau.pop(vtr2)
                    #print(self.list_so[vtr1],' ',vtr2)
                
            print(self.list_so)
            print(self.list_dau)
            
                                    
        pass    

main()



























































