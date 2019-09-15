import requests 
import pandas
from bs4 import BeautifulSoup
import os
import re

links=[]
with requests.Session() as s:
    r = s.get('https://www.geeksforgeeks.org/gate-cs-notes-gq/')
    soup = BeautifulSoup(r.content,'lxml')
    tr = soup.findAll('tr')[1:]
    i=1
    for t in tr:
        print("for i = ",i )
        
        sectionname = t.contents[1].contents[1].text.replace(':','_').strip()
        tempheading = t.contents[3].contents[1].contents
        os.chdir('E:\\GATE\\gate_notes\\')
        os.mkdir(sectionname)
        os.chdir(sectionname)
        for li in range(1,len(tempheading),2):
            sectionheading = str(i)+'-'+t.contents[3].contents[1].contents[li].contents[0].text.replace(':','').strip().replace('/','')
            print(sectionheading)
            
            os.mkdir(sectionheading)
            links =[]
            print(t.contents[3].contents[1].contents[li].contents[2].contents  )
            templinks = t.contents[3].contents[1].contents[li].contents[2].contents
            for tl in range(1,len(templinks),2):
                data ={}
                
                try :
                    data["linkname"] = templinks[tl].a.text
                    data["link"] = templinks[tl].a['href']

                except Exception as e:
                    print('exceptoo in phone',e)
                    data["linkname"] = templinks[tl+1].a.text
                    data["link"] = templinks[tl+1].a['href']
                links.append(data)
            print(sectionheading)
            print(links)
#             os.chdir('E:\\GATE\\gate_notes\\'+sectionname+'\\'+sectionheading)
            file_location = 'E:\\GATE\\gate_notes\\'+sectionname+'\\'+sectionheading+'\\linkfile.csv'
            df =pandas.DataFrame(links)
            df.to_csv(file_location,mode ='a')
            i=i+1

