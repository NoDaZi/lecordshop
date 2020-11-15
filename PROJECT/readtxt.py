'''
Created on 2019. 12. 4.

@author: KMU_USER
'''

#readtxt class read Data from txt file and have search fuctions. 


class read :
    bar = "=================="
    
    
    #first read txt file when we call read class ,
    def __init__(self):
        self.index=[]
        inputFileName = "albumlist.txt" #filename
        inputFile = open(inputFileName, "r")
        self.setGenre=set()
        for line in inputFile : # Save Data in List   
            if ":" in line :
                parts = line.split(" : ")
                self.index.append([parts[0],parts[1],parts[2].upper(),parts[3]])
                self.index.sort()
                self.setGenre.add(parts[2].upper())
                        
        inputFile.close()

    def list(self):
        
        print("\n"+self.bar+"List Of Albums"+self.bar)
        for num in self.index :
            print(num[0]," - ",num[1])
        print(self.bar*3+"\n")
        
    def searchwithSingername(self):
        searchSingername = input("Enter the Singer:")
        print("\n"+self.bar+"Album of "+searchSingername.upper()+self.bar)
        count=0
        for num in self.index :   
            if searchSingername.upper() == num[1].upper() :
                print(num[0])
                count=count+1
        print(self.bar*2)            
     
        if count ==0 :
            print("Sorry! We Don't Have Album with That SingerName.\n")  
        else :
            print("There are ",count ," Album(s)")      
        
    def searchwithgenre(self):
        count=0
        print(self.bar+"We Have Those Genres"+self.bar+"\n")
        print(' / ',end='')
        for num in self.setGenre :
            print(num,end=' / ')
        print("\n\n"+self.bar*2+"====================")
        searchgenre = input("\n\n Enter the genre :")
       
        if self.setGenre.intersection([searchgenre.upper()])==set() :
            print("We Don't Have That Genre! ! !")
        else :
            print("\n"+self.bar+"Albums of "+searchgenre.upper()+self.bar)
            for num in self.index :   
                if searchgenre.upper() == num[2].upper() :
                    print(num[1]+" - "+num[0])
                    count =count+1
            print(self.bar*2+"====================") 
            print("There are ",count ," Album(s)")
        
        
    
        