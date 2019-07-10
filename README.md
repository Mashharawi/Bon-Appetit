# Bon-Appetit
Bon Appetit


Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: . Anna declines to eat item  which costs . If Brian calculates the bill correctly, Anna will pay . If he includes the cost of , he will calculate . In the second case, he should refund  to Anna.

Function Description

Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill
Input Format

The first line contains two space-separated integers  and , the number of items ordered and the -based index of the item that Anna did not eat. 
The second line contains  space-separated integers  where . 
The third line contains an integer, , the amount of money that Brian charged Anna for her share of the bill.



The amount of money due Anna will always be an integer
Output Format

If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., ) that Brian must refund to Anna. This will always be an integer.

Sample Input 0

4 1
3 10 2 9
12
Sample Output 0

5



Sample Input 1

4 1
3 10 2 9
7
Sample Output 1

Bon Appetit



Mash
explain list(map(int, input().strip().split()))[:I]
Let us break it down.

input()
This is used to fetch input from the user. In this case. We are expecting the user to provide a list of integers. How do I know? Look next.

input().strip()
This will eliminate trailing spaces from the user input, if they are there. Why is it required? Because some users will do that and that might break your program.

Remember that input() will cast the input as string. So, now we have a string of integers like so: “1 2 4 42”

input.strip().split()
split() is used to create a Python list out of a string. If no delimiter is given, this breaks the string by spaces. So, now we have: [“1”, “2”, “4”, “42”]

map(int, input().strip().split())
map() takes two arguments. The first one is the method to apply, the second one is the data to apply it to. By this understanding, we can see this is doing nothing but typecasting every element of the list to an integer value. Since map returns the data type it was applied to, the list() method applied over map() is redundant. So now we have covered the following:

list(map(int, input().strip().split()))
And we have: [1, 2, 4, 42]

Note the missing quotes. This means the elements are now all int.

Now, the last bit.

list(map(int, input().strip().split()))[:I]
takes the list we have obtained and returns only the first I elements.

Neat. Right?


2 explain
input() waits for the user to type something, and returns it as a string.
strip() removes whitespace and newlines from the ends of that string and returns the result. 
split() splits that string into a list of parts. If you don't give any arguments, it splits on any whitespace. 
map() takes two arguments: A function and a list. In this case the function is int, and the list is the one from above. It executes the function once on each thing in the list, and returns the result. In this casse the function is int, which converts its argument to an integer (a whole number).
list() converts its argument to a list. 
This is to work around a difference between python 2 and 3: In 2, map returns a list (so converting it to a list is redundant but harmless). In 3, map returns an iterator: An object you can repeatedly asked for its next value. (It saves memory by only running the function on the next thing in its input when asked for the result.) Converting it to a list forces it to run through everything immediately. 
[:I] returns the first I elements of a list, assuming that I contains a number.

So. It reads a line from the keyboard, trims away whitespace at the ends, splits it on whitespace, runs int() on each part (to convert it from a string to a number), forces it to be a list to work around a 2/3 difference, and only keeps the I first numbers. In short, it reads a list of at most I numbers from the keyboard.
