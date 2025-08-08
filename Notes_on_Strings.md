# WORKING WITH STRINGS

- String is a sequence of characters
- The word sequence implies that every character in a string is indexed.
- Slicing a string:
    `string[start:end:step]`
- Duplicating a string:
    `string * int`
- Searching a string for substring:
    `'substring' in string`
    - if substring is in string it returns True; otherwise False.
- looping over characters of a string:
```
    for char in string:
        print(char)
````

##### string methods
1. isalpha()
    - Returns True if all characters are letters
2. islower()
    - Returns True if all the letters are lowercase
3. isupper()
    - Returns True if all the letters are uppercase
4. isdigit()
    - Returns True if all the characters are digits
5. startswith(str)
    - Returns True if a string starts with specified string.
6. endswith(str)
    - Returns True if a string ends with specified string.
7. upper()
    - Converts all the letters to uppercase
8. lower()
    - Converts all the letters to lowercase
9. title()
    - Converts the string to title.
10. lstrip()
    - Removes spaces from the left side of the string.
11. rstrip()
    - Removes spaces from the right side of the string.
12. strip()
    - Removes spaces from both sides of the string.
13. ljust(width)
    - Justify text with the specified width towards left side.
14. rjust(width)
    - Justify text with the specified width towards right side.
15. center(width)
    - Justify text with the specified width towards center.

- The find(str[, start][, end]) method
    - it searches for the specified in the larger string, and then returns the index number of the specified string.
    - The optional start and end arguments specify the start and end index numbers to begin the search and end the search.
    - if the str is not found in the larger string then it returns -1

- replace(old, new[, num])
    - old: specify the substring to be replaced
    - new: specify the replacing substring
    - num: number of occurances to replace

- split([delimiter][, num])
    - delimiter: a character or string that delimits (separates) parts of a string. By default, delimiter is a space.
    - num: number of delimiters to be split

- str.join(sequence)
    - The 'str' specified join the each item from the 'sequence'.

    