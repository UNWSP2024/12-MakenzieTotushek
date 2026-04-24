# Author: Makenzie Totushek
# Date: 4/24/2026
# Title: Joe's Automotive Services
import tkinter as tk
import tkinter.messagebox

class ServiceGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Automotive Services")

        #create the main frames
        self.intro_frame = tk.Frame(self.main_window)
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #create intro label
        self.intro_label = tk.Label(self.intro_frame, text='Please select your desired services below')
        self.intro_label.pack()
        #create check buttons
        self.cb_var1 = tk.IntVar()
        self.cb_var2 = tk.IntVar()
        self.cb_var3 = tk.IntVar()
        self.cb_var4 = tk.IntVar()
        self.cb_var5 = tk.IntVar()
        self.cb_var6 = tk.IntVar()
        self.cb_var7 = tk.IntVar()


        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        self.cb1 = tk.Checkbutton(self.top_frame, text="Oil Change - $30", variable=self.cb_var1, onvalue=30, offvalue=0)
        self.cb2 = tk.Checkbutton(self.top_frame, text="Lube Job - $20", variable=self.cb_var2, onvalue=20, offvalue=0)
        self.cb3 = tk.Checkbutton(self.top_frame, text="Radiator Flush - $40", variable=self.cb_var3, onvalue=40, offvalue=0)
        self.cb4 = tk.Checkbutton(self.top_frame, text="Transmission Fluid - $100", variable=self.cb_var4, onvalue=100, offvalue=0)
        self.cb5 = tk.Checkbutton(self.top_frame, text="Inspection - $35", variable=self.cb_var5, onvalue=35, offvalue=0)
        self.cb6 = tk.Checkbutton(self.top_frame, text="Muffler Replacement - $200", variable=self.cb_var6, onvalue=200, offvalue=0)
        self.cb7 = tk.Checkbutton(self.top_frame, text="Tire Rotation - $20", variable=self.cb_var7, onvalue=20, offvalue=0)

        #pack check buttons
        self.cb1.pack(anchor='w')
        self.cb2.pack(anchor='w')
        self.cb3.pack(anchor='w')
        self.cb4.pack(anchor='w')
        self.cb5.pack(anchor='w')
        self.cb6.pack(anchor='w')
        self.cb7.pack(anchor='w')

        #create bottom frame buttons
        self.ok_button = tk.Button(self.bottom_frame, text='Ok', command=self.show_price)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        #pack main frames
        self.intro_frame.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def show_price(self):
        total_price = (
            self.cb_var1.get() +
            self.cb_var2.get() +
            self.cb_var3.get() +
            self.cb_var4.get() +
            self.cb_var5.get() +
            self.cb_var6.get() +
            self.cb_var7.get())

        tk.messagebox.showinfo(message="Your total price is $" + str(total_price))

if __name__ == "__main__":
    service = ServiceGUI()