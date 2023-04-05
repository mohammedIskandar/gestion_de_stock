from tkinter import*
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

shop = Tk()
shop.resizable(True, True)
shop.title("Boutique")
shop.iconbitmap("shop.ico")

ttk.Label(shop, text="Gestionnaire des stocks - Ouvre Boîte", font=('Ariel', 25)).pack()


shop.geometry("1000x1000")

style = ttk.Style()
style.theme_use('clam')

conn = mysql.connect(host="localhost",user="root",password="msq.575:MRN!", database="boutique_test")
mycursor = conn.cursor()

# Add a Treeview widget
tree = ttk.Treeview(shop, column=("id", "nom", "description", "prix", "id_categorie"), show='headings', height=30)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="id")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="nom")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="description")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="prix")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="id_categorie")


# Insert the data in Treeview widget
mycursor.execute("select * from produit_test")
my_result = result = mycursor.fetchall()
my_result = result
mon_effectif = result
for i in result:
 tree.insert('', 'end', text="1", values= i)
 








tree.pack()

def insert():
    print("ok")

shop.mainloop()
    