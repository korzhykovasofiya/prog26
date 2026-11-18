import pytest

from analyze_text import count_words, frequency, get_words, read_file


@pytest.mark.parametrize(
    "text, expected",
    [
        ("The cat sat on the mat. The end!", 8),
        ("Привіт, світе! Це тест.", 4),
        ("Hello, world! Привіт, світе! 123", 4),
        ("М'яч летить. М’яч котиться.", 4),
    ],
)
def test_word_count(text, expected):
    assert count_words(get_words(text)) == expected


@pytest.mark.parametrize("text", ["", "   \n\t ", "123 !!! ???"])
def test_text_without_words(text):
    assert get_words(text) == []


def test_missing_file():
    text, error = read_file("no_such_file_12345.txt")
    assert text is None
    assert error


def test_empty_file(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_text("   ", encoding="utf-8")
    text, error = read_file(str(path))
    assert text is None
    assert error


def test_read_file(tmp_path):
    path = tmp_path / "text.txt"
    path.write_text("Привіт, світе! Привіт!", encoding="utf-8")
    text, error = read_file(str(path))
    assert error is None
    assert dict(frequency(get_words(text)))["привіт"] == 2


def test_wrong_encoding(tmp_path):
    path = tmp_path / "bad.txt"
    path.write_bytes("привіт".encode("cp1251"))
    text, error = read_file(str(path))
    assert text is None
    assert error