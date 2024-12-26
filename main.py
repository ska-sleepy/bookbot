book_title = input("Enter the name of the book file (including .txt): ")
def main():
    try:   
        with open(f"books/{book_title}") as f:
            file_contents = f.read()
        return(file_contents)
    except FileNotFoundError:
        print(f"Error: The file '{book_title}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def count_words():
    return(len(main().split()))

character_list = []
def count_characters():
    text = main().lower()
    chars = {}
    for i in text:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

def report():
    dictionary = count_characters()
    sorted_dict = dict(sorted(dictionary.items()))
    keyslist = list(sorted_dict.keys())
    valuelist = list(sorted_dict.values())
    part_1 = (f"--- begin report of frankenstein.txt ---\n{count_words()} words found in the document \n")
    char_report = []
    for i in range(len(keyslist)):
        if keyslist[i].isalpha():
            char_report.append(f"The '{keyslist[i]}' charcter was found '{valuelist[i]}' times")
    part_2 = "\n".join(char_report)
    return (f"{part_1}\n{part_2} \n--- End report ---")
    
if __name__ == "__main__":
    print(report())