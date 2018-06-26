# ProfileToCsv
This is a program that takes the .json.gzip file and converts it to a .csv file with ! delimiters. Each row consists of data from one profile shard. Each row for a shard called shard consists of:
1. shard.id
2. shard.searches.query.time_in_nanos
3. shard.aggregations.time_in_nanos

## Usage
Just type `python3 main.py` in a terminal to run the program. Currently, the input and output files can only be changed by changing the `in_filename` and `out_filename` variables in main.py.
