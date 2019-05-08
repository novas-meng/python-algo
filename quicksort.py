import numpy as np
'''
快排算法,思想是分治的思想
array=[2,2,34,34,2,6,45,13,68,3,21,9]
举例 首先对于array，取数组的最后一个元素9作为flag，
将数组小于等于9的都放在9的左侧，大于9的放在右侧，如partition函数
其中p表示数组起点，q表示数组最后一个元素，i表示指针，这个指针左侧的元素都是小于等于flag的元素
然后返回这个指针，将数据切分成[:i-1] array[i] array[i+1:] 这样的三部分，然后在递归调用partition，
直到整体都有序


'''
def partition(array,p,q):
	i=p-1
	x=array[q]
	'''
	range 范围不包括q，所以i的最大值就是q-2
	'''
	for j in range(p,q):
		if array[j] <= x:
			i=i+1
			array[i],array[j]=array[j],array[i]
	'''
	i的最大值是q-2，保证不会数组越界
	'''
	i=i+1
	array[q],array[i]=array[i],array[q]
	return i

def quicksort(array,p,q):
	if q > p:
		mid=partition(array,p,q)
		quicksort(array,p,mid-1)
		quicksort(array,mid+1,q)

def is_correct(array):
	for i in range(len(array)-1):
		if array[i+1] < array[i]:
			return False
	return True 

if __name__=='__main__':
	for i in range(10000):
		count=np.random.randint(1,1000)
		#array=[2,2,34,34,2,6,45,13,68,3,21,9]
		array=list(np.random.randn(count))
		#print(array)
		#print(is_correct(array))
		quicksort(array,0,len(array)-1)
		#print(is_correct(array))
		if is_correct(array) == False:
			print("error")
			break
