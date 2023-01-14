from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    #      // 2.  Ask the user a question
    question1 = simpledialog.askstring(title= 'question1', prompt= 'whats 2+2?')
    if question1 == '4':
        score+=1
    else:
        score+=-1
    #      // 3.  Use an if statement to check if their answer is correct
    #      // 4.  if the user's answer was correct, add one to their score


    question2 = simpledialog.askstring(title= 'question2', prompt= 'whats 4*4?')
    if question2 == '16':
        score+=1
    else:
        score+=-1


    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
