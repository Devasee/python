# //find operation
s ="I am Indian"
found = s.find("di")
print(found)

# //creating the function for the find operation
def myFind(st, ch):
    index = 0
    while index <= len(st) - 1:
        if st[index] == ch:
            return index
        index = index + 1

    return -1

# Test the function
print(myFind("hello", "e")) 
print(myFind("hello", "x"))  



