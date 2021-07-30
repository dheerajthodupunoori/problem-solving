###### https://leetcode.com/problems/map-sum-pairs/

#### Approach:

> Brute force solution for this question is initialize a dictionary in the constructor and whenever an insert method is called add the key to the dictionary if its not present or else update the dictionary with the new value for that key.
>
> Whenever sum method is called run a loop over dictionary and check if the key starts with the prefix , if yes then add the value of that key to the result or else ignore it.



#### Language:Python

```python
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.data = dict()

    def insert(self, key: str, val: int) -> None:
        self.data[key]=val
        

    def sum(self, prefix: str) -> int:
        
        result = 0
        
        for key in self.data:
            if key.startswith(prefix):
                result+=self.data[key]
                
        return result
```

