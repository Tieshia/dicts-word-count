# put your code here.
def count_words(my_file):
    """
        Prints number of times a word appears in a text.
    """

    word_count = {}  # initialize empty dictionary

    with open(my_file) as text_file:  # import the file

        for line in text_file:
            line = line.rstrip()
            words = line.split()  # split each word by a space
            # loop over list
            for word in words:
                # use dictionary.get('word',0) + 1 to track count of words
                word_count[word] = word_count.get(word, 0) + 1

    # print key, values;  use .iteritems()
    for key, value in word_count.iteritems():
        print key, value

count_words('twain.txt')
