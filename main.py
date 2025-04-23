#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def moltiplica_per_due(numero):
    """
    Restituisce il doppio del valore passato.
    
    :param numero: numero da raddoppiare
    :return: numero * 2
    """
    return numero * 2

if __name__ == "__main__":
    # Chiede all'utente di inserire un numero (intero o decimale)
    n = float(input("Inserisci un numero: "))
    # Calcola il doppio e lo stampa
    risultato = moltiplica_per_due(n)
    print(f"Il doppio di {n} è {risultato}")
