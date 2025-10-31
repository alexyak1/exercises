'''
String Reflection
A string consisting only of the characters b, d and w is painted on a glass window of a store. Alex walks past the store, standing directly in front of the glass window, and observes string s. Alex then heads inside the store, looks directly at the same glass window, and observes string r.

Alex gives you string s. Your task is to find and output string r.

Example 1
Input:
dwd
Output:
bwb
Example 2
Input:
bbwwwddd
Output:
bbbwwwdd
'''


class Solution(object):
    def solve(self, s:str) -> str:
        end_index = len(s) - 1 
        s = list(s)
        for i in range(len(s)//2):

            if i == end_index:
                continue
           
            left = self.swap_value(s[i])
            right = self.swap_value(s[end_index])

            s[i], s[end_index] = right, left
                
            end_index -= 1
        
        return("".join(s))


    def swap_value(self, letter:str) -> str:
        if letter == "b":
            return "d"
        elif letter == "d":
            return "b"
        else:
            return "w"