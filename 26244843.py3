A,B,V=map(int, input().split())
k=(V-B)/(A-B)
print(int(k) if k == int(k) else int(k)+1)

# 달팽이는 목적지에 도착하면 미끄러지지않으므로
# 달팽이가 올라가야할 총 길이는 V-B가 된다.
# 일수로 생각하여 k=전체길이/하루올라가는 길이로 둔다.
# 만약 k가 정수값이면 그대로 출력하지만
# k가 소수값이라면 하루를 더 올라야하므로 k+1을 출력한다.
