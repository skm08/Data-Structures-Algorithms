class TrieNode:
    def __init__(self):
        self.wordEnd = False
        self.child = {}

class Solution:
    def trieInsert(self, folder: str, curr: TrieNode):
        i = 1
        while i < len(folder):
            name = []
            while i < len(folder) and folder[i] != '/':
                name.append(folder[i])
                i += 1
            
            name = ''.join(name)
            if curr.wordEnd:
                return  # Stop if a parent folder already exists
            
            if name not in curr.child:  # Create a new node if the path doesn't exist
                curr.child[name] = TrieNode()
            
            curr = curr.child[name]
            i += 1
        
        curr.wordEnd = True
    
    def searchTrie(self, curr: TrieNode, res: list, path: str):
        if not curr:
            return
        if curr.wordEnd:
            path = path[:-1]  # Remove '/'
            res.append(path)  # Save path
            return
        
        for name, child in curr.child.items():
            self.searchTrie(child, res, path + name + '/')
    
    def removeSubfolders(self, folders: list) -> list:
        root = TrieNode()

        # Insert all folders into the Trie
        for folder in folders:
            self.trieInsert(folder, root)
        
        res = []  # Stores result
        self.searchTrie(root, res, "/")
        return res