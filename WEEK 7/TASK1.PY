print("Program starting.")
nums = []

print("Collect positive integers.")
while True:
    n = int(input("Insert positive integer(negative stops): "))
    if n < 0:
        print("Stopped collecting positive integers.")
        break
    nums.append(n)

if len(nums) == 0:
    print("No integers to display.")
else:
    print(f"Displaying {len(nums)} integers:")
    for i, v in enumerate(nums):
        print(f"- Index {i} => Ordinal {i+1} => Integer {v}")

print("Program ending.")
    