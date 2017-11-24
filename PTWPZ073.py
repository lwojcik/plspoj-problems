n = input()

while n:
    a = raw_input()
    b = ""
    for x in a:
        
        if x=="A" or x=="B" or x=="C":
            b=b+"2"
            
        elif x=="D" or x=="E" or x=="F":
            b=b+"3"
            
        elif x=="G" or x=="H" or x=="I":
            b=b+"4"
            
        elif x=="J" or x=="K" or x=="L":
            b=b+"5"
            
        elif x=="M" or x=="N" or x=="O":
            b=b+"6"
            
        elif x=="P" or x=="Q" or x=="R" or x=="S":
            b=b+"7"

        elif x=="T" or x=="U" or x=="V":
            b=b+"8"

        elif x=="W" or x=="X" or x=="Y" or x=="Z":
            b=b+"9"

    print b
    n-=1
