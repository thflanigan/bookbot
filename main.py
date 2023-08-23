def main():
    book = "books/Frankenstein.rtf"
    text = get_book_text(book)
    make_report(book, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(file_contents):
    words = file_contents.split()
    count = 0
    for i in words:
        count += 1
    return count

def letters(text_in):
    letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    letter_count = {}
    for letter in letters:
        letter_count[letter] = 0
    text_split = text_in.split()
    for text in text_split:
        for letter in text:
            if letter.lower() in letters:
                letter_count[letter.lower()] += 1 

    return letter_count
            
def make_report(book, text):
    letter_count = letters(text)
    word_count = count_words(text)
    letter_list = letter_count.keys()
    print(f"--- Begin Report on {book}---")
    print(f"There are {word_count} words in the document")
    for letter in letter_list:
        print(f"The letter {letter} is used {letter_count[letter]}")
    print("---End of Report---")
        
main()




