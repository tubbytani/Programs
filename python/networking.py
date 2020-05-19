import requests as req
url="https://lipsum.com/"
r=req.get(url)
content=r.text
lowerlim=content.index('<p>')
upperlim=content.index('</p>')
print(content[lowerlim+4:upperlim]) #shifts 4 letters in the content from lowerlimit 
