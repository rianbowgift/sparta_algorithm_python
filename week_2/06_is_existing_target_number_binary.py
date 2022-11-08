finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):

    mins=0
    maxd=len(array)-1
    guess=maxd+mins//2

    #최소값이 최대값보다 같거나작다면 계속진행한다
    while mins<=maxd:
        if array[guess] == target:
            return True
        if array[guess] < target:
            #....여기까지






    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)