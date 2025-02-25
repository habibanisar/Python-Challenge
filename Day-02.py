#Day 2 – Daily Python Challenge 
# Write a Python program that takes a sentence from the user and counts the number of words in it.

#input(): Takes the sentence from the user.
sentence = input("Drop a sentence here, and I'll tell you how many words it has:")

#split(): Splits the sentence into a list of words (default separator is space).
words = sentence.split()

#len(): Counts the number of items in the list (i.e., the number of words).
word_count = len(words)

#print(): Displays the total word count.
print(f"Awsome! your sentense has {word_count} words.")