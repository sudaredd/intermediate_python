from collections import deque

dq = deque()

dq.append(1)
dq.append(2)

dq.appendleft(3)
dq.append(4)

print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)