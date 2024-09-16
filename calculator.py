from tkinter import *
import tkinter as t
c=t.Tk()
c.iconbitmap(r'C:\Users\rajku\OneDrive\Desktop\programs\Rays\Python\GUI\Calicon.ico')
c.geometry('450x580')
c.resizable(0,0)
c.title('Calculator')
flag=True;onn=False;check=True      # flag for = , onn - on/off , check - !opr after 0 
def cal(a):
    global onn;global flag;global check
    l=len(tf.get());area=str(tf.get());opr=['+','-','*','/','**']
    if a=='swc':
        tf.config(state='normal')
        if onn==True:
            tf.delete(0,l); tf.insert(0,'OFF')
            res.config(text='')
            flag=True;onn=False
            bswc.config(bg='green',text='ON')
        else:
            tf.delete(0,l); tf.insert(0,0)
            flag=True;onn=True;check=True
            bswc.config(bg='red',text='OFF')
        tf.config(state='disabled')

    elif a=='.'and onn and check:
        tf.config(state='normal')
        if area=='0':
            tf.delete(0,l); tf.insert(0,'0.')       # if . after 0 , then 
        else:
            if '.' not in area:            # . does't repeat
                tf.insert(l,a)
        tf.config(state='disabled')
    elif a in opr and onn and area!='0':       # if area 0 , opr's not work
        tf.config(state='normal')
        if flag:
            res.config(text=res.cget('text')+tf.get()+a)
        else:
            res.config(text=area+a)   # after = res will be update
        flag=True;check=True
        tf.delete(0,l);tf.insert(0,0)
        tf.config(state='disabled')
    elif a=='=' and onn and check:  # check for (after = not again =)
        tf.config(state='normal')
        flag=False;check=False
        res.config(text=res.cget('text')+tf.get())
        tf.delete(0,l)
        tf.insert(0,eval(res.cget('text')))
        res.config(text=res.cget('text')+a)    # for = sym in res after = clicked
        tf.config(state='disabled')
    elif a=='c' and onn:
        tf.config(state='normal')
        flag=True;check=True
        tf.delete(0,l); tf.insert(0,0)
        res.config(text='')
        tf.config(state='disabled')
    elif a=='b' and onn:
        tf.config(state='normal')
        if l==1:                    # for last bkspc , insert 0
            tf.delete(0,l); tf.insert(0,0)
        else:
            tf.delete(l-1,l)
        tf.config(state='disabled')
    elif '9'>=a>='0' and onn:
        tf.config(state='normal')
        if area=='0':            # replace 0 with number
            tf.delete(0,l);tf.insert(0,a) 
        elif check==False :
            tf.delete(0,l);tf.insert(0,a)
            res.config(text='')
            check=True
        else:
            tf.insert(l,a)
        tf.config(state='disabled')
#----------------------------------UI PART-------------------------------------------
res=t.Label(c,width=42,border=7,height=7,font=('bold',13),fg='#38211d',anchor='e',bg='#c3d1b0')
res.place(x=23,y=49)
tf=t.Entry(c,disabledbackground='#c3d1b0',disabledforeground='black',width=27,bg='#c3d1b0',font=('bold',19),justify='right',border=0)
tf.place(x=29,y=160);tf.insert(0,'OFF');tf.config(state='disabled')#-----buttons-----
t.Button(c,text='',font=('bold',25),bg='#c3d1b0',width=3,height=1,border=0).place(x=105,y=480)
bpow=t.Button(c,text='xⁿ  ',font=('bold',16),bg='#c3d1b0',width=4,height=2,border=0,command=lambda:cal('**'))
bpow.place(x=105,y=480)
b1=t.Button(c,text='1',font=('bold',30),border=0,width=3,command=lambda:cal('1')).place(x=30,y=240)
b4=t.Button(c,text='4',font=('bold',30),border=0,width=3,command=lambda:cal('4')).place(x=30,y=320)
b7=t.Button(c,text='7',font=('bold',30),border=0,width=3,command=lambda:cal('7')).place(x=30,y=400)
bc=t.Button(c,text='C',font=('bold',25),bg='#c3d1b0',width=4,height=1,border=0,command=lambda:cal('c'))
bc.place(x=25,y=480)
b2=t.Button(c,text='2',font=('bold',30),border=0,width=3,command=lambda:cal('2')).place(x=138,y=240)
b5=t.Button(c,text='5',font=('bold',30),border=0,width=3,command=lambda:cal('5')).place(x=138,y=320)
b8=t.Button(c,text='8',font=('bold',30),border=0,width=3,command=lambda:cal('8')).place(x=138,y=400)
b0=t.Button(c,text='0   ',font=('bold',25),bg='#c3d1b0',width=3,height=1,border=0,command=lambda:cal('0')).place(x=157,y=480)
b3=t.Button(c,text='3',font=('bold',30),border=0,width=3,command=lambda:cal('3')).place(x=246,y=240)
b6=t.Button(c,text='6',font=('bold',30),border=0,width=3,command=lambda:cal('6')).place(x=246,y=320)
b9=t.Button(c,text='9',font=('bold',30),border=0,width=3,command=lambda:cal('9')).place(x=246,y=400)
beq=t.Button(c,text='=',font=('bold',25),bg='#c3d1b0',width=4,height=1,border=0,command=lambda:cal('='))
beq.place(x=272,y=480)
bp=t.Button(c,text='+',font=('bold',25),bg='#c3d1b0',width=3,height=2,border=0,command=lambda:cal('+'))
bp.place(x=354,y=250)
bm=t.Button(c,text='-',font=('bold',25),bg='#c3d1b0',width=3,height=0,border=0,command=lambda:cal('-'))
bm.place(x=354,y=335)
bmul=t.Button(c,text='⨯',font=('bold','25'),bg='#c3d1b0',width=3,height=2,border=0,command=lambda:cal('*'))
bmul.place(x=354,y=390)
bdiv=t.Button(c,text='/',font=('bold',25),bg='#c3d1b0',width=3,height=1,border=0,command=lambda:cal('/'))
bdiv.place(x=354,y=480)
bbk=t.Button(c,text='⬅️',font=('bold',25),bg='#c3d1b0',width=3,height=0,border=0,command=lambda:cal('b')).place(x=354,y=198)
bdot=t.Button(c,text='•  ',font=('bold',25),bg='#c3d1b0',width=3,height=1,border=0,command=lambda:cal('.'))
bdot.place(x=220,y=480)
bswc=t.Button(c,activebackground='yellow',fg='white',disabledforeground='black',text='ON',font=('bold',10),bg='green',width=4,height=1,command=lambda:cal('swc'))
bswc.place(x=295,y=198)
right=t.Label(c,text='by : RAJ',font=('times new roman',8),bg='#c3d1b0',fg='#021a5c')
right.place(x=25,y=49)
c.mainloop()