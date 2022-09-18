def test_example(vectorizer, corpus, feature_names_t, matrix_t):
    matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()
    return feature_names == feature_names_t and matrix == matrix_t


if __name__ == '__main__':
    from main import CountVectorizer
    corpuses = [
        [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ], [
            'Congress leader Bharat Singh Solanki recovers from Covid-19 \
            after 101 days. In our good news section, watch the story \
            of former Gujarat Congress president and member of Parliament \
            Bharat Singh Solanki who has created a unique record.'
        ], [
            'vectorizer = CountVectorizer()',
            'count_matrix = vectorizer.fit_transform(corpus)',
            'print(vectorizer.get_feature_names())'
        ], [
            'There',
            'are',
            'many',
            'variations',
            'of',
            'passages',
            'of',
            'Lorem',
            'Ipsum',
            'available,',
            'but',
            'the',
            'majority',
            'are',
            'suffered',
            'alteration',
            'in',
            'some',
            'form.'
        ], [
            'Example: "Fear leads to anger; anger leads to hatred; \
            hatred leads to conflict; conflict leads to suffering." \
            — Yoda, in Star Wars Episode I: The Phantom Menace.'
        ], [
            'An enlightened dog named Buddha loves spending his days \
            parading around a Colorado animal sanctuary with his new BFF: \
            a 4-week-old lamb named Cheerio.',
            'The mixed-breed dog spent his first two years of life chained \
            outside in the hot sun, but now he’s living the good life \
            befriending baby animals when they arrive at \
            Luvin Arms Animal Sanctuary in Erie, Colorado.',
            '“Buddha has this way with all of our new rescues,” \
            Shartrina White, the sanctuary’s executive director, told TODAY. \
            “The cutest thing in the world is watching Cheerio get all \
            excited and do these little and jumps and run after Buddha \
            to follow him and play with him.”'
        ]
    ]
    feature_names = [
        [
            'crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
            'fresh', 'ingredients', 'parmesan', 'to', 'taste'
        ], [
            'congress', 'leader', 'bharat', 'singh', 'solanki', 'recovers',
            'from', 'covid-19', 'after', '101', 'days', 'in', 'our', 'good',
            'news', 'section', 'watch', 'the', 'story', 'of', 'former',
            'gujarat', 'president', 'and', 'member', 'parliament', 'who',
            'has', 'created', 'a', 'unique', 'record'
        ], [
            'vectorizer', 'countvectorizer', 'count_matrix', 'fit_transform',
            'corpus', 'print', 'get_feature_names',
        ], [
            'there', 'are', 'many', 'variations', 'of', 'passages', 'lorem',
            'ipsum', 'available', 'but', 'the', 'majority', 'suffered',
            'alteration', 'in', 'some', 'form'
        ], [
            'example', 'fear', 'leads', 'to', 'anger', 'hatred', 'conflict',
            'suffering', 'yoda', 'in', 'star', 'wars', 'episode', 'i', 'the',
            'phantom', 'menace'
        ], [
            'an', 'enlightened', 'dog', 'named', 'buddha', 'loves',
            'spending', 'his', 'days', 'parading', 'around', 'a', 'colorado',
            'animal', 'sanctuary', 'with', 'new', 'bff', '4-week-old', 'lamb',
            'cheerio', 'the', 'mixed-breed', 'spent', 'first', 'two', 'years',
            'of', 'life', 'chained', 'outside', 'in', 'hot', 'sun', 'but',
            'now', 'he', 's', 'living', 'good', 'befriending', 'baby',
            'animals', 'when', 'they', 'arrive', 'at', 'luvin', 'arms',
            'erie', 'has', 'this', 'way', 'all', 'our',
            'rescues', 'shartrina', 'white', 'executive', 'director', 'told',
            'today', 'cutest', 'thing', 'world', 'is', 'watching', 'get',
            'excited', 'and', 'do', 'these', 'little', 'jumps', 'run',
            'after', 'to', 'follow', 'him', 'play'
        ]
    ]
    matrixes = [
        [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]],
        [[2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1,
          1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [[1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 0, 0],
         [1, 0, 0, 0, 0, 1, 1]],
        [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]],
        [[1, 1, 4, 4, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [[1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 1,
          1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
          1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 1, 3, 0,
          0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
          4, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]]
    ]
    for i in range(len(corpuses)):
        result = test_example(CountVectorizer(), corpuses[i],
                              feature_names[i], matrixes[i])
        print(f'Test No {i}: {result}')
