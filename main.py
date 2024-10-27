def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    word_count = count_words(file_contents)
    char_counts = count_chars(file_contents)
    print_report(path, word_count, char_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    counts = {}
    for c in text.lower():
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def print_report(path, word_count, char_counts):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    letter_counts = get_letter_counts(char_counts)
    for x in letter_counts:
        print(f"The '{x["letter"]}' character was found {x["num"]} times")
    print("--- End report ---")

def get_letter_counts(dict):
    letters = [{"letter": c, "num": dict[c]} for c in dict if c.isalpha()]
    letters.sort(reverse=True, key=lambda dict: dict["num"])
    return letters

main()
