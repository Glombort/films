import pandas as pd 
import csv
any_film=pd.read_csv('Films.csv')

def adder():
    print('Name of Film')
    name=input()
    print('Platform')
    platform=input()
    print('Genres')
    genre=input()
    print('Language')
    language=input()
    print('Timings')
    timings=input()
    print('Year')
    year=input()
    print('Director')
    director=input()

    #new_row= "\n%s,%s,%s,%s,%s,%s,%s\n" % (name,platform,genre,language,timings,year,director)

    with open('Films.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([name,platform,genre,language,timings,year,director])
    return print('Thanks for adding :)')