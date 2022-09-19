import re


class CountVectorizer:
    """Convert a corpus of text documents to a list of unique words
    (vocabulary) and create document-term matrix of this corpus"""
    pattern_word = r'\w[-\w]+|\w'

    def __init__(self):
        self._vocabulary = []

    def _preprocess(self, corpus: [str]) -> [[str]]:
        """Performs preprocessing of a corpus of text documents
        accepted as a parameter. Splits each document into a list of words.
        Leaves every word without punctuation marks and other extraneous
        characters and converts them to lower case
        corpus: [str] - list of transmitted text documents
        Returns a cleaned corpus of text documents [[str]] - list with
        elements - lists of tokenized texts"""
        cleaned_corpus = []
        for text in corpus:
            cleaned_text = re.findall(self.pattern_word, text.lower())
            cleaned_corpus.append(cleaned_text)
        return cleaned_corpus

    def _build_vocabulary(self, corpus: [str]):
        """Creates a dictionary from a cleaned corpus of text documents.
        Dictionary contains only unique words
        corpus: [str] - list of transmitted text documents
        Returns a cleaned corpus of text documents [[str]] - list with
        elements - lists of tokenized texts - needed for transform corpus
        and creating a document-term matrix"""
        for text in corpus:
            for word in text:
                if word not in self._vocabulary:
                    self._vocabulary.append(word)

    def fit_transform(self, corpus: [str]) -> [[int]]:
        """Accepts a corpus of text documents, performs its preprocessing,
        builds a vocabulary and creates a term-document matrix.
        corpus: [str] - list of transmitted text documents
        Returns a term-document matrix [[int]] of corpus of text documents"""
        cleaned_corpus = self._preprocess(corpus)
        self._build_vocabulary(cleaned_corpus)
        matrix = [[0] * len(self._vocabulary) for _ in range(len(corpus))]
        for i in range(len(cleaned_corpus)):
            for word in cleaned_corpus[i]:
                matrix[i][self._vocabulary.index(word)] += 1
        return matrix

    def get_feature_names(self) -> [str]:
        """Returns a list of features (unique words from the corpus),
        creating during fitting"""
        return self._vocabulary


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    # Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    #       'fresh', 'ingredients', 'parmesan', 'to', 'taste']

    print(count_matrix)
    # Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
