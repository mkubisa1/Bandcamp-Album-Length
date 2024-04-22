from bs4 import BeautifulSoup
import requests
import math

url = input("enter Bandcamp link to album: ")

soup = BeautifulSoup(requests.get(url).text, 'html5lib') # retrieve html from page
spans = soup.find_all('span',attrs={'class':'time secondaryText'})  # parse out all the spans which contain the track times

# summate lengths for all tracks converted into seconds
totalSec = 0
for i in spans:
    t = i.text.strip()
    t = t.split(":")
    totalSec += (int(t[0])*60 + int(t[1]))

# convert to appx. minutes and seconds; print result
print("Album length is ABOUT", math.floor(totalSec/60), "min", math.ceil(60 * (totalSec/60 - math.floor(totalSec/60))), "sec")
# print("Length in seconds =",totalSec)
input("Press enter to exit")