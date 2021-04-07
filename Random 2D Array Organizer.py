import random


nums2D = []

for i in range(0,4):
    nums2D.append([])
    for j in range(0,5):
        nums2D[i].append(random.randint(0,100))
        print(nums2D[i][j], end = '\t')
    print()

