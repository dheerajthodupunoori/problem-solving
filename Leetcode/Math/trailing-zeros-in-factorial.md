https://leetcode.com/problems/factorial-trailing-zeroes/

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

