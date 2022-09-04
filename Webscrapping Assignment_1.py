#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


page


# In[5]:


bs = BeautifulSoup(page.content)
bs


# In[34]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
 
 
# Downloading imdb top 100 movie's data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]
  
 
# create a empty list for storing
# movie information
list = []
 
# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
     
    # Separating movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
    list.append(data)
 
# printing movie details with its rating.
for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year']+')', movie['rating'])
 
 
##.......##
df = pd.DataFrame(list)


# In[7]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
 
 
# Downloading imdb top 100 Indian movie's data
url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]
 
  
# create a empty list for storing
# movie information
list = []
 
# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
     
    # Separating movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
    list.append(data)
 
# printing movie details with its rating.
for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
        ') -', 'Starring:', movie['star_cast'], movie['rating'])
 
 
##.......##
df = pd.DataFrame(list)


# In[9]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
 
 
# Downloading Presidents list data
url = 'https://presidentofindia.nic.in/former-presidents.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


# In[10]:


url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
page5 = requests.get(url)
# see content in page5
soup5 = BeautifulSoup(page5.content)
#scrape team names
team = soup5.find_all("span",class_='u-hide-phablet')
team_name = []
for i in team:
    team_name.append(i.text)
matches = [] #empty list
points = [] #empty list
ratings = [] #empty list
new_list = [] #empty list

for i in soup5.find_all("td",class_='rankings-block__banner--matches'): # first place team number of matches
    matches.append(i.text)
for i in soup5.find_all("td",class_='rankings-block__banner--points'):# first place team points
    points.append(i.text)
for i in soup5.find_all("td",class_='rankings-block__banner--rating u-text-right'):# first place team ratings
    ratings.append(i.text.replace("\n",""))
for i in soup5.find_all("td",class_='table-body__cell u-center-text'):# other teams number of matches and points
    new_list.append(i.text)
for i in range(0,len(new_list)-1,2):
    matches.append(new_list[i]) # other teams matches
    points.append(new_list[i+1]) # other teams points
for i in soup5.find_all("td",class_='table-body__cell u-text-right rating'):# other teams ratings
    ratings.append(i.text)
    
# Make data frame of top 10 ICC teams
icc=pd.DataFrame({})
icc['Team_name']=team_name[:10]
icc['Matches']=matches[:10]
icc['Points']=points[:10]
icc['Ratings']=ratings[:10]
icc    


# In[11]:


#send get request to the webpage server to get the source code of the page
url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
page6 = requests.get(url)
# see content in page6
soup6 = BeautifulSoup(page6.content)
players = [] #empty list
team_name = [] #empty list
rating = [] #empty list

for i in soup6.find_all("div",class_='rankings-block__banner--name-large'): # first place player name
    players.append(i.text)
for i in soup6.find_all("div",class_='rankings-block__banner--nationality'): # first place player team name
    team_name.append(i.text.replace("\n",""))
for i in soup6.find_all("div",class_='rankings-block__banner--rating'): # first place player rating
    rating.append(i.text)
for i in soup6.find_all("td",class_='table-body__cell rankings-table__name name'):# players name
    for j in i.find_all('a'):
        players.append(j.text)
for i in soup6.find_all("span",class_='table-body__logo-text'): # players team name
    team_name.append(i.text)
for i in soup6.find_all("td",class_='table-body__cell rating'): # players rating
    rating.append(i.text)
# Make data frame of top 10 ICC Batsmen
Batsmen=pd.DataFrame({})
Batsmen['Player']=players[:10]
Batsmen['Team']=team_name[:10]
Batsmen['Rating']=rating[:10]
Batsmen


# In[12]:


#send get request to the webpage server to get the source code of the page
url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
page7 = requests.get(url)

# see content in page7
soup7 = BeautifulSoup(page7.content)

players = [] #empty list
team_name = [] #empty list  
rating = [] #empty list 

for i in soup7.find_all("div",class_='rankings-block__banner--name-large'): # first place player name
    players.append(i.text)
for i in soup7.find_all("div",class_='rankings-block__banner--nationality'): # first place player team name
    team_name.append(i.text.replace("\n",""))
for i in soup7.find_all("div",class_='rankings-block__banner--rating'): # first place player rating
    rating.append(i.text)
for i in soup7.find_all("td",class_='table-body__cell rankings-table__name name'):# players name
    for j in i.find_all('a'):
        players.append(j.text)
for i in soup7.find_all("span",class_='table-body__logo-text'): # players team name
    team_name.append(i.text)
for i in soup7.find_all("td",class_='table-body__cell rating'): # players rating
    rating.append(i.text)
# Make data frame of top 10 ICC bowlers
bowlers=pd.DataFrame({})
bowlers['Player']=players[:10]
bowlers['Team']=team_name[:10]
bowlers['Rating']=rating[:10]
bowlers


# In[13]:


#send get request to the webpage server to get the source code of the page
url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
page8 = requests.get(url)
#see content in page8
soup8 = BeautifulSoup(page8.content)
#scrape team names
womens_team = soup8.find_all("span",class_='u-hide-phablet')
womens_team_name = []
for i in womens_team:
    womens_team_name.append(i.text)
womens_matches = [] #empty list
womens_points = [] #empty list
womens_ratings = [] #empty list
womens_new_list = [] #empty list
for i in soup8.find_all("td",class_='rankings-block__banner--matches'): # first place team number of matches
    womens_matches.append(i.text)
for i in soup8.find_all("td",class_='rankings-block__banner--points'):# first place team points
    womens_points.append(i.text)
for i in soup8.find_all("td",class_='rankings-block__banner--rating u-text-right'):# first place team ratings
    womens_ratings.append(i.text.replace("\n",""))
for i in soup8.find_all("td",class_='table-body__cell u-center-text'):# other teams number of matches and points
    womens_new_list.append(i.text)
for i in range(0,len(womens_new_list)-1,2):
    womens_matches.append(womens_new_list[i]) # other teams matches
    womens_points.append(womens_new_list[i+1]) # other teams points
for i in soup8.find_all("td",class_='table-body__cell u-text-right rating'):# other teams number of matches and ratings
    womens_ratings.append(i.text)
# Make data frame of top 10 ICC teams
womens_icc=pd.DataFrame({})
womens_icc['Team_name']=womens_team_name[:10]
womens_icc['Matches']=womens_matches[:10]
womens_icc['Points']=womens_points[:10]
womens_icc['Ratings']=womens_ratings[:10]
womens_icc    


# In[14]:


#send get request to the webpage server to get the source code of the page
url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"
page9 = requests.get(url)
# see content in page9
soup9 = BeautifulSoup(page9.content)
players = [] #empty list
team_name = [] #empty list
rating = [] #empty list

for i in soup9.find_all("div",class_='rankings-block__banner--name-large'): # first place player name
    players.append(i.text)
for i in soup9.find_all("div",class_='rankings-block__banner--nationality'): # first place player team name
    team_name.append(i.text.replace("\n",""))
for i in soup9.find_all("div",class_='rankings-block__banner--rating'): # first place player rating
    rating.append(i.text)
for i in soup9.find_all("td",class_='table-body__cell rankings-table__name name'):# players name
    for j in i.find_all('a'):
        players.append(j.text)
for i in soup9.find_all("span",class_='table-body__logo-text'): # players team name
    team_name.append(i.text)
for i in soup9.find_all("td",class_='table-body__cell rating'): # players rating
    rating.append(i.text)
# Make data frame of top 10 Women's ODI Batting Rankings
top_players=pd.DataFrame({})
top_players['Player']=players[:10]
top_players['Team']=team_name[:10]
top_players['Rating']=rating[:10]
top_players


# In[46]:



#Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)_

import requests
from bs4 import BeautifulSoup

url='https://presidentofindia.nic.in/former-presidents.htm'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
Prsidents = soup.find('body').find_all('h3')
Terms = soup.find('body').find_all('P')
for x in headlines:
    print(x.text.strip())


# In[49]:


# Importing Libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

#send get request to the webpage server to get the source code of the page
page = requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
# page content
soup=BeautifulSoup(page.content)

name=[]
for i in soup.find_all("div", class_="restnt-info cursor"):
    name.append(i.text)
location=[]
for i in soup.find_all("div", class_="restnt-loc ellipsis"):
    location.append(i.text)

price = []
cuisine = []
for i in soup.find_all("span", class_="double-line-ellipsis"):
    price.append(i.text.split('|')[0])
    cuisine.append(i.text.split('|')[1])

rating=[]
for i in soup.find_all("div", class_="restnt-rating rating-3"):
    rating.append(i.text)
for i in soup.find_all("div", class_="restnt-rating rating-4"):
    rating.append(i.text)

images = []
for i in soup.find_all("img", class_="no-img"):
    images.append(i['data-src'])
print(len(name), len(location), len(price), len(cuisine), len(rating), len(images))

# Make data frame
DineOut=pd.DataFrame({})
DineOut['Restaurant Name']=name
DineOut['Location']=location
DineOut['Price']=price 
DineOut['Cuisine']=cuisine  
DineOut['Rating']=rating  
DineOut['IMAGES']=images
DineOut


# In[50]:


#Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)_

import requests
from bs4 import BeautifulSoup

url='https://scholar.google.com/citations?view_op=top_venues&hl=en'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
Prsidents = soup.find('body').find_all('h3')
for x in headlines:
    print(x.text.strip())


# In[68]:


from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=web+scraping&btnG='
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')
#print(soup.select('[data-lid]'))
for item in soup.select('[data-lid]'):
	try:
		print('----------------------------------------')
		print(item)
		
	except Exception as e:
		#raise e
		print('')


# In[ ]:




