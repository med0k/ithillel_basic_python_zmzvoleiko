import random


def permute(text: str) -> str:
    words = text.split()
    result = []

    for word in words:
        if len(word) <= 3:
            result.append(word)
            continue

        first_char = word[0]
        last_char = word[-1]
        middle_chars = list(word[1:-1])
        shuffled_chars = middle_chars.copy()

        while shuffled_chars == middle_chars:
            random.shuffle(shuffled_chars)
        result_word = first_char + ''.join(shuffled_chars) + last_char
        result.append(result_word)

    return ' '.join(result)


def main():
    text = "За результатами дослідженнь одного англійського університету, не має значення, в якому порядку \n" \
           "розташовані літери у слові. Головне, щоб перша та остання літери були на своєму місці. Решта літер \n" \
           "можуть знаходитися в абсолютно випадковому порядку, все одно текст читається без проблем. Причиною\n" \
           " цього є те, що ми читаємо не кожну букву окремо, а все слово разом."

    permuted_text = permute(text)
    print(permuted_text)


if __name__ == "__main__":
    main()
