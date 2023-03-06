num_list=list(range(1,11))
print("Number list:",num_list)
num_sum=0
for num in num_list:
    num_sum+=num
avg=num_sum/len(num_list)
print(f"sum is {num_sum} and average is {avg}")
