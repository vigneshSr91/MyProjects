class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
		water_accumulated = 0
		left_max=[]
		right_max=[]
		for i in range(len(A)):
			if i == 0:
				left_max.append(A[0])
			else:
				left_max.append(max(A[i],left_max[i-1]))
				
		for i in range(len(A)-1,-1,-1):
			if i == len(A)-1:
				right_max.append(A[i])
			else:
				right_max.append(max(A[i],right_max[len(right_max)-1]))
		right_max = right_max[::-1]        
		for i in range(1,len(A)-1):
			right_max_for_i = right_max[i]
			left_max_for_i = left_max[i]
			
			if left_max_for_i == 0 or right_max_for_i == 0:
				continue
			water_accumulated += min(left_max_for_i,right_max_for_i) - A[i]
		return water_accumulated
	

if __name__ == '__main__':
	A = [4,2,5,7,4,2,3,6,8,2,3]
	print(Solution().trap(A))