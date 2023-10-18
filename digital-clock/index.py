from tkinter import *
import time

class relogio:
    def __init__(self, dude):
        self.dude = dude
    def get_time(self):
        global var
        timer= time.localtime()
        hora= timer.tm_hour
        min= timer.tm_min
        sec= timer.tm_sec
        model= f'{hora:02}:{min:02}:{sec:02}'
        var.set(model)
        label_main.after(1000, self.get_time)
    def get_date(self):
        timerd= time.localtime()
        dia= timerd.tm_mday
        mes= timerd.tm_mon
        ano=timerd.tm_year
        molde= f'{dia:02}/{mes:02}/{ano:02}'
        var_date.set(molde)
        label_text.after(10000, self.get_time)



root= Tk()
root.title('Relógio virtual')

largura = root.winfo_screenwidth()
altura = root.winfo_screenheight()
root.minsize(largura,altura)
root.config(bg='black')
var= StringVar()
var.set('00:00')

var_date= StringVar()
var_date.set('momfaommfadmomfamdoao')
label_text= Label(textvariable=var_date, bg='black', fg='purple', font='SansSerif 20 bold')
label_text.place(relx=0.5, rely=0.3, anchor='center')


label_main= Label(textvariable=var, fg='purple', font='SansSerif 80 bold', bg='black')
label_main.place(relx=0.5, rely=0.5, anchor='center')
img= PhotoImage(file=r'assets\photodump.png')
label_img= Label(image=img, bg='black' )
label_img.place(relx=0.5, rely=0.2, anchor="center")

clock= relogio('')
clock.get_time()
clock.get_date()



root.mainloop()
