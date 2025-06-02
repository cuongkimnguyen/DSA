# String in Python are immutable, meaning they cannot be changed after creation.
# However, you can create new strings based on existing ones.
# This script demonstrates various string operations in Python.
def demonstrate_string_immutability():
    s = "Hello"
    print("Original string:", s)
    try:
        s[0] = "h"  # This will raise an error because strings are immutable
    except TypeError as e:
        print("Error:", e)

# String in Python are immutable, meaning they cannot be changed after creation.
# When concatenating strings, a new string is created rather than modifying the original.
def demonstrate_string_concatenation():
    s1 = "Hello"
    s2 = "World"
    print("Concatenated string:", s1 + ", " + s2 + "!")

# Python checks for substring existence in a parent string using the `in` and `not in` operators.
# These operators return a boolean value indicating whether the substring is found in the parent string.
def demonstrate_membership_testing():
    s = "Python programming"
    print("'Python' in string:", "Python" in s)
    print("'Java' not in string:", "Java" not in s)

def reverse_string(s: str) -> str:
    return s[::-1]

# This function reverses the given string using slicing.
# It returns a new string that is the reverse of the input string.
# It uses the slicing technique where `s[::-1]` creates a new string with characters in reverse order.
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print("Demonstrating string immutability:", demonstrate_string_immutability())
print("\nDemonstrating string concatenation:", demonstrate_string_concatenation())
print("\nDemonstrating membership testing:", demonstrate_membership_testing())
test_string = "Hello World"
print("Reversed string:", reverse_string(test_string))
print("\nChecking if a string is a palindrome:", is_palindrome(test_string))
print("\nCounting vowels in a string:", count_vowels(test_string))

def convert_to_camel_case(sentence: str) -> str:
    words = sentence.split()
    if not words:
        return ""
    # Capitalize the first letter of each word except the first one
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

# Example usage
sentence = "convert this sentence to camel case"
print("\nConverted to camel case:", convert_to_camel_case(sentence))