input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    list = [0] * 26

    for i in string:
        if i.isalpha():
            list[ord(i) - ord('a')]+=1

    max=0
    index=0
    num=0

    for i in list:
        if max<i:
            max=i
            index=num
        num+=1




    return chr(index+97)

result = find_max_occurred_alphabet(input)
print(result)