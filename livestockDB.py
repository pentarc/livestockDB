# livestockDB.py
# Built with love using Python, tkinter, Pillow, sqlite, and Github.
# Please see LICENSE and README for more information.
# kthxbai

from tkinter import *
from tkinter import ttk

# main window
root = Tk()
root.title("livestockDB")

# menu bar

# main frame
cframe = ttk.Frame(root)

# set up the window structure
p = ttk.Panedwindow(cframe, orient=HORIZONTAL)
f1 = ttk.Frame(p, width=100)
f2 = ttk.Frame(p)
p.add(f1)
p.add(f2)

# set up tree in left pane (f1)
tree = ttk.Treeview(f1)
tree.insert('', 0, 'herdInfo', text='Herd Info')
tree.insert('herdInfo', 0, 'addCritter', text='Add Critter')
tree.insert('herdInfo', 1, 'updateCritter', text='Update Critter')
tree.insert('herdInfo', 2, 'listCritters', text='List Critters')
tree.insert('', 1, 'breedInfo', text='Breeding')
tree.insert('breedInfo', 0, 'addBreeding', text='Add Breeding')
tree.insert('breedInfo', 1, 'updateBreeding', text='Update Breeding')
tree.insert('breedInfo', 2, 'listBreedings', text='List Breedings')
tree.insert('breedInfo', 3, 'breedingResults', text='Breeding Results')
tree.insert('', 2, 'medicalInfo', text='Medical')
tree.insert('medicalInfo', 0, 'updateMedRecord', text='Update Med Record')
tree.insert('medicalInfo', 1, 'batchUpdateMedRecords', text='Batch Update Med Records')
tree.insert('medicalInfo', 2, 'updateProcedures', text='Update Procedures')


# run main loop
root.mainloop()
