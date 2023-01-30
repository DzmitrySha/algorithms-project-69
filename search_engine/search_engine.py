import re


def search(docs: list, search_word: str) -> list:
    result = []
    for item in docs:
        token = item['text']
        term = re.findall(r'\w+', token)
        for word in term:
            if search_word.lower() == word.lower():
                result.append(item['id'])
                break
    return result
