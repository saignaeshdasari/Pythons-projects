from tkinter import *
import speedtest 

def speedcheck():
    spd = speedtest.Speedtest()
    spd.get_servers()
    down = str(round(spd.download() / (10**6), 2)) + " Mbps"
    up = str(round(spd.upload() / (10**6), 2)) + " Mbps"
    lab_down_val.config(text=down)
    lab_up_val.config(text=up)

# main window
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="black")

# title label
lab_title = Label(sp, text="Internet Speed Test", font=("Times New Roman", 25, "bold"), fg="white", bg="black")
lab_title.place(x=50, y=30, height=50, width=400)

# download label
lab_down_text = Label(sp, text="Download Speed", font=("Times New Roman", 20, "bold"), fg="cyan", bg="black")
lab_down_text.place(x=100, y=120, height=40, width=300)

lab_down_val = Label(sp, text="00 Mbps", font=("Times New Roman", 20, "bold"), fg="white", bg="black")
lab_down_val.place(x=100, y=170, height=40, width=300)

# upload label
lab_up_text = Label(sp, text="Upload Speed", font=("Times New Roman", 20, "bold"), fg="cyan", bg="black")
lab_up_text.place(x=100, y=250, height=40, width=300)

lab_up_val = Label(sp, text="00 Mbps", font=("Times New Roman", 20, "bold"), fg="white", bg="black")
lab_up_val.place(x=100, y=300, height=40, width=300)

# button
button = Button(sp, text="Check Speed", font=("Times New Roman", 20, "bold"), bg="blue", fg="white", relief=RAISED, command=speedcheck)
button.place(x=100, y=400, height=50, width=300)

sp.mainloop()
