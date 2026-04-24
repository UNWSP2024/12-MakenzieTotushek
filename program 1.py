# Author: Makenzie Totushek
# Date: 4/24/2026
# Title: MPG Calculator
import tkinter as tk
class MPGCalculatorGUI:
    def __init__(self):
        #Main window
        self.main_window = tk.Tk()
        self.main_window.title("MPG Calculator")

        #create three frames
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame1 = tk.Frame(self.main_window)
        self.mid_frame2 = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #top frame
        self.prompt_label = tk.Label(self.top_frame, text='How many gallons of gas can your car hold? ')
        self.gallon_entry = tk.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.gallon_entry.pack(side='left')

        #Mid frame 1
        self.prompt_label = tk.Label(self.mid_frame1, text='How many miles can you drive on a full tank of gas? ')
        self.miles_entry = tk.Entry(self.mid_frame1, width=10)
        self.prompt_label.pack(side='left')
        self.miles_entry.pack(side='left')

        #Mid frame 2
        self.descr_label = tk.Label(self.mid_frame2, text=f'Your miles per gallon: ')
        self.descr_label.pack(side='left')
        self.value = tk.StringVar()
        self.mpg_label = tk.Label(self.mid_frame2, textvariable=self.value)

        self.descr_label.pack(side='left')
        self.mpg_label.pack(side='left')

        #Bottom frame
        self.calc_button = tk.Button(self.bottom_frame, text='Calculate', command=self.calculate)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        #Pack the frames
        self.top_frame.pack()
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def calculate(self):
        miles = float(self.miles_entry.get())
        gallons = float(self.gallon_entry.get())
        mpg = miles / gallons
        self.value.set(f'{mpg:.2f}')

if __name__ == '__main__':
    mpg = MPGCalculatorGUI()