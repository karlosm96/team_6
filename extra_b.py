
def find_char(string):
    leters = {}
    
    new_string = string.lower().replace(' ', '')
    
    
    for i in (new_string):
        leters[i] = new_string.count(i)
    
    leters = sorted(leters.items(), key=lambda x: x[1], reverse = True)
    print(leters)
    
    for i in range(3):
        print(leters[i])
        i += 1
    
    return ""
        
name = "Codo a Codo"
print(find_char(name))
