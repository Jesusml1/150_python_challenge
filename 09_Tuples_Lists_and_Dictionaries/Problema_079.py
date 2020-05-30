nums = []
for i in range(3):
    nums.insert(i, int(input("Enter a number...")))

print(nums)
listLength = len(nums) - 1
wantItRemove = str(input("Want to remove the last one? (y/n) "))
if wantItRemove == "y":
    del nums[listLength]
print()
print(nums)