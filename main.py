from stats import count_words, count_characters, split_and_sort
import sys

def get_book_text(filepath:str)->str:
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    characters_count = split_and_sort(count_characters(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(*[f"{k}: {v}" for dic in characters_count for k,v in dic.items()], sep='\n')
main()
