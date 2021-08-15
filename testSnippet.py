"""
"""
# Given a String separated by space, reshape it to a 3 * 3 Numpy Array
"""
import numpy

def ShapeArr( l1 ):
    array = numpy.array(l1)
    return(numpy.reshape(array,(3,3)))

if(__name__=='__main__'):
    lst = list(map(int,input( ).split(' ')))
    print(ShapeArr(lst))
"""
"""
"""
# Numpy eye
"""
import numpy as np

if(__name__=='__main__'):
    n,m = map(int,input().split(' '))
    np.set_printoptions(legacy='1.13')
    print( np.eye(n,m,k=0) )
"""
"""
import numpy
if(__name__ == '__main__'):

    n = int(input())
    list1 = []
    for i in range(n):
        list_temp = []
        list_temp = map(int, input().split(' '))
        list1.append([int(i) for i in list_temp])

    list2 = []
    for i in range(n):
        list_temp = []
        list_temp = map(int, input().split(' '))
        list2.append([int(i) for i in list_temp])

    print(numpy.dot(numpy.array(list1), numpy.array(list2)))
"""
"""
if(__name__ == '__main__'):
    l = [1,2,3,4,5]
    a = range(len(l))
    l1 = a[4::-1]

    for i in l1:
        print(l[i])
"""
"""
if(__name__ == '__main__'):
    a, b, c = "a", "b", "c"

    c, a, b = a, b, c

    print(a, b, c)
 
"""
"""
if __name__ == '__main__':
    list = [1,2,3,4,5,6,7]
    list2 = list[-2::-1]

    print(list2)
"""

"""
if __name__=='__main__':
    for i in range(20,11,-1):
        print(i)
"""

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import math

def computeTFIDF (corpus):
    tf_idf_vect = TfidfVectorizer(ngram_range=(1,1), min_df=1)
    tf_idf_vect.fit(corpus)
    print(tf_idf_vect.get_feature_names())

    final_tf_idf = tf_idf_vect.transform(corpus)
    print(final_tf_idf.toarray())

def getUniqueWords(corpus):
    unique_words = []
    for sentence in corpus:
        word_string = sentence.split(" ")
        for word in word_string:
            if word not in unique_words:
                unique_words.append(word)
            else:
                continue
    
    return unique_words

def getTF(corpus):
    
    
    tf = np.empty((4,6), dtype=object)
    count_sentence=0
    for sentence in corpus:
        count=0
        words = np.array(sentence.split(" "))
        tf_row = np.empty(words.shape, dtype=object)
        for word in words:
            occurrences = words[words==word].shape[0]
            total_words = words.size
            tf_row[count] = occurrences / total_words
            count += 1
        tf[count_sentence] = tf_row
        count_sentence += 1
    # print(tf)
    return tf

def getIDF(corpus, UniqueWords):
    
    corpus_arr = np.empty((4,6), dtype=object)
    count = 0
    for sentence in corpus:
        words = np.array(sentence.split(" "))
        corpus_arr[count] = words
        count += 1
    
    total_no_docs = len(corpus)
    for word in UniqueWords:
        count = 0
        for sentence in corpus:
            if word not in sentence:
                continue
            else:
                count += 1
        
        corpus_arr[corpus_arr==word] = math.log(total_no_docs/count)
    # print(corpus_arr)
    return corpus_arr

def customTFIDF(corpus):
    TF = getTF(corpus)
    UniqueWords = np.array(getUniqueWords(corpus))
    IDF = getIDF(corpus, UniqueWords)

    TF_IDF = TF * IDF
    dummy = TF_IDF.tolist()
    return np.around(dummy,decimals=2)


if __name__ == '__main__':
    corpus = [
        'this is the first document mostly',
        'this document is the second document',
        'and this is the third one',
        'is this the first document here',
    ]

    # computeTFIDF(corpus)
    print(customTFIDF(corpus))



