# --------Libraries--------
from tkinter import Label,LabelFrame,Button,Entry,Spinbox,Tk,Toplevel
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo,showerror
from time import sleep,strftime
from random import choice,randint,randrange
from os import system
from platform import system as sys
# --------Terminal Cleaning--------
def terminal_cleaner():
    os_name = sys()
    if os_name == "Windows":
        system("cls")
    elif os_name == "Linux" or os_name == "Darwin":
        system("clear")
# --------Creating The Main Page--------
def second_page(btn):
    counter = 0
    if btn == "show":
        counter += 1
        if counter < 2:
            global name_entry,arrival_d_entry,return_d_entry,start_p_cb,destination_cb,nop_sb
            cities_list = ["Tehran","Berlin","Kandahar","Rasht","Toronto","Venice","Madrid","Canary Island","Tokyo","Rome","Kyoto","Los Angeles","New York"]

            second_page = Toplevel()
            second_page.title("Buying Ticket")
            second_page.config(bg="#2c4cd2")
            
            first_label_frame = LabelFrame(second_page, text="Flights Inc.", font=("JetBrains Mono",7), bg="#2c4cd2")
            name_label = Label(first_label_frame,text="Name:",font=("Consolas",18),bg="#2c4cd2",fg="white")
            arrival_d_label = Label(first_label_frame,text="Arrival Date:",font=("Consolas",18),bg="#2c4cd2",fg="white")
            return_d_label = Label(first_label_frame,text="Return Date:",font=("Consolas",18),bg="#2c4cd2",fg="white")
            start_p_label = Label(first_label_frame,text="Start Place:",font=("Consolas",18),bg="#2c4cd2",fg="white")
            destination_label = Label(first_label_frame,text="Destination:",font=("Consolas",18),bg="#2c4cd2",fg="white")
            nop_label = Label(first_label_frame,text="Number Of People:",font=("Consolas",18),bg="#2c4cd2",fg="white")

            second_label_frame = LabelFrame(second_page, text="Flight Info", font=("JetBrains Mono",7), bg="darkred")
            name_entry = Entry(second_label_frame,font=("Consolas",16))
            arrival_d_entry = Entry(second_label_frame,font=("Consolas",16))
            return_d_entry = Entry(second_label_frame,font=("Consolas",16))
            start_p_cb = Combobox(second_label_frame,values=cities_list,font=("JetBrains Mono",16),state="readonly")
            destination_cb = Combobox(second_label_frame,values=cities_list,font=("JetBrains Mono",16),state="readonly")
            nop_sb = Spinbox(second_label_frame,from_=0,to=4,wrap=True,font=("JetBrains Mono",18),state="readonly")

            third_label_frame = LabelFrame(second_page, text="Saving", font=("JetBrains Mono",7), bg="darkred")
            save_button = Button(third_label_frame,text="Save",font=("JetBrains Mono",16),command=lambda:save_info())
            exit_button = Button(third_label_frame,text="Exit",font=("JetBrains Mono",16),command=lambda:second_page.destroy())

            first_label_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20)
            second_label_frame.grid(column=1, row=0, sticky="nsew", padx=20, pady=20)
            third_label_frame.grid(column=0, row=1, sticky="nsew", padx=20, pady=20, columnspan=2)
            third_label_frame.columnconfigure(0,weight=2)
            third_label_frame.columnconfigure(1,weight=2)

            name_label.grid(column=0 ,row=0 ,sticky="nsew", padx=10, pady=10)
            arrival_d_label.grid(column=0 ,row=1 ,sticky="nsew", padx=10, pady=10)
            return_d_label.grid(column=0 ,row=2 ,sticky="nsew", padx=10, pady=10)
            start_p_label.grid(column=0 ,row=3 ,sticky="nsew", padx=10, pady=10)
            destination_label.grid(column=0 ,row=4 ,sticky="nsew", padx=10, pady=10)
            nop_label.grid(column=0 ,row=5 ,sticky="nsew", padx=10, pady=10)
            
            name_entry.grid(column=0 ,row=0 ,sticky="nsew", padx=10, pady=10)
            arrival_d_entry.grid(column=0 ,row=1 ,sticky="nsew", padx=10, pady=10)
            return_d_entry.grid(column=0 ,row=2 ,sticky="nsew", padx=10, pady=10)
            start_p_cb.grid(column=0 ,row=3 ,sticky="nsew", padx=10, pady=10)
            destination_cb.grid(column=0 ,row=4 ,sticky="nsew", padx=10, pady=10)
            nop_sb.grid(column=0 ,row=5 ,sticky="nsew", padx=10, pady=10)

            save_button.grid(column=0 ,row=0 ,sticky="nsew")
            exit_button.grid(column=1 ,row=0 ,sticky="nsew")
            
            second_page.mainloop()
        else:
            showerror(title="There is already a opened window!")

def save_info():
    global name,arrival_d,return_d,start_p,destination,nop

    time = strftime("%H:%M")
    name = name_entry.get()
    arrival_d = arrival_d_entry.get()
    return_d = return_d_entry.get()
    start_p = start_p_cb.get()
    destination = destination_cb.get()
    nop = nop_sb.get()

    profile_file = open("PassengerInfo.txt","a")
    profile_file.write(f"Time:{time}\n")
    profile_file.write(f"""Name:{name}
Arrival Date:{arrival_d}
Return Date:{return_d}
Start Place:{start_p}
Destination:{destination}
Number Of People:{nop}""")
    profile_file.write(30*".__.")
    profile_file.close()

def save_initial_info():
    ...

second_page("show")
main_page = Tk()
main_page.title("First Page")

username_label = Label()
username_entry = Entry()
password_label = Label()
password_entry = Entry()

main_page.mainloop()
