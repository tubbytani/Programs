
class Myclass:
    _count=0
    def __init__(self):
        Myclass._count+=1
    def __del__(self):
        Myclass._count-=1
    @staticmethod
    def qty_objects():
        return Myclass._count
obj=[Myclass() for i in range(10)]
print(Myclass.qty_objects())
import time
for i in range(len(obj)):
    try:
        print(Myclass.qty_objects())
        del obj[i]
        t.sleep(5)
    except:
        break
        
