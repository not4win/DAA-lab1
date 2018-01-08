class Stablematching:
    def __init__(self,n):
        self.size=n
        self.male=[i for i in range(n)]
        self.female=[i for i in range(n)]
        self.prefmale=[[0 for i in range(n)]for i in range(n)]
        self.preffemale=[[0 for i in range(n)]for i in range(n)]
        self.freemale=[i for i in range(n)]
        self.engfemale=[False for i in range(n)]
        self.engfemaleto=[-1 for i in range(n)]
        self.maleno=[0 for i in range(n)]
    def insertprefmale(self,mn,b):
        size=self.size
        for i in range(size):
            self.prefmale[mn][i]=b[i]
    def insertpreffemale(self,fn,b):
        size=self.size
        for i in range(size):
            self.preffemale[fn][i]=b[i]
    def Matching(self):
        while(len(self.freemale)!=0):
            z=1
            fm=self.freemale.pop(0)
            for i in range(self.maleno[fm],self.size):
                if z==1:
                    y=self.prefmale[fm][i]
                    if self.engfemale[y]==False:
                        self.engfemale[y]=True
                        self.engfemaleto[y]=fm
                        self.maleno[fm]=y
                        #print(fm,y)
                        break
                    if self.engfemale[y]==True:
                        #print("XXX")
                        engaged_male=self.engfemaleto[y]
                        for i in range(self.size):
                            if self.preffemale[y][i]==engaged_male :
                                break
                            if self.preffemale[y][i]==fm :
                                self.maleno[engaged_male]=-1
                                self.freemale.append(engaged_male)
                                #print('x',self.freemale)
                                self.engfemaleto[y]=fm
                                self.maleno[fm]=y
                                z=0
                                #print(fm,y)
                                break
                        









y=Stablematching(5)
y.insertprefmale(0,[1,0,3,4,2])
y.insertprefmale(1,[3,1,0,2,4])
y.insertprefmale(2,[1,4,2,3,0])
y.insertprefmale(3,[0,3,2,1,4])
y.insertprefmale(4,[1,3,0,4,2])
y.insertpreffemale(0,[4,0,1,3,2])
y.insertpreffemale(1,[2,1,3,0,4])
y.insertpreffemale(2,[1,2,3,4,0])
y.insertpreffemale(3,[0,4,3,2,1])
y.insertpreffemale(2,[3,1,4,2,0])
print(y.prefmale)
print(y.preffemale)
y.Matching()
print(y.maleno)

