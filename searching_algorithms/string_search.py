# String search
# Naive one
def search(pat, txt):
    substring_length = len(pat)
    string_length = len(txt)

    for i in range(string_length - substring_length + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while j < substring_length:
            if txt[i + j] != pat[j]:
                break
            j += 1

        if j == substring_length:
            print("Pattern found at index ", i)


if __name__ == "__main__":
    search('omg', 'wowomgzomg')
