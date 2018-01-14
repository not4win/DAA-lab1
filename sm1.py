class Stablematching:
    def __init__(self,n):
        self.size=n
        self.male=[i for i in range(n)]
        self.female=[i for i in range(n)]
        self.prefmale=[[0 for i in range(n)]for i in range(n)]
        self.preffemale=[[0 for i in range(n)]for i in range(n)]
        self.prefmalex=[[0 for i in range(n)]for i in range(n)]
        self.preffemalex=[[0 for i in range(n)]for i in range(n)]
        self.freemale=[i for i in range(n)]
        self.engfemale=[False for i in range(n)]
        self.engfemaleto=[-1 for i in range(n)]
        self.maleno=[0 for i in range(n)]
        
    def insertprefmale(self,mn,b):
        size=self.size
        for i in range(size):
            self.prefmale[mn][i]=b[i]
            self.prefmalex[mn][b[i]]=i

    def insertpreffemale(self,fn,b):
        size=self.size
        for i in range(size):
            self.preffemale[fn][i]=b[i]
            self.preffemalex[fn][b[i]]=i
                                    
    def Matching(self):
        count=0
        while(len(self.freemale)!=0):
            fm=self.freemale.pop(0)
            for i in range(self.maleno[fm],self.size):
                count=count+1
                y=self.prefmale[fm][i]
                if self.engfemale[y]==False:
                    self.engfemale[y]=True
                    self.engfemaleto[y]=fm
                    self.maleno[fm]=i+1
                    break
                if self.engfemale[y]==True:
                    engaged_male=self.engfemaleto[y]
                    if self.preffemalex[y][engaged_male]<self.preffemalex[y][fm]:
                        xyz=1
                    else:
                        self.maleno[fm]=i+1
                        self.freemale.append(engaged_male)
                        self.engfemaleto[y]=fm
                        break
        print(count)
y=Stablematching(8)
y.insertprefmale(0,[4,6,0,1,5,7,3,2])
y.insertprefmale(1,[1,2,6,4,3,0,7,5])
y.insertprefmale(2,[7,4,0,3,5,1,2,6])
y.insertprefmale(3,[2,1,6,3,0,5,7,4])
y.insertprefmale(4,[6,1,4,0,2,5,7,3])
y.insertprefmale(5,[0,5,6,4,7,3,1,2])
y.insertprefmale(6,[1,4,6,5,2,3,7,0])
y.insertprefmale(7,[2,7,3,4,6,1,5,0])
y.insertpreffemale(0,[4,2,6,5,0,1,7,3])
y.insertpreffemale(1,[7,5,2,4,6,1,0,3])
y.insertpreffemale(2,[0,4,5,1,3,7,6,2])
y.insertpreffemale(3,[7,6,2,1,3,0,4,5])
y.insertpreffemale(4,[5,3,6,2,7,0,1,4])
y.insertpreffemale(5,[1,7,4,2,3,5,6,0])
y.insertpreffemale(6,[6,4,1,0,7,5,3,2])
y.insertpreffemale(7,[6,3,0,4,1,2,5,7])
y.Matching()
for i in range(8):
    print(y.engfemaleto[i],i)

