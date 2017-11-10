#!/home/styx97/miniconda3/bin/python


import requests,urllib
import os,sys,re,zipfile,shutil,io
from bs4 import BeautifulSoup
cwd = os.getcwd()
#print(cwd)  get the current working directory 


movie_name = [s.lower() for s in re.split("[^a-zA-Z]",input("enter the movie name \n"))]
movie_name = list(filter(lambda a: a != '', movie_name))
m1 = '-'.join(map(str,movie_name))
#print(m1)
print("you have searched for \n",m1)


r = requests.get("https://subscene.com/subtitles/" + m1 + "/english")
#print(r.url)
soup = BeautifulSoup(r.content,"lxml")
#print(len(soup))
#print(soup)



# case where year is require (eg zero dark thirty)
if len(soup) == 0 :
    print("Movie not found in Subscene")
    print("Enter the year of release")
    release = input()
    print("including year of release in search parameters...")
    m2 = m1 + '-' + release
    r = requests.get("https://subscene.com/subtitles/" + m2 + "/english")
    soup = BeautifulSoup(r.content,"lxml")
    if len(soup) > 0:
        print("success! :)")
    else:
        print("Failed   :(")
else:
    print("Success!  :) ")
    m2 = m1
atags = soup.find_all('a')
href= ""
options_array = []
#print(atags)

# find all html download tags and put them in options_array
for i in range(0,len(atags)):
    spans=atags[i].find_all("span")
    if(len(spans)==2 and spans[0].get_text().strip()=="English"):
        #print(spans)
        href=atags[i].get("href").strip()  
        if len(options_array) <= 10:
            options_array.append(href)
        else: 
            break 
#see if the options array is actually filled or not    
try :
    choice = options_array[0]  # Set the first link by default
except IndexError:
    print("Subtitles found in Subscene") #eta oi memento r case e hobe


# download that link
r1 = requests.get("http://subscene.com" + choice)
soup = BeautifulSoup(r1.content,"lxml")
download = soup.find_all('a',attrs={'id':'downloadButton'})[0].get("href")
#print(download)
r2 = requests.get("http://subscene.com" + download)
download_link = r2.url
#print(r2.encoding)
#print(file_path) 


f = requests.get(download_link)
zipped = zipfile.ZipFile(io.BytesIO(f.content))
zipped.extractall()

print("subtitles downloaded succesfully")
