#  Given a list iterate it and display numbers which are divisible by 5 and if you find 
# number greater than 150 stop the loop iteration. 
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200] 
list2 = []
for i in list1:
    if i > 150 :
        continue
    elif i % 5 == 0 :
        list2.append(i)

print(list2)
