# Longest Uncommon Subsequence I

**Tags : Strings**

[Link to the question on Leetcode]: https://leetcode.com/problems/longest-uncommon-subsequence-i/

**Problem Statement**

Given two strings `a` and `b`, return *the length of the **longest uncommon subsequence** between* `a` *and* `b`. If the longest uncommon subsequence does not exist, return `-1`.

An **uncommon subsequence** between two strings is a string that is a **subsequence of one but not the other**.

A **subsequence** of a string `s` is a string that can be obtained after deleting any number of characters from `s`.

- For example, `"abc"` is a subsequence of `"aebdc"` because you can delete the underlined characters in `"aebdc"` to get `"abc"`. Other subsequences of `"aebdc"` include `"aebdc"`, `"aeb"`, and `""` (empty string).



**Example 1:**

```
Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.
```

**Example 2:**

```
Input: a = "aaa", b = "bbb"
Output: 3
Explanation: The longest uncommon subsequences are "aaa" and "bbb".
```

**Example 3:**

```
Input: a = "aaa", b = "aaa"
Output: -1
Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a.
```

 

**Constraints:**

- `1 <= a.length, b.length <= 100`

- `a` and `b` consist of lower-case English letters.

  

***



**Idea**

> **Brute Force Solution:** Generate all the subsequences of both the strings and store the frequency of each subsequence in a hashmap/dictionary. The subsequence whose frequency equal to **1** will be the longest uncommon subsequence. If there is not subsequence with frequency as **1** , then there is no uncommon subsequence for given strings.



> **Optimized Solution:** 
>
> 1. If **both the given strings are equal** then there will not be uncommon subsequences for given strings. In this case we can directly return **-1**
> 2. If the **strings are not equal and length of both the strings are equal** , then one string cannot be the subsequence of other string. In this case we can either return **length of any one of the strings**.
> 3. If **both strings are not equal and length of one string is greater than length of other string**, then in this case we can directly return the **length of the largest string** as the largest string cannot be the subsequence of the smaller string.



***



**Code(Python)**

```python
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        a_length = len(a)
        b_length = len(b)
        return max(a_length,b_length)
```

