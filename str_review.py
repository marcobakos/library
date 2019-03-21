highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
#
print(highlighted_poems)
#
highlighted_poems_list = highlighted_poems.split(',')
#
print(highlighted_poems_list)
#
highlighted_poems_stripped = []
for poema in highlighted_poems_list:
    highlighted_poems_stripped.append(poema.strip())

#
print(highlighted_poems_stripped)
#
highlighted_poems_details = []
#
for poema in highlighted_poems_stripped:
    highlighted_poems_details.append(poema + '\n')
#
highlighted_poems_details = []
#
for poema in highlighted_poems_stripped:
    highlighted_poems_details.append(poema.split(':'))
#
print(highlighted_poems_details)
#
titles = []
poets = []
dates = []
#
for poema in highlighted_poems_details:
    titles.append(poema[0])
    poets.append(poema[1])
    dates.append(poema[2])
#
for poema in highlighted_poems_details:
    print('The poem {poem} was published by {poet} in {date}.'.format(poem=poema[0], poet=poema[1], date=poema[2]))

