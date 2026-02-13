# -*- coding: utf-8 -*-
from livre import creer_livre


def import_livres(nom_fichier:str)->list:
   
    fichier = open(nom_fichier, "r", encoding="UTF-8")
    liste_livres = []

    ligne = fichier.readline()
    while ligne != "" :
        livre = parse_chaine_livre(ligne)
        liste_livres.append(livre)

        ligne = fichier.readline()
        
    fichier.close()
    return liste_livres


def parse_chaine_livre(chaine: str)-> dict:
    _, genre, _, titre, auteur = chaine.strip().split(";")
    livre = creer_livre(titre, auteur, genre)

    return livre



