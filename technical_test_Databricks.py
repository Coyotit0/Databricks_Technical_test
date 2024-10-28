"""
1. Write a query that will display the results below (Note: some columns might be renamed
but use the column names above). It should only show 2020 data and order by driver
points
"""
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# SQL query to retrieve 2020 data and order by driver points
query = """
SELECT circuit_location, grid, position, fastest_lap, points, drivers_name,
       race_name, race_time, race_year, team, race_date
FROM JoinRaceResults
WHERE race_year = 2020
ORDER BY points ASC;
"""

# Execute the query and fetch results
cursor.execute(query)
results = cursor.fetchall()

# Display results
for row in results:
    print(row)

# Close the connection
conn.close()

""""
2. Write a Python function that checks whether a word or phrase is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"
"""

def palindrome(s):

    # Remove spaces and convert to lowercase to remove case sensitivy.
    word = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return word == word[::-1]

# Example usage
print(palindrome("madam"))
print(palindrome("kayak"))
print(palindrome("jack"))
print(palindrome("racecar"))
print(palindrome("nurses run"))
print(palindrome("ewe"))
print(palindrome("hello"))

"""
3.  Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
Note: Pangrams are words or sentences containing every letter of the  alphabet at least once. For example: "The quick brown fox jumps over the
lazy dog"

"""
def pangram(sentence):
    # Define the alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    # Convert the input string to lowercase and create a set of characters
    sentence = sentence.lower()
    characters = set(sentence)

    # Check if all alphabet letters are in the set of characters
    return alphabet.issubset(characters)

#Function Calling
input_sentence = input("Enter a string: ")


if pangram(input_sentence):
    print(f'"{input_sentence}" is a pangram.')
else:
    print(f'"{input_sentence}" is not a pangram.')

print(pangram("The quick brown fox jumps over the lazy dog"))
print(pangram("Hello, world!"))

"""
4. Write a program that takes an integer as input and returns an integer with reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.
"""
def reverse_digits():
    # Get input from the user
    user_input = input("Enter an integer: ")

    # Check if input is a valid integer
    try:
        num = int(user_input)
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    # Convert integer to string and reverse it, handling the negative sign
    if num >= 0:
        reversed_str = str(num)[::-1]
    else:
        reversed_str = '-' + str(num)[:0:-1]

    # Convert the reversed string back to an integer to remove any leading zeros
    reversed_num = int(reversed_str)

    print("Reversed integer:", reversed_num)

# Run the function
reverse_digits()

"""5. Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"
"""
def capitalize_words():
    # Get input from the user
    user_input = input("Enter a string: ")

    # Check if input is a string and contains alphabetic characters
    if not any(char.isalpha() for char in user_input): # Indented this line to align with other statements in the function
        print("Invalid input! Please enter a string containing at least one letter.")
        return
    # Capitalize the first letter of each word
    capitalized_string = user_input.title()

    print("Result:", capitalized_string)

# Run the function
capitalize_words()
