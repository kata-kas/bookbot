def count_words(text:str)->int:
    return len(text.split())

def count_characters(text:str)->int:
    characters = list(text.lower())
    unique_characters = set(characters)
    ledger = {}
    for char in unique_characters:
        ledger[char] = characters.count(char)
    return ledger

def split_and_sort(dic: dict)->list:
    splitted = [{k: v} for k, v in dic.items()]
    filtered = filter(lambda x: list(x.keys())[0].isalpha(),splitted)
    return sorted(filtered, key=lambda x: list(x.keys())[0])
