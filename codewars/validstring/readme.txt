You are given a sequence of valid words and a string. Test if the string is made up by one or more words from the array.

Task
Test if the string can be entirely formed by concatenating words of the dictionary.

For example:

string[] dictionary = ["code", "wars"]; 

string s = "codewars"; // true -> match 'code', 'wars'

string s1 = "codewar"; // false -> match 'code', unmatched 'war'