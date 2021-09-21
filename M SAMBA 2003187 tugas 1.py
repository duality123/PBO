"""Muhammad Samba Al Faraby L
   NIM 2003187
   SIKB 
"""

#Nomor 1
class gambarBangunDatar:
    def __init__(self,tinggiJajarGenjang,tinggiSegitiga):
        self.tinggiJajarGenjang = tinggiJajarGenjang
        self.tinggiSegitiga = tinggiSegitiga
    
    def gambarJajarGenjang(self):
        t = self.tinggiJajarGenjang
        i = 0
        a = ''
        while (i<t):
            j,u = t,0
            while(j>i):
                a += ' '
                j -= 1
            while(u<=i):
                a += '*'
                u += 1
            j = t-1
            while(j>i):
                a += '*'
                j -= 1
            a += '\n'
            i += 1
        print(a)
    
    def gambarSegitiga(self):
        t = self.tinggiSegitiga
        i = 0
        a = ''
        while (i<t):
            j,u = t,0
            while(j>i):
                a += '*'
                j -= 1
            a += '\n'
            i += 1
        print(a)
    
       

a = gambarBangunDatar(9,7)
a.gambarJajarGenjang()
a.gambarSegitiga()


#Nomor 2
class Kalkulasi:
    def __init__(self,aSegitiga,tSegitiga,pBalok,lBalok,tBalok):
        self.aSegitiga = aSegitiga
        self.tSegitiga= tSegitiga
        self.pBalok = pBalok
        self.lBalok = lBalok
        self.tBalok = tBalok

    def hitungLuasSegitiga(self):
        print((self.aSegitiga * self.tSegitiga)/2)
    
    def hitungVolumeBalok(self):
        print(self.pBalok * self.tBalok * self.lBalok)

b = Kalkulasi(3,4,5,6,7)

b.hitungLuasSegitiga()
b.hitungVolumeBalok()



class Segitiga:
    def __init__(self,aSegitiga,tSegitiga):
        self.aSegitiga = aSegitiga
        self.tSegitiga= tSegitiga

    def hitungLuasSegitiga(self):
        print((self.aSegitiga * self.tSegitiga)/2)
    

class Balok:
    def __init__(self,pBalok,lBalok,tBalok):
        self.pBalok = pBalok
        self.lBalok = lBalok
        self.tBalok = tBalok
    
    def hitungVolumeBalok(self):
        print(self.pBalok * self.tBalok * self.lBalok)


b = Segitiga(3,4)
c = Balok(5,6,8)

b.hitungLuasSegitiga()
c.hitungVolumeBalok()
