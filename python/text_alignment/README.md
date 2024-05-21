[]()

| Memory | Time |
| ----- | -------- |
| KB| ms

---
In Python, a string of text can be aligned left, right and center.

**.ljust(width)**

This method returns a left aligned string of length width.
<pre>
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
</pre>
**.center(width)**

This method returns a centered string of length width.
<pre>
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
</pre>
**.rjust(width)**

This method returns a right aligned string of length width.
<pre>
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
</pre>
---
## Task
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

---

## Input Format
A single line containing the thickness value for the logo.

---

## Output Format
Output the desired logo.

---

## Sample Input 0
<pre>
5
</pre>
---

## Sample Output 0
<pre>
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
</pre>