from sys import argv, exit
# not using numpy because i don't know if it's allowed or not;
# not using decimal for proper rounding,
# using function from https://stackoverflow.com/a/38239574 instead

path = argv
lines = []

def percentile(num, data):
    rank = (num / 100) * (len(data) - 1) + 1
    if rank.is_integer():
        return data[int(rank)-1]
    else:
        try:
            ir = int(rank // 1) - 1
            fr = rank % 1
            return data[ir] + fr * ((ir + 1) - ir)
        except IndexError:
            exit('can\'t count percentile from 1 number!')

def roundTraditional(val,digits):
    return round(val+10**(-len(str(val))-1), digits)

def median(data):
    num = len(data)
    if num % 2 == 0: # number is even
        return (data[int(num / 2)] + data[int((num / 2) + 1)]) / 2
    else:
        return data[int((num / 2) - 0.5)]
# statistics.median(data) returns same result

# min and max can be found with any sorting algorithm (bubble sorting for instance)
# but i don't know what's expected of me so i'll just do this

def min_num(data):
    return min(data)

def max_num(data):
    return max(data)

def avg_num(data):
    s = 0
    for n in data:
        s += n
    return s / len(data)
# statictics.mean(data) returns same result

try:
    with open(path[1]) as infile:
        for line in infile:
            lines.append(int(line.rstrip()))
    lines.sort()
    # there are different ways to calculate percentile with different results
    print("{:.2f}".format(roundTraditional(percentile(90, lines), 2)))
    # print("{:.2f}".format(roundTraditional(percentile(50, lines), 2))) 
    # median can be calculated as 50th percentile
    print("{:.2f}".format(median(lines)))
    print("{:.2f}".format(max_num(lines)))
    print("{:.2f}".format(min_num(lines)))
    print("{:.2f}".format(roundTraditional(avg_num(lines), 2)))

except IndexError:
    print('no file was passed') # need proper way to check if no args passed

except FileNotFoundError:
    print('no such file')

except ValueError:
    print('invalid value, can\'t convert to integer')
