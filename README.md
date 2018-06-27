# ProfileToCsv
This is a program that takes the .json.gzip file and converts it to a .csv file with ! delimiters. Each row consists of data from one profile shard. Each row for a shard called shard consists of:
1. shard.id
2. shard.searches.query.time_in_nanos
3. shard.aggregations.time_in_nanos

## Usage
Just type `python3 main.py -o output_file input_file` in a terminal to run the program. 
