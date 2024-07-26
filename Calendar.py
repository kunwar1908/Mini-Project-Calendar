# import specific classes and functions from the tkinter 
from tkinter import Tk, Label, Entry, Button, PhotoImage

# import calendar module
import calendar

# Function for showing the calendar of the given year
def showCal():
    # Create a GUI window
    new_gui = Tk()

    # Set the background colour of GUI window
    new_gui.config(background="white")

    # set the name of tkinter GUI window 
    new_gui.title("CALENDAR")

    # Set the configuration of GUI window
    new_gui.geometry("550x600")

    # get method returns current text as string
    fetch_year = int(year_field.get())

    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)

    # Create a label for showing the content of the calendar
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure.
    cal_year.grid(row=5, column=1, padx=20)

    # start the GUI 
    new_gui.mainloop()

# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background="white")

    # set the name of tkinter GUI window 
    gui.title("CALENDAR")

    # Set the configuration of GUI window
    gui.geometry("550x600")

    # Set the background image of GUI window
    bg_image = PhotoImage(file="C:/Users/kunwa/Downloads/school-845196_1920.png")
    background_label = Label(gui, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a CALENDAR label with specified font and size
    cal = Label(gui, text="CALENDAR", bg="dark gray", font=("times", 28, 'bold'))

    # Create a Enter Year label 
    year = Label(gui, text="Enter Year", bg="light green")

    # Create a text entry box for filling or typing the information. 
    year_field = Entry(gui)

    # Create a Show Calendar Button and attach it to showCal function
    Show = Button(gui, text="Show Calendar", fg="Black", bg="Red", command=showCal)

    # Create an Exit Button and attach it to exit function
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=gui.quit)

    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure.
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    Show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)

    # start the GUI 
    gui.mainloop()