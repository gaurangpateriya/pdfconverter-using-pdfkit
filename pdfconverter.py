import pdfkit  
import requests 
import pandas
from bs4 import BeautifulSoup
import os
import re

# 'Section 3_ Algorithms', 'Section 5_ Operating Systems','Section 7_ Computer Networks',
sections = [ 'Section 1_ Numerical and Verbal Ability', 'Section 2_ Mathematics', 'Section 3_ Algorithms', 'Section 4_ Programming and Data Structures', 'Section 5_ Operating Systems', 'Section 6_ Databases', 'Section 7_ Computer Networks', 'Section 8_ Computer Organization and Architecture', 'Section 9_ Theory of Computation','Section 10_ Compiler Design', 'Section 11_ Digital Logic',]
for s in sections:
    os.chdir(s)
    headings = os.listdir()
    for h in headings:
        os.chdir(h)
        
        data= pandas.read_csv('linkfile.csv',)
        data = data.values
        link = data
        i=1
        for l in link :
            
            out = str(i)+'-'+l[2].replace('|','').replace('/','').replace('"','')+'.pdf'
            li = l[1]
            print() 
            print('section = ',s)
            print()
            pdfkit.from_url(l[1],out) 
    
            print(out)                      
            i+=1
        os.chdir('..')
        
    
    os.chdir('..')


# pdfkit.from_url('https://www.geeksforgeeks.org/placements-gq/','output.pdf') ~