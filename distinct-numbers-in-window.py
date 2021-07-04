class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        
        answer = []
        value_index={}
        index_value={}
        
        for i in range(0,B):
            
            value_index[A[i]] = i
            index_value[i] = A[i]
        
        answer.append((len(value_index)))

        print(A)

        print("**********")

        print(value_index)
        print(index_value)
        print("**********")
        
        for j in range(B,len(A)):
            
            temp = j-B
            value = index_value[temp]

            if value in value_index and value_index[value] == temp:
                
                value_index.pop(value)
                value_index[A[j]] = j
                
            else:
                
                value_index[A[j]] = j

            index_value[j] = A[j]
                
            answer.append(len(value_index))

            print(value_index,index_value)
            
        return answer


if __name__=="__main__":
    sol = Solution()
    lst = [2, 7, 7, 81, 81 ]
    k = 1
    print(sol.dNums(lst,k))