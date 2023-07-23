import random
passlen = int(input("Password lenth: "))
s ="abdvehsdskruuhvnnjhhyffjfjgjkljfvkjgjkfhurtfhugvnfdljklnmklj@#$U&!@*#(9"
p = "".join(random.sample(s,passlen))
print(p)

