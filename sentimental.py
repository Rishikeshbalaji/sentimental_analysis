
import string
from collections import Counter
import matplotlib.pyplot as plt

read_text= open("read.txt", encoding='utf-8').read()
print(read_text)
lower_case=read_text.lower()
# print(lower_case)
clr_text = lower_case.translate(str.maketrans('','',string.punctuation))
print(clr_text)
#tokenization 
token_text = clr_text.split()
print(token_text)
# stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now","u"]
# removing stop words
finnel_text=[]
for word in token_text:
    if word not in stop_words:
        finnel_text.append(word)
        print(finnel_text)
 with open('emotions.txt', 'r') as file:
    for line in file:
        print(file)
print(finnel_text)
w = Counter(finnel_text)
print(w)

# Plotting the emotions on the graph

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
