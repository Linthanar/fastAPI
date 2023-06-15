from tkinter import *

# main = Tk()
# main.title('Main.py')
# main.geometry('600x400')

# label = Label(main, text='Look at me!', font = 30, fg='purple')
# label.pack()

# main.mainloop()

# def click_action(button):
#     button.config(text=f"You are so Hot!")

# def create_command(func, *args, **kwargs):
#     def command():
#         return func( *args, **kwargs)
#     return command

# root = Tk()
# root.geometry('200x200')

# click_button = Button(root,text='Click me!', width=8)
# click_button.pack()

# click_button.config(command=create_command(click_action, click_button))

# root.mainloop()

clicks = 0

def click_action(button):
    global clicks
    clicks += 1
    button.config(text="You are so Hot! x {}".format(clicks))

root = Tk()
root.geometry('200x200')

click_button = Button(root,text='Click me!')
click_button.pack()

click_button.config(command=lambda: click_action(click_button))

root.mainloop()