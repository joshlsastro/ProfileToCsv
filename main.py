#!/usr/bin/python3
"""This code takes JSON from a gzip'd input file and writes an output CSV file.
Consult the README for details."""

import csv
import gzip
import json

in_filename = "uprightRevenge14d-20180625-232147.json.gzip" #Name of input file
out_filename = "output_table.csv" #Name of output file

with gzip.open(in_filename, "rb") as f:
    text = f.read()

text = text.decode()
all_json = json.loads(text)
shards = all_json["profile"]["shards"]

def get_info_from_row(number_of_shard):
    """Returns id, the searches' query time in nanos, and the aggregations' time in nanos for a shard given its number."""
    global shards
    shard = shards[0]
    what = shard['id']
    searches = shard['searches']
    agg = shard['aggregations']
    searches_time_in_nanos = searches[0]['query'][0]['time_in_nanos']
    agg_time_in_nanos = agg[0]['time_in_nanos']
    return what, searches_time_in_nanos, agg_time_in_nanos

outputList = []
for i in range(len(shards)):
    what, s_time, a_time = get_info_from_row(i)
    outputList.append([what, s_time, a_time])

with open(out_filename, "w") as f:
    writer = csv.writer(f, delimiter = "!")
    for row in outputList:
        writer.writerow(row)

