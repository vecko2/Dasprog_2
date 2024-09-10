arr = list(map(int, input().split()))
cat = int(input())
dog = int(input())
for _ in range(dog):
    temp = arr[:7-cat]
    arr[:7-cat] = arr[-cat:]
    arr[-cat:] = temp
    
    # print(arr)
fish, bird, duck = map(int,input().split())
print(arr[fish], arr[bird], arr[duck])