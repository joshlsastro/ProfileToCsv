# ProfileToCsv
This is a program that takes in the .json.gz file and outputs a .json file. The .json file is a dictionary; the keys are the "metric" parts of shard.id. The values correspond to the keys in triplets like this: 
1. The rest of shard.id
2. shard.searches.query.time_in_nanos
3. shard.aggregations.time_in_nanos

## Usage
Just type `python3 main.py -o output_file input_file` in a terminal to run the program. It will **not** work with Python 2.
