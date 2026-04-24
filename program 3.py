# Author: Makenzie Totushek
# Date: 4/24/2026
# Title: Long-Distance Calls
import tkinter as tk
import tkinter.messagebox
class DistanceCallsGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Long-Distance Call Price")

        #create frames
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #create radio buttons
        self.radio_var = tk.DoubleVar()
        self.radio_var.set(0.02)

        self.rb1= tk.Radiobutton(self.top_frame, text="Daytime(6:00am - 5:59) $0.02 per minute", variable=self.radio_var, value=0.02)
        self.rb2 = tk.Radiobutton(self.top_frame, text="Evening(6:00pm - 11:59pm) $0.12 per minute", variable=self.radio_var, value=0.12)
        self.rb3 = tk.Radiobutton(self.top_frame, text="Off-Peak(12:00am - 5:59am) $0.05 per minute", variable=self.radio_var, value=0.05)


        self.rb1.pack(anchor='w')
        self.rb2.pack(anchor='w')
        self.rb3.pack(anchor='w')

        #get minutes on phone
        self.prompt_label = tk.Label(self.mid_frame,text='How many minutes long will your call be? ')
        self.minutes_entry = tk.Entry(self.mid_frame, width=10)
        self.prompt_label.pack(side='left')
        self.minutes_entry.pack(side='left')

        #create bottom frame buttons
        self.ok_button = tk.Button(self.bottom_frame,text='Ok', command=self.calculate_call)
        self.ok_button.pack(side='left')
        self.quit_button = tk.Button(self.bottom_frame,text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(side='left')
        #pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def calculate_call(self):
        price = self.radio_var.get()
        minutes = float(self.minutes_entry.get())
        total_price = price * minutes
        tk.messagebox.showinfo(message=f'Your total price is ${total_price:.2f}')

if __name__ == "__main__":
    calls = DistanceCallsGUI()