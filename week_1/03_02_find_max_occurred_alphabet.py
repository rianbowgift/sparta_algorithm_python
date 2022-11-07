input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    list = [0] * 26

    for i in string:
        if i.isalpha():
            list[ord(i) - ord('a')]+=1

    max_num=0;
    max_index=0;

    for i in range(len(list)):
        if max_num<list[i]:
            max_num=list[i]
            max_index=i

    return chr(max_index+ord('a'))
   

result = find_max_occurred_alphabet(input)
print(result)