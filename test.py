'''
@Author: Haodada
@Date: 2019-12-05 09:33:15
@LastEditTime: 2019-12-06 17:26:03
@Description: file content
'''
import time
class Point:
    def __init__(self,index):
        self.index = index
l = []
start = time.process_time()
for i in range(1000000):
    l.append(Point(i))
end = time.process_time()
print(end - start)
m = []
start = time.process_time()
for i in range(1000000):
    m.append(i)
end = time.process_time()
print(end - start)

start = time.process_time()
for i in range(1000000):
    l[i].index = 2*i
end = time.process_time()
print(end - start)
start = time.process_time()
for i in range(1000000):
    m[i] = 2*i
end = time.process_time()
print(end - start)
