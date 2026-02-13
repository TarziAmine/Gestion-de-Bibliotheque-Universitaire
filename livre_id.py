# -*- coding: utf-8 -*-

Dernier_Id = 0

def nouvel_identifiant()->int:
    global Dernier_Id
    Dernier_Id = Dernier_Id + 1
    return Dernier_Id
