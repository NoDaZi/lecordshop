'''
Created on 2019. 12. 4.

@author: KMU_USER
'''
from readtxt import read


r=read()

class write : 

    def modifyAlbum(self):
        print(r.bar)
        albumname = input("\nPlease enter Album's Name Want To Modify : ")
        modifyed = 0
        
        for num in r.index :
            if albumname.upper() == num[0].upper() :
                modifyAlbumname = input("Enter the New Album Name: ")
                modifyAlbuumsinger = input("Enter the New Album Singer: ")
                modifyAlbumgenre = input("Enter the New Album Genre: ")
                num[0]=modifyAlbumname
                num[1]=modifyAlbuumsinger
                num[2]=modifyAlbumgenre.upper()
                modifyed=1
                
        print(r.bar)
        if modifyed == 1 :
            print("\nSuccessfully Modified!!!")
        else :
            print("\nSorry!i Can't Find Album has that name!!!\n")
        
        self.save()
        
    def deleteAlbum(self):
        print(r.bar)
        albumname=input("please enter AlbumName:")
        delete=0
        deleted=0
        for num in r.index:
            if albumname.upper()==num[0].upper() :
                deleted= r.index.index(num)
                delete = 1
        
        if delete ==1:
            del r.index[deleted]
            print("\nSuccessfully deleted!!")
        else :
            print("\nThere are no Album has name as",albumname)
        
        self.save()
            
        
    def addAlbum(self):
        
        print(r.bar)
        albumname=input("please enter AlbumName:")
        signername=input("please enter Singer:")
        genre=input("please enter genre:")
        r.index.append([albumname,signername,genre.upper(),str(1)])
        self.save()
        print(r.bar+"\n")
        print(" Completion of Adding !!")
         
        
        
    def save(self):
        outputFileName="albumlist.txt"
        outputFile = open(outputFileName,"w")
        r.index.sort()
        
        for j in r.setGenre :
            albumnumber = 1
            for num in r.index : 
                if num[2]==j :
                    num[3]= albumnumber
                    albumnumber =albumnumber+1
        
        for num in r.index :
            outputFile.write(num[0]+" : "+num[1]+" : "+num[2].upper()+" : "+str(num[3])+"\n")
            
        outputFile.close()