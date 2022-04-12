import pandas as pd
import tkinter as tk
import glob as gb
from tkinter import *
from tkinter import filedialog




# Window build
root = tk.Tk()
root.title('File Agregator @ eMVi software')
# root.iconbitmap('icon path here')
root.geometry('400x400')



# Empty lists to use
folder_selected_in = []
folder_selected_out = []
files = []




#Functions
def sciezka_in():
    folder_selected_in = []
    folder_selected_in.append(filedialog.askdirectory() + "/")
    text_box = Text(root, width = 47, height = 2)
    text_box.pack(expand=True)
    text_box.insert('end', folder_selected_in)
    text_box.config(state='disabled')
    text_box.place(x = 10, y = 90)
    



def sciezka_out():
    folder_selected_out = []
    folder_selected_out.append(filedialog.askdirectory() + "/")
    text_box1 = Text(root, width = 47, height = 2)
    text_box1.pack(expand=True)
    text_box1.insert('end', folder_selected_out)
    text_box1.config(state='disabled')
    text_box1.place(x = 10, y = 230)
    

# outdated
# def agreguj():
#     fin = "".join(folder_selected_in)
#     fout = "".join(folder_selected_out)
#     files = gb.glob(fin + "*")
#     df = pd.concat(map(pd.read_csv, files), ignore_index=True)
#     df.to_csv(fout + "ALLtest.csv", mode='w', index = False)


def agreguj2():
    files = []
    fin = "".join(folder_selected_in)
    fout = "".join(folder_selected_out)
    files = gb.glob(fin + "*")
    f_csv = [path for path in files if path.endswith("csv")]
    f_xlsx = [path for path in files if path.endswith("xlsx")]

    if f_csv != [] and f_xlsx == []:
        df_csv = pd.concat(map(pd.read_csv, f_csv), ignore_index=True)
        df_csv.to_csv(fout + "ALLtest.csv", mode='w', index = False)
        f_csv = []

    elif f_csv == [] and f_xlsx != []:
        df_xlsx = pd.concat(map(pd.read_excel, f_xlsx), ignore_index=True)
        df_xlsx.to_excel(fout + "ALLtest.xlsx", index = False)
        f_xlsx = []
    
    elif f_csv != [] and f_xlsx != []:
        df_csv = pd.concat(map(pd.read_csv, f_csv), ignore_index=True)
        df_csv.to_csv(fout + "ALLtest.csv", mode='w', index = False)
        df_xlsx = pd.concat(map(pd.read_excel, f_xlsx), ignore_index=True)
        df_xlsx.to_excel(fout + "ALLtest.xlsx", index = False) 
        f_csv = []
        f_xlsx = []

    else:
        lab3 = tk.Label(root, text = 'W KATALOGU BRAK PLIKÓW CSV LUB XLSX')
        lab3.place(x=80,y=260)             




#Labels
lab = tk.Label(root, text = 'Agreguj pliki csv lub xlsx')
lab.pack()
lab1 = tk.Label(root, text = 'Katalog z plikami do zagregowania:')
lab1.place(x=10,y=60)
lab2 = tk.Label(root, text = 'Katalog gdzie zapisać zagregowany plik:')
lab2.place(x=10,y=200)




#Butons
b_text = tk.Button(root, text = 'Wybierz', width = 10, height = 1, command = sciezka_in)
b_text.place(x = 310, y = 60)
b_text1 = tk.Button(root, text = 'Wybierz', width = 10, height = 1, command = sciezka_out)
b_text1.place(x = 310, y = 200)
b_text2 = tk.Button(root, text = 'Agreguj', width = 50, height = 5, command = agreguj2)
b_text2.place(x = 20, y = 300)




#keep window open
root.mainloop()
