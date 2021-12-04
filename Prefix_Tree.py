#Tries or Prefix Tree implementation 


class TrieNode:
  def __init__(self, letter):
    self.letter = letter
    self.children = {}
    self.is_end_of_word = False

class Trie:
  def __init__(self):
    self.root = TrieNode("*")
  #insertion
  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        curr_node.children[letter] = TrieNode(letter)
      curr_node = curr_node.children[letter]
    curr_node.is_end_of_word = True
  
  def does_word_exist(self, word):
    #check for empty string
    if word == "":
      return True
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        return False
      curr_node = curr_node.children[letter]
    return curr_node.is_end_of_word 

#Test
trie = Trie()
#team, tetris, tea, steam, teacher, teaching, teach
words = ["team", "tetris", "tea", "steam", "teacher", "teaching", "teach"]
for word in words:
  trie.add_word(word)

print(trie.does_word_exist("team")) #True
print(trie.does_word_exist("")) #True
print(trie.does_word_exist("teacher")) #False
print(trie.does_word_exist("sh")) #False
print(trie.does_word_exist("teach")) #Truecd