from pyspark import SparkContext
from pyspark.streaming import StreamingContext
if __name__ == "__main__":
    sc = SparkContext(appName="PythonStreamingNetworkWordCount")
    ssc = StreamingContext(sc, 5)                                  # 2nd parameter is duration in seconds

    lines = ssc.socketTextStream('localhost', 9000)
    counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda word: (word, 1))\
                  .reduceByKey(lambda a, b: a + b)
    
    counts.pprint()
        
    ssc.start()
    ssc.awaitTermination()