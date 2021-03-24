# [Exercice] Le rêve américain

The original data is in the 'data/01_raw' folder

In the notebook folder, there are two files to check : 'Career_visualization.ipynb' 'Data_cleaning.ipynb'

In the 'src/d00_utils' folder, there is one file 'mysql_utils.py' This file defines the functions to connect and to save to MySQL.

In the 'src/d01_data' folder, there is 'load_data.py' This script loads the data from the excel and csv tables into a MySQL database

The 'requirements.txt' lists the libraries installed in the Python3 enviromnment, it was created using 'pip freeze > requirements.txt'



# Contexte du projet

Cela ne fait qu’un mois que vous faites de la data-science mais, ambitieux, vous avez déjà les yeux tournés vers l’avenir. C’est de l’Amérique dont vous rêvez. Cependant, vous savez que le rêve américain n’est plus aussi facilement accessible qu’avant, il va vous falloir un plan! Vous avez à votre disposition deux jeux de données, à vous de construire votre plan de carrière.

Ce que vous devez réaliser:

                       ++I Mise en place de l'environnement de code dans les respects des bonnes pratiques.++

* Créer un repository git et le cloner en local

* créer votre structure de projet à partir de la proposition de template

* Créer votre environnement virtuel
  
                       ++II Data cleaning++

* Télécharger et importez vos données dans un moteur de base de données (au choix) (d01_data)

* Selectionner parmis les tables les colonnes qui de près ou de loin pourraient être intéressantes pour l'étude (d02_intermediate)

* Rechercher s'il existe des valeurs manquantes, les traiter (d02_intermediate)

* Rechercher s'il y a des colonnes qu'il faudrait transformer en datetime (d02_intermediate)

* Vérifier la consistence des données (d02_intermediate)

* Rechercher les valeurs abbérantes et les traiter (d02_intermediate)

                      ++III Data visualisation (Carreer_visualization.ipynb)++

  Pour les travailleurs de la data aux Etats Unis donnez:

* le salaire moyen, le salaire median, et représentez les dix déciles. Faites l'exercice pour les deux bases et comparez les résultats.

* Le salaire moyen en fonction du job title + diagramme circulaire de la répartitions de ses jobtitles (base 1)

                     ++Répondre aux questions (en justifiant):++

* Est-il préférable de travailler pour une seule ou plusieurs compagnies?

* Le nombre de personne dans son équipe a-t-il une influence sur votre salaire?

* Le nombre d'année d'expérience dans ce type d'emploi a t il une influence sur votre salaire?

* Il y-a-t-il une inégalité salariale entre les hommes et les femmes dans les emplois liées à la data aux Etats Unis?

* Si cette inégalité salariale existe (suspense), est-elle due au fait que les femmes soient moins bien représentées dans les jobs les mieux payés ou que pour un travail identique elles sont en moyenne moins bien payées?

* Y a t il une différence entre l'évolution salariale liées à l'expérience dans un même emploi entre les hommes et les femmes?

* Résumé en quelques lignes votre plan de carrière pour conquérir le rêve américain.

# Pour allez plus loin (facultatif)

Pour chaque exercice, venir vers moi pour des précisions sur les consignes:

* Représentez une "heat-map" des Etats-Unis en fonction du salaire moyen

* Que pensez vous de mon hypothèse HO: "Les personnes bien payées ont tendance à vouloir rester dans leur entreprise."

* Est ce que le salaire moyen et la répartion en fonction du job-title est cohérente dans les deux bases.

# Livrables

Deadlines: Environ 3 jours

# Critères de performance

L'ensemble des requêtes doit être correct, l'intégration de nouvelles données se fait correctement, le code est bien commenté et ajouté sur GIT.



# Ressources 

https://www.kaggle.com/learn/data-visualization
https://github.com/charles-42/American_dream