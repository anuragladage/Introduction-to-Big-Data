import MapReduce
import sys

#Creating a map reduce object.
mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    joined_list = list()
    for i in range(1,len(list_of_values)):
    	mr.emit(list_of_values[0] + list_of_values[i])



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
