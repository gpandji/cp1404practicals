"""
Word Occurrences
Estimate: 45 minutes
Actual:   27 minutes
"""


def main():
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    longest_word_length = find_longest_word_length(word_counts)
    for word in sorted(word_counts):
        print(f"{word:{longest_word_length}} : {word_counts[word]}")


def count_word_occurrences(text):
    """Count the occurrences of each word in the given text."""
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def find_longest_word_length(word_counts):
    """Find the length of the longest word in the word_counts dictionary."""
    longest_word_length = max(len(word) for word in word_counts)
    return longest_word_length


main()