import string
from typing import List

def is_english_text(text: str) -> bool:
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

def infer_prompt_type(batch_strs: List[str], input_file: str) -> str:
    if not (input_file.endswith(".md") or input_file.endswith(".markdown")):
        return "txt"
    all_batch_is_txt = True
    for text in batch_strs:
        if text.strip().startswith("#"):
            all_batch_is_txt = False
            break
    if all_batch_is_txt:
        return "txt"
    else:
        return "md"