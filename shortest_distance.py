import re
from typing import Union

def find_shortest_distance(text: str, word1: str, word2: str, 
                           ignore_case: bool=False) -> Union[int, None]:
    """Shortest word distance calculator

    Finds the shortest distance counted in number of words of two 
    given words in a text.

    Executes in linear time.

    Args:
        text (str): The text to search through
        word1 (str): First word
        word2 (str): Second word
        ignore_case (bool): Ignore case of words matched

    Returns:
        Number of words inbetween. None unless both words are found.
    """
    
    flags = re.IGNORECASE if ignore_case else 0
    
    # Find sequences of word1 followed by whatever string up to word2,
    # and the reverse (from word2 to word1)
    pattern = r'(?:^|\W)%s(.{1,}?)%s(?:\W|$)'
    matches = re.findall(pattern % (word1, word2), text, flags)
    if not word1 == word2:
        matches += re.findall(pattern % (word2, word1), text, flags)

    if matches:
        word_match = re.compile(r'\w+')
        # Count the words found in the matches and return the smallest
        return min(len(word_match.findall(m)) for m in matches)
    else:
        return None


if __name__ == '__main__':
    sample = 'We do value and reward motivation in our development team. Development is a key skill for a DevOp.'
    distance = find_shortest_distance(sample, 'motivation', 'development')
    print("Sample: ", sample)
    print("Distance for 'motivation' and 'development': ", distance)
