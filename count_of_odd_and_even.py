num_list=list(range(0,100))
print(num_list)
even_count=0
odd_count=0
for num in num_list:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even count:",even_count)
print("Odd count:",odd_count)
