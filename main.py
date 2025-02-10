with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    to_lowercase = file_contents.lower()
    character_count = []

    def total_characters():
        for i in range(0, len(file_contents)):
            if to_lowercase[i].isalpha():
                exists = False
                for char in character_count:
                    if char["letter"] == to_lowercase[i]:
                        char["amount"] += 1
                        exists = True
                        break
                if not exists:
                    character_count.append({"letter": to_lowercase[i], "amount": 1})

    def sort_on(dict):
        return dict["char"]

    total_characters()
    heading = "--- Begin report of books/frankenstein.txt ---"
    total_words = f"{len(words)} words found in the document \n"
    footer = "--- End report ---"

    print(heading)
    print(total_words)

    for char in character_count:
        print(f"The '{char['letter']}' character was found {char['amount']} times")
    print(footer)
