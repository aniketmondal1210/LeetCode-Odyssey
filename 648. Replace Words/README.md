# Replace Words (Prefix Root Replacement)

## Problem Description

In English, we have a concept called a **root**, which can be followed by another word to form a **derivative** (e.g., the root `"help"` followed by `"ful"` forms `"helpful"`).

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the **shortest length**.

Return the sentence after all replacements have been made.

---

## Examples

### Example 1
- **Input:** 
  - `dictionary = ["cat", "bat", "rat"]`
  - `sentence = "the cattle was rattled by the battery"`
- **Output:** `"the cat was rat by the bat"`
- **Explanation:** 
  - `"cattle"` starts with `"cat"` $\rightarrow$ replaced by `"cat"`
  - `"rattled"` starts with `"rat"` $\rightarrow$ replaced by `"rat"`
  - `"battery"` starts with `"bat"` $\rightarrow$ replaced by `"bat"`

### Example 2
- **Input:** 
  - `dictionary = ["a", "b", "c"]`
  - `sentence = "aadsfasf absbs bbab cadsfafs"`
- **Output:** `"a a b c"`

---

## Constraints

- $1 \le \text{dictionary.length} \le 1000$
- $1 \le \text{dictionary}[i].\text{length} \le 100$
- `dictionary[i]` consists of only lowercase English letters.
- $1 \le \text{sentence.length} \le 10^6$
- `sentence` consists of lowercase letters and spaces.
- $1 \le \text{number of words in sentence} \le 1000$
- $1 \le \text{length of each word} \le 1000$
- Every two consecutive words in `sentence` are separated by exactly one space.
- `sentence` does not have leading or trailing spaces.

---

## Approach: Trie (Prefix Tree)

1. **Build the Trie:**
   - Insert every root from the `dictionary` into a Trie.
2. **Shortest Match Search:**
   - For each word in `sentence`, traverse through the Trie character by character.
   - The **first time** we encounter a node marked as an end of a word (`is_end = True`), we return the accumulated prefix. This guarantees we pick the shortest matching root.
   - If we reach a character not present in the Trie branch, or reach the end of the word without hitting `is_end`, no replacement occurs, and the original word is kept.
3. **Reconstruct Sentence:**
   - Rejoin the replaced words using a space separator.

---

## Complexity Analysis

- **Time Complexity:** 
  - **Trie Building:** $\mathcal{O}(D)$, where $D$ is the total number of characters across all dictionary roots.
  - **Sentence Replacement:** $\mathcal{O}(S)$, where $S$ is the total length of the sentence.
  - **Overall:** $\mathcal{O}(D + S)$ — optimal linear time complexity.
- **Space Complexity:** $\mathcal{O}(D)$ to store dictionary roots inside the Trie.

---

## Code Implementations

### Python 3

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def find_shortest_root(self, word: str) -> str:
        node = self.root
        prefix = []
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix.append(char)
            if node.is_end:
                return "".join(prefix)
        return word

def replaceWords(dictionary: list[str], sentence: str) -> str:
    trie = Trie()
    for root in dictionary:
        trie.insert(root)

    words = sentence.split(" ")
    return " ".join(trie.find_shortest_root(word) for word in words)

# Example Execution
if __name__ == "__main__":
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(replaceWords(dictionary, sentence))  # Output: "the cat was rat by the bat"
```

---

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>

struct TrieNode {
    std::unordered_map<char, TrieNode*> children;
    bool is_end = false;
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() { root = new TrieNode(); }

    void insert(const std::string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->is_end = true;
    }

    std::string findShortestRoot(const std::string& word) {
        TrieNode* node = root;
        std::string prefix = "";
        for (char c : word) {
            if (!node->children.count(c)) break;
            node = node->children[c];
            prefix += c;
            if (node->is_end) return prefix;
        }
        return word;
    }
};

std::string replaceWords(std::vector<std::string>& dictionary, std::string sentence) {
    Trie trie;
    for (const std::string& root : dictionary) {
        trie.insert(root);
    }

    std::stringstream ss(sentence);
    std::string word, result = "";
    while (ss >> word) {
        if (!result.empty()) result += " ";
        result += trie.findShortestRoot(word);
    }
    return result;
}

int main() {
    std::vector<std::string> dict = {"cat", "bat", "rat"};
    std::string sentence = "the cattle was rattled by the battery";
    std::cout << replaceWords(dict, sentence) << std::endl;
    return 0;
}
```

---

### Java

```java
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Solution {
    private final TrieNode root = new TrieNode();

    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEnd = true;
    }

    private String findShortestRoot(String word) {
        TrieNode node = root;
        StringBuilder prefix = new StringBuilder();
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) break;
            node = node.children.get(c);
            prefix.append(c);
            if (node.isEnd) return prefix.toString();
        }
        return word;
    }

    public String replaceWords(List<String> dictionary, String sentence) {
        for (String rootWord : dictionary) {
            insert(rootWord);
        }

        String[] words = sentence.split(" ");
        for (int i = 0; i < words.length; i++) {
            words[i] = findShortestRoot(words[i]);
        }

        return String.join(" ", words);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<String> dict = Arrays.asList("cat", "bat", "rat");
        String sentence = "the cattle was rattled by the battery";
        System.out.println(sol.replaceWords(dict, sentence));
    }
}
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
