def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

        print(word_count(file_contents))
        char_count = character_count(file_contents)
        print(char_count)


def word_count(text):
    words = len(text.split())
    return words

def character_count(text):
    lowered_text = text.lower()
    character_dict = {}
    for x in range(ord('a'), ord('z') + 1):
        character_dict[chr(x)] = 0

    for x in lowered_text:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            character_dict[x] += 1

    return character_dict


main()
