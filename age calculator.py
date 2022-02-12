import datetime as d
import calendar as c

d1=d.datetime.now()
y=int(input('enter year:'))
m=int(input('enter month:'))
d=int(input('enter day:'))
yy=d1.year-y
mm=d1.month-m
if mm<0:
    yy-=1
    mm+=12
    dd=d1.day-d
    if dd<0:
        mm-=1
        dd+=30
else:
    dd=d1.day-d
    if dd<0:
        mm-=1
        dd+=30



#-------------------------------------------------------
'''
from tkinter import *
from tkinter import ttk

root = Tk()
root.configure(bg='#0f5a4e')
root.geometry('450x500+300+100')
root.title('Age Calculator')

label = Label(root,bg='#0f5a4e',fg='#fff',text='Age Calculator',font=('Comic 25 bold'))
label.place(x=100,y=30)

lbl1 = Label(root,bg='#0f5a4e',fg='#fff',text='year',font=('times 15 bold'))
lbl1.place(x=20,y=100)

lbl2 = Label(root,bg='#0f5a4e',fg='#fff',text='month',font=('times 15 bold'))
lbl2.place(x=20,y=150)

lbl3 = Label(root,bg='#0f5a4e',fg='#fff',text='day',font=('times 15 bold'))
lbl3.place(x=20,y=200)


ent1 = Entry(root,bg='#fff',font=('times 13 bold'))
ent1.place(x=110,y=105)

months= ['1','2','3','4','5','6','7','8','9','10','11','12']
ent2=ttk.Combobox(root,width=27)
ent2.place(x=110,y=155)
ent2.config(value = months)

days= ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

ent3=ttk.Combobox(root,width=27)
ent3.place(x=110,y=205)
ent3.config(value = days)
'''









root.mainloop()
#-------------------------------------------------------
print(yy,'years ',mm,'months ',dd+1,'days')
print('\n or')
print((yy*12)+mm,'months ',dd+1,'days')
print('\n or')
days = ((yy+mm/12)*365.25+dd)
  
print(days,'days')
print('\n or')
print(days*24,'hours')
print('\n or')
print(days*24*60,'minutes')
print('\n or')
print(days*24*60*60,'seconds')    

