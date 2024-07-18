import string


def is_english_text(text):
    english_count = 0
    chinese_count = 0

    for char in text:
        # Check if character is an English letter
        if char in string.ascii_letters:
            english_count += 1
        # Check if character is a Chinese character
        elif '\u4e00' <= char <= '\u9fff':
            chinese_count += 1
    # print(f'english_count = {english_count}')
    # print(f'chinese_count = {chinese_count}')
    if english_count / 10 > chinese_count:
        print(f'The text is probably in English.')
        return True
    else:
        print(f'The text is probably in Chinese.')
        return False
