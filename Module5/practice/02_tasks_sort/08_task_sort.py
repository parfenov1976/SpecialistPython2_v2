# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

def sort_choice(nums):
    i = 0
    while i < len(nums) - 1:
        min_index = i
        next_index = i + 1
        while next_index < len(nums):
            if nums[next_index] < nums[min_index]:
                min_index = next_index
            next_index += 1
        nums[i], nums[min_index] = nums[min_index], nums[i]
        i += 1


phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]

sort_choice(phones)
print(phones)
