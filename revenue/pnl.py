rev = [1,2,3,4,5,6,7,8,9,10,11,12]
cog = [2,2,3,3,4,4,5,5,6,6,7,7]
rev_multipler = 10

total = 0
best = 0
worst = None
all = []

for m in rev:
    real_rev = rev[m-1] * rev_multipler
    profit = real_rev - cog[m-1]
    net_rev = profit * 0.7
    margin = round(net_rev / real_rev,2)
    total += profit
    mean = round(total / m,2)
    
    if not worst:
        worst = profit

    best = max(best, profit)    
    worst = min(worst, profit)
    all.append(profit)
    print('{} {} {} {} {} {} {} {}'.format(real_rev, profit, net_rev, margin, total, mean, best, worst))

#reduce(lambda x, y: x + y, l) / len(l)
#import numpy as np  print np.mean(l)
#from statistics import mean  mean(l)
#other methods

def avg(lst):
    return sum(lst)/float(len(lst))

print(avg(all))
