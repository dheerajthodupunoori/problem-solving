#### Odd Fibonacci

**Problem Description**

Given two integers **A** and **B** representing an interval **[A, B]**.

Fibonacci sequence is a sequence whose definition is as follows:

**F[1] = 1 , F[2] = 1**

**F[i] = F[i-1] + F[i-2] for i > 2**

Your task is to find the count of integers **x** in the range **[A, B]** such that **F[x]** is **odd**.

**Problem Constraints**

- 1 <= A <= 109
- 1 <= B <= 109
- A <= B



**Input Format**

The first argument given is an integer **A**.

The second argument given is an integer **B**.

**Output Format**

Return the count of integers x in the range [A, B] such that F[x] is odd.

**Example Input**

Input 1:

```
 A = 2
 B = 6
```

Input 2:

```
 A = 6
 B = 20
```

**Example Output**

Output 1:

```
 3
```

Output 2:

```
 10
```

**Example Explanation**

Explanation 1:

```
 All x and their F[x] values:
    x = 2, F[x] = 1
    x = 3, F[x] = 2
    x = 4, F[x] = 3
    x = 5, F[x] = 5
    x = 6, F[x] = 8
 From the above values only three values are odd.
```



#### Approach

> The brute force approach for this problem would be just finding the Fibonacci of all the numbers into an temporary array.
>
> Next traverse that array and check if the Fibonacci value is odd , then increment the result by 1.After traversing return the result which will hold the number of odd numbers in the given interval 



> Above approach would be of **O(B) time and space complexity**. This problem can also be solved in **O(1) time and space complexity**.



> If we write the Fibonacci sequence for some of the number then we can observe that,
>
> F(0) = 0 
>
> F(1) = 1
>
> F(2) = 1
>
> F(3) = 2
>
> F(4) = 3
>
> F(5) = 5
>
> F(6) = 8
>
> F(7) = 13
>
> F(8) = 21
>
> F(9) = 34
>
> F(10) = 55
>
> If we observe above sequence , then we say that Fibonacci values always occur as pair of **(ODD,ODD,EVEN)**
>
> With this observation we just need to find out the number of odd number from **1->B** and substract this value with the number of odd numbers from **1->(A-1)**.



[You can run the code at this url]: https://replit.com/@DheerajThodupun/odd-fibonacci#main.py	"Odd Fibonacci"



#### Solution

```python
class OddFibonacci:

  def __init__(self,a,b):
    self.a=a
    self.b=b
    print(self.getOddFibCount())

  def getOddFibCount(self):
    return self.getOddCount(self.b)-self.getOddCount(self.a-1)

  def getOddCount(self,number):
    if number%3!=0:
      remainder = number//3
      return (number//3) + remainder
    else:
      return (number//3)*2

odd_fibonacci = OddFibonacci(10,20)
```

