def solution(stones, k):
    answer = 0
    start = 1
    limit = max(stones)
    mid = 0


    # 문제에서 제한 조건은 2가지, 1. 건너는 사람은 디딤돌 중 최고 수보다 많을 수 없다. 2. 건너는 사람은 연속된 디딤돌 수 k의 n보다 많을 수 없다.
    
    while start <= limit:
        if (start+limit) % 2 == 0:    # 이진 탐색 조건
            mid = (start+limit) // 2
        else:
            mid = ((start+limit) // 2)+1 

        count= 0         # k와 비교하기 위해서 설정, 연속적으로 0인 디딤돌의 수.
        max_count = 0    

        for i in range(len(stones)):
            if stones[i] - mid <= 0:               # 현재 건너고 있는 돌이 중간값보다 작다면 일단은 count를 증가시킴
                count += 1
                max_count = max(max_count, count)  # max_count로 max_count가 k보다 크다면 터지도록 만들어줘야함.
                if max_count >= k:
                    break
            else:
                count = 0                          # 아직 디딤돌이 0이 아니라면 count는 계속 0이다. 

        if max_count < k:    
            start = mid + 1
        elif max_count >= k: # 개념적 접근, 애초에 for문에 count가 k보다 커지는 경우 break가 있기 때문에 없어도 될듯? 안됨.....
            limit = mid - 1
	
    answer = start
    return answer
