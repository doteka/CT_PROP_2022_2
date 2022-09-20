# 프로그래머스 Lv2 n개의 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12953

# 작성자 : 강동준
# 최초 작성일 : 2022-09-19
# 최종 작성일 : 2022-09-20
def GCD(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

def LCM(arr1):
    arr = [] + arr1
    while len(arr) != 1:
        gcd = GCD(arr[0], arr[1])
        lcm = int(arr[0] * arr[1] / gcd)
        for i in range(0, 2):
            del arr[0]
        arr.insert(0, lcm)
    return arr[0]

def solution(arr):
    answer = 0
    lcm = LCM(arr)
    answer = lcm
    return answer

arr = [3,4,9,16] 
print(solution(arr))