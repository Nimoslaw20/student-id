FINDperson = {2015}
def SCHOOLREP():
    K = input("Enter Password:")
    K = int(K)
    print ("YOU ARE WELCOME. THESE ARE THE SCHOOL REPS IN THE VARSITY GAMES")

SCHOOLREP()



def RegSys(alist):  # make a list of numbers 
    a=str(alist)
    b=a.split(',')
    c=len(b)
    for i in range(0,c-1):
        k=b[i]
        k[-1]
        l=int(k[-1])      # last number of the item
        k[1]
        d=int(k[1])     # first  number of the item
        
        if l==0:        # if the last number of the item ends with 0, 
            if d%2==0:
                print('Ashesi','Male- RANDY NANA BOATENG')   # if the first number is even print Ashesi Male
            else:
                print('Ashesi','Female- DORA SALLY') #  if the first number is odd print Ashesi Female
                
             
            
        elif l==1:     # if the number ends with 1, 
            if d%2==0:
              print('Legon','Male- RON TERRY') # if the first number is even print Legon Male
            else:
                print('Legon','Female - ABENA ADU') # if the first number is odd print Legon Female

                
        elif l==2:       # if the last number of the item ends with 2
           if d%2==0:
              print('KNUST','Male - EMMANUEL NIMO')  # if the first number is even print KNUST Male
           else:
               print('KNUST','Female- SARA MENSAH') # if the first number is odd print KNUST Female
              
        elif l==3:
            if d%2==0:
               print('UCC','Male - ANDY COLE')
            else:
                print('UCC','Female - STEPHANIE APPIAH')
                
        elif l==4:
            if d%2==0:
               print('UMAT','Male - KWAKU MANU ')
            else:
               print('UCC','Female- CINDY AKUA')
               
        elif l==5:
            if d%2==0:
               print('UDS','Male - AKWASI FRIMPONG')
            else:
                print('UDS','Female - YAA SARPOMAA')
                
        elif l==6:
            if d%2==0:
               print('UHAS','Male - KWADWO AINOO')
            else:
                print('UHAS','Female - GRACE SALLAR')
                
        elif l==7:
            if d%2==0:
               print('Accra Poly','Male - CARL VANS')
            else:
                print('Accra Poly','Female - ANITA AGARO')
        elif l==8:
            if d%2==0:
               print('KPOly','Male- LOUIS OSEI OWUSU')
            else:
                print('KPoly','Female - AFIA BOATEMAA')
        elif l==9:
            if d%2==0:
               print('Central University','Male- HARUNA ATTA')
            else:
               print('Central University','Female - VICENTIA AMA')
    
    lastch=b[-1]
    number=lastch[-2]
    y=int(number)
    if y==0:
        if d%2==0:
            print('Ashesi','Male- RANDY NANA BOATENG')
        else:
            print('Ashesi','Female- DORA SALLY')
            
    elif y==1:
        if d%2==0:
           print('Legon','Male- RON TERRY')
        else:
         print('Legon','Female-  ABENA ADU')
         
    elif y==2:
        if d%2==0:
            print('KNUST','Male- EMMANUEL NIMO')
        else:
             print('KNUST','Female- SARA MENSAH')
    elif y==3:
        if d%2==0:
            print('UCC','Male- ANDY COLE')
        else:
            print('UCC','Female- STEPHANIE APPIAH')
    elif y==4:
        if d%2==0:
            print('UMAT','Male- KAWKU MANU')
        else:
            print('UMAT','Female- CINDY AKUA')
    elif y==5:
        if d%2==0:
            print('UDS','Male- AKWASI FRIMPONG')
        else:
               print('UDS','Female- YAA SARPOMAA')
    elif y==6:
        if d%2==0:
            print('UHAS','Male- KWADWO AINOO')
        else:
               print('UHAS','Female- GRACE SALLAR')
    elif y==7:
        if d%2==0:
            print('Accra Poly','Male- CARLS VANS')
        else:
               print('Accra Poly','Female- ANITA AGARO')
    elif y==8:
        if d%2==0:
            print('KPOly','Male- LOUIS OSEI OWUSU ')
        else:
            print('KPoly','Female- AFIA BOATEMAA')
    elif y==9:
        if d%2==0:
            print('Central University','Male- HARUNA ATTA ')
        else:
            print('Central University','Female - VICENTIA AMA ')
RegSys([36,13,91,90,46,67,35,63,18,99])        
print("THE FOLLWOING ARE THE HALLS AND CLASSES OF THE VARIOUS SCHOOL REP")
    
def HALL(alist):       
    a=str(alist)
    b=a.split(',')
    c=len(b)
    for i in range(0,c-1):
        k=b[i]
        k[-1]
        l=int(k[-1])
        d = int(k[1])
        
     
        if (l + d) <= 2:    # if the sum of last and the first numbers is less than or equal to 2
            print('HALL A') # print HALL A

        elif (l + d) <=5:
            print('HALL B')

        elif (l + d) <= 8:
            print('HALL C')

        elif (l + d) <= 12:
            print('HALL D')

        elif (l + d) >= 13:
            print('HALL E')

    lastch=b[-1]
    number=lastch[-3]
    y=int(number)
    digit = lastch[-2]
    t = int(digit)
    
    if (y + t) <= 2:
        print('HALL A')

    elif (y + t) <=5:
        print('HALL B')

    elif (y + t) <= 8:
        print('HALL C')

    elif (y + t) <= 12:
        print('HALL D')

    elif (y + t) >= 13:
        print('HALL E')
       
HALL([36,13,91,90,46,67,35,63,18,99])      

def YearGroup(alist):       
    a=str(alist)
    b=a.split(',')
    c=len(b)
    for i in range(0,c-1):
        k=b[i]
        k[-1]
        l=int(k[-1])
        d = int(k[1])
        
     
        if (d - l) <= -3:
            print('CLASS OF 2016')

        elif (d - l) >= 1:
            print('CLASS OF 2017')

        elif (d - l) >= 3:
            print('CLASS OF 2018 ')

        elif (d - l) <= 0 :
            print('CLASS OF 2019')

         

    lastch=b[-1]
    number=lastch[-3]
    y=int(number)
    digit = lastch[-2]
    t = int(digit)
    
    if (y - t) <= -3:
        print('CLASS OF 2017')

    elif (y - t) >= 1:
        print('CLASS OF 2018')

    elif (y - t) <= 0:
        print('CLASS OF 2019')
            
YearGroup([36,13,91,90,46,67,35,63,18,99])                 
                  
            
        
        
    
