# -*- coding: utf-8 -*-
from livre_id import nouvel_identifiant

Livre_exemple = {
    "Titre" : "Apprendre a programmer avec Python",
    "Auteur" : "G. Swinnen",
    "Catégorie" : "Informatique",
    "Identifiant" : nouvel_identifiant()}


Livre_1 = {
    "Titre" : "The Devil And The Dark Water",
    "Auteur" : "Stuart Turton",
    "Catégorie" : "Meurtre et Mystere",
    "Identifiant" : nouvel_identifiant()}

Livre_2 = {
    "Titre" : "David Copperfield",
    "Auteur" : "Charles Dickens",
    "Catégorie" : "Roman",
    "Identifiant" : nouvel_identifiant()}

Livre_3 = {
    "Titre" : "A Study in Scarlet",
    "Auteur" : "Arthur Conan Doyle",
    "Catégorie" : "Roman policier",
    "Identifiant" : nouvel_identifiant()}

def titre_livre(livre: dict) -> str:
    """Entree : dictionnaire livre
    Sortie : chaine de caracteres, titre du livre
    """
    return livre["Titre"]


def auteur_livre(livre: dict) -> str:
    """Entree : dictionnaire livre
    Sortie : chaine de caracteres, auteur du livre
    """
    return livre["Auteur"]


def categorie_livre(livre: dict) -> str:
    """Entree : dictionnaire livre
    Sortie : chaine de caracteres, categorie du livre
    """
    return livre["Categorie"]


def afficher_livre(livre: dict) -> None:
    """Entree : dictionnaire livre
    Sortie : None, affiche les infos du livre
    """
    print("Titre du Livre :", titre_livre(livre) + ",")
    print("Auteur :", auteur_livre(livre) + ",")
    print("Categorie :", categorie_livre(livre))


def creer_livre(titre: str, auteur: str, categorie: str) -> dict:
    """Entrees : titre (chaine), auteur (chaine), categorie (chaine) Sortie : dictionnaire representant un livre """
    livre = {
    "Titre": titre,
    "Auteur": auteur,
    "Categorie": categorie,
    "Identifiant": nouvel_identifiant()}
    return livre

def saisir_livre() -> dict:
    """Entree : aucune (utilise input)
    Sortie : dictionnaire representant un nouveau livre
    """
    print("Quel est le titre du livre ?")
    titre = input()
    print("Quel est l'auteur du livre ?")
    auteur = input()
    print("Quelle est la categorie du livre ?")
    categorie = input()
    return creer_livre(titre, auteur, categorie)