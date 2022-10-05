import requests
from bs4 import BeautifulSoup
import csv
import json
HEADERS = ({'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                           'Accept-Language': 'en-US, en;q=0.5'})
with open("Amazon Scraping - Sheet1.csv") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    line=0

    mydict={}
    for row in csv_reader:
     if line!=5:
        #try:
            line+=1
            
            URL=f"https://www.amazon.de/dp/000104317X" 
            page=requests.get(URL,headers=HEADERS)
            soup=BeautifulSoup(page.content,"html.parser")
            title=soup.find("h1")
            mytitle=title.find('span',class_='a-size-extra-large')
            print(mytitle)
            mydict["title"]=mytitle
    
            myimg=soup.find('img' , class_='a-dynamic-image image-stretch-horizontal frontImage')
            
            mydict["imageUrl"]=myimg['src']

            
                
            mydict['price']=soup.find('span', class_="a-size-base a-color-price a-color-price").text
                
            print(soup.find('span', class_="a-size-base a-color-price a-color-price"))

            #mydict['price']=myprice.text
            
            mydetail=soup.find('ul',class_='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list')
            mydetailinfo=mydetail.find_all('li')
            for x in mydetailinfo:
                v=x.find('span')
                mydict["detail"]=v.text.replace(" ","")
                
        
        #except:
         #   print(URL + ' not availabel')


    
    json_object=json.dumps(mydict,indent=2)
    with open('info.json','w') as outfile:
        outfile.write(json_object)

            

        