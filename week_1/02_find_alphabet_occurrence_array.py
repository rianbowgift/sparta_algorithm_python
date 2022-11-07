input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    list = [0] * 26

    for i in string:
        if i.isalpha():
            list[ord(i) - ord('a')]+=1




    return list

result = find_max_occurred_alphabet(input)
print(result)