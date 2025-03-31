def sum(n:int) -> int:
    sum:int = 0
    if n < 0:
        print("Error! Inserted number is negative!")
        return None
    else:
        while n >= 0:
            sum += n
            n -= 1
        return sum

print(sum(5))
print(sum(-5))