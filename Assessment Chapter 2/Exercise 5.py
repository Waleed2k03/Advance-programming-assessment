product =["Health items","Kitchen items","Pet items","Comfort items","Fashion items","Gadget items","Comfort items","Gadget items","Comfort items","Kitchen items","Fashion items"]
print("Number of times items appeared in the list:")
[print(product.count(item), item) for item in set(product)]