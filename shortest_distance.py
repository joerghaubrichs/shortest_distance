import re
from typing import Union

def find_shortest_distance(text: str, word1: str, word2: str, 
                           ignore_case: bool=False) -> Union[int, None]:
    
    flags = re.IGNORECASE if ignore_case else 0
    
    pattern = r'(?:^|\W)%s(.{1,}?)%s(?:\W|$)'
    matches = re.findall(pattern % (word1, word2), text, flags)
    if not word1 == word2:
        matches += re.findall(pattern % (word2, word1), text, flags)

    if matches:
        word_match = re.compile(r'\w+')
        return min(len(word_match.findall(m)) for m in matches)
    else:
        return None
