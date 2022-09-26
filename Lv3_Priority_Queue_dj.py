# 프로그래머스 Lve 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

# 작성자 : 강동준
# 최초 작성일 : 2022-09-26
# 최종 작성일 : 2022-09-

def solution(operations):
    answer = []
    
    for key in operations:
        a, b = key.split()
        if a == 'I':
            answer.append(int(b))
        else:
            if len(answer) != 0:
                if b == '1':
                    maxValue = max(answer)
                    answer.remove(maxValue)
                else:
                    minValue = min(answer)
                    answer.remove(minValue)

    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), min(answer)]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	
print(solution(operations))