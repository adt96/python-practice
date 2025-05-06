import re
'''
✅ 2. Basic Functions & Examples
🔹 re.search(): Search for pattern anywhere in the string
'''

text = "My email is user@example.com"
match = re.search(r'\w+@\w+\.\w+', text)
print(match.group())  # Output: user@example.com

'''
🔹 re.match(): Match pattern at the beginning of string

'''

match = re.match(r'\d+', '123abc')
print(match.group())  # Output: 123


match = re.match(r'\d+', 'abc123')
print(match)  # Output: None


'''
 re.findall(): Find all non-overlapping matches

'''
text = "123 and 456 and 789"
numbers = re.findall(r'\d+', text)
print(numbers)  # Output: ['123', '456', '789']

'''''
✅ 3. Common Regex Patterns
Pattern	Meaning	Example Match
\d	Digit (0–9)	    5
\w	Word character (a-z, A-Z, 0-9)	    hello123
\s	Whitespace	(space, tab)
.	Any character except newline	a, 1, #
*	0 or more	ca*t matches ct, cat, caaat
+	1 or more	ca+t
?	0 or 1	ca?t
[]	Match any in set	[aeiou]
^ / $	Start / end of string	^Hi, end$
'''

'''
🔹 re.sub(): Replace pattern with another string
'''
text = "This is a test. Test this string."
result = re.sub(r'test', 'sample', text, flags=re.IGNORECASE)
print(result)
# Output: This is a sample. sample this string.

'''
🔹 re.split(): Split string by a regex pattern
'''
text = "one, two; three:four"
parts = re.split(r'[;,: ]+', text)
print(parts)  # Output: ['one', 'two', 'three', 'four']


def is_strong_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$'
    return bool(re.match(pattern, password))

# Test cases
print(is_strong_password("Hello123!"))  # True
print(is_strong_password("weakpass"))   # False

'''
🧠 Explanation:
(?=.*[a-z]) — at least one lowercase letter

(?=.*[A-Z]) — at least one uppercase letter

(?=.*\d) — at least one digit

(?=.*[@$!%*#?&]) — at least one special character

{8,} — minimum 8 characters

'''