'''
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
'''
def _groupAnagrams(strs):
    d = {}
    for word in strs:
        sword = ''.join(sorted(word))
        d[sword].extend([word]) if d.get(sword) else d.setdefault(sword, []).extend([word])
    return d.values()

# test
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print _groupAnagrams(strs)

########################################################

'''
Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
def _isAnagram(str1, str2):
    if str1 is None or str2 is None:
        return False
    return sorted(str1) == sorted(str2)

# test
s = u'anagram'
t = u'nagaram'
print _isAnagram(s, t)


########################################################

'''
Given one string s, write a function to determine which characters repete.
For example,
s = "anagram", return "a".
Note:
You may assume the string contains only lowercase alphabets.
'''
def _duplicateCharacters(s):
    d = {}
    for c in s:
        d[c] = d[c] + 1 if d.get(c) else 1
    return [key for key, value in d.iteritems() if value > 1]

# test
s = 'anagram program'
print _duplicateCharacters(s)
