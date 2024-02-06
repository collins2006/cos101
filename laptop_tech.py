import tkinter as tk
from tkinter import messagebox


def submit():
    name = name_entry.get()
    phone = phone_entry.get()
    make = make_var.get()
    model = model_var.get()

    if make == "mac":
        if model == "macbook air":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected macbook air, the cost is $500")
        elif model == "macbook pro":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected macbook pro, the cost is $700")
        elif model == "macbook air m1":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected macbook air, the cost is $6500")
    elif make == "HP":
        if model == "envy":
            messagebox.showinfo("Laptop Sales Tech", "Mr/Mrs " + name + ", you have selected Envy, the cost is $500")
        elif model == "elitebook":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected HP Elitebook, the cost is $800")
        elif model == "pavilion":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected pavilion, the cost is $800")
    elif make == "Dell":
        if model == "xps17":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected Dell xps17, the cost is $500")
        elif model == "inspion":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected Dell inspion, the cost is $6600")
        elif model == "latitude":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected Dell latitude, the cost is $800")


root = tk.Tk()
root.title("Laptop Sales Tech")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

make_label = tk.Label(root, text="Brand:")
make_label.grid(row=2, column=0)
make_var = tk.StringVar()
make_option = tk.OptionMenu(root, make_var, "MAC", "HP", "DELL")
make_option.grid(row=2, column=1)

model_label = tk.Label(root, text="Model:")
model_label.grid(row=3, column=0)
model_var = tk.StringVar()
model_option = tk.OptionMenu(root, model_var, "MACBOOK AIR", "MACBOOK PRO", "MACBOOK AIR M1", "ENVY", "ELITEBOOK",
                             "PAVILION", "XPS17", "INSPION", "LATITUDE")
model_option.grid(row=3, column=1)

submit_button = tk.Button(root, text="SUBMIT", command=submit)
submit_button.grid(row=4, column=1)

root.mainloop()