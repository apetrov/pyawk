import sys

def count_words_from_stdin():
    word_count = 0
    for line in sys.stdin:
        words = line.split()
        word_count += len(words)
    return word_count

if __name__ == "__main__":
    total_words = count_words_from_stdin()
    print("Total word count:", total_words)
