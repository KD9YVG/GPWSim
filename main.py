from tkinter import Tk, Scale, Checkbutton, IntVar, Spinbox, HORIZONTAL

class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("My Python GUI App")
        master.geometry("600x400")  # Make the window larger

        # Shared variable for the slider and the number picker
        self.value_var = IntVar(value=0)

        # Slider that goes from 0 to 3000
        self.slider = Scale(
            master, from_=0, to=3000, orient=HORIZONTAL,
            label="Slider", variable=self.value_var, length=400
        )
        self.slider.pack(pady=10)

        # Number picker using a Spinbox with slightly smaller text
        self.number_picker = Spinbox(
            master, from_=0, to=3000, textvariable=self.value_var, font=("Arial", 12)
        )
        self.number_picker.pack(pady=10)

        self.crc_var = IntVar()
        self.gear_var = IntVar()
        self.flaps_var = IntVar()

        self.crc_checkbox = Checkbutton(master, text="CRC", variable=self.crc_var, fg="red")
        self.crc_checkbox.pack()

        self.gear_checkbox = Checkbutton(master, text="Gear", variable=self.gear_var)
        self.gear_checkbox.pack()

        self.flaps_checkbox = Checkbutton(master, text="Flaps", variable=self.flaps_var)
        self.flaps_checkbox.pack()

if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()