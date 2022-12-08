

          
def recursive_bsearch(list, element):
    
    first = 0
    last = len(list)-1 
    mid = (first+last)//2
    found = False

    if len(list) == 0:
        return False

    else:
        if list[mid] == element:
            found = True
            return found
        else: 
            if element < list[mid]:
                x = slice(0, mid)
                recursive_bsearch(list[x],element)
            else:
                x = slice(mid,len(list))
                recursive_bsearch(list[x], element)
    
    return found

    

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(recursive_bsearch(test_list, 12))
      