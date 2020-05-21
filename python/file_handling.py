text=open("temp_monitor.txt",'r')
print(text.read())
text.seek(0,0)
for i in text:
    print(i)
text.close()    
