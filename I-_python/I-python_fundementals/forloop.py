print("1. Integers from 0 to 150:")
for i in range(0, 151):
    print(i)

print("\n" + "="*50 + "\n")

print("2. Multiples of 5 from 5 to 1000:")
for i in range(5, 1001, 5):
    print(i)

print("\n" + "="*50 + "\n")

print("3. Counting the Dojo Way (1 to 100):")
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

print("\n" + "="*50 + "\n")

print("4. Sum of odd integers from 0 to 500,000:")
total = 0
for i in range(1, 500001, 2):  
    total += i
print(f"Final sum: {total:,}")

print("\n" + "="*50 + "\n")

print("5. Countdown by fours from 2018:")
for i in range(2018, 0, -4):
    print(i)

print("\n" + "="*50 + "\n")

print("6. Flexible Counter:")
lowNum = 2
highNum = 9
mult = 3
print(f"Multiples of {mult} between {lowNum} and {highNum}:")
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)

print("\nAnother example (lowNum=1, highNum=20, mult=4):")
lowNum = 1
highNum = 20
mult = 4
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)