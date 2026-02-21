import time

numb = int(input("how many numbers to make "))
my_list = []
start = time.time_ns()
for i in range(1,numb):
    my_list.append(i)
    if (len(my_list) % 2500000) == 0:
        diff = time.time_ns()
        print((f"\rNumbers made: {len(my_list)} in: {round(((int(diff) - int(start))/ 1000000000),2)} sec for {int((len(my_list) / ((int(diff) - int(start)) / 1000000000)))} Nunbers pr second"""),end="", flush=True)



find = int(input('\n\nEnter the number to find: '))



def find_numb(li:list, find:int, itr:int):
    x = len(li)//2
    val = li.index(x)
    
    if val == find:
        print(f"Found {find} in the list ")
        return 
    if val > find:
        li = li[:x]
        print(li)
        find_numb(li, find=find)
    if val < find:
        li = li[x:]
        print(li)
        find_numb(li, find=find)


find_numb(my_list, find)
