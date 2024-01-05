def count_words(sentence):
    
    wordcount = 0
    
    for i in sentence:
        if i == ' ':
            wordcount += 1
    wordcount += 1
    
    return wordcount

sentence = "Counting Words in a Sentence."
result = count_words(sentence)

print(f"Number of words in the sentence: {result}")
