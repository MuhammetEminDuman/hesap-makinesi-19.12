import tkinter as tk
import tkinter.font as tkFont




class App:
    
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        çarpma=tk.Button(root)
        çarpma["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        çarpma["font"] = ft
        çarpma["fg"] = "#000000"
        çarpma["justify"] = "center"
        çarpma["text"] = "çarpma"
        çarpma.place(x=160,y=200,width=70,height=25)
        çarpma["command"] = self.GButton_938_command

        bölme=tk.Button(root)
        bölme["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        bölme["font"] = ft
        bölme["fg"] = "#000000"
        bölme["justify"] = "center"
        bölme["text"] = "bölme"
        bölme.place(x=350,y=200,width=70,height=25)
        bölme["command"] = self.GButton_749_command

        GLineEdit_165=tk.Entry(root)
        GLineEdit_165["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_165["font"] = ft
        GLineEdit_165["fg"] = "#333333"
        GLineEdit_165["justify"] = "center"
        GLineEdit_165["text"] = "Entry"
        GLineEdit_165.place(x=250,y=140,width=70,height=25)

        GLineEdit_642=tk.Entry(root)
        GLineEdit_642["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_642["font"] = ft
        GLineEdit_642["fg"] = "#333333"
        GLineEdit_642["justify"] = "center"
        GLineEdit_642["text"] = "Entry"
        GLineEdit_642.place(x=160,y=140,width=70,height=25)

        çıkarma=tk.Button(root)
        çıkarma["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        çıkarma["font"] = ft
        çıkarma["fg"] = "#000000"
        çıkarma["justify"] = "center"
        çıkarma["text"] = "çıkarma"
        çıkarma.place(x=250,y=200,width=70,height=25)
        çıkarma["command"] = self.GButton_892_command

        toplama=tk.Button(root)
        toplama["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        toplama["font"] = ft
        toplama["fg"] = "#000000"
        toplama["justify"] = "center"
        toplama["text"] = "toplama"
        toplama.place(x=450,y=200,width=70,height=25)
        toplama["command"] = self.GButton_711_command

        GLineEdit_545=tk.Entry(root)
        GLineEdit_545["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_545["font"] = ft
        GLineEdit_545["fg"] = "#333333"
        GLineEdit_545["justify"] = "center"
        GLineEdit_545["text"] = "Entry"
        GLineEdit_545.place(x=350,y=140,width=70,height=25)

        GLineEdit_688=tk.Entry(root)
        GLineEdit_688["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_688["font"] = ft
        GLineEdit_688["fg"] = "#333333"
        GLineEdit_688["justify"] = "center"
        GLineEdit_688["text"] = "Entry"
        GLineEdit_688.place(x=450,y=140,width=70,height=25)

    
    
    def GButton_938_command(self):
        
       print("buton 2 basıldı")

        

    def GButton_749_command(self):
        print("buton 2 basıldı")


    def GButton_892_command(self):
        print("command")


    def GButton_711_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    textBoxYazilanlar = tk.StringVar()#Değişken
    textBoxYazilidir = tk.StringVar()#Değişken
    textBoxYazilidirlar = tk.StringVar()#Değişken

    root.mainloop()

