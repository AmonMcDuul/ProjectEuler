from tkinter import *
import math

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Nth number')
        self.lbl3=Label(win, text='Calculated prime number')
        self.t1=Entry(bd=3)
        self.t3=Entry()
        self.btn2=Button(win, text='Calculate nth prime number')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b2=Button(win, text='Calculate nth prime number')
        self.b2.bind('<Button-1>', self.sub)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        result = self.nthPrimeNumber(num1)
        self.t3.insert(END, str(result))   
    def nthPrimeNumber(self, event):
        start = 2
        count = 0
        num1=int(self.t1.get())
        while True:
            if all([start % i for i in range(2, int(math.sqrt(start)) + 1)]) != 0:
                count += 1
                if count == num1:
                    return start
            start += 1 
            
window=Tk()
mywin=MyWindow(window)
window.title('Euler 7 bitchas')
window.geometry("400x300+10+10")
window.mainloop()
# Launch ...
if __name__ == '__main__':
    app = MyWindow()