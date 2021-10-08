#Problem 1

#option 1
def reverse_string_1(string_to_reverse):
    reversed_string = string_to_reverse[::-1]
    return reversed_string

string_to_reverse = 'Hello world'
reversed_string = reverse_string_1(string_to_reverse)
print(reversed_string)

#option 2
def reverse_string_2(string_to_reverse):
    for counter in range(len(string_to_reverse) - 1,-1,-1):
        print((string_to_reverse[counter]), end = '')

reverse_string_2(string_to_reverse)

#option 3
print('')
print(''.join(reversed(string_to_reverse)))

#problem 2

#option 1
def capitalize_first(string_to_capitalize):
    split_string = string_to_capitalize.split()
    
    number_of_elements = len(split_string)

    for count in range(0,number_of_elements):
        split_string[count] = (split_string[count][0]).upper() + (split_string[count][1:])

    capitalized_string = ' '.join(split_string)
    print(capitalized_string)

capitalize_first(string_to_reverse)

#option 2
print(string_to_reverse.capitalize())

#Problem 3

def compress_string(string_name):

    string_size = len(string_name)
    elements = 0
    same_count = 1
    result_list = []

    for char in example_string:

        if elements + 1 == string_size:
                result_list.append(f'{same_count}{char}')
                break

        result = example_string[elements] == example_string[elements + 1]
        
        if result is True:
            same_count += 1

        elif result is False:
            result_list.append(f'{same_count}{char}')
            same_count = 1

        elements += 1

    results = ''.join(result_list)
    
    return results

example_string = 'aaabbbbbccccaacccbbbaaabbbaaa'
print(compress_string(example_string))

#Problem 4

def palindrome_check():

    string_to_check = input('Enter a word to see if it is a palindrome: ')
    string_length = len(string_to_check)
    reverse_string = string_to_check[::-1]

    count = 0

    for char in reverse_string:
        
        if char == string_to_check[count]:
            count += 1

            if count == string_length:
                print('This word is a palindrome.')
        
        else:
            print('This is not a palindrome')
            break

palindrome_check()