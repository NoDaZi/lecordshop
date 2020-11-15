'''
Created on 2019. 12. 4.

@author: KMU_USER
'''


from writetxt import write
from readtxt import read
w=write()

#This is main Class
def main():
    
    
    select=1
    
    
    print("* * * Welcome To The Album Store!!! * * * ")
    #We Can Select menu
    while select != 0:
        print("\n 1.List of Album\n","2.Modify Album\n","3.Search Album\n","0.EXIT")
        select =int( input("\n please select contents: "))
        if select == 1 :
            r=read()
            r.list()
          
        elif select ==2 :
            print("\n 1.Add Album\n","2.Modify Album\n","3.Delete Album\n","0.BacK")
            inselect =int(input("\n please select contents: "))
            if inselect ==1 :
                w.addAlbum()    
            elif inselect ==2 :
                w.modifyAlbum()
            elif inselect == 3:
                w.deleteAlbum()
            
          
        elif select ==3 :
            r=read()
            print("\n 1.Search With Singer\n","2.Search With Genre\n","0.BacK")
            inselect =int(input("\n please select contents: "))
            if inselect ==1 :
                r.searchwithSingername()    
            elif inselect ==2 :
                r.searchwithgenre()
            

main()