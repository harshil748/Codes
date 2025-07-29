class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = []


def insert_substrings(root, s, label):
    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            c = s[j]
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.ends.append((i, j + 1, label))  # store substring info


def solve(x, y, S, R):
    n = len(x)
    dp = [(float("inf"), float("inf"))] * (n + 1)
    dp[0] = (0, 0)

    root = TrieNode()
    # Insert all substrings of Y and reversed Y into Trie
    insert_substrings(root, y, "Y")
    insert_substrings(root, y[::-1], "R")

    for i in range(n):
        if dp[i][0] == float("inf"):
            continue
        node = root
        for j in range(i, n):
            c = x[j]
            if c not in node.children:
                break
            node = node.children[c]
            for _, _, label in node.ends:
                parts = dp[i][0] + 1
                cost = dp[i][1] + (S if label == "Y" else R)
                if parts < dp[j + 1][0] or (
                    parts == dp[j + 1][0] and cost < dp[j + 1][1]
                ):
                    dp[j + 1] = (parts, cost)

    return dp[n][1] if dp[n][0] != float("inf") else "Impossible"
