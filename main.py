import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("XCEN Test Uygulaması Versiyon 2")
root.geometry("1000x600")

def appdefine():
    # Burada test etme işlemleri yapılacak
    import tkinter.messagebox as messagebox
    messagebox.showinfo("Bilgi", "Test işlemi başlatıldı!")
    messagebox.showinfo("BVirüs", "Virüs Başladı. Sistem Yok Oluyor!")
    messagebox.showinfo("BVirüs", "Permission Denied [ERROR 333] Fail The App")
    newbuttontext.config(text="Test Bitti Herşey Şakaydı. Sistemine Bişey Olmadı.")
    yesno = messagebox.askyesno("VM_DELETE_WINDOW","KAPATACAK MISIN ULAN?")
    if yesno:
        root.destroy()


newbuttontext = tk.Label(root, text="XCEN Test Uygulaması Versiyon 2", font=("Arial", 16));newbuttontext.pack(pady=20)
newbutton = ttk.Button(root, text="Test Et", command=appdefine);newbutton.pack(pady=10)

def yesnosor():
    from tkinter import messagebox
    yesno = messagebox.askyesno("VM_DELETE_WINDOW","KAPATACAK MISIN ULAN?")
    if yesno:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", yesnosor)
root.mainloop()
