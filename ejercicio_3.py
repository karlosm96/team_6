def my_function(string, indice_1, char):
    init = indice_1
    
    ori_string = string
    mod_string = string[:init] + char + string[init + 1 :]
    
    return (ori_string + " " + "---->String modificado----->" + " " + mod_string)
    
    
    
print(my_function("este es el primer texto de prueba", 5, "#"))