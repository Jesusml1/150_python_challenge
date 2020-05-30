from array import array

nums = array('i', [])

for y in range(0, 5):
    num = int(input("introduce a number: "))
    nums.append(num)

nums = sorted(nums)
newlist = nums.reverse()
print(nums)