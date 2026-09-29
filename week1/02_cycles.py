"""
здесь знакомимся с:
1. условными операторами, 
2. логическими конструкциями, 
3. функциями 
4. циклами
"""

# простой цикл
for i in range (13):
    print(i)
print("---------------------")

for a in range (15):
    print(a**2)
print("---------------------")

for cube in range (15):
    print(cube**3)
print("---------------------")

for kris in range(65, 77, 2):
    print(f"happy number = {kris}")
print("---------------------")


colors = ['red', 'green', 'blue', 'klein_blu']
print(f"Our colors are: {colors}")
print(*colors, sep="; ")
print("---------------------")


for fav_color in colors:
    print(f"My favourite color is {fav_color}")

print("---------------------")


idxs = [0, 1, 2, 3, 4, 5, 6, 7]
for my_idx in idxs:
    print(f"current index = {my_idx}. squared = {my_idx**2}")

print("---------------------")

slice_idxs = idxs[2:5]
print(slice_idxs)

slice_with_step = idxs[1:7:2]
print(slice_with_step)

reverse_idxs = idxs[::-1]
print(reverse_idxs)

for elem in reverse_idxs:
    print(elem)
print("---------------------")


for bang in range(100):
    ostatok = bang % 4
    if ostatok == 0:
        print("bang!!!!!!!")
    else:
        print("---")

print("----------beat-----------")    
for bang in range(100):
    ostatok = bang % 4
    if bang % 4 == 0 and bang % 3 == 0:
        print("bang! hihat!")
    elif bang % 4 == 0:
        print("bang!")
    elif bang % 3 == 0:
        print("hihat!")
    else:
        print("---")






print("Hello world")