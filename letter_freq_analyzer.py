def char_count(sentence):
    # Initialize the dictionary
    char_dict = {}

    # Iterate over each character in the sentence
    for char in sentence:
        # If the character is already in the dictionary, increment its value
        if char in char_dict:
            char_dict[char] += 1
        # If the character is not in the dictionary, add it with a value of 1
        else:
            char_dict[char] = 1

    # Print the key:value pairs of the dictionary
    for key, value in char_dict.items():
        print("'{}': {}".format(key, value))

# Test the function
char_count('Hello, World!')

