import unittest
import Social

class TestSetup(unittest.TestCase):
    def test_01(self):
        social_links = ['HI', 'HERE', 'THERE', 'HER', 'HE', 'SHE', 'HEAR', 'HALLOW']
        tree = Social.set_up_tree(social_links)
        tree_keys = tree.children.keys()
        self.assertEqual(list(tree_keys), ['H','T','S'])
    def test_02(self):
        social_links = ['FIST', 'FISTS', 'LISTS', 'LISTY', 'LIT', 'LITAI', 'LITANIES', 'LITANY', 'LITAS', 'LITCHI', 'LITCHIS', 'LUSTY', 'LISTS']
        tree = Social.set_up_tree(social_links)
        tree_keys = tree.children.keys()
        self.assertEqual(list(tree_keys), ['F', 'L'])
    def test_03(self):
        social_links = Social.set_up_dictionary_from_text('eighth_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        tree_keys = tree.children.keys()
        self.assertEqual(list(tree_keys), ['G', 'H', 'I', 'J', 'K', 'L'])
    def test_04(self):
        social_links = Social.set_up_dictionary_from_text('half_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        tree_keys = tree.children.keys()
        self.assertEqual(list(tree_keys), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])

class TinyTests(unittest.TestCase):
    def test_simple_01(self):
        social_links = ['HI', 'HERE', 'THERE', 'HER', 'HE', 'SHE', 'HEAR', 'HALLOW']
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'HI')
        self.assertEqual(friends, 7)
    def test_simple_02(self):
        social_links = ['HI', 'HERE', 'THERE', 'HER', 'HE', 'SHE', 'HEAR', 'HALLOW']
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'HALLOW')
        self.assertEqual(friends, 1)
    def test_simple_03(self):
        social_links = ['FIST', 'FISTS', 'LISTS', 'LISTY','LIT','LITAI', 'LITANIES', 'LITANY','LITAS','LITCHI', 'LITCHIS','LUSTY', 'LISTS']
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'LISTY')
        self.assertEqual(friends, 5)
    def test_simple_04(self):
        social_links = ['FIST', 'FISTS', 'LISTS', 'LISTY', 'LIT', 'LITAI', 'LITANIES', 'LITANY', 'LITAS', 'LITCHI', 'LITCHIS', 'LUSTY', 'LISTS']
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'LUSTY')
        self.assertEqual(friends, 5)

class SmallTests(unittest.TestCase):
    def test_small_01(self):
        social_links = Social.set_up_dictionary_from_text('eighth_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'LISTY')
        self.assertEqual(friends, 5132)
    def test_small_02(self):
        social_links = Social.set_up_dictionary_from_text('eighth_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'GROUNDS')
        self.assertEqual(friends, 1)
    def test_small_03(self):
        social_links = Social.set_up_dictionary_from_text('eighth_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'GROUNDSELS')
        self.assertEqual(friends, 2)
    def test_small_04(self):
        social_links = Social.set_up_dictionary_from_text('eighth_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'GROWLED')
        self.assertEqual(friends, 6)

class MediumTests(unittest.TestCase):
    def test_medium_01(self):
        social_links = Social.set_up_dictionary_from_text('quarter_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'LISTY')
        self.assertEqual(friends, 11008)
    def test_medium_02(self):
        social_links = Social.set_up_dictionary_from_text('quarter_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'DISTASTE')
        self.assertEqual(friends, 3)
    def test_medium_03(self):
        social_links = Social.set_up_dictionary_from_text('quarter_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'GENERA')
        self.assertEqual(friends, 5)
    def test_medium_04(self):
        social_links = Social.set_up_dictionary_from_text('quarter_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'GRIND')
        self.assertEqual(friends, 11008)

class LargeTests(unittest.TestCase):
    def test_large_01(self):
        social_links = Social.set_up_dictionary_from_text('half_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'LISTY')
        self.assertEqual(friends, 22741)
    def test_large_02(self):
        social_links = Social.set_up_dictionary_from_text('half_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'ABATES')
        self.assertEqual(friends, 22741)
    def test_large_03(self):
        social_links = Social.set_up_dictionary_from_text('half_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'EPISCIA')
        self.assertEqual(friends, 2)
    def test_large_04(self):
        social_links = Social.set_up_dictionary_from_text('half_dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'HALL')
        self.assertEqual(friends, 22741)

class AllTests(unittest.TestCase):
    def test_all_01(self):
        social_links = Social.set_up_dictionary_from_text('dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'LISTY')
        self.assertEqual(friends, 51710)
    def test_all_02(self):
        social_links = Social.set_up_dictionary_from_text('dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'GROUNDS')
        self.assertEqual(friends, 51710)
    def test_all_03(self):
        social_links = Social.set_up_dictionary_from_text('dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'GROUNDSELS')
        self.assertEqual(friends, 2)
    def test_all_04(self):
        social_links = Social.set_up_dictionary_from_text('dictionary.txt')
        tree = Social.set_up_tree(social_links)
        friends = Social.find_all_links(tree, 'GROWLED')
        self.assertEqual(friends, 51710)