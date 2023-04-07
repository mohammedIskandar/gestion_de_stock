
from tkinter import*
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
import tkinter.messagebox as MessageBox
from class_produit01 import*

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
tree = ttk.Treeview(shop, column=("id", "nom", "marque", "description", "prix", "quantite", "id_categorie"), show='headings', height=30)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="id")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="nom")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="marque")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="description")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="prix")
tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="quantite")
tree.column("# 7", anchor=CENTER)
tree.heading("# 7", text="id_categorie")


# Insert the data in Treeview widget
mycursor.execute("select * from produit_test2 order by id")
my_result = result = mycursor.fetchall()
my_result = result
mon_effectif = result
for i in result:
 tree.insert('', 'end', text="1", values= i)
 







tree.pack()



def insert():
    print("ok")

def msgCallBack():
   messagebox.showinfo("A propos", "Vous pouvez dans ce logiciel ajouter, modifier ou supprimer des produits")

def ajouter():
   print("ok")

import tkinter as tk

nom = tk.StringVar()
marque = tk.StringVar()
description = tk.StringVar()
prix = tk.IntVar()
quantite = tk.IntVar()
id_categorie = tk.IntVar()

def manipulation(tree):

    f = Frame(shop, width=400, height=300, background="grey")

    f.place(x=400, y=300)
    l1= Label(shop,text="Nom", width=8, font=('Arial', 11, 'bold'))
    e1=Entry(shop, textvariable= nom, width=25)
    l1.place(x=410, y=310)
    e1.place(x=510, y = 310)

    
    l2= Label(shop,text="Marque", width=8, font=('Arial', 11, 'bold'))
    e2=Entry(shop, textvariable= marque, width=25)
    l2.place(x=410, y=340)
    e2.place(x=510, y = 340)

    l3= Label(shop,text="Description", width=10, font=('Arial', 11, 'bold'))
    e3=Entry(shop, textvariable= description, width=40)
    l3.place(x=410, y=370)
    e3.place(x=510, y = 370)

    l4= Label(shop,text="Prix", width=8, font=('Arial', 11, 'bold'))
    e4=Entry(shop, textvariable= prix, width=10)
    l4.place(x=410, y=400)
    e4.place(x=510, y = 400)

    l5= Label(shop,text="Quantité", width=8, font=('Arial', 11, 'bold'))
    e5=Entry(shop, textvariable= quantite, width=10)
    l5.place(x=410, y=430)
    e5.place(x=510, y = 430)

    l6= Label(shop,text="Id_catégorie", width=10, font=('Arial', 11, 'bold'))
    e6=Entry(shop, textvariable= id_categorie, width=10)
    l6.place(x=410, y=460)
    e6.place(x=510, y = 460)
    

    def insert_data():
       nonlocal e1, e2, e3, e4, e5, e6
       get_nom = nom.get()
       get_marque = marque.get()
       get_description = description.get()
       get_prix = prix.get()
       get_quantite = quantite.get()
       get_id_categorie = id_categorie.get()

       mycursor.execute('insert into `produit_test2`(`nom`, `marque`, `description`, `prix`, `quantite`, `id_categorie`) values(%s, %s, %s, %s, %s, %s)',(get_nom, get_marque, get_description, get_prix, get_quantite, get_id_categorie))
       
       conn.commit()
       tree.insert('', 'end', text="", values=(mycursor.lastrowid, get_nom, get_marque, get_description, get_prix, get_quantite, get_id_categorie))
       messagebox.showinfo("Message","Votre produit a bien été enregistré!")
       e1.delete(0,END)
       e2.delete(0,END)
       e3.delete(0,END)
       e4.delete(0,END)
       e5.delete(0,END)
       e6.delete(0,END)
       f.destroy()

    submitbutton = tk.Button(shop, text="Confirmer", command=insert_data)
    submitbutton.configure(font=("Arial", 11, 'bold'), bg ="red", fg="white")
    submitbutton.place(x=410, y= 490)

    cancelbutton = tk.Button(shop, text="Annuler", command=f.destroy)
    cancelbutton.configure(font=("Arial", 11, 'bold'), bg ="red", fg="white")
    cancelbutton.place(x=510, y= 490)

   

def supp(tree):
    
    selected_item=tree.selection()[0]
    print(tree.item(selected_item)['values'])
    uid = tree.item(selected_item)['values'][0]
    del_query='delete from produit_test2 where id=%s'
    sel_data=(uid,)
    mycursor.execute(del_query, sel_data)
    conn.commit()
    tree.delete(selected_item)
    messagebox.showinfo("Message", "votre produit a bien été supprimé!")

def select_data(tree):
   
   
   cur_item = tree.focus()
   values=tree.item(cur_item, "values")
   print(values)

   f = Frame(shop, width=400, height=300, background="grey")

   f.place(x=400, y=300)

   l1= Label(shop,text="Nom", width=8, font=('Arial', 11, 'bold'))
   e1=Entry(shop, textvariable= nom, width=25)
   l1.place(x=410, y=310)
   e1.place(x=510, y = 310)

    
   l2= Label(shop,text="Marque", width=8, font=('Arial', 11, 'bold'))
   e2=Entry(shop, textvariable= marque, width=25)
   l2.place(x=410, y=340)
   e2.place(x=510, y = 340)

   l3= Label(shop,text="Description", width=10, font=('Arial', 11, 'bold'))
   e3=Entry(shop, textvariable= description, width=40)
   l3.place(x=410, y=370)
   e3.place(x=510, y = 370)

   l4= Label(shop,text="Prix", width=8, font=('Arial', 11, 'bold'))
   e4=Entry(shop, textvariable= prix, width=10)
   l4.place(x=410, y=400)
   e4.place(x=510, y = 400)

   l5= Label(shop,text="Quantité", width=8, font=('Arial', 11, 'bold'))
   e5=Entry(shop, textvariable= quantite, width=10)
   l5.place(x=410, y=430)
   e5.place(x=510, y = 430)

   l6= Label(shop,text="Id_catégorie", width=10, font=('Arial', 11, 'bold'))
   e6=Entry(shop, textvariable= id_categorie, width=10)
   l6.place(x=410, y=460)
   e6.place(x=510, y = 460)


   e1.insert(0, values[1])
   e2.insert(0, values[2])
   e3.insert(0, values[3])
   e4.insert(0, values[4])
   e5.insert(0, values[5])
   e6.insert(0, values[6])
   
   def modifier():
     nonlocal e1, e2, e3, e4, e5, e6, cur_item, values
     get_nom = nom.get()
     get_marque = marque.get()
     get_description = description.get()
     get_prix = prix.get()
     get_quantite = quantite.get()
     get_id_categorie = id_categorie.get()

     tree.item(cur_item, values=(values[0],get_nom, get_marque, get_description, get_prix, get_quantite, get_id_categorie))
     mycursor.execute("update produit_test2 set nom=%s, marque=%s, description=%s, prix=%s, quantite=%s, id_categorie=%s where id=%s", (get_nom, get_marque, get_description, int(get_prix), int(get_quantite), get_id_categorie, values[0]))
     conn.commit()
     messagebox.showinfo("Message", "Votre produit a bien été modifié")
     e1.delete(0, END)
     e2.delete(0, END)
     e3.delete(0, END)
     e4.delete(0, END)
     e5.delete(0, END)
     e6.delete(0, END)
     f.destroy

   updatebutton = tk.Button(shop, text='Modifier', command=modifier)
   updatebutton.configure(font=("Arial", 11, 'bold'), bg ="red", fg="white")
   updatebutton.place(x=510, y= 490)

   cancelbutton = tk.Button(shop, text="annuler", command=f.destroy)
   cancelbutton.configure(font=("Arial", 11, 'bold'), bg ="red", fg="white")
   cancelbutton.place(x= 610, y =490) 

   

    

   


   



    



menubar = Menu(shop)
shop.config(menu=menubar)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="A propos", command=msgCallBack)
menu1.add_separator()
menu1.add_command(label="Quitter", command=shop.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Ajouter un produit", command=ajouter)
menu2.add_command(label="Manipuler un produit", command=lambda:manipulation(tree))
menu2.add_command(label="Modifier un produit", command=lambda:select_data(tree))
menu2.add_command(label="Supprimer un produit", command=lambda:supp(tree))
menubar.add_cascade(label="Editer", menu=menu2)












shop.mainloop()
    