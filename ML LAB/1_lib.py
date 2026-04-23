import statistics

data = list(map(int,input("Enter the Numbers with space : ").split()))

#mean = sum(data)/len(data)

mean = statistics.mean(data)

median = statistics.median(data)

try:
    mode = statistics.mode(data)
except statistics.StatisticsError(data):
    mode = statistics.multimode(data)

variance = statistics.variance(data)
stdev = statistics.stdev(data)


print("The mean :",mean)
print("The median :",median)
print("The mode :",mode)
print("The varoiance :",variance)
print("The stddev :",stdev)