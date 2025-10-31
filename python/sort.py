'''Making Addition Easy
Jane, a budding mathematician and a second-grade student, is learning how to perform addition. Her teacher wrote down a sum of several numbers on the board, and the students were asked to calculate the total. To keep things simple, the sum only includes the numbers 1, 2, and 3. However, Jane is still getting the hang of addition, so she can only calculate the sum if the numbers are arranged in non-decreasing order (i.e., each number is greater than or equal to the one before it). For example, she cannot compute a sum like 2+1+3+2, but she can handle sums like 1+2+2+3.

Your task is to rearrange the numbers in the given sum so that Sophia can compute it.

Example 1
Input:
1+3+2+1
Output:
1+1+2+3
'''


class Solution(object):
    def solve(self, s:str) -> str:
        number_list = list(map(int, s.split("+")))

        # show bubbe sorting algoritm
        '''for i in range(len(number_list)):
            for j in range(0, len(number_list) -i - 1): #-i because we don't need to compare the last element, -1 because we need to compare the current element with the next one
                if number_list[j] > number_list[j+1]:
                    number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
        return "+".join(map(str, number_list))
                    
        '''

        # use language
        number_list.sort()
        return "+".join(map(str, number_list))
        