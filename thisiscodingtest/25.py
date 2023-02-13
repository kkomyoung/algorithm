N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    
    answer = []
    failedRateArr = [] #실패율
    countStayArr = [0]*(N+1) #각 스테이지에 머물러 있는 사람 수
    people = len(stages) #전체 사람 수

    for stage in stages:
        if stage > N:
            continue
        countStayArr[stage] += 1

    for i in range(1, N+1):
        if people == 0:
            failedRateArr.append((0, i))
        else:
            # 실행시간 오래걸림 : array.append((stages.count(i)/num*100, i))
            failedRateArr.append((countStayArr[i]/people*100, i))
            people -= countStayArr[i]

    failedRateArr.sort(key=lambda x : (-x[0], x[1]))

    for i in failedRateArr:
        answer.append(i[1])

    return answer

print(solution(N, stages))