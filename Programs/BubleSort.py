numbers = list(map(int,input("Enter the list of numbers separated by space:").split()))

n = len(numbers)

for i in range(n - 1):

    swap = False

    for j in range(n - i - 1):

        if numbers[j] > numbers[j + 1]:

            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

            swap = True

    if swap == False:
        break

print(numbers)