![alt text](https://4.bp.blogspot.com/-gbL5nZDkpFQ/XScFYwoTEII/AAAAAAAAAGY/CcVb_HDLwvs2Brv5T4vSsUcz7O4r2Q79ACK4BGAYYCw/s1600/kk3-header00-beta.png)<br>
[Praxis Business School](https://praxis.ac.in)<br>
## Big Data with Spark & NoSQL in Google Colab

Students of Data Science need to install or have access to a range of complex software. Most of these softwares run on Linux. This means that students have to either reconfigure their Windows machines to run Linux VMs with Dockers, WSL etc or get a separate Linux machine. Even then, installation of these softwares proves difficult because of differences in machine configuration, different home directories, differing paths and many other complications. <br>

To avoid wasting time in sorting out these myriad installation challenges, students at [Praxis Business School](https://praxis.ac.in/Programs/data-science-course-program/) are encouraged to work on Google Colab. While Colab was designed to be a hosted version of Jupyter Notebook and run Python programs, it is in reality a very powerful Ubuntu VM whose underlying shell and OS can be accessed by prefixing commands with '__!__' <br>

Using this strategy, it is possible to install and use any software in the terminal mode on the underlying VM and use it for academic and pedagogical purposes. Obviously production grade installations are not recommended. Since the VM is not persistent, the installion needs to be done each time the Colab notebook is started. However data and configuration files can be persistently stored on the users Google Drive that can be mounted in the VM and be used with read-write access. The biggest advantage of using this strategy is that all dependencies are taken care of within the notebook cells itself. _Web based GUI frontends can be accessed with tunnels as shown in the Spark Wordcount example_ <br>

The following notebook URLs demonstrate and serve as templates for Colab Notebooks for the installation and usage of different software. They should work out-of-the-box. After opening the URL, use ![button](https://camo.githubusercontent.com/52feade06f2fecbf006889a904d221e6a730c194/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667) button to open a safe, editable and executable copy of the codebase in Google Colab. The only change that might be necessary is the version number of the download file and the corresponding change in names of directories, the values of the $HOME environment variables and the contents of the $PATH <br>

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
In certain cases, passwords and other user credentials need to be supplied. While normal users may hardcode this into the notebook as a variable, a public notebook -- like the ones that are stored here -- cannot have them hardwired and visible. Hence in these cases, we have taken the strategy of storing the credentials as .py files in Google Drive. During usage, these Google Drive is mounted, the file copied into the VM and then the variables are _imported_. <br> <br>


[Data Science @ Praxis Business School](https://praxis.ac.in/Programs/data-science-course-program/)<br>
