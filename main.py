#!/usr/bin/python3
"""This code takes JSON from a gzip'd input file and writes an output CSV file.
Consult the README for details."""

import argparse
import gzip
import json

parser = argparse.ArgumentParser(description = "Converts gzip'd JSON file to more useful JSON format.")
parser.add_argument("-o", help = "Output file.")
parser.add_argument("in_file", help="Input .json.gz file.")
args = parser.parse_args()
if args.in_file:
    args = vars(args)
    in_filename = args['in_file']
    out_filename = args['o']

with gzip.open(in_filename, "rb") as f:
    text = f.read()

text = text.decode()
all_json = json.loads(text)
shards = all_json["profile"]["shards"]

def get_info_from_row(number_of_shard):
    """Returns id, the searches' query time in nanos, and the aggregations' time in nanos for a shard given its number."""
    global shards
    shard = shards[number_of_shard]
    what = shard['id']
    searches = shard['searches']
    agg = shard['aggregations']
    searches_time_in_nanos = searches[0]['query'][0]['time_in_nanos']
    agg_time_in_nanos = agg[0]['time_in_nanos']
    return what, searches_time_in_nanos, agg_time_in_nanos

def parse_id(what):
    """Parses ID. Returns index and the rest of the ID."""
    what = what.split("][")
    index = what[1]
    rest = what[0] + "][" + what[2]
    return index, rest

l_output = []
for i in range(len(shards)):
    what, s_time, a_time = get_info_from_row(i)
    index, what = parse_id(what)
    l_output.append([index, what, s_time, a_time])

output = {}
for elem in l_output:
    index = elem[0]
    keys = output.keys()
    if index in keys:
        pass
    else:
        output[index] = []
    output[index].append([elem[1], elem[2], elem[3]])

output = json.dumps(output)
with open(out_filename, "w") as f:
    f.write(output)
