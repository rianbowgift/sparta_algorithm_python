input = "abadabac"

def find_not_repeating_character(string):

    list = [0]  * 26

    for i in string:
        list[ord(i)-ord('a')]+=1



    for i in string:
        if list[ord(i)-ord('a')]==1:
            return i




result = find_not_repeating_character(input)
print(result)