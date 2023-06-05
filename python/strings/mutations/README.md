[Mutations](https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true)

---

We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

---

## Example
<pre>
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
</pre>

<pre>
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
</pre>

---

## Task
Read a given string, change the character at a given index and then print the modified string.

---

## Input Format
The first line contains a string, string.
The next line contains an integer position, the index location and a string character, separated by a space.

---

## Sample Input 0
<pre>
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
</pre>
---

## Sample Output 0
<pre>
abrackdabra
</pre>