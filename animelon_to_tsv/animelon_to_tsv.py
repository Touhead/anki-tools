import argparse
import os
import romkan

parser = argparse.ArgumentParser(description='Animelon vocabulary files to .tsv converter')
parser.add_argument('--f', dest='filename', help='File to convert')

args = parser.parse_args()

if args.filename:
	with open(args.filename, encoding='utf-8') as f:
		dest = os.path.splitext(args.filename)[0] + ".tsv"
		dest_file = open(dest, "w", encoding='utf-8')
		for line in f.readlines():
			if len(line) == 1:
				continue
			r = line.replace("\n","").split(" :    ")
			r = r[0].split(" ") + r[1:2]
			print(r)
			dest_file.write(r[0])
			dest_file.write("	")
			dest_file.write(r[2])
			dest_file.write("	")
			dest_file.write(romkan.to_hiragana(r[1]))
			dest_file.write("\n")