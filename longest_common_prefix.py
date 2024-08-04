# a = 'thejaswi'
# b = 'thejasw'
# c = 'thejas'
# min_lenth = min(len(a),len(b),len(c))
# print(min_lenth)
# for i in range(min_lenth):
#     if a[i]!=b[i]!=c[i]:
#         pass
# print(a[:min_lenth])
#
# # print(a[1])
#
#

def longest_common_prefix(strings):
    if not strings:
        return ""

    # Find the shortest string in the list
    smallest_string = min(strings, key=len)

    # Initialize the prefix as an empty string
    prefix = ""

    # Iterate through each character position up to the length of the shortest string
    for i in range(len(smallest_string)):
        # Get the character from the first string
        current_char = smallest_string[i]
        print(current_char)

        # Check if this character is the same in all strings
        if all(s[i] == current_char for s in strings):
            prefix += current_char
        else:
            break

    return prefix


# Example usage:
strings = ['appale', 'appa', 'appayya']
print(longest_common_prefix(strings))  # Output: "app"