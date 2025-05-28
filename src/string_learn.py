def demonstrate_string_immutability():
    """Example of string immutability."""
    s = "Hello"
    print("Original string:", s)
    try:
        s[0] = "h"  # This will raise an error because strings are immutable
    except TypeError as e:
        print("Error:", e)

def demonstrate_string_concatenation():
    """Example of string concatenation."""
    s1 = "Hello"
    s2 = "World"
    print("Concatenated string:", s1 + ", " + s2 + "!")

def demonstrate_membership_testing():
    """Example of membership testing in strings."""
    s = "Python programming"
    print("'Python' in string:", "Python" in s)
    print("'Java' not in string:", "Java" not in s)

def reverse_string(s: str) -> str:
    """Reverse the given string."""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Check if the given string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s: str) -> int:
    """Count the number of vowels in the given string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print("Demonstrating string immutability:", demonstrate_string_immutability())
print("\nDemonstrating string concatenation:", demonstrate_string_concatenation())
print("\nDemonstrating membership testing:", demonstrate_membership_testing())
test_string = "Hello World"
print("Reversed string:", reverse_string(test_string))
print("\nChecking if a string is a palindrome:", is_palindrome(test_string))
print("\nCounting vowels in a string:", count_vowels(test_string))
