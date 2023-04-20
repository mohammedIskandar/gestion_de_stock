
import mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="msq.575:MRN!", database="laplateforme")
mycursor = conn.cursor()

exe_database = "create database boutique_test"
exe_table1 = "create table produit_test (id integer auto_increment primary key, nom varchar(255), description text, prix int, id_categorie int)"
exe_table2 = "create table categorie (id integer auto_increment primary key, nom varchar(255))"


exe_insert1 = ("insert into `produit_test`(`nom`, `marque` `description`, `prix`, `quantite` `id_categorie`) values(%s, %s, %s, %s)")
exe_insert2 = ("insert into `categorie_test`(`nom`) values(%s)")

val_produit = [("Pull", "Pull en laine differentes tailles et couleur disponible", 39, 1),
       ("Chouchou", "Différentes couleurs disponible", 5, 1),
       ("Tote bag", "Sac de transport, différentes couleurs disponible", 5, 1),
       ("Bob", "Bob en tissu recyclé, création artisanale", 45, 2),
       ("Chouchou", "Différentes couleurs disponible", 5, 2),
       ("Robe", "Robe en coton, création artisanale, pièce unique", 300, 3),
       ("Chouchou", "Différentes couleurs disponible", 5, 3),
       ("Sac", "Sac en cuir de veau recyclé, création artisanale, different coloris disponible", 315, 4),
       ("Pochette", "Pochette en cuir de veau recyclé, création artisanale", 65, 4),
       ("Jeu", "Jeu de société comprenant 100 cartes et un dé jouable de 2 à 6 joueurs", 19, 5),
       ("Short", "Short de bain en plastique recyclé, differentes tailles et couleurs disponible", 315, 6),]

val_categorie = [("Jijel Factory"),
                 ("Comptoir de Mogo"),
                 ("Nosabari"),
                 ("Kariere"),
                 ("Esprit Declic"),
                 ("Calanques")]

mycursor.executemany(exe_database, exe_table1, exe_table2)
mycursor.execute(exe_insert1, val_produit)
mycursor.execute(exe_insert2, val_categorie)


def ajout_sql():
    print("insertion en cours...")
    mycursor.execute("insert into `produit_test2`(`nom`, `marque`, `description`, `prix`, `quantite`, `id_categorie`) values(%s, %s, %s, %s, %s, %s)")
    query = "INSERT INTO  `produit_test2` (`nom` ,`marque` ,`description` ,`prix`, `quantite`, `id_categorie`) \
            VALUES(%s,%s,%s,%s, %s, %s)"
    my_data = (input_nom, input_marque, input_description, input_prix, input_quantite, input_id_categorie)
    id = mycursor.execute(query, my_data) 
