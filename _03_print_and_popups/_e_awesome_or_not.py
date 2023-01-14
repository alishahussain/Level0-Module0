from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    num = random.randint(0, 3)
    # 2. Print your iariable to the console
    messagebox.showinfo(title='print', message= num)
    # 3. Get the user to enter something that they think is awesome
    answer = simpledialog.askstring(title='answer', prompt='enter something that u think is awesome')
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if num == 0:
        messagebox.showinfo(title='outcome0', message= 'woah ur awesome sauce')
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if num == 1:
        messagebox.showinfo(title='outcome1', message= 'ur cool ig')

    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if num == 2:
        messagebox.showinfo(title='outcome2', message= 'ur so basic')
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if num == 3:
        messagebox.showinfo(title='outcome3', message= 'get a life bro')
    # Run the window's .mainloop() method
window.mainloop()
