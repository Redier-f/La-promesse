import csv

r_fileTSV = 'data_promesse.tsv'

w_fileTSV = '/root/Documents/Faustine/data_promesse_avec_sommes.tsv'

titres=["Auteur","Titre","Date","Genre","Citation","parjure","serment","promesse","engagement","pacte","gage","foi","voeu","parole","traitre","alliance","caution","garantie","contrat","traite"]

with open("data_promesse.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        print(row)
