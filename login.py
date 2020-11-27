from tkinter import *
from tkinter import simpledialog ,messagebox
from datetime import datetime
#create main window and style it. Add a title, sizing etc
window=Tk()
window.title("Lottery Entry")
window.configure(background="#dedede", relief="solid")
window.geometry("650x650")


today= datetime.today().strftime('%Y-%m-%d')


def qualify():
    try:
        age = int(entry1.get())

        if age < 18:
            raise ValueError

    except ValueError as e:
         messagebox.showwarning("Verification Unsuccessful","Note: Only persons over the age of 18 may enter the National Lottery.\n \nEnsure that you have keyd in a number.")


    else:

        if age >= 18:
            messagebox.showinfo("Verified.", "You qualify to take part in the National Lottery.")

        file=open('/home/user/Desktop/lotto.txt','w')
        file.write(
        "Player:" + str(entryname.get())+" "+str(entrysurname.get()+"\n"+
        "Age:" + str(entry1.get())+"\n"+
        "Email:" + str(entry_email.get())+"\n"+
        "Date Played:"+str(today)))
        file.close()

        window.withdraw()
        import Qualify_lotto





def exit():
    sure = messagebox.askyesno(title="Alert",message="Are you sure you want to exit this app?")
    if sure==True:
        window.destroy()
    else:
        return  None




labelHeading = Label(window,text="National Lottery | Home", font="arial 18 bold", bg="yellow")
labelHeading.pack()

label1=Label(window, text="To qualify, please enter your details in the space below.", font="arial 14 bold")
label1.pack(pady=10)

label2=Label(window, text="Please note, no persons under the age of 18 may enter.", font="arial 10 italic")
label2.pack(pady=10)

label3=Label(window, text="Name:", font="arial 14")
label3.pack()

entryname= Entry(window)
entryname.pack()

label3=Label(window, text="Surname:", font="arial 14")
label3.pack(pady=10)

entrysurname= Entry(window)
entrysurname.pack()

label4=Label(window, text="Age:", font="arial 14")
label4.pack(pady=10)

entry1= Entry(window)
entry1.pack()

label4=Label(window, text="Email Address:", font="arial 14")
label4.pack(pady=10)

entry_email= Entry(window,width=30)
entry_email.pack()

btn1= Button(window, text="Verify",command=qualify)
btn1.pack(pady=20)


btn2= Button(window, text="Exit",command=exit)
btn2.pack(pady=30)

window.mainloop()

