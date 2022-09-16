# 프로그래머스 Lv2 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 작성자 : 강동준
# 최초 작성일 : 2022-09-09
# 최종 작성일 : 2022-09-16
def init():                                     # variable init
    Reference_String = ""
    Match_String = ""
    count = 0
    return Reference_String, Match_String, count

def Divide_letters(words, Number_Of_Char):
    index = 0
    Reference_String, Match_String, count = init()
    result = ""
    while index < len(words):                        
        if Reference_String == "":
            if (index+Number_Of_Char >= len(words)):     # prevent list out of range
                result += words[index:len(words)]         # Paste all remaining strings
                break
            else:
                Reference_String = words[index:index+Number_Of_Char]     # Reference String
                count = 1
        for index2 in range(index+Number_Of_Char, len(words), Number_Of_Char):
            Match_String = words[index2:index2+Number_Of_Char]         # Match String
            if Reference_String == Match_String:                        # If two strings are the same
                count += 1
            else:
                break
        if count <= 1:                              # If you have 1 identical character
            result += Reference_String
        else:
            temp_var = str(count)
            result += (temp_var + Reference_String)                  # Create a String to Format
            index += ((count-1) * Number_Of_Char)       # Skip the same number of strings
            

        index += Number_Of_Char
        Reference_String, Match_String, count = init()
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