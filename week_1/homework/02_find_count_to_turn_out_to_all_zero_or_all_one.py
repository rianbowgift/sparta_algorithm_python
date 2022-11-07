input = "011110"
temp = ""


#그리디 알고리즘 사용
def find_count_to_turn_out_to_all_zero_or_all_one(string):

    lists = list(string) #리스트료 형변환하여 접근
    num = 0


    for i in range(1,len(lists)):
        if lists[i]!=lists[i-1]:    #이전과 다르다면
            temp=lists[i-1]
            for j in range(i,len(lists)):
                if temp!=j:
                    lists[j] = temp
                else:
                    break
            num+=1

    return num




result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)