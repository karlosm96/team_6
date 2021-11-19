### cambia a mayuscula la primera letra de 2 strings ###
def cap_letter(first_name, second_name):
    full_name = first_name + " " + second_name
    full_name = full_name.title()
    print(full_name)

first_name = "pepito"
second_name = "perez"
cap_letter(first_name, second_name)