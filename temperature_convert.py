from tkinter import*

# Celcius to Kelvin convert calculation
def convert_kelvin():
    temp = temp_input.get()
    if temp == '':
       result_label.config(text="Please insert the value")
    else:
        kelvin = int(temp) + 273.15
        result_label.config(text=f"{kelvin} K")

# Configurating the window
window = Tk()
window.title('Temperature Converter')
window.geometry('300x200')

# Configurating the label
judul = Label(window,text="Temperature Converter")
judul.pack()

label2 = Label(window,text="Celcius to Kelvin")
label2.pack()

label3 = Label(window, text="Input the here")
label3.pack()

# Configurating entry box
temp_input = Entry(window)
temp_input.pack(pady=10)

# Configurating button
button = Button(window, text="Convert", command=convert_kelvin)
button.pack()

# Convert Result label
result_label = Label(window, text="")
result_label.pack(pady=10)

# Creator label
creator = Label(window, text = "Created by Ramadhany")
creator.pack(pady=10)

window.mainloop()