import collections
from collections import deque 

class Solution(object):
    # method that will help find the path
    def ladderLength(self, beginWord, 
                        endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :returntype: int
        """

        # Queue for BFS
        queue = deque()

        # start by adding begin word
        queue.append((beginWord, [beginWord]))

        while queue:
            # let's keep a watch at active queue
            print('Current queue:',queue)
            print('\n')

            # get the current node and 
            # path how it came
            node, path = queue.popleft()

            # let's keep track of path length 
            # traversed so far
            print('Current transformation count:',
                                        len(path))

            # find possible next set of 
            # child nodes, 1 diff
            for next in self.next_nodes(node, 
                            wordList) - set(path):
                # traversing through all child nodes
                # if any of the child matches, 
                # we are good               
                if next == endWord:
                    print('found endword at path:', path)
                    print('\n')
                    if endWord == 'RUIN':
                        print('Overall shortest path:', path + [endWord])                       
                    return len(path)
                else:
                    # keep record of next 
                    # possible paths
                    queue.append((next, 
                                path + [next]))
        return 0

    def next_nodes(self, word, word_list):
        # start with empty collection
        possiblenodes = set()

        # all the words are of fixed length
        wl_word_length = len(word)

        # loop through all the words in 
        # the word list
        for wl_word in word_list:
            mismatch_count = 0

            # find all the words that are 
            # only a letter different from 
            # current word those are the 
            # possible next child nodes
            for i in range(wl_word_length):
                if wl_word[i] != word[i]:
                    mismatch_count += 1
            if mismatch_count == 1:
                # only one alphabet different-yes
                possiblenodes.add(wl_word)

        # lets see the set of next possible nodes 
        print('possible next nodes:',possiblenodes)
        return possiblenodes

# Setup
beginWord = "SAIL"
endWord = "RUIN"
wordList = ["SAIL","RAIN","REST","BAIL","MAIL",
                                    "MAIN","RUIN"]

# Call
print('Least number of transformations needed: ',
    Solution().ladderLength(beginWord, 
                            endWord, wordList))

# Transformation expected == 4
# One possible shortes path with 4 transformation:
# SAIL -> MAIL -> MAIN -> RAIN -> RUIN
            
           
