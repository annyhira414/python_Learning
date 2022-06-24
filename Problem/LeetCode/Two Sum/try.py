class Sum_array:
    def twoSum(self, number, target):
        empty = {}
        for i, n in enumerate(number):
            diff = target - n
            if diff in empty:  # if the diff is already in the hash map,
                return [empty[diff], i]  # then we can return the solution which is going to be pair
            empty[n] = i  # if I don't find the solution, the I update my hash map which is n value
        return


ans = Sum_array()
number = [2, 15, 7, 9, 3, 1]
print(ans.twoSum(number, 3))
