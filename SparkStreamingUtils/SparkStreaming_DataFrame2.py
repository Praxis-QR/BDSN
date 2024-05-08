from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9000) \
    .load()

# Split the lines into words
words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)

# Generate running word count
wordCounts = words.groupBy("word").count()

# Sort the wordCounts DataFrame by count in descending order
sortedWordCounts = wordCounts.orderBy("count", ascending=False)

# Take top 10 words
topWords = sortedWordCounts.limit(10)

 # Start running the query that prints the running counts to the console
query = topWords \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()


query.awaitTermination()