from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("appingest").getOrCreate()
    #.config('spark.jars','/home/maheshp/Downloads/mysql-connector-j-9.1.0/mysql-connector-j-9.1.0.jar')\


print(spark) 

df = spark.read.csv('sample.csv')
#df = spark.createDataFrame(data)
# df = crt_sn.read.format("jdbc")\
#     .option("driver","com.mysql")\
#     .option("url","jdbc:mysql://localhost:3306/")\
#     .option("driver",)\
#     .option("dbtable",)\
#     .option("user","root")\
#     .option("pasword",)\
#     .load()

#df = spark.read.json("/home/maheshp/Desktop/student.json")
print(df.show())

# df.createOrReplcaeView("student")

# sprkdf = spark.sql("select * from student")

# print(sprkdf.show())

