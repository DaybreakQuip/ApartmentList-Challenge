import unittest
import Social
#Test Files for Social (the actual solver for this problem)
def traversal_word_check(tree, words_list):
    #Used to see if all words are in trie by traversing the whole tree and appending it to words_list
    parent = tree
    if tree.word is not None:
        words_list.append(tree.word)
    for i in tree.children:
        traversal_word_check(tree.children[i], words_list)
    return words_list

def set_up_and_check_returns(social_links, words_to_find, text = None):
    #Used to see if the number of neighbors is correct
    if text is None:
        tree = Social.set_up_tree(social_links)
    else:
        social_links = Social.set_up_dictionary_from_text(text)
        tree = Social.set_up_tree(social_links)
    friends = Social.find_all_links(tree, words_to_find)
    return friends

class TestSetup(unittest.TestCase):
    def setup_checker(self,social_links, expected_keys):
        #Used to see if tree was set up correctly, by checking the first Trie's children and all the words inside trie
        tree = Social.set_up_tree(social_links)
        tree_keys = tree.children.keys()
        self.assertEqual(list(tree_keys), expected_keys)
        words = traversal_word_check(tree, [])
        self.assertEqual(set(words), set(social_links))

    def test_01(self):
        social_links = ['HI', 'HERE', 'THERE', 'HER', 'HE', 'SHE', 'HEAR', 'HALLOW']
        self.setup_checker(social_links, ['H','T','S'])
    def test_02(self):
        social_links = ['FIST', 'FISTS', 'LISTS', 'LISTY', 'LIT', 'LITAI', 'LITANIES', 'LITANY', 'LITAS', 'LITCHI', 'LITCHIS', 'LUSTY', 'LISTS']
        self.setup_checker(social_links, ['F', 'L'])
    def test_03(self):
        social_links = Social.set_up_dictionary_from_text('eighth_dictionary.txt')
        self.setup_checker(social_links, ['G', 'H', 'I', 'J', 'K', 'L'])
    def test_04(self):
        social_links = Social.set_up_dictionary_from_text('half_dictionary.txt')
        self.setup_checker(social_links, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])

class TinyTests(unittest.TestCase):
    def test_simple_01(self):
        social_links = ['HI', 'HERE', 'THERE', 'HER', 'HE', 'SHE', 'HEAR', 'HALLOW']
        friends = set_up_and_check_returns(social_links, 'HI')
        self.assertEqual(friends, 7)
    def test_simple_02(self):
        social_links = ['HI', 'HERE', 'THERE', 'HER', 'HE', 'SHE', 'HEAR', 'HALLOW']
        friends = set_up_and_check_returns(social_links, 'HALLOW')
        self.assertEqual(friends, 1)
    def test_simple_03(self):
        social_links = ['FIST', 'FISTS', 'LISTS', 'LISTY','LIT','LITAI', 'LITANIES', 'LITANY','LITAS','LITCHI', 'LITCHIS','LUSTY', 'LISTS']
        friends = set_up_and_check_returns(social_links, 'LISTY')
        self.assertEqual(friends, 5)
    def test_simple_04(self):
        social_links = ['FIST', 'FISTS', 'LISTS', 'LISTY', 'LIT', 'LITAI', 'LITANIES', 'LITANY', 'LITAS', 'LITCHI', 'LITCHIS', 'LUSTY', 'LISTS']
        friends = set_up_and_check_returns(social_links, 'LUSTY')
        self.assertEqual(friends, 5)

class SmallTests(unittest.TestCase):
    def test_small_01(self):
        friends = set_up_and_check_returns(None, 'LISTY', 'eighth_dictionary.txt')
        self.assertEqual(friends, 5132)
    def test_small_02(self):
        friends = set_up_and_check_returns(None, 'GROUNDS', 'eighth_dictionary.txt')
        self.assertEqual(friends, 1)
    def test_small_03(self):
        friends = set_up_and_check_returns(None, 'GROUNDSELS', 'eighth_dictionary.txt')
        self.assertEqual(friends, 2)
    def test_small_04(self):
        friends = set_up_and_check_returns(None, 'GROWLED', 'eighth_dictionary.txt')
        self.assertEqual(friends, 6)

class MediumTests(unittest.TestCase):
    def test_medium_01(self):
        friends = set_up_and_check_returns(None, 'LISTY', 'quarter_dictionary.txt')
        self.assertEqual(friends, 11008)
    def test_medium_02(self):
        friends = set_up_and_check_returns(None, 'DISTASTE', 'quarter_dictionary.txt')
        self.assertEqual(friends, 3)
    def test_medium_03(self):
        friends = set_up_and_check_returns(None, 'GENERA', 'quarter_dictionary.txt')
        self.assertEqual(friends, 5)
    def test_medium_04(self):
        friends = set_up_and_check_returns(None, 'GRIND', 'quarter_dictionary.txt')
        self.assertEqual(friends, 11008)

class LargeTests(unittest.TestCase):
    def test_large_01(self):
        friends = set_up_and_check_returns(None, 'LISTY', 'half_dictionary.txt')
        self.assertEqual(friends, 22741)
    def test_large_02(self):
        friends = set_up_and_check_returns(None, 'ABATES', 'half_dictionary.txt')
        self.assertEqual(friends, 22741)
    def test_large_03(self):
        friends = set_up_and_check_returns(None, 'EPISCIA', 'half_dictionary.txt')
        self.assertEqual(friends, 2)
    def test_large_04(self):
        friends = set_up_and_check_returns(None, 'HALL', 'half_dictionary.txt')
        self.assertEqual(friends, 22741)

class AllTests(unittest.TestCase):
    def test_all_01(self):
        friends = set_up_and_check_returns(None, 'LISTY', 'dictionary.txt')
        self.assertEqual(friends, 51710)
    def test_all_02(self):
        friends = set_up_and_check_returns(None, 'GROUNDS', 'dictionary.txt')
        self.assertEqual(friends, 51710)
    def test_all_03(self):
        friends = set_up_and_check_returns(None, 'GROUNDSELS', 'dictionary.txt')
        self.assertEqual(friends, 2)
    def test_all_04(self):
        friends = set_up_and_check_returns(None, 'GROWLED', 'dictionary.txt')
        self.assertEqual(friends, 51710)