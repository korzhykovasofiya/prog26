from analyze_text import read_file, get_words, count_words, frequency


def main():
    file_name = input("Введіть ім'я файлу: ").strip()
    library = input("Бібліотека (nltk або spacy, Enter = nltk): ").strip()

    text, error = read_file(file_name)
    if error:
        print("Помилка:", error)
        return

    words = get_words(text, library)
    if not words:
        print("Помилка: у тексті немає слів.")
        return

    print("Кількість слів:", count_words(words))
    print("Унікальних слів:", len(set(words)))
    print("Частотний словник (топ-20):")
    for word, n in frequency(words):
        print(f"{word} {n}")


if __name__ == "__main__":
    main()