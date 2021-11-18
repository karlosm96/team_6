def sup_champion(my_list):
    points_list = my_list
    points_list.sort(reverse = True)
    second_place = 0
    
    for i in range(len(points_list)):
        if points_list[i] <= points_list[i+1]:
            i = i+1
        else:
            second_place = second_place + points_list[i+1]
            break
    return second_place        

my_list = [2,6,10,10,7,5,6]
print(sup_champion(my_list))