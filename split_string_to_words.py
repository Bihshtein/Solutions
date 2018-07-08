content = open('words.txt').read().splitlines()


def split(_str):  
    if _str in content:                
        return _str        
    else: 
        for i in range(1,len(_str)):
            if _str[:i] in content:
                trySplit = split(_str[i:])                
                if (trySplit != ''):
                    return _str[:i] +' '+ trySplit                
        return ''
		
print split('hellosbellybuttonfood')

		
		
