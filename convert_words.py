words = open('words.txt').read().splitlines()
usedWords = []
def GetSimilarWords(word):
    similar = []
    for currWord in words:       
        if len(word) != len(currWord):
            continue
        if GetMatchingCount(word,currWord) == len(word)-1:
            similar.append(currWord)
    return similar   
   
def GetMatchingCount(a,b):    
    count = 0
    for i in range(0,len(a)):        
        if a[i] == b[i]:
            count += 1
    return count
        
  
    
def sort(word, arr):
    for j in range(1,len(arr)):
        for i in range(0,len(arr)-j):
            if (GetMatchingCount(arr[i],word)<GetMatchingCount(arr[i+1], word)):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

    
def is_route(origin, dest):
    print  origin + ' ' + dest
    usedWords.append(origin)
    if origin not in words:
        return False
    destCities = GetSimilarWords(origin)
    destCities = sort(dest, destCities)
    if dest in destCities:
        return (True,[dest])
    else:
        for city in destCities:                    
            if (city not in usedWords):                
                res = is_route(city, dest)
                if (not res):
                    continue
                if (res[0]):
                    res[1].append(city)
                    return (True,res[1])
        return False
				

print is_route('train', 'plane')