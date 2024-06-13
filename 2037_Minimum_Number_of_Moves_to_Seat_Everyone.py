from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sorted_seats=sorted(seats)
        sorted_students=sorted(students)
        
        return sum([ abs(sorted_seats[i]-sorted_students[i]) for i in range(len(seats))])
    
seats = [3,1,5] 
students = [2,7,4]
s=Solution()
print(s.minMovesToSeat(seats,students))