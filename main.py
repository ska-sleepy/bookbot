def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return(file_contents)
def count_words():
    return(len(main().split()))

def count_characters():
    text = main().lower()
    character_list = []
    numbered_list = []
    for i in text:
        if i not in character_list:
            character_count = 0
            character_list.append(i)
            for z in text:
                if i == z:
                    character_count += 1
            numbered_list.append(f"{i} : {character_count}")
    joined_list = ", ".join(numbered_list)
    return f"The number of times each charater appears is the following {joined_list}"


    
if __name__ == "__main__":
    print(count_words())
    print(count_characters())
