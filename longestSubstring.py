def longestSubstring(text):
    '''
    text: string
    returns: the longest substring in alphabetical order
    '''
    longest = text[0]
    current = text[0]
    for letter in text[1:]:
        if letter >= current[-1]:
            current += letter
            if len(current) > len(longest):
                longest = current
        else:
            current = letter
    print ("Longest substring in alphabetical order is:", longest)


