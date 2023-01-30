def search(docs: list, search_word: str) -> list:
    result = []
    for item in docs:
        if f" {search_word} " in item['text']:
            result.append(item['id'])
    return result
