import pandas as pd 
import inquirer
import csv

any_film=pd.read_csv('Films.csv')

print(any_film['Genre'].value_counts())


