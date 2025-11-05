from typing import List

class Solution(object):
    def solve(self,nums:List[List[int]]) -> List[int]:
        print(f"nums: {nums}")
        # Write your code here
        vertor_sum_1 = 0
        vertor_sum_2 = 0
        vertor_sum_3 = 0
        '''golang
            for _, triple := range nums {
                a := triple[0]
                b := triple[1]
                c := triple[2]
                fmt.Println(a, b, c)
            }
        '''
        for first, second, third in nums: #
            vertor_sum_1 += first
            vertor_sum_2 += second
            vertor_sum_3 += third
        return [-vertor_sum_1, -vertor_sum_2, -vertor_sum_3]
