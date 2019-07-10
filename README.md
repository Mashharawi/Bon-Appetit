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
