def tokenize_text(text):
    # Sentence tokenization based on periods, exclamation marks, and question marks
    sentences = []
    temp_sentence = ""
    for char in text:
        temp_sentence += char
        if char in ".!?":
            sentences.append(temp_sentence.strip())
            temp_sentence = ""
    if temp_sentence:  # Add the last sentence if there's no punctuation at the end
        sentences.append(temp_sentence.strip())

    # Word tokenization by splitting on spaces and handling punctuation
    words = []
    for sentence in sentences:
        word = ""
        for char in sentence:
            if char.isalnum():  # Include letters and numbers
                word += char
            elif word:  # Word ends at punctuation or space
                words.append(word)
                word = ""
        if word:  # Add the last word in the sentence
            words.append(word)

    return {
        "sentences": sentences,
        "words": words
    }

# Example usage
if __name__ == "__main__":
    input_text = "Hello world! NLP is fascinating. Let's tokenize this text."
    tokens = tokenize_text(input_text)

    print("Sentences:")
    for sentence in tokens["sentences"]:
        print(f" - {sentence}")

    print("\nWords:")
    for word in tokens["words"]:
        print(f" - {word}")
