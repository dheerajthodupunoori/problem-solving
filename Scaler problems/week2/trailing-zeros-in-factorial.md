# Trailing Zeros in Factorial

### **Problem Description**

Given an integer **A**, return the number of trailing zeroes in **A!** i.e. factorial of A.

**Note:** Your solution should run in logarithmic time complexity.

**Problem Constraints**

1 <= A <= 109

**Input Format**

First and only argument is a single integer A.

**Output Format**

Return a single integer denoting number of zeroes.

**Example Input**

Input 1

```
 A = 5
```

Input 2:

```
 A = 6
```

**Example Output**

Output 1:

```
 1
```

Output 2:

```
 1
```

**Example Explanation**

Explanation 1:

```
 A! = 120.
 Number of trailing zeros = 1. So, return 1.
```

Explanation 2:

```
 A! = 720 
 Number of trailing zeros = 1. So, return 1.
```

#### Language:Python

```python
class FactorialTrailingZeros:

  def __init__(self,number):
    self.number=number
    self.count=0
    self.getTrailingZeros()

  def getTrailingZeros(self):

    while self.number>=5:

      self.number = self.number//5
      self.count +=self.number

trailing_zeros = FactorialTrailingZeros(5)
print(trailing_zeros.count)
trailing_zeros = FactorialTrailingZeros(10)
print(trailing_zeros.count)
trailing_zeros = FactorialTrailingZeros(15)
print(trailing_zeros.count)
trailing_zeros = FactorialTrailingZeros(20)
print(trailing_zeros.count)
trailing_zeros = FactorialTrailingZeros(25)
print(trailing_zeros.count)

trailing_zeros = FactorialTrailingZeros(100)
print(trailing_zeros.count)
trailing_zeros = FactorialTrailingZeros(1000)
print(trailing_zeros.count)
trailing_zeros = FactorialTrailingZeros(1)
print(trailing_zeros.count)
trailing_zeros = FactorialTrailingZeros(5)
print(trailing_zeros.count)
```

