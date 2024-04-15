// Trie Exercise - addWord
// This function should add the given word starting from the given index to the Trie.

// It will be recursive and notify the correct child of this Trie to add the word starting from a later index.

// Consider what the add function should do when it reaches the end of the word as a word does not necessarily end at a leaf.

// You must mark nodes which are the ends of words so that the words can be reconstructed later.

var firstTrie = new Trie();
firstTrie.addWord("fun")
firstTrie.characters // {f: Trie}
!!firstTrie.characters["f"] // true
 
firstTrie.characters.f.characters.u // {u: Trie}
!!firstTrie.characters.f.characters.u // true
 
firstTrie.characters.f.characters.u.characters.n.isWord // true
!!firstTrie.characters.f.characters.u.characters.n // true
!!firstTrie.characters.f.characters.u.characters.n.characters // {}
 
!!firstTrie.characters.f.characters.u.characters.l // true
 
var secondTrie = new Trie();
secondTrie.addWord("ha")
secondTrie.addWord("hat")
secondTrie.addWord("has")
secondTrie.addWord("have")
secondTrie.addWord("hate")
 
secondTrie.characters.h.characters.a.isWord // true
secondTrie.characters.h.characters.a.characters.t.isWord // true
secondTrie.characters.h.characters.a.characters.v.isWord // false
secondTrie.characters.h.characters.a.characters.v.characters.e.isWord // true
secondTrie.characters.h.characters.a.characters.t.characters.e.isWord // true
 
Object.keys(secondTrie.characters.h.characters.a.characters).length // 3

// Write a function called removeWord which accepts a string and removes the word from the Trie. addWord is implement to help you test the function.

var t = new Trie();
t.addWord('fun')
t.addWord('fast')
t.addWord('fat')
t.addWord('fate')
t.addWord('father')
t.addWord('forget')
t.addWord('awesome')
t.addWord('argue')
 
 
t.removeWord('fat')
t.characters.f.characters.a.characters.t.isWord // false
t.characters.f.characters.a.characters.t.characters.e.isWord // true
 
t.removeWord('argue')
 
t.characters.a.characters.r // undefined

// Write a function called findWord which accepts a string and returns the characters object for the last character in that word if the string is a word in the Trie, otherwise it returns undefined. Try to solve this without having to find every single word in the Trie. addWord is implement to help you test the function.

var t = new Trie();
t.addWord('fun')
t.addWord('fast')
t.addWord('fat')
t.addWord('fate')
t.addWord('father')
 
t.findWord('taco') // undefined
t.findWord('fat').characters // {t: Trie}
t.findWord('father').characters // {}
t.findWord('father').isWord // true

// Write a function on the Trie.prototype called getWords which returns an array of all of the words in the Trie.

var t = new Trie();
t.addWord('fun')
t.addWord('fast')
t.addWord('fat')
t.addWord('fate')
t.addWord('father')
t.addWord('forget')
t.addWord('awesome')
t.addWord('argue')
 
t.getWords() // ["fun", "fast", "fat", "fate", "father", "forget", "awesome", "argue"]
 
t.getWords().length // 8

// Write a function on the trie class which accepts a string and returns an array of all the possible options in the trie for that string.

var t = new Trie();
t.addWord('fun')
t.addWord('fast')
t.addWord('fat')
t.addWord('fate')
t.addWord('father')
t.addWord('forget')
t.addWord('awesome')
t.addWord('argue')
 
t.autocomplete('fa') // ["fast","fat", "fate", "father"] 
t.autoComplete('a') // ["awesome", "argue"]
t.autoComplete('arz') // []
