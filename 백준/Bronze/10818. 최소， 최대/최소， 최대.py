n = int(input())
numbers = list(map(int, input().split()))

srtNumbers = sorted(numbers)
print(f"{srtNumbers[0]} {srtNumbers[n-1]}")