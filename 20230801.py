# APS 기본

# 카운팅 정렬 (Counting Sort)

# 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

# 제한 사항

# 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 :
# 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.

# 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.

# 시간 복잡tjd
# O(n + k) : n은 리스트 길이, k는 정수의 최대값

# [0, 4, 1, 3, 1, 2, 4, 1] 을 카운팅 정렬하는 과정
# 1단계
# Data에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts 저장한다

# data = [0, 4, 1, 3, 1, 2, 4, 1]
# counts = [0, 0, 0, 0, 0, 0] -> counts [1, 3, 1, 1, 2]
# count[i] = i의 발생 회수

# 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소를 조정한다
# counts[i] += counts[i-1]

# count[1]을 감소시키고 temp에 1을 삽입한다.

# count[4]를 감소시키고 temp에 4를 삽입한다.

# count[0]를 감소시키고 temp에 0을 삽입한다

def Counting_Sort(A, B, k):
# A [] -- 입력 배열 (0 to k)
# B [] -- 정렬된 배열
# C [] -- 카운트 배열

    C = [0] * (k+1)

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range (1, len(C)):
        C[i] += C[i-1]

    for i in range (len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

# Baby-gin Game

# 설명
# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
# 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.

# 그리고 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다

# 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라

# 입력 예
# 667767은 두 개의 triple이므로 bab-gin이다
# 054060은 한 개의 run과 한 개의 triplet이므로 역시 baby-gin(456, 000)
# 101123은 한 개의 triplet가 존재하나, 023이 run이 아니므로 baby-gin이 아니다

# 완전 검색 (Exacustive Search)

# 완전 검색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법이다
# Brute-force 혹은 generate-and-test 기법이라고도 불리 운다.
# 모든 경우의 수를 테스트한 후, 최종 해법을 도출한다
# 일반적으로 경우의 수가 상대적으로 작을 때 유용하다

# 완전 검색으로 시작하라
# 모든 경우의 수를 새성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 작다.

# 자격검정평가 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해
# 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직하다.

# 완전 검색을 활용한 Baby-gin 접근
# 고려할 수 있는 모든 경우의 수 생성하기
# 6개의 숫자로 만들 수 있는 모든 숫자 나열(중복 포함0

# 순열을 어떻게 생성할 것인가
# 순열 (Permutation)

# 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
# 서로 다른 n개 중 r개를 택하는 순열은 아래와 같이 표현한다.
# nPr
# nPr = n * (n-1) * (n-2) * ... * (n-r+1)
# nPn = n!

# 단순하게 순열을 생성하는 방법
# 예) {1, 2, 3} 을 포함하는 모든 순열을 생성하는 함수
# 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop을 이용해 아래와 같이 구현할 수 있다.

for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)

# 탐욕(Greedy) 알고리즘
# 탐욕 알고리즘은 최적해를 구하는데 사용되는 근시안적인 방법
# 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행
# 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만,
# 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없다.
# 일반적으로 경우의 수가 상대적으로 작을 때 유용하다

# Baby - gin
# 구현 예
num = 456789 # Baby Gin 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0

while i < 10:
    if c[i] >= 3: # triplete 조사 후에 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: #run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print('Baby Gin')
else:
    print('Lose')

# 자주 실수하는 오답
# 입력받은 숫자를 정렬한 후, 앞뒤 3자리씩 끊어서 run 및 triplet을 확인하는 방법을 고려할 수 있다

# SWEA 11092 최대 최소의 간격

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0 # 최소값의 인덱스
    max_idx = 0 # 최대값의 인덱스
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] < arr[i]:
            max_idx = i
    ans = max_idx - min_idx
    if ans < 0:
        ans *= -1

# SWEA 9386
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))   # 0011001110



"""
def Counting_Sort(A,B,K)
# A [] -- 입력 배열 (0 to K)
# B [] -- 정렬된 배열
# C [] -- 카운트 배열

C = [0] * (k+1) 
# 입력된 값의 + 1 만큼(0부터 시작이니까) 배열 초기화

for i in range(0, len(A)): # 입력배열 순회하는데 
    C[A[i]] += 1   # 입력배열의 각 요소값은 카운트배열의 인덱스가 된다
# A배열의 0번자리의 값이 '3'이라면 C배열의 3번째 자리가 +1 카운트
# 즉, C배열은 A배열의 값의 개수를 순서대로 카운트한 값을 가진 배열

for i in range(1, len(C)): # 카운트배열(C배열) 순회
    C[i] += C[i-1] # 카운트 배열이 값 순서대로 정렬되어야 하므로
# 오름차순이 되어 순서가 생기도록 자기 앞의 값을 더한다.

for i in range(len(B)-1, -1, -1): # 입력 배열(A)의 모든 값의 횟수를 정렬배열(B)
                    # 에 담아두었으므로(즉, 입력배열의 값이 모두 정렬 배열에 있으므로) 
                            #  정렬배열을 순회 인덱스를 위해 -1 

    C[A[i]] -= 1   # 입력배열의 뒤부터 순회하는데, 입력배열 값이 C배열에서 
                                    # 입력배열의 값의 갯수를 가지고 있으므로 
                                     #찾아서 -1 카운트(0부터 시작하므로 -1해야 의도한 위치에 인덱스가능)
    B[C[A[i]]] = A[i]  # A[i] = 입력배열의 값이 C[A[i]] = 몇개이고 
                                            # B[C[A[i]]] = 그 몇개가 B배열의 위치(B배열의 인덱스)이며
                                                # = A[i] = 그 위치에 입력 배열 값(원래 값)이 들어가야함
"""
 