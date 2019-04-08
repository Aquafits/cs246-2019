import sys

from pyspark import SparkContext, SparkConf

conf = SparkConf()
sc = SparkContext(conf=conf)
print("{0} lines".format(sc.textFile(sys.argv[1]).count()))
