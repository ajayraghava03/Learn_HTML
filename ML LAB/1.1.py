ip = input("Enter numbers separated by commas : ")

nums = [int(num) for num in ip.split(',')]

n = len(nums)

mean = sum(nums)/n

print("Mean : ",round(mean,2))

num = sorted(nums)

if(n%2 == 0):
    m = (num[n//2-1]+num[n//2])/2
else :
    m = num[n//2]

print("Median : ",m)

freq = {}
high = 0

for i in nums :
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    if(high < freq[i]):
        high = freq[i]

modes = {k for k,v in freq.items() if v == high}

l = len(modes)

if(l < n):
    for i in modes:
        print("Mode",i,end=" ")
else :
    print("NO mode available")


var = sum((k-mean)**2 for k in nums)/n
stddev = var ** 0.5

print("var : ",var)
print("std : ",round(stddev,2))