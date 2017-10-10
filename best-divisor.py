import math
def find_sum(number):
    sum_num = 0
    while number > 0:
        sum_num += number % 10
        number /= 10
    return sum_num

def best_divisor():
    num = input()
    sum_best_fact = find_sum(num)
    best_factor = num
    for x in range(1, int(num/2)+1):
        if num % x == 0:
            sum_ = find_sum(x)
            if sum_ > sum_best_fact:
                best_factor = x
                sum_best_fact = sum_
            if sum_ == sum_best_fact:
                best_factor = min(x, best_factor)
    print best_factor

def main():
    best_divisor()

if __name__ == "__main__":
    main()