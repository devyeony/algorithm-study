n, k = map(int, input().split())

thing = [[0,0]] # 무게,가치의 리스트, 처음에는 0.0 넣어주기
d = [[0]*(k+1) for _ in range(n+1)] # dp를 실행하기 위해 리스트 dp를 실행하기위해 [0][0]을 남겨둔다.

for i in range(n): # 첫번째를 다음 [1]부터 무게,가치 항목넣어주기
    thing.append(list(map(int, input().split())))

for i in range(1, n+1): # 0번째 있으니까 [1]번째부터 [n]까지 돌아야하니 n+1까지
    for j in range(1, k+1): # 
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])