import argparse
import os

parser = argparse.ArgumentParser(description='Add tag to .tsv file')
parser.add_argument('--f', dest='filename', help='File to add tag')
parser.add_argument('--t', dest='tag', help='Tag to be added')

args = parser.parse_args()

if args.filename:
	with open(args.filename, encoding='utf-8') as f:
		dest = os.path.splitext(args.filename)[0] + "_tag.tsv"
		dest_file = open(dest, "w", encoding='utf-8')
		for line in f.readlines():
			dest_file.write(line.strip("\n"))
			dest_file.write("	")
			dest_file.write(args.tag)
			dest_file.write("\n")