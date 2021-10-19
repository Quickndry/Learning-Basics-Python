A list S will be given. You need to generate a list T from it by following the given process:

Remove the first and last element from the list S and add them to the list T.
Reverse the list S
Repeat the process until list S gets emptied.
Example
S = [1,2,3,4,5,6]
T = []

S = [2,3,4,5] => [5,4,3,2]
T = [1,6]

S = [4,3] => [3,4]
T = [1,6,5,2]

S = []
T = [1,6,5,2,3,4]
return T
BF Users:
Input will be a string

1<=Input string length<100

The Input will consist of alphabets (Upper and lowercase), Numbers and special characters.

The input will be terminated with a null character for EOF.

Note
List given will never be empty.
size of S goes up to 10^6
Keep the efficiency of your code in mind