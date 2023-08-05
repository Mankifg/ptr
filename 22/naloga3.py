import random

symbols = ["+", "-", ""]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sul = []

# get every possible combinaton of numbers
def gen():
    s = ""
    for i in range(len(nums) - 1):
        # the best i can do is random :)
        # don't know how to get like every possible combination of numbers
        s = f"{s}{nums[i]}{random.choice(symbols)}"

    s = f"{s}{nums[8]}"

    return s


while True:

    a = gen()
    if a not in sul:
        if eval(a) == 100:
            sul.append(a)
            print(a)
            if len(sul) == 11:
                break

print("ended")
print(f"Found: {len(sul)}")
