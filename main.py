def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()  # Notice this line is indented!
        print(file_contents)      # This line too!

main()  # This line should not be indented

def count_words(text):

    words = text.split()
    print (len(words))

def count_char(text):
    dict ={}
    for t in text:
        t = t.lower()
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        # Create a dictionary with "char" and "num" keys
        char_data = {"char": char, "num": count}
        # Add it to char_list
        char_list.append(char_data)
    return char_list

# Add your file reading code here
with open("books/frankenstein.txt") as f:
    text = f.read()

# Now use your functions in sequence:
char_dict = count_char(text)
char_list = convert_dict_to_list(char_dict)
char_list.sort(reverse=True, key=sort_on)

# Now add code to print the report
print("--- Begin report of books/frankenstein.txt ---")
# Count words (split text by spaces)
words = text.split()
print(f"{len(words)} words found in the document\n")

# Print character counts
for char_data in char_list:
    char = char_data["char"]
    # Only print if it's an alphabetic character
    if char.isalpha():
        print(f"The '{char}' character was found {char_data['num']} times")
print("--- End report ---")

