# INFO 202 - TP 3

# -*- coding: utf-8 -*-

from import_livres import import_livres
from livre import afficher_livre, titre_livre, auteur_livre, categorie_livre




Bibliotheque = import_livres("listelivres.csv")




def affiche_liste_livres(bibliotheque: list) -> None:
    """Entree : bibliotheque (liste de dictionnaires livre)
    Sortie : None, affiche tous les livres
    """
    for livre in bibliotheque:
        afficher_livre(livre)
        print("-" * 40)




def ajouter_livre(bibliotheque: list, livre: dict) -> None:
    """Entrees : bibliotheque (liste), livre (dictionnaire)
    Sortie : None, ajoute le livre a la bibliotheque
    """
    bibliotheque.append(livre)



def recherche_par_titre(bibliotheque: list, titre: str) -> dict:
    """Entrees : bibliotheque (liste), titre (chaine)
    Sortie : dictionnaire livre s'il est trouve, dictionnaire vide sinon
    """
    for livre in bibliotheque:
        if titre_livre(livre) == titre:
            return livre
    return {}



def recherche_par_auteur(bibliotheque: list, auteur: str) -> list:
    """Entrees : bibliotheque (liste), auteur (chaine)
    Sortie : liste de livres de cet auteur
    """
    resultat = []
    for livre in bibliotheque:
        if auteur_livre(livre) == auteur:
            resultat.append(livre)
    return resultat



def recherche_par_categorie(bibliotheque: list, categorie: str) -> list:
    """Entrees : bibliotheque (liste), categorie (chaine)
    Sortie : liste de livres de cette categorie
    """
    resultat = []
    for livre in bibliotheque:
        if categorie_livre(livre) == categorie:
            resultat.append(livre)
    return resultat
