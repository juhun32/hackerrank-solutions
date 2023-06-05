[ Java Stdin and Stdout I](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/problem?isFullScreen=true)

---
Most HackerRank challenges require you to read input from stdin (standard input) and write output to stdout (standard output).

One popular way to read input from stdin is by using the Scanner class and specifying the Input Stream as System.in. For example:

<pre>
Scanner scanner = new Scanner(System.in);
String myString = scanner.next();
int myInt = scanner.nextInt();
scanner.close();

System.out.println("myString is: " + myString);
System.out.println("myInt is: " + myInt);
</pre>

The code above creates a Scanner object named <code>scanner</code> and uses it to read a String and an int. It then closes the Scanner object because there is no more input to read, and prints to stdout using System.out.println(String). So, if our input is:

<pre>
Hi 5
</pre>
Our code will print:
<pre>
myString is: Hi
myInt is: 5
</pre>
Alternatively, you can use the <code>BufferedReader</code> class.

---
## Task
In this challenge, you must read 3 integers from stdin and then print them to stdout. Each integer must be printed on a new line. To make the problem a little easier, a portion of the code is provided for you in the editor below.

---

## Input Format
There are 3 lines of input, and each line contains a single integer.

---

## Sample Input 0
<pre>
42
100
125
</pre>

---

## Sample Output 0
<pre>
42
100
125
</pre>
