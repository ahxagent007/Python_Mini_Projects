import json
import spark as spark
import time as today


def convertToJson(json_list):
    load_date = today.strftime("%Y-%m-%d")
    client = 'zeus'

    output = load_date + '|' + client + '|' + str(json.dumps(json_list))
    return output

jsonDF = spark.sql("""select * from json_ready_tbl""")
#jsonRDD = jsonDF.rdd.map(lambda x: convertToJson(x)).saveAsTextFile('/hdfs/output/dir')

# n is the number of batch
n = 1000
i = 0
json_list = []
for jdf in jsonDF:
    json_list.append(jdf)
    i += 1
    if i>n-1:
        output = convertToJson(json_list)
        #print(output)
        jsonRDD = jsonDF.rdd.map(output).saveAsTextFile('/hdfs/output/dir')
        i=0
        json_list = []