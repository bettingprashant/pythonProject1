# deque - double ended que
#FIFO - Bus StandQue, Airport Que


from collections import deque

d = deque([1,2,3])
print(d)

d.append(4)
print(d)

#Add an element to the left end
d.appendleft(0)
print(d)

# extend(list) the deque
d.extend([5])
print(d)

print(d.pop())
print(d.popleft())
d.reverse()
print(d)