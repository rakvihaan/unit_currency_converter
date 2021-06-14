import tkinter as tk
from tkinter import font
from tkinter import ttk
import unit_conv as uc
import temp_conv as tc
import currency_conv as cc


#unit_converter
# units=uc.send()
sub_units=uc.get_units('dbl')
# print(sub_units)
unit_db=['Length','Area','Volume','Mass','Energy','Pressure']
dbm='dbl'

def get_units(event):
    global dbm
    db=db_options.get()
    # print(db)
    # dbm='dbl'
    if db == 'Length':
        dbm = 'dbl'
        # sub_units=uc.get_units(dbm)
    elif db =='Area':
        dbm = 'dba'
        # sub_units=uc.get_units(dbm)
    elif db == 'Mass':
        dbm = 'dbm'
        # sub_units=uc.get_units(dbm)
    elif db == 'Volume':
        dbm = 'dbv'
        # sub_units=uc.get_units(dbm)
    elif db == 'Energy':
        dbm = 'dbe'
    elif db == 'Pressure':
        dbm = 'dbp'
    sub_units=uc.get_units(dbm)
    unit_options_from['values'] = sub_units
    unit_options_to['values'] = sub_units
    # print(sub_units)


def calc(fval):
    # global converted_unit
    from_unit=unit_options_from.get()
    to_unit=unit_options_to.get()
    converted_unit=uc.conv_unit(from_unit,to_unit,float(fval),dbm)
    unit_entry2['text'] = converted_unit

#currency_converter
currencies=cc.send()
# print(currencies)

def convert_currency(fval):
    # global converted_val
    from_curr=options_from.get()
    to_curr=options_to.get()
    converted_val=cc.conv_curr(from_curr,to_curr,float(fval))
    curr_entry2['text'] = converted_val



#temperature converter
temperature=['Celsius','Fahrenheit','Kelvin']

def convert_temp(fval):
    # global converted_temp
    from_temp=temp_options_from.get()
    to_temp = temp_options_to.get()
    # to_temp=temp_options_to.get()
    converted_val=tc.call_convert(from_temp,to_temp,float(fval))
    temp_entry2['text'] = converted_val


    

root = tk.Tk()
root.resizable(False, False)

root.title('Unit and Currency Converter')
WIDTH = 700
HEIGHT = 400



bg_clr = '#0f083b'
body_clr = '#eeb462'
box_clr = '#534666'
# body_clr = '#ffa64d'
# box_clr = '#262626'
# body_clr = '#355c7d'
# box_clr = '#f6956f'
text_clr = 'white'
# body_clr = '#99ccff'
# box_clr = '#004d66'
text_clr = '#002633'

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, highlightthickness=0) 
canvas.pack(fill="both")

# bk_clr = "#d2ffd2"
bk_clr = "white"

style = ttk.Style()
style.theme_create( "Florina", parent="default", settings={
    "TLabel": {"configure": {"background": bk_clr }},
    "TFrame": {"configure": {"background": bk_clr }},
    "TNotebook": {
        "configure": {"background": bg_clr, "tabmargins": [5, 10, 2, 0] }},
    "TNotebook.Tab": {
        "configure": {"background": bk_clr, "padding": [4, 2], "font" : ('Ubuntu Bold',10),"foreground":text_clr  },
        "map":       {"background": [("selected", body_clr)],
                      "expand": [("selected", [1, 1, 1, 0])]
                      } } } )


nb=ttk.Notebook(canvas)
nb.pack(pady=1,fill="both")
style.theme_use("Florina")


unit_tab=tk.Frame(nb,height=400, width=700)
unit_tab.pack(fill="both", expand=True)

currency_tab=tk.Frame(nb,height=400, width=700)
currency_tab.pack(fill="both",expand=True)

temp_tab=tk.Frame(nb,height=400, width=700)
temp_tab.pack(fill="both",expand=True)

team_tab=tk.Frame(nb,height=400, width=700)
team_tab.pack(fill="both",expand=True)

nb.add(unit_tab, text="Unit Converter")
nb.add(currency_tab, text="Currency Converter")
nb.add(temp_tab, text="Temperature Converter")
nb.add(team_tab, text="Team info")

unit_can = tk.Canvas(unit_tab, bg=body_clr, height=HEIGHT, width=WIDTH, highlightthickness=0)
unit_can.pack(fill="both", expand=True)

currency_can = tk.Canvas(currency_tab, bg=body_clr, height=HEIGHT, width=WIDTH, highlightthickness=0)
currency_can.pack(fill="both", expand=True)

temp_can = tk.Canvas(temp_tab, bg=body_clr, height=HEIGHT, width=WIDTH, highlightthickness=0)
temp_can.pack(fill="both", expand=True)

team_can = tk.Canvas(team_tab, bg=body_clr, height=HEIGHT, width=WIDTH, highlightthickness=0)
team_can.pack(fill="both", expand=True)

title_x = int(WIDTH//2)+5
title_y = int(HEIGHT*0.044)+5

#unit
unit_can.create_text(title_x,title_y, text="Unit Converter", font=('Ubuntu Bold', 20,'underline'), fill=text_clr,justify="center")


db_frame = tk.Frame(unit_can, bg=box_clr, bd=6)
db_frame.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.09, anchor='n')

db_options=ttk.Combobox(db_frame, value=unit_db)
db_options.current(0)
db_options.bind("<<ComboboxSelected>>", get_units)
db_options.place(relx=0.5,relheight=1,relwidth=1,anchor='n')

frame = tk.Frame(unit_can, bg=box_clr, bd=5)
frame.place(relx=0.5, rely=0.35, relwidth=0.6, relheight=0.09, anchor='n')

unit_entry = tk.Entry(frame, font=('Ubuntu', '11'), bd=2)
unit_entry.place(rely=0, relwidth=0.62, relheight=1)

frame2 = tk.Frame(unit_can, bg=box_clr, bd=6)
frame2.place(relx=0.5, rely=0.52, relwidth=0.6, relheight=0.09, anchor='n')

unit_entry2 = tk.Label(frame2, font=('Ubuntu', '11'), bd=2,anchor="w")
unit_entry2.place(relwidth=0.62, relheight=1)

button_frame = tk.Frame(unit_can)
button_frame.place(relx=0.4,rely=0.7, height=40, width=160)

button = tk.Button(button_frame, text="Convert",font=('Ubuntu', 14),command=lambda: calc(unit_entry.get()),anchor="center")
button.place(relheight=1, relwidth=1)

sub_units=uc.get_units('dbl')

unit_options_from=ttk.Combobox(frame, value=sub_units)
unit_options_from.current(0)
unit_options_from.place(relx=0.65, relheight=1, relwidth=0.35)

unit_options_to=ttk.Combobox(frame2, value=sub_units)
unit_options_to.current(1)
unit_options_to.place(relx=0.65, relheight=1,relwidth=0.35)


#currency
currency_can.create_text(title_x,title_y, text="Currency Converter", font=('Ubuntu Bold', 20,'underline'), fill='black',justify="center")

framec = tk.Frame(currency_can, bg=box_clr, bd=6)
framec.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.09, anchor='n')

curr_entry = tk.Entry(framec, font=('Ubuntu', '11'), bd=2)
curr_entry.place(rely=0, relwidth=0.62, relheight=1)

frame2 = tk.Frame(currency_can, bg=box_clr, bd=6)
frame2.place(relx=0.5, rely=0.4, relwidth=0.6, relheight=0.09, anchor='n')

curr_entry2 = tk.Label(frame2, font=('Ubuntu', '11'), bd=2,anchor="w")
curr_entry2.place(relwidth=0.62, relheight=1)

button_frame = tk.Frame(currency_can)
button_frame.place(relx=0.4,rely=0.6, height=40, width=160)

button = tk.Button(button_frame, text="Convert",font=('Ubuntu', 14),command=lambda: convert_currency(curr_entry.get()),anchor="center")
button.place(relheight=1, relwidth=1)

options_from=ttk.Combobox(framec, value=currencies)
options_from.current(11)
# options_from.bind("<<ComboboxSelected>>", convert_currency)
options_from.place(relx=0.65, relheight=1,relwidth=0.35)

options_to=ttk.Combobox(frame2, value=currencies)
options_to.current(0)
# options_to.bind("<<ComboboxSelected>>", convert_currency)
options_to.place(relx=0.65, relheight=1,relwidth=0.35)

#temp
temp_can.create_text(title_x,title_y, text="Temperature Converter", font=('Ubuntu Bold', 20,'underline'), fill='black',justify="center")

framet = tk.Frame(temp_can, bg=box_clr, bd=6)
framet.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.09, anchor='n')

entry = tk.Entry(framet, font=('Ubuntu', '11'), bd=2)
entry.place(rely=0, relwidth=0.62, relheight=1)

frame2 = tk.Frame(temp_can, bg=box_clr, bd=6)
frame2.place(relx=0.5, rely=0.4, relwidth=0.6, relheight=0.09, anchor='n')

temp_entry2 = tk.Label(frame2, font=('Ubuntu', '11'), bd=2,anchor="w")
temp_entry2.place(relwidth=0.62, relheight=1)

button_frame = tk.Frame(temp_can)
button_frame.place(relx=0.4,rely=0.6, height=40, width=160)

button = tk.Button(button_frame, text="Convert",font=('Ubuntu', 14),command=lambda: convert_temp(entry.get()),anchor="center")
button.place(relheight=1, relwidth=1)

temp_options_from=ttk.Combobox(framet, value=temperature)
temp_options_from.current(0)
# options_from.bind("<<ComboboxSelected>>", convert_currency)
temp_options_from.place(relx=0.65, relheight=1,relwidth=0.35)

temp_options_to=ttk.Combobox(frame2, value=temperature)
temp_options_to.current(1)
# options_to.bind("<<ComboboxSelected>>", convert_currency)
temp_options_to.place(relx=0.65, relheight=1,relwidth=0.35)


#team info
title_x=title_x-80
team_can.create_text(title_x,title_y+30, text="Group 6 PCPS FSA Project", font=('Ubuntu Bold', 16,), fill='black',justify="center")
team_can.create_text(title_x-60,title_y+65, text="Team Members:", font=('Ubuntu', 14), fill='black',justify="left")

team_can.create_text(title_x+75,title_y+100, text="1. RAKSHITHVIHAAN BADIGER - PES1UG20ME080", font=('Ubuntu', 13), fill='black',justify="left")
team_can.create_text(title_x+75,title_y+125, text="2. REVANTH S KALAGUDI - PES1UG20EE116 ", font=('Ubuntu', 13), fill='black',justify="left")
team_can.create_text(title_x+75,title_y+150,text="3. RISHITH H - PES1UG20ME082", font=('Ubuntu', 13), fill='black',justify="left")


root.mainloop()