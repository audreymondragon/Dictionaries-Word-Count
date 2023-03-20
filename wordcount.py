"""Count words in file."""


# file = open("test.txt")

# word_counts = {}

# for word in text:
#     word_counts[word] = word_counts.get(word, 0) +1

# return word_counts

file = open("twain.txt")

word_counts = {}

for line in file:
    # rstrip removes the trailing whitespace at the end of each line
    line = line.rstrip()

    # split splits the rstripped line by spaces to get a list of words
    words = line.split()

    for word in words:
        # This will set the word count to what it was +1
        # If it was not found at all, .get(word, 0) returns 0 if the word was not in the dictionary already
        word_counts[word] = word_counts.get(word, 0) +1

for word,count in word_counts.items():
    print(word,count)
