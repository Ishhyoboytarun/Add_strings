def findDelimiters(x):
    #separating the total no. of delimiters given
    delimiters = set()
    i = 0    
    while i<len(x):
        delimiter=""
        if x[i]=='[':
            i+=1
            while x[i]!=']':
                delimiter+=x[i]
                i+=1
                
        delimiters.add(delimiter)
        i+=1
        
    return delimiters
