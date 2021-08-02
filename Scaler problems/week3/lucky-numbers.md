### Lucky Numbers



**Problem Description**

A **lucky number** is a number which has exactly **2 distinct** prime divisors.

You are given a number **A** and you need to determine the **count** of lucky numbers between the range 1 to A (both inclusive).



**Problem Constraints**

​	1 <= A <= 50000



**Input Format**

​	The first and only argument is an integer A.



**Output Format**

​	Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.



**Example Input**

Input 1:

```
 A = 8
```

Input 2:

```
 A = 12
```

**Example Output**

Output 1:

```
 1
```

Output 2:

```
 3
```

**Example Explanation**

Explanation 1:

```
 Between [1, 8] there is only 1 lucky number i.e 6.
 6 has 2 distinct prime factors i.e 2 and 3.
```

Explanation 2:

```
 Between [1, 12] there are 3 lucky number: 6, 10 and 12.
```



##### Executable code link 

[Executable link]: https://replit.com/@DheerajThodupun/lucky-numbers#main.py	"Lucky Numbers"



#### Approach

> The question is to find out numbers which had exactly two distinct prime factors.
>
> Brute force approach is , for every number find the number of unique/distinct prime factors it has , if it has exactly two distinct prime factors increment the result by 1 and at the end return the result.
>
> 1. Initialize the result variable as "0".
> 2. Start traversing from **1->A**.
> 3. for every number find the number of unique prime factors.
>    1. if it has exactly 2 unique prime factors , increment the result by 1.
>    2. else continue with the next number.



> Optimized solution is as follows:
>
> 1. Initialize a list with the size of **a+1** with default values as "0" , the value at each index indicates the number of prime factors that number has. If the value at particular index is **zero**, then that number is **prime number**.
> 2. Now if a number is prime number(if value at index is "0")
>    1. Increment the count of all the multiples of that number by 1
> 3. Now you have generated an array , which has count of prime number it has for every number.
>    1. Traverse that array and check if the value at each index , if it is equal to **2**, then increment the result by 1
> 4. Return the result



#### Code

```python
class LuckyNumbers:

  def __init__(self,a):
    self.a=a
    self.getLuckyNumbers()

  def getLuckyNumbers(self):
    sieve = [0]*(self.a+1)
    for i in range(2,self.a):
      if sieve[i] == 0:
        for j in range(i+i,self.a+1,i):
          sieve[j] += 1
    count = 0

    for item in sieve:
      if item ==2:
        count+=1
    print(count)

lucky_numbers = LuckyNumbers(15)

```