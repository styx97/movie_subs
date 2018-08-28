import requests,urllib
import os,sys,re,zipfile,shutil,io
from bs4 import BeautifulSoup
cwd = os.getcwd()


# taking the movie input 


movie_name = [s for s in re.split("[^0-9a-zA-Z]",input("enter the movie name : \n"))]
movie_name = list(filter(lambda a: a != '', movie_name))
m1 = ' '.join(map(str,movie_name))

encodings = []
while len(encodings) == 0:
	encodings = [s.lower() for s in re.split("[^0-9a-zA-Z]",input("enter the storage format (eg.720p,bluray,brrip,xvid,hdtv etc) (must) \n"))]
	if len(encodings) == 0 :
		print("You must enter some encoding format")
encodings = list(filter(lambda a: a != '', encodings))
m2 = ' '.join(map(str,encodings))
m1 = m1 + ' ' + m2

print("you have searched for \n",m1)


search_string = m1.split()
#search_string


''' Preparing the query '''

search_url = "https://subscene.com/subtitles/title?q="
search_url += search_string[0]
for words in search_string[1:]:
    search_url += ("+" +  words)
search_url += "&l="    
print(search_url)


r = requests.get(search_url)
soup = BeautifulSoup(r.content,"lxml")
#print(soup)

subs = soup.find_all("td", class_ = "a1") 
#print(subs)


for elements in range(len(subs)) :
    res = subs[elements].find_all("span", class_="l r positive-icon")
    s = str(res)
    m = re.search('English',s)
    if m :
        target = subs[elements]
        t = target.find("a")
        download_link = t['href']
        break
        

# download that link
r1 = requests.get("https://subscene.com" + download_link)
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

