list=[5,95,15,6,16,26,98,38,48,90]
for number in list:
 print(list)
 print("highest value is:",max(list))
 print("smallest value is:",min(list))
list.sort()
print("Ascending order :",list)
list.reverse()
print("Descending order :",list)
list.append(80)
list.append(70)
print(list)