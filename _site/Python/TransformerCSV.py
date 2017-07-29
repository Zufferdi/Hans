#!/usr/bin/env python
# -*- coding: utf-8 -*-
    
import csv

file = "Tableau.csv"
 
with open(file) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    header = csvReader.next()

    entree = 0
    
    #creation des posts a partir des lignes du csv
    
    for row in csvReader:
        
        date = row[0] # date de la page
        entree = entree + 1
        title = row[1]
        moment = row[2]
        date_md = row[0]
        # Coordonnees des lieux visites par Hans
        lat= row[8]
        long= row[9]
                
        # Le texte et ses explications
        texte = row[4]
        element_histo = row[5] # complement historiographique
        comment_histo = row[6] # commentaire
        photo = row[13] # photo
        
        # Les noms de fichiers
        fichier = "../_posts/" + date_md + "-" + str(entree)+ ".md"

# creation des articles
        
        string= '---'
        string += '\nlayout: "post"'
        string += '\ntitle: "'+ title + '"'
        string += '\ndate: "'+ date + '"'
        if moment != "":
            string += '\nmoment: "'+ moment + '"'
        if lat != "":
            string += '\nlatitude: "' + lat + '"'
        if long != "":
            string += '\nlongitude: "' + long + '"'
        string += '\n---'
        string += '\n\n' + texte + '\n'
        string += '\n\n<div class="histoire">' + element_histo + '</div>'
        string += '\n\n<div class="commentaire">' + comment_histo + '</div>'
        if photo != "":
            string += '\n\n<img class="photo" src="{{\''+ photo + '\' | prepend: site.baseurl}}">'
        
        
# automatisation de la création des posts piece par piece
        
        text_file = open(fichier, "w")
        text_file.write(string)
        text_file.close()
    
    



