### working brute force attempt 🤷‍♂️

#test input
input = [16,1,2,0,4,2,7,1,2,14]


# Task 1
def task1(input):
    min_fuel = 100000000000000
    x = 5
    for x in range(max(input)):
        fuel = sum(i - x if i - x >= 0 else x - i for i in input)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


# Task 2
def task2(input):
    min_fuel = 100000000000000
    for x in range(max(input)):
        fuel = 0
        for i in input:
            if i-x >= 0:
                for k in range(1, (i -x) +1):
                    fuel += k
            else:
                for k in range(1+ (x-i)):
                    fuel += k 
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel

print(task1(input))
print(task2(input))
            


