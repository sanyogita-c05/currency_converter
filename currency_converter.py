
import tkinter as tk
from tkinter import OptionMenu

m = tk.Tk()
m.title("Exchange Master")
m.minsize(500, 600)
m.maxsize(600, 800)
m['bg'] = "powderblue"

# Define the font style for the heading
font_style_heading = ('Algerian', 16, 'bold')

heading = tk.Label(m, text="CURRENCY CONVERTER", height=1, padx=140, pady=16,anchor="center", font=font_style_heading, bg="mediumpurple")
heading.place(x=0, y=0)

Font_tuple = ("Comic Sans MS", 15, "bold")   
l1 = tk.Label(text="FROM:", anchor="w", width=11, bg="turquoise", fg="white")
l1.configure(font=Font_tuple)
l1.place(x=100, y=80)
l2 = tk.Label(text="TO:", anchor="w", width=11, bg="skyblue", fg="white")
l2.configure(font=Font_tuple)
l2.place(x=250, y=80)

conversion_table = {
    "Rupees": {
        "Rupees": 1,
        "Yuan": 0.085,
        "Dollar": 0.012,
        "Euro": 0.011,
        "JPY": 1.84
    },
    "Yuan": {
        "Rupees": 11.75,
        "Yuan": 1,
        "Dollar": 0.14,
        "Euro": 0.13,
        "JPY":21.57
    },
    "Dollar": {
        "Rupees": 83.30,
        "Yuan": 7.23,
        "Dollar": 1,
        "Euro": 0.92,
        "JPY": 153.09
    },
    "Euro": {
        "Rupees": 90.37,
        "Yuan": 7.85,
        "Dollar": 1.08,
        "Euro": 1,
        "JPY":164.31
    },
    "JPY": {
       "Rupees": 0.54,
       "Yuan": 0.047,
       "Dollar": 0.0065,
       "Euro": 0.0061,
       "JPY": 1
    }
}

conversion_rate_euro_to_rupees = 90.91

def convert_currency():
    amount = float(E1.get())
    from_currency = drop1_var.get()
    to_currency = drop2_var.get()
    # Conversion logic
    if from_currency == "Euro" and to_currency == "Rupees":
        converted_amount = amount * conversion_rate_euro_to_rupees
    elif from_currency == "Rupees" and to_currency == "Euro":
        converted_amount = amount / conversion_rate_euro_to_rupees
    else:
        conversion_rate = conversion_table[from_currency][to_currency]
        converted_amount = amount * conversion_rate

    E2.delete(0, tk.END)
    E2.insert(0, str(converted_amount))

def clear():
    E1.delete(0, tk.END)
    E2.delete(0, tk.END)

def exit_program():
    m.destroy()

E1 = tk.Entry(m, font=("Arial", 10))
E1.place(x=80, y=220)

E2 = tk.Entry(m, font=("Arial", 10))
E2.place(x=250, y=220)

font_style=('CityBlueprint', 16, 'bold')
drop1_var = tk.StringVar()
drop1_var.set("Currency")
drop1 = OptionMenu(m, drop1_var, "Euro", "Dollar", "Rupees", "Yuan","JPY")
drop1.place(x=100, y=130)
drop1.config(font=font_style,width=5,bg="plum")

drop2_var = tk.StringVar()
drop2_var.set("Currency")
drop2 = OptionMenu(m, drop2_var, "Euro", "Dollar", "Rupees", "Yuan","JPY")
drop2.place(x=250, y=130)
drop2.config(font=font_style,width=5,bg="plum")

button = tk.Button(m, text="Convert", command=convert_currency,width=12,bg="sandybrown", font=("Arial", 12))
button.place(x=180, y=180)

clear_button = tk.Button(m, text='Clear', command=clear,bg="pink",width=12, font=("Arial", 12))
clear_button.place(x=180, y=250)

exit_button = tk.Button(m, text='Exit', command=exit_program,bg="rosybrown",width=12,font=("Arial", 12))
exit_button.place(x=180, y=300)

m.mainloop()
