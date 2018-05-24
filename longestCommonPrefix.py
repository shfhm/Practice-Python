

def strs(str):
    if not str:
        return""
    key=str[0] 
    len_key=len(key)
    for i in str:
        while key != i[0:len_key]:
            len_key-=1
            key=key[0:len_key]        
    return key

