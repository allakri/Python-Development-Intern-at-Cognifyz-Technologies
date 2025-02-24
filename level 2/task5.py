# Task: File Manipulation

# Write a Python program that reads a text
# file and counts the occurrences of each
# word in the file. Display the results in
# alphabetical order along with their
# respective counts.


import string

def count_word_occurrences(file_path):
    """
    Reads a text file, counts the occurrences of each word,
    and displays the results in alphabetical order.
    :param file_path: Path to the text file
    """
    word_count = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                words = line.split()
                
                # Count occurrences of each word
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1
        
        # Display results in alphabetical order
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")
    
    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")  # Get file path from user
    count_word_occurrences(file_path)  # Call function to count words





# solution

"""
Enter the file path: C:\Users\Abhi\Desktop\internship\level 2\random_words.txt
a: 2
ai: 1
also: 1
analytics: 1
and: 6
areas: 1
artificial: 1
businesses: 1
cognifyz: 2
company: 3
cuttingedge: 1
data: 2
delivering: 2
dynamic: 1
enhance: 1
evolving: 1
excels: 1
field: 1
focuses: 1
impactful: 1
in: 3
including: 1
innovative: 1
intelligence: 1
is: 1
knowledge: 1
leading: 1
learning: 1
machine: 1
meet: 1
ml: 1
needs: 1
of: 3
offers: 1
on: 1
products: 1
programs: 1
projects: 1
provides: 1
range: 1
science: 1
services: 1
skills: 1
solutions: 2
specializes: 1
technologies: 2
technology: 1
that: 1
the: 4
these: 1
to: 2
tools: 1
training: 1
wide: 1
"""