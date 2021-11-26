import pandas as pd 
import inquirer
import csv

any_film=pd.read_csv('Films.csv')

def picker():
    def numOfFilms(choice,column,database):
        number = database[database[column].str.contains(choice)]
        return number[column].count()
    def intNumOfFilms(choice,column,database):
        number=database[database[column]==choice]
        return number[column].count()

    print('Choose Max Timings')
    timings=int(input())

    new_choices=any_film
    if timings==0:
        pass
    else:
        new_choices=new_choices[new_choices['Timing']<=timings+10]
        new_choices=new_choices[new_choices['Timing']>timings-40]

    print('Choose Genre')
    
    confirm = {
    inquirer.Confirm('confirmed',
                     message="Do you want to pick a genre?" ,
                     default=True),}
    confirmation = inquirer.prompt(confirm)

    genre_fin = []
    genre_choices=['crime', 'drama', 'horror', 'thriller', 'comedy', 'action','adventure','animation','anime','sci-fi','romance','history','western', 'mystery', 'music','fantasy','war']
    
    while confirmation['confirmed']==True:
        genre_choices_q=[]
        for genre in genre_choices:
            number =numOfFilms(genre,'Genre',new_choices)
            if number==0:
                genre_choices.remove(genre)
            else:
                genre_choices_q.append(genre+' ('+str(number)+')') 
        genre_q = [
            inquirer.List('genre',
                    message="What genre do you want?",
                    choices=genre_choices_q,),]
        genre_a = inquirer.prompt(genre_q)
        genre_fin.append(genre_a['genre'].split(' ')[0])
        genre_choices.remove(genre_a['genre'].split(' ')[0])
        new_choices=new_choices[new_choices['Genre'].str.contains(genre_fin[0])]
        genre_fin.pop()
        confirm = {
    inquirer.Confirm('confirmed',
                     message="Do you want to pick another genre?" ,
                     default=True),}
        confirmation = inquirer.prompt(confirm)

    confirmation='any'
    
    
    print('Choose Language')
    lang_choices=['English', 'Japanese', 'Spanish', 'German','Italian','Danish','Icelandic','Mandarin','Foreign','any']
    lang_choices_q=[]
    for lang in lang_choices:
        number =numOfFilms(lang,'Language',new_choices)
        if lang=='any':
            number=new_choices['Language'].count()
            lang_choices_q.append(lang+' ('+str(number)+')')

        elif number==0:
            print(lang)
            lang_choices.remove(lang)
        else:
            lang_choices_q.append(lang+' ('+str(number)+')')
    lang_q = [
        inquirer.List('lang',
                message="What language do you want?",
                choices=lang_choices_q,),]
    language = inquirer.prompt(lang_q)

    if language['lang'].split(' ')[0]=='Foreign':
        new_choices=new_choices[new_choices['Language']!='English']
    elif language['lang'].split(' ')[0]!='any':
        new_choices=new_choices[new_choices['Language'].str.contains(language['lang'].split()[0])]

    decade_choices=[1950, 1960, 1970, 1980, 1990, 2000,2010,2020,'any']
    decade_choices_q=[]
    for decade in decade_choices:
        if decade=='any':
            number=new_choices['Year'].count()
            decade_choices_q.append(decade+' ('+str(number)+')')
        else:
            number=0
            for i in range(10):
                number+=intNumOfFilms(decade+i,'Year',new_choices)
            decade_choices_q.append(str(decade)+' ('+str(number)+')')
    print('Choose Decade')
    decade_q = [
        inquirer.List('year',
                message="What decade do you want?",
                choices=decade_choices_q,),]
    decades = inquirer.prompt(decade_q)
    
    if decades['year'].split(' ')[0]=='any':
        pass
    else:
        new_choices=new_choices[new_choices['Year']>=int(decades['year'].split(' ')[0])]
        new_choices=new_choices[new_choices['Year']<=int(decades['year'].split(' ')[0])+10]



    if new_choices.shape[0]<5:
        return print(new_choices.head())
    else:
        return print(new_choices.sample(5))


    