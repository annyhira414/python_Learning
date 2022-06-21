def hashmap(nums):
    emptyBox = set()
    for n in nums:
        if n in emptyBox:
            return True
        emptyBox.add(n)
    return False


nums = [2, 3, 4, 5]
print(hashmap(nums))

# the output is false because here is no duplicat numbers in num array
