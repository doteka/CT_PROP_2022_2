# 프로그래머스 Lv2 n개의 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12953

# 작성자 : 강동준
# 최초 작성일 : 2022-09-19
# 최종 작성일 : 2022-09-20
def GCD(arr1):
    arr = [] + arr1
    while len(arr) != 1:
        a = arr[0]
        b = arr[1]
        while b != 0:
            temp = a % b
            a = b
            b = temp
        for i in range(0, 2):
            del arr[0]
        arr.insert(0, a)
    return arr[0]

def LCM(arr1, gcd):
    arr = [] + arr1
    while len(arr) != 1:
        lcm = int(arr[0] * arr[1] / gcd)
        for i in range(0, 2):
            del arr[0]
        arr.insert(0, lcm)
    return arr[0]

def solution(arr):
    answer = 0
    gcd = GCD(arr)
    lcm = LCM(arr, gcd)
    answer = lcm
    return answer

arr = [2,6,8,14]
print(solution(arr))