from collections import deque
#deque始终双向列表，适用于队列和栈
q=deque(['1','23',3,'ad'])
q.append('w')
q.appendleft('id')
print(q)
q.popleft()
print(q)
q.pop()
print(q)