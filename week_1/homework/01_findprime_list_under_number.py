import math

input = 20

#에라토스테네스의 체 사용
def find_prime_list_under_number(number):

    array = [True for i in range(number+1)]
    answer = []
    for i in range(2,int(math.sqrt(number))+1):
        if array[i] == True:
            j=2
            while i * j <=number:
                array[i*j] = False
                j+=1




    for i in range(2,number+1):
        if array[i]:
            #print(i,end=' ')
            answer.append(i)

    # 이 부분을 채워보세요!
    return answer


result = find_prime_list_under_number(input)
print(result)