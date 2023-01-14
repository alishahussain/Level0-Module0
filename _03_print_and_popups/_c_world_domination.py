from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    for i in range(1):
        answer =  simpledialog.askstring(title='code' , prompt='do you know how to write code?')
        if answer == 'yes':
            messagebox.showinfo(title= 'yes', message= 'omg yay! you will rule the world')
        elif answer =='no':
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
            messagebox.showerror(title= 'no', message= 'thats embarrasing for you, u should prolly sign up for the league of amazing programmers.')

    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.

    # Run the window's .mainloop() method
    window.mainloop()
