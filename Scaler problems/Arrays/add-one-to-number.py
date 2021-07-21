# https://www.interviewbit.com/problems/add-one-to-number/



from typing import List

class AddOne:

    def __init__(self,number:List[int]):

        self.number = number

    def addOne(self) -> str:

        result = ""

        carry = 1

        length = len(self.number)

        for i in range(length-1,-1,-1):

            if self.number[i]+carry > 9:

                carry = 1
                result += str(0)

            else:

                result += str(self.number[i]+carry)
                carry = 0

        if carry == 1:
            result += str(carry)

        result = result.rstrip("0")

        return list(result[::-1])



numbers = [0,0,1,1,0]

add  = AddOne(numbers)
print(add.addOne())