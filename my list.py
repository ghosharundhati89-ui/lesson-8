lst=["Apple","Mango","Banana","Kiwi"]
print("length of the list ",len(lst))
print("first element",lst[0])
print("last element",lst[-1])
lst.append("papaya")
print("updated list ",lst)
lst.remove("Banana")
print("uptated list ",lst)
lst.pop(3)
lst.sort()
print("updated list ",lst)
lst.reverse()
print("updated list ",lst)
lst=lst[:3]
print("sliced list ",lst)
lst.clear()
print("updated list ",lst)



