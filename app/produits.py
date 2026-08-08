import os
import json  

from models.produit import Produit
from .utils import valider_nom, valider_prix #sera utile pour la validation

DATA_FILE="data/produits.json"

produits=[]#liste globale des produits. (Elle sera rempli par charger_produits)

def initialiser_stockage():
    data_dir=os.path.dirname(DATA_FILE)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

def sauvegarder_produits():#Fonction de sauvegarde sur le disque
    data=[]
    for p in produits:
        data.append({"nom":p.nom,"prix":p.prix})
    with open(DATA_FILE,"w") as f:
        json.dump(data,f,indent=4)

def charger_produits():#Fonction de chargement depuis le disque
    global produits

    if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE,"r") as f:
                    data=json.load(f)
                    produits=[Produit(item["nom"],item["prix"]) for item in data]
                print(len(produits),"produits charges")
            except json.JSONDecodeError:
                print("Erreur : le fichier produits.json est corrompu.")
                print("Un nouveau fichier vierge va etre cree.")

                if os.path.exists(DATA_FILE):
                    os.rename(DATA_FILE, "data/produits.corrompu.json")
                    produits=[]
                    sauvegarder_produits()
    else:           
        produits=[]
        sauvegarder_produits()

def ajouter_produits(nom,prix):#Fonction d'ajout de produits
    """
    Ajoute un produit a la liste 'produits'
    """
    global produits
    if not valider_nom(nom):
        print("Nom invalide: le nom ne peux pas etre vide")
        return False
    
    if not valider_prix(prix):
        print("Prix invalide : le prix doit etre un nombre positif.")
        return False
    #si tout est valide, on ajoute.
    prix_float=float(prix)
    nouveau_produit=Produit(nom.strip(), prix_float)
    produits.append(nouveau_produit)
    sauvegarder_produits()
    print("Produit",nom.strip(),"ajouter et sauvegarder avec succes !")
    return True

def lister_produits():#Fonction de listage de produits
    """
    Afficher tous les produits stockes dans la liste
    """
    if not produits:
       print("Aucun produit en stock.")
       return
    
    print("\n Liste des produits :")
    for index, produit in enumerate(produits, start=1):
        print(index,".",end="")
        produit.afficher()

def rechercher_produits(nom_recherche):#Fonction de recherche des produits
    """
    Recherche un produit par son nom(insensible a la casse).
    """
    for produit in produits:
        if produit.nom.lower()==nom_recherche.lower():
            print("",end="")
            produit.afficher()
            return
    print("Aucun produit trouve avec le nom",nom_recherche)

def supprimer_produits(nom_supprimer):
    """
    Supprime le produit dont le nom correspond.
    Retourne True si le produit a ete supprime, False sinon.
    """

    for produit in produits:
        if produit.nom.lower()==nom_supprimer.lower():
            produits.remove(produit)
            sauvegarder_produits()
            print("Produit",nom_supprimer,"supprime avec succes.")
            return True
    print("Aucune produit trouve avec le nom",nom_supprimer,".")
    return False

initialiser_stockage()
charger_produits()