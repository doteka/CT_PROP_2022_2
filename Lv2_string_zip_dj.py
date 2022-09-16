# 프로그래머스 Lv2 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 작성자 : 강동준
# 최초 작성일 : 2022-09-09
# 최종 작성일 : 2022-09-16
def init():                                     # variable init
    str1 = ""
    str2 = ""
    count = 0
    return str1, str2, count

def Divide_letters(wStr, Number_Of_Char):
    i = 0
    str1, str2, count = init()
    result = ""
    while i < len(wStr):                        
        if str1 == "":
            if (i+Number_Of_Char >= len(wStr)):     # prevent list out of range
                result += wStr[i:len(wStr)]         # Paste all remaining strings
                break
            else:
                str1 = wStr[i:i+Number_Of_Char]     # Reference String
                count = 1
        for j in range(i+Number_Of_Char, len(wStr), Number_Of_Char):
            str2 = wStr[j:j+Number_Of_Char]         # Match String
            if str1 == str2:                        # If two strings are the same
                count += 1
            else:
                break
        if count <= 1:                              # If you have 1 identical character
            result += str1
        else:
            tmp = str(count)
            result += (tmp + str1)                  # Create a String to Format
            i += ((count-1) * Number_Of_Char)       # Skip the same number of strings
            

        i += Number_Of_Char
        str1, str2, count = init()
        # print(result)
    
    return result      

def solution(s):
    answer = 0
    min = 1001
    if len(s) == 1:
        return 1
    for i in range(0, int(len(s)/2)):               # If it's over half of the time, there's only one letter
        result = Divide_letters(s, i+1)
        if (len(result) < min):                     # minimum value
            min = len(result)
    answer = min
    return answer

s = "xababcdcdababcdcd"	
print(solution(s))