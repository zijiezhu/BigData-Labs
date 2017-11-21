from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext

def pair(line):
    words = line.split()
    return [(words[i].encode('utf-8'), words[i+1].encode('utf-8')) for i in range(len(words)-1)]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    sentences = lines.glom() \
                  .map(lambda x: " ".join(x)) \
                  .flatMap(lambda x: x.split("."))

    #Your code goes here

    bigrams = sentences.flatMap(lambda line: pair(line)).map(lambda bigram: (bigram, 1))
    counts = bigrams.reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False)
    result = sc.parallelize(counts.take(100))
    
    result.saveAsTextFile("bi.out")  

    sc.stop()
