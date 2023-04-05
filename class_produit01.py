class Produit:
    
    def __init__(self, nom, description, prix, marque, id_categorie, stock):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.marque = marque
        self.id_categorie = id_categorie
        self.stock = stock

    def set_nom(self, nom):
         self.nom = nom
    def get_nom(self, nom):
        self.nom = nom

    def set_description(self, description):
         self.description = description
    def get_description(self, description):
        self.description = description

    def set_prix(self, prix):
         self.prix = prix
    def get_prix(self, prix):
        self.prix = prix

    def set_marque(self, marque):
         self.marque = marque
    def get_marque(self, marque):
        self.marque = marque

    def set_id_categorie(self, id_categorie):
         self.id_categorie = id_categorie
    def get_id_categorie(self, id_categorie):
        self.id_categorie = id_categorie

    def set_stock(self, stock):
         self.stock = stock
    def get_stock(self, stock):
        self.stock = stock