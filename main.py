def get_book_text(path_to_file):
    with open (path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    text.split()
    return len(text)




def main(): 
    print(f"Found {count_words(get_book_text("books/frankenstein.txt"))} total words")

main()
