#This implements a general Damerau–Levenshtein distance with edit distance of max cost
#Credit to Steve Hanov for original Levenshtein code
#His website is here: http://stevehanov.ca/blog/index.php?id=114
#Helps to test understanding of Trie
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


def search_neighbors_helper(tree, letter, word, prev_row_cost, two_rows_up_cost, word_list, max_cost):
    '''
    Recursive helper to search for words with editDistance of <= max_cost
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
        # Definition of Levenshtein Distance
        # Calculates the supposed insert_cost and delete_cost to be used as defined by Levenshtein distance
        insert_cost = current_row_cost[i - 1] + 1
        delete_cost = prev_row_cost[i] + 1
        transposition_cost = None
        if word[i-1] != letter:
            sub_cost = prev_row_cost[i - 1] + 1
        else:
            #if no letter is substituted
            sub_cost = prev_row_cost[i - 1]
        #Damerau–Levenshtein distance includes transposition cost
        #Transposition cost is only valid if prev_row_cost[i] == current_row_cost[i-1] == and prev_row_cost[i-1]
        if two_rows_up_cost is not None and i > 1 and (prev_row_cost[i] == current_row_cost[i-1] ==prev_row_cost[i-1]):
            transposition_cost = two_rows_up_cost[i-2] + 1
        #If transposition cost applies, include it in calculating in the minimum, otherwise do normal levenshtein distance
        if two_rows_up_cost is not None and transposition_cost is not None:
            current_row_cost.append(min(insert_cost, delete_cost, sub_cost, transposition_cost))
        else:
            current_row_cost.append(min(insert_cost, delete_cost, sub_cost))
    # Checks to see if Levenshtein distance exceeds 1, if not, and current Trie is a word, append it to the list to return
    # Checks to see if we traversed through the tree before to not double count
    if current_row_cost[-1] <= max_cost and tree.word is not None:
        word_list.append(tree.word)
    # Continues down the trie to find friends if edit distance does not exceed 1
    if min(current_row_cost) <= max_cost:
        for i in tree.children:
            search_neighbors_helper(tree.children[i], i, word, current_row_cost, prev_row_cost, word_list, max_cost)

def search(tree, word, max_cost):
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
        search_neighbors_helper(tree.children[i], i, word, current_row_cost, None, word_list, max_cost)
    return word_list


def set_up_tree(social_links):
    '''
    :param social_links: List of words in the dictionary
    :return: new Trie with all words in dictionary
    '''
    tree = Trie()
    for i in social_links:
        tree.insert(i)
    return tree
