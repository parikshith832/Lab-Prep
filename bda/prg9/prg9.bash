sudo service cloudera-scm-server start
sudo service cloudera-scm-agent start
sudo service --status-all | grep cloudera
cd /home/cloudera
ls
cat employees.csv
hdfs dfs -mkdir -p /user/cloudera/data
hdfs dfs -put employees.csv /user/cloudera/data/
hdfs dfs -ls /user/cloudera/data
hdfs dfs -cat /user/cloudera/data/employees.csv