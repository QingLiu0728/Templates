from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

html = urlopen("http://cs231n.stanford.edu/syllabus.html")

bsObj = BeautifulSoup(html.read())
# print(bsObj.h1)

urlList = bsObj.findAll("a", href=True)
pdfList = []
nameList = []
for name in urlList:
    if name['href'].endswith('pdf') and name['href'].startswith('http'):
        pdfList.append(name['href'])
        nameList.append(name['href'].rsplit("/")[-1])

print(pdfList)

for url in pdfList:
    print(url)
    response = requests.get(url, stream=True)
    with open(url.rsplit("/")[-1],"wb") as pdf: 
        for chunk in response.iter_content(chunk_size=1024): 
         # writing one chunk at a time to pdf file 
            if chunk: 
                pdf.write(chunk)