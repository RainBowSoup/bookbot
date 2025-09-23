def get_num_words(text):
    print(f"Found {len(text.split())} total words")
    return len(text.split())

def num_char(text):
    char_dict = {}
    for i in text.split():
        for j in i:
            character = j.lower()
            if character not in char_dict:
                char_dict[character] = 1
            else:
                char_dict[character] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def report(char_dict):
    report_list = []
    for i in char_dict:
        report_list.append({"name": i, "num": char_dict[i]})
    return report_list