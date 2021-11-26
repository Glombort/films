import pandas as pd 
import inquirer
import csv


any_film=pd.read_csv('Films.csv')

print('Name of Film for deletion')
name=input()
films_for_del=any_film[any_film['Name']==name]
if films_for_del.shape[0]==0:
    print('Try again')
    name=input()
    films_for_del=any_film[any_film['Name']==name]

print(films_for_del)
print('What is the index of the film for deletion?')
index=input()
any_film.index