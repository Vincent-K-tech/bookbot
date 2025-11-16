def get_book_text(path_to_file):
    with open (path_to_file) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

#test


def main(): 
    print(f"Found {get_num_words(get_book_text("books/frankenstein.txt"))} total words")

main()
