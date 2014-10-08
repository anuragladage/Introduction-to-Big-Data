import MapReduce
import sys

mr = MapReduce.MapReduce()
def mapper(record):
	if record[0] == "a":
		for i in range(5):
			key = (record[1],i)
			value = (record[0],record[2],record[3])
			mr.emit_intermediate(key,value)
	if record[0] == "b":
		for i in range(5):
			key = (i,record[2])
			value = (record[0],record[1],record[3])
			mr.emit_intermediate(key,value)

def reducer(key,list_of_values):
	multiplied_value = 0
	for v1 in list_of_values:
		for v2 in list_of_values:
			if v1[0]=="a" and v2[0]=="b" and v1[1] ==v2[1]:
				multiplied_value = multiplied_value + v1[2]*v2[2]
	mr.emit((key,multiplied_value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)