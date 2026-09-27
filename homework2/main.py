from collections import Counter
import re

with open("lab2709/text.txt", "rt", encoding="utf-8") as file:
    example = file.read()

def get_text_analysis(text: str) -> str:
    words = re.findall(r"\b\w+\b", text.lower())
    print(f"Кількість слів у тексті: {len(words)}")

    counted_words = Counter(words)
    total = sum(counted_words.values())

    print("Частотний словник:")
    for word, count in counted_words.most_common(20):
        percentage = (count/total)*100
        print(f"{word}: {count} ({percentage:.1f}%)")

    word_length = []
    for word in words:
        word_length.append(len(word))
    min_len = min(word_length)
    max_len = max(word_length)

    shortest_words = set()
    longest_words = set()
    for word in words:
        if len(word) == min_len:
            shortest_words.add(word)
        elif len(word) == max_len:
            longest_words.add(word)
    
    print(f"Найкоротші слова: {shortest_words}")
    print(f"Найдовші слова: {longest_words}")

    least_common = counted_words.most_common()[-10:]
    print(f"Унікальні слова (вживані найменше): {least_common}")
    letters = re.findall(r"[^\d\W]", text.lower())
    print(f"Використані літери: {set(letters)}")
    counted_letters = Counter(letters)
    print(f"Літера, що зустрічалася найчастіше: {counted_letters.most_common(1)}")


get_text_analysis(example)