input = [0, 3, 5, 6, 1, 2, 4]


# 둘중하나가 1또는 0이면 더하는게이득, 나머지는 곱하는게 이득
def find_max_plus_or_multiply(array):

    sum= 0
    for i in range(0,len(input)):
        if sum<=1 or input[i]<=1:
            sum+=input[i]
        else:
            sum*=input[i]

    return sum


result = find_max_plus_or_multiply(input)
print(result)