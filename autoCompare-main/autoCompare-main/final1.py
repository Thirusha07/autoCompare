# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 16:22:34 2022

@author: Swarneshwar S
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

root=Tk()
root.title('Login')
root.geometry('925x500+200+100')
root.configure(bg="#fff")
root.resizable(False,False)
def graph(n):
        screen2=Toplevel(root)
        screen2.title("plot")
        screen2.geometry('925x500+200+100')
        screen2.config(bg="white")
        screen2.resizable(False,False)
        company=n.get() 
        if company=='Select':
                messagebox.showinfo("select","select something")
        else:
                df=pd.read_csv('C:\\Users\\Swarneshwar S\\Desktop\\FILES\\SEMESTER 2\\python package\\New folder\\dataset01.csv')
                x=df['year']
                y=df[company]
                fig=plt.Figure(figsize=(10,8), dpi=100)
                fig.add_subplot(111).bar(x,y,color="#57a1f8", width=0.5)
                chart=FigureCanvasTkAgg(fig,screen2)
                chart.get_tk_widget().pack()
                screen2.mainloop()

        

        
        
def sales(c1, c2):
        option1=c1.get()
        option2=c2.get()
    
        if option1==1: 
                screen1=Toplevel(root)
                screen1.title("SALES")   
                screen1.geometry('925x500+200+100')
                screen1.config(bg="white")
                screen1.resizable(False,False)
                l2=Label(screen1,text="Sales Analysis", fg="#57a1f8", bg="#fff", font=('calibri(body)',23))
                l2.place(x=100, y=5)
                l3=Label(screen1, text="select manufacturer:", fg="#57a1f8", bg="#fff", font=('calibri(body)', 18))
                l3.place(x=150, y=100)
                n=StringVar()
                manufacturer=ttk.Combobox(screen1, width=27, textvariable = n)
                manufacturer['values']=('Select','Maruti Suzuki', 'Hyundai', 'Tata','Kia','Mahindra','Renault','Toyota','Honda','Ford','Morris Garage','volkswagen','Skoda','Datsun','Fiat','Nissan','HM-Mitsubishi','Chevrolet')
                manufacturer.current(0)
                manufacturer.place(x=400,y=105)
                Button(screen1,width=39,pady=7,text='next', bg='#57a1f8',fg='white',border=0,command=lambda: graph(n)).place(x=435,y=200)
                screen1.mainloop()
        elif option2==1:
                screen1=Toplevel(root)
                screen1.title("COMPARE")   
                screen1.geometry('925x500+200+100')
                screen1.config(bg="white")
                screen1.resizable(False,False)
                def SelectModel1(*args):
                        model=data1.loc[data1['Make']==ma1.get(), 'Model'].tolist()
                        model1=set(model)
                        model2=tuple(model1)
                        model4['values']=model2    
                def SelectModel2(*args):
                        model=data1.loc[data1['Make']==ma2.get(), 'Model'].tolist()
                        model1=set(model)
                        model2=tuple(model1)
                        model5['values']=model2 
                def SelectModel3(*args):
                        model=data1.loc[data1['Make']==ma3.get(), 'Model'].tolist()
                        model1=set(model)
                        model2=tuple(model1)
                        model6['values']=model2 
                def SelectModel4(*args):
                        model=data1.loc[data1['Make']==ma4.get(), 'Model'].tolist()
                        model1=set(model)
                        model2=tuple(model1)
                        model7['values']=model2 
                def SelectModel5(*args):
                        model=data1.loc[data1['Make']==ma5.get(), 'Model'].tolist()
                        model1=set(model)
                        model2=tuple(model1)
                        model8['values']=model2 
                        
                        
                def SelectVariant1(*args):
                        var=data1.loc[data1['Model']==mo1.get(), 'Variant'].tolist()
                        var1=set(var)
                        var2=tuple(var1)
                        var4['values']=var2
                def SelectVariant2(*args):
                        var=data1.loc[data1['Model']==mo2.get(), 'Variant'].tolist()
                        var1=set(var)
                        var2=tuple(var1)
                        var5['values']=var2
                def SelectVariant3(*args):
                        var=data1.loc[data1['Model']==mo3.get(), 'Variant'].tolist()
                        var1=set(var)
                        var2=tuple(var1)
                        var6['values']=var2
                def SelectVariant4(*args):
                        var=data1.loc[data1['Model']==mo4.get(), 'Variant'].tolist()
                        var1=set(var)
                        var2=tuple(var1)
                        var7['values']=var2
                def SelectVariant5(*args):
                        var=data1.loc[data1['Model']==mo5.get(), 'Variant'].tolist()
                        var1=set(var)
                        var2=tuple(var1)
                        var8['values']=var2
                
                def plotGraph(*args):
                        filt=filt1.get()
                        carsy=[]
                        car1=data1.loc[(data1['Make']==ma1.get()) & (data1['Model']==mo1.get()) & (data1['Variant']==va1.get()), filt].tolist()
                        carsy.append(car1)
                        car2=data1.loc[(data1['Make']==ma2.get()) & (data1['Model']==mo2.get()) & (data1['Variant']==va2.get()), filt].tolist()
                        carsy.append(car2)
                        car3=data1.loc[(data1['Make']==ma3.get()) & (data1['Model']==mo3.get()) & (data1['Variant']==va3.get()), filt].tolist()
                        carsy.append(car3)
                        car4=data1.loc[(data1['Make']==ma4.get()) & (data1['Model']==mo4.get()) & (data1['Variant']==va4.get()), filt].tolist()
                        carsy.append(car4)
                        car5=data1.loc[(data1['Make']==ma5.get()) & (data1['Model']==mo5.get()) & (data1['Variant']==va5.get()), filt].tolist()
                        carsy.append(car5)
                        carsyf=[num for x in carsy for num in x]
                        carsx=[]
                        car11= va1.get()
                        carsx.append(car11)
                        car22= va2.get()
                        carsx.append(car22)
                        car33= va3.get()
                        carsx.append(car33)
                        car44= va4.get()
                        carsx.append(car44)
                        car55= va5.get()
                        carsx.append(car55)
                        #carsxf=[num1 for x1 in carsx for num1 in x1]
                        screen5=Toplevel(root)
                        screen5.title("graph")   
                        screen5.geometry('925x500+200+100')
                        screen5.config(bg="white")
                        screen5.resizable(False,False)
                        fig=plt.Figure(figsize=(10,8), dpi=100)
                        fig.add_subplot(111).bar(carsx,carsyf,color="#57a1f8", width=0.5)
                        chart=FigureCanvasTkAgg(fig,screen5)
                        chart.get_tk_widget().pack()
                        
                        
                        
                l2=Label(screen1,text="Car Analysis", fg="#57a1f8", bg="#fff", font=('calibri(body)',23))
                l2.place(x=80, y=5)
                data1=pd.read_csv("C:\\Users\\Swarneshwar S\\Desktop\\FILES\\SEMESTER 2\\python package\\New folder\\Book3.csv")
                
                f1=Label(screen1, text="Filter", fg="#57a1f8", bg="#fff", font=('calibri(body)', 15))
                f1.place(x=530, y=25)
                filt1=StringVar()
                filt2=ttk.Combobox(screen1, width=27, textvariable=filt1, values=['Ex-Showroom_Price','Fuel_Tank_Capacity','Highway_Mileage','Gears','Seating_Capacity'] )
                filt2.place(x=600,y=30)
                filt2.current(4)
                
                l3=Label(screen1, text="Manufacturer", fg="#57a1f8", bg="#fff", font=('calibri(body)', 15))
                l3.place(x=130, y=95)
                ma1=StringVar()
                manu=data1['Make'].tolist()
                manu1=set(manu)
                manu2=sorted(tuple(manu1))
                manufacturer1=ttk.Combobox(screen1, width=27, textvariable = ma1, values=manu2)
                manufacturer1.place(x=100,y=140)
                mak1=ma1.get()
                
                ma2=StringVar()
                manufacturer2=ttk.Combobox(screen1, width=27, textvariable = ma2, values=manu2)
                manufacturer2.place(x=100,y=190)
                mak2=ma2.get()
                
                ma3=StringVar()
                manufacturer3=ttk.Combobox(screen1, width=27, textvariable = ma3, values=manu2)
                manufacturer3.place(x=100,y=240)
                mak3=ma3.get()
                
                ma4=StringVar()
                manufacturer4=ttk.Combobox(screen1, width=27, textvariable = ma4, values=manu2)
                manufacturer4.place(x=100,y=290)
                mak4=ma4.get()
                
                ma5=StringVar()
                manufacturer5=ttk.Combobox(screen1, width=27, textvariable = ma5, values=manu2)
                manufacturer5.place(x=100,y=340)
                mak5=ma5.get()
                
                
                
                
                
                
                
                l4=Label(screen1, text="Model", fg="#57a1f8", bg="#fff", font=('calibri(body)', 15))
                l4.place(x=420, y=95)
                
                
                mo1=StringVar()
                model4=ttk.Combobox(screen1, width=27, textvariable = mo1, values=["select"])
                model4.place(x=360,y=140)
                ma1.trace('w', SelectModel1)
                
                
                mo2=StringVar()
                model5=ttk.Combobox(screen1, width=27, textvariable = mo2, values=["select"])
                model5.place(x=360,y=190)
                ma2.trace('w', SelectModel2)
                
                
                mo3=StringVar()
                model6=ttk.Combobox(screen1, width=27, textvariable = mo3, values=["select"])
                model6.place(x=360,y=240)
                ma3.trace('w', SelectModel3)
                
                
                mo4=StringVar()
                model7=ttk.Combobox(screen1, width=27, textvariable = mo4, values=["select"])
                model7.place(x=360,y=290)
                ma4.trace('w', SelectModel4)
                
                
                mo5=StringVar()
                model8=ttk.Combobox(screen1, width=27, textvariable = mo5, values=["select"])
                model8.place(x=360,y=340)
                ma5.trace('w', SelectModel5)
                
                
                
                l5=Label(screen1, text="Variant", fg="#57a1f8", bg="#fff", font=('calibri(body)', 15))
                l5.place(x=680, y=95)
                
                va1=StringVar()
                var4=ttk.Combobox(screen1, width=27, textvariable=va1, values=["select"] )
                var4.place(x=620,y=140)
                mo1.trace('w',SelectVariant1)
                
                va2=StringVar()
                var5=ttk.Combobox(screen1, width=27, textvariable=va2, values=["select"] )
                var5.place(x=620,y=190)
                mo2.trace('w',SelectVariant2)
                
                va3=StringVar()
                var6=ttk.Combobox(screen1, width=27, textvariable=va3, values=["select"] )
                var6.place(x=620,y=240)
                mo3.trace('w',SelectVariant3)
                
                va4=StringVar()
                var7=ttk.Combobox(screen1, width=27, textvariable=va4, values=["select"] )
                var7.place(x=620,y=290)
                mo4.trace('w',SelectVariant4)
                
                va5=StringVar()
                var8=ttk.Combobox(screen1, width=27, textvariable=va5, values=["select"] )
                var8.place(x=620,y=340)
                mo5.trace('w',SelectVariant5)
                
                
                Button(screen1,width=39,pady=7,text='next', bg='#57a1f8',fg='white',border=0, command=plotGraph).place(x=600,y=400)
                screen1.mainloop()
                
        else:
                messagebox.showerror("enter something", "enter something")
def signin():
	username=user.get()
	password=code.get()
	if username=='admin' and password=='1234':
            screen=Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+200+100')
            screen.config(bg="white")
            screen.resizable(False,False)
            l1=Label(screen, text="Select Your Option", fg="black", bg="#fff", font=('calibri(body)',23))
            l1.place(x=450, y=100)
            img=PhotoImage(file="screen.png")
            Label(screen, image=img, bg='white').place(x=50, y=75)
            c1=IntVar()
            c2=IntVar()
            chk1=Checkbutton(screen, text="Units Sales Analysis", variable=c1,fg="#57a1f8", bg="#fff" , font=('calibri(body)',15),onvalue=1, offvalue=0)
            chk2=Checkbutton(screen, text="Compare Features", variable=c2,fg="#57a1f8", bg="#fff", font=('calibri(body)',15),onvalue=1, offvalue=0)
            chk1.place(x=550, y=150)
            chk2.place(x=550, y=200)
            Button(screen,width=35,pady=7,text='Next', bg='#57a1f8',fg='white',border=0,command=lambda: sales(c1, c2)).place(x=600,y=280)
            screen.mainloop()
            
            
            
            
        
	else:
            messagebox.showerror("Invalid","invalid username and password")
		

img=PhotoImage(file="login.png")
Label(root, image=img, bg='white').place(x=50, y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('microsoft YaHei UI Light',23,'bold'))
heading.place(x=100, y=5)

def on_enter(e):
	user.delete(0,'end')
def on_leave(e):
	name=user.get()
	if name=='':
		user.insert(0,'Username')

user=Entry(frame, width=25, fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
def on_enter(e):
	code.delete(0,'end')
def on_leave(e):
	name=code.get()
	if name=='':
		code.insert(0,'Password')

code=Entry(frame, width=25, fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
code.place(x=30, y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Sign in', bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)

label=Label(frame, text="Don't have an account?", fg='black', bg='white',font=('microsoft Yahei UI Light',11))
label.place(x=75,y=270)
sign_up=Button(frame, width=7, text='Sign up', border=0, bg='white',font=('microsoft Yahei UI Light',11), cursor='hand2', fg='#57a1f8')
sign_up.place(x=240, y=267)
root.mainloop()