
import bisect
 
L = [1,3,3,6,8,12,15]
x = 3
x_insert_point = bisect.bisect_left(L,x)
x_insert_point = bisect.bisect_right(L,x)  #在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回右侧位置３
x_insort_left = bisect.insort_left(L,x)  #将x插入到列表L中，x存在时插入在左侧
x_insort_rigth = bisect.insort_right(L,x) #将x插入到列表L中，x存在时插入在右侧　　　　
 
