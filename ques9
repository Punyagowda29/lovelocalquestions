def count_digit_one(n):
    count = 0 #initial the count variable
    for i in range(1, n + 1):
        num = i 
        while num > 0:
            if num % 10 == 1:
                count += 1
            num //= 10   # each iteration reduce the num by 10
    return count

# Example Usage
number = int(input())
total_ones = count_digit_one(number)
print("Output:", total_ones)
