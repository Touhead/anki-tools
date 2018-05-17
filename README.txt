Anki Tools - Version 1.0 - Python 3.5.3 / Ruby 2.4.1 - 05/17/2018

This project has for goal to gather multiple tools to enhance Anki. 
These tools are mainly focused on Japanese.

FEATURES AND USAGES
--------------------

# Convert Imiwa or Animelon vocabulary list to .tsv
python animelon_to_tsv.py --f <file_path>
or
.\ImiImport.exe <file_path.imixch> > <file_path.tsv>

# Add sample phrase to a .tsv
add_sample_sentences.rb
Which file contains your cards? The first column must be in your target language.
<file_path>
What is the Tatoeba code for your target language?
jpn
Do you want the translations of the sample sentences as well? If so, enter the appropriate Tatoeba code for the language to translate them to (e. g. 'eng' for English). Leave blank if you don't want a translation.
eng

# Add tag at the end of a .tsv
python add_tag.py --f <file_path> --t <tag>

LINKS
--------------------

https://github.com/rotud/ImiImport
https://github.com/Sprachprofi/anki_utils