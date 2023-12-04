def last_word(s):
    #here i'm splitting the string into parts using spilt function
    words = s.split()
    #here checking if list is empty that is if it doesnt have any words
    if len(words) == 0:
        return 0
    #getting the last word
    last_word = words[-1]
    #returning the length of last word
    return len(last_word)

#input from user
user_input = input("Enter a string: ")

#call the function and print it
result = last_word(user_input)
print(result)
