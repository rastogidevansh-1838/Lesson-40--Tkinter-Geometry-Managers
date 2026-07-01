from tkinter import *
from datetime import date
root = Tk()
root.title('Age Calcuator')
root.geometry('500x500')
today = date.today()
frame = Frame(master = root, height = 200, width = 360, bg = '#d0efff')
lbl1 = Label(frame, text = 'Enter ur date of birth', bg = '#356382', width = 10 )
lbl2 = Label(frame, text = 'Enter ur birth month', bg = '#356382', width = 10 )
lbl3 = Label(frame, text = 'Enter ur birth year', bg = '#356382', width = 10 )
date_entry = Entry(frame)
month_entry = Entry(frame)
year_entry = Entry(frame)
year = today.year - year_entry
month = today.month - month_entry
date1 = today.date - date_entry
print('you are ' +date1+ 'days old, ' +month+ 'months old and ' +year+ 'year old.')