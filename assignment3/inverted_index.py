import MapReduce
import sys

#Creating a map reduce object.
mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    document_id = record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w, document_id)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = list()
    for v in list_of_values:
        if v not in total:
            total.append(v)
    mr.emit((key, total))    


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
