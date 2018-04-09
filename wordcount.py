# put your code here.
def count_words(my_file):
    """
    """
    text = []
    with open(my_file) as text_file: # import the file
        
        for line in text_file:    
            line = line.rstrip()
            words = line.split(' ')  # split each word by a space
            text.extend(words)
        return text
        # initialize empty dictionary
    # loop over list
        # use dictionary.get('word',0) + 1 to track count of words
    # print key, values
        # use .items()
print count_words('test.txt')
