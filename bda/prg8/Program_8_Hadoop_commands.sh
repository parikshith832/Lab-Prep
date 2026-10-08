javac -classpath `hadoop classpath` -d . WordCount.java
jar cf wc.jar Wordcount*.class
hdfs dfs -mkdir -p /user/cloudera/input
hdfs dfs -put sample.txt /user/cloudera/input/
hadoop jar wc.jar WordCount /user/cloudera/input /user/cloudera/output
hdfs dfs -cat /user/cloudera/output/part-r-00000
spark-submit wordcount.py
hdfs dfs -ls /user/cloudera/output_spark
hdfs dfs -cat /user/cloudera/output_spark/part-00000
