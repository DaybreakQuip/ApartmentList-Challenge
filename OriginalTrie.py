#Trie Based off of Steve Hanov's implementation of Levenshtein Distance
#His website is here: http://stevehanov.ca/blog/index.php?id=114
#Different implementation of Trie Search, Used to develop test cases
#Not as efficient because list keeps on appending and popping double counting elements
#Uses extra storage space for already_in_set
#Important: Used PyPy as Interpreter, See README for more details
class Trie:
    def __init__(self):
        self.word = None
        #Dictionary of Letters mapped to a new Trie
        self.children = {}

    def insert(self, word):
        '''
        :param word: Word (string) to be inserted into tree
        :return: None
        '''
        #Traverses through the tree to find appropriate letters
        parent = self
        for i in word:
            if i not in parent.children:
                parent.children[i] = Trie()
            parent = parent.children[i]
        parent.word = word


def search_neighbors_helper(tree, letter, word, prev_row_cost, word_list):
    '''
    Recursive helper to search for words with editDistance of <= 1
    :param tree: Current Trie object to be traversed through
    :param letter: Current letter (string) of the trie object
    :param word: word (string) to search for
    :param prev_row_cost: rowCost of the previous letter (int)
    :param word_list: List of words that are friends
    :return: None
    '''
    word_col = len(word) + 1
    current_row_cost = [prev_row_cost[0] + 1]
    for i in range(1, word_col):
        #Definition of Levenshtein Distance
        #Calculates the supposed insert_cost and delete_cost to be used as defined by Levenshtein distance
        insert_cost = current_row_cost[i - 1] + 1
        delete_cost = prev_row_cost[i] + 1
        if word[i-1] != letter:
            sub_cost = prev_row_cost[i - 1] + 1
        else:
            #If no letter is substituted
            sub_cost = prev_row_cost[i - 1]
        #Levenshtein Distance is the minimum of the three costs
        current_row_cost.append(min(insert_cost, delete_cost, sub_cost))
    #Checks to see if Levenshtein distance exceeds 1, if not, and current Trie is a word, append it to the list to return
    if current_row_cost[-1] <= 1 and tree.word is not None:
        word_list.append(tree.word)
    #Continues down the trie to find friends if edit distance does not exceed 1
    if min(current_row_cost) <= 1:
        for i in tree.children:
            search_neighbors_helper(tree.children[i], i, word, current_row_cost, word_list)

def search(tree, word):
    '''
    Main search method to find a friend
    :param tree: Current Trie object to be traversed through
    :param word: word (string) to search for
    :return: words in a list that have edit distance of 1
    '''
    #Default cost to supply to recursive helper
    current_row_cost = (range(len(word) + 1))
    word_list = []
    for i in tree.children:
        search_neighbors_helper(tree.children[i], i, word, current_row_cost, word_list)
    return word_list

def set_up_dictionary_from_text(file_name):
    '''
    :param file_name: Dictionary in .txt format
    :return: list of all words from dictionary
    '''
    with open(file_name, 'r') as word_list:
        words = word_list.read().split()
    return words
def set_up_tree(social_links):
    '''
    :param social_links: List of words in the dictionary
    :return: new Trie with all words in dictionary
    '''
    tree = Trie()
    for i in social_links:
        tree.insert(i)
    return tree

def find_all_links(tree, keyword):
    '''
    :param tree: Trie object containing dictionary
    :param keyword: word (string) to find friends for
    :return: the number of friends in the word's social link
    '''
    #initiates the list of friends yet to check
    neighbors = [keyword]
    #Used in counting the number of friends as well as making sure to remove double counting words
    already_in_set = set()
    while len(neighbors) > 0:
        if neighbors[-1] not in already_in_set:
            temp = neighbors[-1]
            #Searches the current element of neighbor by popping, O(1) time
            already_in_set.add(neighbors.pop())
            current_neighbors = search(tree, temp)
            #adds all the neighbors, including double counting neighbors
            neighbors.extend(current_neighbors)
        else:
            #Removes double counting neighbor from list
            already_in_set.add(neighbors.pop())
    return len(already_in_set)