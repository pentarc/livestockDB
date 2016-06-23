# livestockDB.py
# Built with love using Python, tkinter, Pillow, sqlite, and Github.
# Please see LICENSE and README for more information.
# kthxbai

from tkinter import *

class ldb(Frame):

  def __init__(self, parent):
    Frame.__init__(self, parent, background="white")
    self.parent = parent
    self.parent.title("livestockDB")
    self.pack(fill=BOTH, expand=1)
    self.centerWindow()
    
    # set up the window structure
    p = Panedwindow(self, orient=HORIZONTAL)
    p.pack(fill=BOTH, expand=1)
    f1 = Frame(p, width=100)
    f2 = Frame(p)
    p.add(f1)
    p.add(f2)
    
    # set up tree in left pane (f1)
    tree = Treeview(f1)
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

  def centerWindow(self):
    w = 800
    h = 600
    sw = self.parent.winfo_screenwidth()
    sh = self.parent.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

# main window
def main():
    root = Tk()
    ex = ldb(root)
    root.mainloop()

# run main loop
if __name__ == '__main__':
  main()
