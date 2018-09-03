import unittest

from shortest_distance import find_shortest_distance


class TestFindShortestDistance(unittest.TestCase):

    def test_sample(self):
        """Basic test case"""
        result = find_shortest_distance('bar foo bar foobar bar', 'foo', 'foobar')
        self.assertEqual(1, result)

    def test_sample_reverse(self):
        """Distance should be the same with word parameters in reverse order"""
        result = find_shortest_distance('bar foo bar foobar bar', 'foobar', 'foo')
        self.assertEqual(1, result)

    def test_noword1_match(self):
        """Should return None if word 1 is not found"""
        result = find_shortest_distance('bar foo bar foobar bar', 'NOTHING', 'foo')
        self.assertEqual(None, result)

    def test_noword2_match(self):
        """Should return None if word 2 is not found"""
        result = find_shortest_distance('bar foo bar foobar bar', 'foo', 'NOTHING')
        self.assertEqual(None, result)

    def test_noword_matches(self):
        """Should return None if both words are not found"""
        result = find_shortest_distance('bar foo bar foobar bar', 'NOTHING', 'REALLYNOTHING')
        self.assertEqual(None, result)

    def test_min_distance(self):
        """Check that we return the minimum distance"""
        result = find_shortest_distance('foo bar foofoo bar foofoo', 'foo', 'foofoo')
        self.assertEqual(1, result)

    def test_case_sensitivity(self):
        """Check that ignore_case parameter is used correctly if set to False"""
        result = find_shortest_distance('foo bar Foofoo foofoo', 'foo', 'foofoo', ignore_case=False)
        self.assertEqual(2, result)

    def test_case_insensitivity(self):
        """Check that ignore_case parameter is used correctly if set to True"""
        result = find_shortest_distance('foo bar Foofoo foofoo', 'foo', 'foofoo', ignore_case=True)
        self.assertEqual(1, result)

    def test_same_words(self):
        """Searching for word1==word2 should work"""
        result = find_shortest_distance('foo bar bar foo', 'foo', 'foo')
        self.assertEqual(2, result)

if __name__ == '__main__':
    unittest.main()