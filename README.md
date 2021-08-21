# KKolab

Students of Data Science need to install or have access to a range of complex software. Most of these software run on Linux and this means that students have to either reconfigure their Windows machines to have access to Linux VMs. Even then, installation of these softwares proves difficult because of differences in machine configuration, different home directories, differing paths and many other complications. <br>

To avoid wasting time in sorting out these myriad installation challenges, students at Praxis Business School, are encouraged to work on Google Colab. While Colab was designed to be a hosted version of Jupyter Notebook, it is in reality a very powerful Ubuntu VM whose underlying shell can be accessed by prefacing commands with ! <br>

Using this strategy, it is possible to install a whole range of software on the underlying VM and use it for academic and pedagogical purposes. Since the VM is not persistent, the installion needs to be done each time the Colab notebook is started. However data and configuration files can be persistently stored on the users Google Drive. This drive can be mounted in the VM and can be used. The biggest advantage of using this strategy is that all dependencies are taken care of within the notebook cells itself. <br>

The following notebooks demonstrate the installation and usage of different software. They should work out-of-the-box. The only change that might be necessary is the version number of the download file and the corresponding change in name directory, the value of the $HOME environment variable and the contents of the $PATH <br>

1. Install MySQL in Colab VM and execute SQL statements [MySQL Local Shell Pandas](https://github.com/prithwis/KKolab/blob/main/KK_A1_MySQL_Local_Shell_Pandas.ipynb)
2. Connect to a remote MySQL server and execute SQL statements [MySQL Remote Shell Pandas](https://github.com/prithwis/KKolab/blob/main/KK_A2_MySQL_Remote_Shell_Pandas.ipynb)
3. Install Hadoop in VM, Run Wordcount program : [Hadoop Wordcount](https://github.com/prithwis/KKolab/blob/main/KK_B1_Hadoop_WordCount.ipynb)
4. Install Hadoop, Hive. Run queries, load bulk data [Hadoop Hive](https://github.com/prithwis/KKolab/blob/main/KK_B2_Hadoop_and_Hive.ipynb)
5. Install Hadoop, HBase, Run queries, load bulk data [Hadoop HBase](https://github.com/prithwis/KKolab/blob/main/KK_B3_Hadoop_HBase.ipynb)
6. Install Spark, Run WordCount program [Spark WordCount](https://github.com/prithwis/KKolab/blob/main/KK_C2_Spark_WordCount.ipynb)
7. Install Spark, use SparkSQL, SQLContext, HiveContext [Spark SQL Hive](https://github.com/prithwis/KKolab/blob/main/KK_C1_SparkSQL_SQLContext_HiveContext.ipynb)
8. Install MongoDB in local VM, Run basic CRUD operations [MongoDB getting started](https://github.com/prithwis/KKolab/blob/main/KK_D1_MongoDB_Local_CRUD_operations.ipynb)
9. Access MongoDB on a remote site, load bulk data, complex queries [MongoDB Remote Complex queries](https://github.com/prithwis/KKolab/blob/main/KK_D2_MongoDB_Remote_Complex_Queries.ipynb)
10. Install MongoDB, Spark on local VM and access MongoDB from Spark [MongoDB Spark](https://github.com/prithwis/KKolab/blob/main/KK_D3_MongoDB_Spark.ipynb)
11. Install Cassandra, Access from Shell and Python [Cassandra Getting Started](https://github.com/prithwis/KKolab/blob/main/KK_E1_Cassandra_Getting_Started.ipynb)

## Password matters
In certain cases, passwords and other user credentials need to be supplied. While normal users may hardcode this into the notebook as a variable, a public notebook -- like the ones that are stored here -- cannot have them hardwired and visible. Hence in these cases, we have taken the strategy of storing the credentials as .py files in Google Drive. During usage, these Google Drive is mounted, the file copied into the VM and then the variables are _imported_.
