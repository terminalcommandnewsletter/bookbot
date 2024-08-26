def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    print(f"--- Begin report of {file_path} ---")
    print(f"{get_num_words(file_contents)} words found in the document")
    print()
    character_frequency_dict = get_character_frequency(file_contents)
    sorted_character_frequency_list = character_frequency_dict_to_sorted_list(
        character_frequency_dict
    )
    for i in sorted_character_frequency_list:
        if i["character"].isalpha():
            print(f"The '{i['character']}' character was found {i['frequency']} times")
    print("--- End report ---")


def get_num_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(d):
    return d["frequency"]


def character_frequency_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for i in chars_dict:
        sorted_list.append({"character": i, "frequency": chars_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_character_frequency(text):
    freq_table = {}
    text = text.lower()
    for char in text:
        if char not in freq_table:
            freq_table[char] = 0
        freq_table[char] = freq_table[char] + 1
    return freq_table


if __name__ == "__main__":
    main()
