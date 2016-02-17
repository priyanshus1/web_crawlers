#! /usr/bin/python3

import requests
import os,sys
from bs4 import BeautifulSoup

#Download top 100 Songs from billboard
'''
fw = open('.songs.txt','w')
fr = open('.downloaded.txt','r')
downloaded = fr.read()
downloaded = downloaded.split('\n')
fr.close()
url1 = 'http://www.billboard.com/charts/hot-100'
sc = requests.get(url1)
soup1 = BeautifulSoup(sc.text,'lxml')
li = soup1.findAll('h2',{'class':'chart-row__song'})
art = soup1.findAll('h3',{'class':'chart-row__artist'})
for i in range(len(li)):
    fw.write(li[i].text+' '+art[i].find('a').text.strip()+'\n')
fw.close()

fr = open('.songs.txt','r')
songs = fr.read()
songs = songs.split('\n')
fa = open('.downloaded.txt','a')

for x in songs:
    for y in downloaded:
        if x == y:
            break
    else:
        url2 = 'https://www.youtube.com/results?search_query='+x
        sc =requests.get(url2)
        soup2 = BeautifulSoup(sc.text,'lxml')
        title = soup2.findAll('h3',{'class':'yt-lockup-title '})
        print ('Downloading...')
        os.system("youtube-dl --extract-audio --audio-format mp3 " + 'https://www.youtube.com'+title[0].find('a')['href'])
        print ('Downloaded.')
        fa.write(x+'\n')
print ('Download Complete')   
fr.close()
fa.close()
'''

#Download songs from the file song.txt

fr = open('.downloaded.txt','r')
downloaded = fr.read()
downloaded = downloaded.split('\n')
fr.close()
fr = open('song.txt','r')
songs = fr.read()
songs = songs.split('\n')
fa = open('.downloaded.txt','a')

for x in songs:
    for y in downloaded:
        if x == y:
            break
    else:
        url2 = 'https://www.youtube.com/results?search_query='+x
        sc =requests.get(url2)
        soup2 = BeautifulSoup(sc.text,'lxml')
        title = soup2.findAll('h3',{'class':'yt-lockup-title '})
        print ('Downloading...')
        os.system("youtube-dl --extract-audio --audio-format mp3 " + 'https://www.youtube.com'+title[0].find('a')['href'])
        print ('Downloaded.')
        fa.write(x+'\n')
print ('Download Complete')   
fr.close()
fa.close()


#Search and download songs
'''
fa = open('.downloaded.txt','a')
search = input('Enter the name of the song: ')
url = 'https://www.youtube.com/results?search_query='+search
sc =requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')
title = soup.findAll('h3',{'class':'yt-lockup-title '})
link = []
for i in range(min(10,len(title))):
    link.append(title[i].find('a')['href'])
for i in range(min(10,len(title))):
    print (str(i+1)+'. '+title[i].find('a').text)

while True:
    try:
        user_input = int(input('Enter the song no. to download: '))
        if user_input not in range(1,11):
            print ('Enter correct input')
            continue
        break
    except NameError:
        print ('Enter correct input')
        continue

print ('Downloading...')
os.system("youtube-dl --extract-audio --audio-format mp3 " + 'https://www.youtube.com'+link[user_input-1])
fa.write(search+'\n')
'''


