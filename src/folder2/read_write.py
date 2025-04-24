#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script che legge un file di testo, trasforma ogni riga in maiuscolo
e salva il risultato in un nuovo file.
"""

def process_file(input_path, output_path):
    # Apri il file di input in lettura e quello di output in scrittura
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Trasforma la riga in maiuscolo e la scrive nel file di output
            outfile.write(line.upper())

def main():
    src = 'input.txt'
    dst = 'output.txt'
    print(f"Lettura da {src} e scrittura in {dst}")
    process_file(src, dst)
    print("Elaborazione completata!")

if __name__ == "__main__":
    main()
