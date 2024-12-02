from collections import defaultdict
import math

# Step 1: Prepare the dataset
messages = [
    ("Win a free iPhone now!", "spam"),
    ("Don't forget our meeting tomorrow", "not spam"),
    ("Congratulations, you've won!", "spam"),
    ("Let's catch up this weekend", "not spam"),
    ("Special offer just for you", "spam"),
    ("Can you send me the report?", "not spam"),
]

# Separate messages and labels
texts, labels = zip(*messages)

# Step 2: Preprocess the text (convert to lowercase and split words)
def preprocess(text):
    return text.lower().split()

# Apply preprocessing to all texts
preprocessed_texts = [preprocess(text) for text in texts]

# Step 3: Calculate probabilities for Naive Bayes
class NaiveBayesClassifier:
    def __init__(self):
        self.word_counts = defaultdict(lambda: defaultdict(int))  # Word frequencies per class
        self.class_counts = defaultdict(int)                     # Document counts per class
        self.vocabulary = set()                                  # Set of all unique words
        self.total_docs = 0                                      # Total number of documents
    
    def train(self, texts, labels):
        self.total_docs = len(labels)
        for text, label in zip(texts, labels):
            self.class_counts[label] += 1
            for word in text:
                self.word_counts[label][word] += 1
                self.vocabulary.add(word)
    
    def predict(self, text):
        words = preprocess(text)
        class_scores = {}
        
        for class_label in self.class_counts:
            # Start with the log probability of the class
            class_scores[class_label] = math.log(self.class_counts[class_label] / self.total_docs)
            
            # Add the log probabilities of the words
            for word in words:
                # Apply Laplace smoothing
                word_probability = (self.word_counts[class_label][word] + 1) / \
                                   (sum(self.word_counts[class_label].values()) + len(self.vocabulary))
                class_scores[class_label] += math.log(word_probability)
        
        # Return the class with the highest score
        return max(class_scores, key=class_scores.get)

# Step 4: Train the model
classifier = NaiveBayesClassifier()
classifier.train(preprocessed_texts, labels)

# Step 5: Test the model
test_messages = [
    "Win a free vacation!",
    "Can we reschedule our meeting?",
    "Exclusive deal just for you!"
]

# Make predictions
for message in test_messages:
    prediction = classifier.predict(message)
    print(f"Message: '{message}' -> Predicted: {prediction}")
