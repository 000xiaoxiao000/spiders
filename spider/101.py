from tkinter import *

root = Tk()


def print_value():
    count = 0
    for my_list in list_entry:
        count += 1
        value = "%5s" % my_list.get()
        print(value, end='')
        if count % 9 == 0:
            print()


list_entry = []
for i in range(9):
    for j in range(9):
        vij = StringVar()
        eij = Entry(root, textvariable=vij, width=3)
        # eij vij 都行，意思就是可以不用textvarriable这个属性
        list_entry.append(eij)
        eij.grid(row=i, column=j)

btn_test = Button(root, text='p', comman=print_value)
btn_test.grid(row=9, column=0)

root.mainloop()