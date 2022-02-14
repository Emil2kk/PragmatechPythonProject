lst=['banan','alma','armud']

menu="""
1.banan
2.alma
3.armud
"""
print(menu)
a=input()
if a in lst:
    print(input("qiymet-"))
else:
    print("o meyve yoxdu")