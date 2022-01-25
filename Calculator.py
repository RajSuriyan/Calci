from tkinter import *
#operations
#Hello This is Raj Suriyan
#The Guy Who Wrote This Code

def btn(place,textx,rowx,columnx,functions=None):
    button1 = Button(place, text=str(textx), font=('Helvetica', 18), command=functions)
    button1.grid(row=rowx, column=columnx)


def printer():
    print('Hi')




def clicked(a):
    length=len(entry_box.get())


    entry_box.insert(length+1,a)

def clear1():
    length=len(entry_box.get())

    entry_box.delete(length-1)
def total_clear():
    entry_box.delete(0,END)

def calci():
    try:
        equals=eval(entry_box.get())
        entry_box.delete(0,END)
        entry_box.insert(0,str(equals))
    except:
        pass

def sign_it():
    s=entry_box.get()
    lis=[]
    sign=['-']
    for i in s:
        lis.append(i)
    s=sign+lis
    s1=''
    word=s1.join(s)
    entry_box.delete(0,END)

    entry_box.insert(0,word)




#Activator

root=Tk()
root.geometry('800x800')
root.iconbitmap('icon.ico')
root.title('Calculator')

entry_box=Entry(root,width=30,font=('Helvetica',18))
entry_box.grid(row=0,column=0)

btn1=btn(root,'1 ',rowx=1,columnx=2,functions=lambda p=1:clicked(1))
btn2=btn(root,'2 ',rowx=1,columnx=3,functions=lambda p=1:clicked(2))
btn3=btn(root,'3 ',rowx=1,columnx=4,functions=lambda p=1:clicked(3))

btn4=btn(root,'4 ',rowx=2,columnx=2,functions=lambda p=1:clicked(4))
btn5=btn(root,'5 ',rowx=2,columnx=3,functions=lambda p=1:clicked(5))
btn6=btn(root,'6 ',rowx=2,columnx=4,functions=lambda p=1:clicked(6))

btn7=btn(root,'7 ',rowx=3,columnx=2,functions=lambda p=1:clicked(7))
btn8=btn(root,'8 ',rowx=3,columnx=3,functions=lambda p=1:clicked(8))
btn9=btn(root,'9 ',rowx=3,columnx=4,functions=lambda p=1:clicked(9))

btn_eql=btn(root,'= ',rowx=4,columnx=2,functions=lambda p=1:calci())
btn_add=btn(root,'+ ',rowx=4,columnx=3,functions=lambda p=1:clicked('+'))
btn_sub=btn(root,'- ',rowx=4,columnx=4,functions=lambda p=1:clicked('-'))

btn_div=btn(root,'/ ',rowx=5,columnx=2,functions=lambda p=1:clicked('/'))
btn_mul=btn(root,'* ',rowx=5,columnx=3,functions=lambda p=1:clicked('*'))
btn_clear=btn(root,'CE ',rowx=5,columnx=4,functions=lambda p=1:total_clear())

delete1=btn(root,'C ',rowx=6,columnx=2,functions=lambda p=1:clear1())
btn_decimal=btn(root,'. ',rowx=6,columnx=3,functions=lambda p=1:clicked('.'))
btn_sign=btn(root,'+-',rowx=6,columnx=4,functions=lambda p=1:sign_it())

btn0=btn(root,'0 ',rowx=7,columnx=3,functions=lambda p=1:clicked(0))









root.mainloop()

#Thankyou For Looking My Code Caci 2.0