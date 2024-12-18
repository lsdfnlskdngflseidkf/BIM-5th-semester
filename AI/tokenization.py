text = "Hello, how are you? I'm learning NLP."

# Combined Sentence and Word Tokenization
def tokenize(text):
    sentences = []  # List to store sentences
    words_in_sentences = []  # List to store words in each sentence

    # Split text into sentences (basic split by punctuation)
    sentence = ""
    punctuation = ".!?"

    for char in text:
        sentence += char
        if char in punctuation:
            sentences.append(sentence.strip())
            sentence = ""  # Reset sentence for the next one

    if sentence:  # If there's any remaining sentence, add it
        sentences.append(sentence.strip())

    # Now, tokenize words in each sentence
    for sentence in sentences:
        words = []
        word = ""
        for char in sentence:
            if char.isalnum() or char == "'":  # Keep alphanumeric and apostrophes
                word += char
            elif word:  # When we hit a non-alphanumeric character, store the word
                words.append(word)
                word = ""  # Reset word

        if word:  # If there's any leftover word, add it
            words.append(word)

        words_in_sentences.append(words)  # Store words of this sentence

    return sentences, words_in_sentences

# Tokenizing the example text
sentences, words_in_sentences = tokenize(text)

print("Sentences:")
print(sentences)
print("\nWords in each sentence:")
print(words_in_sentences)
