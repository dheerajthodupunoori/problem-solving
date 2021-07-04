from heapq import heappush,heappop

class ValueIndexes:

    def __init__(self,value,i,j):
        self.value = value
        self.i=i
        self.j=j


    def __lt__(self,other):
        return self.value<other.value

class MaximumSumCombinations:

    def __init__(self,input1,input2,k):
        self.input1=input1
        self.input2=input2
        self.k=k

    def find(self):

        print("Finding k max sum combinations")

        combinations = []
        heap = []
        inserted = set()
        inserted.add((0,0))

        heappush(heap,ValueIndexes(-(self.input1[0]+self.input2[0]),0,0))

        for i in range(self.k):
            popped = heappop(heap)
            combinations.append(-popped.value)

            i,j = popped.i , popped.j+1

            if (i,j) not in inserted and i<len(self.input1) and j<len(self.input2):

                 heappush(heap,ValueIndexes(-(self.input1[i]+self.input2[j]),i,j))
                 inserted.add((i,j))

            i,j = popped.i+1,popped.j

            if (i,j) not in inserted and i<len(self.input1) and j<len(self.input2):

                 heappush(heap,ValueIndexes(-(self.input1[i]+self.input2[j]),i,j))
                 inserted.add((i,j))

        return combinations



if __name__=="__main__":

    input1 = [1, 4, 2, 3]
    input2 = [2, 5, 1, 6]

    # input1 = input1.sort()
    # input2 = input2.sort()

    print(sorted(input1,reverse=True))
    print(sorted(input2,reverse=True))

    combinations = MaximumSumCombinations(sorted(input1,reverse=True),sorted(input2,reverse=True),4)

    result = combinations.find()

    print(result)

