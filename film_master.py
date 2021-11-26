import film_chooser as fc 
import film_add as fa
import pandas as pd 
import inquirer
import csv
any_film=pd.read_csv('Films.csv')

what_q = [
    inquirer.List('what',
            message="What do you want to do today?",
            choices=['Pick', 'Add'],),]
what = inquirer.prompt(what_q)

if what['what']=='Pick':
    fc.picker()
else:
    fa.adder()

