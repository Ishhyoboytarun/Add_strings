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

def add(numbers):
    #base condition
    if numbers == "": return 0

    delimiters = set()
    delimiters.add(",")
    start_index = 0

    
    #setting delimiter and starting index
    if numbers[0][0:2]=="//":
        if numbers[0][2]!="[":
            delimiters = numbers[0][2:]
        else:
            delimiters = findDelimiters(numbers[0][2:])

        start_index = 1
        
        
    #finding sum of the numbers
    sum = 0
    negatives = []
    for i in range(start_index,len(numbers)):
        num = ""
        j = 0
        while j<len(numbers[i]):  
            #checking if it is an integer
            if numbers[i][j] in ['1','2','3','4','5','6','7','8','9','0','-']:
                num+= numbers[i][j]
                
            else:        
                #extracting the delimiter from the given string
                k = j+1
                while k<len(numbers[i]) and numbers[i][k] not in ['1','2','3','4','5','6','7','8','9','0','-']:
                    k+=1

                #invalid delimiter(s)
                if numbers[i][j:k] not in delimiters: raise Exception("invalid delimiter(s) found",numbers[i][j:k])
                    
                j = k-1
                if num=="": continue

                #if num is negative
                if int(num)<0: negatives.append(int(num))

                #if num is positive
                sum+=int(num) if int(num)<1001 else 0

                #initializing num
                num = ""
            j+=1
       
        #if num is negative
        if int(num)<0: negatives.append(int(num))

        #if num is positive
        sum+=int(num) if int(num)<1001 else 0


    #checking negative numbers
    if negatives:
        raise Exception("negatives not allowed",negatives)

    return sum 

            
if __name__ == "__main__":
    #taking infinite input
    numbers = []
    while 1:
        num = input()
        if num is "": break
        numbers.append(num)
    print(add(numbers))
