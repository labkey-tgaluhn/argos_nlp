--author@esilgard--
--last updated October 2014--


This is the primary directory for the HIDRA (Hutch Integraded Data Repository and Archive) natural language processing engine for the parsing of clinical documents and the classification and automated extraction of clinical data elements

command_line_flags.txt 
	a tab delimited text file containing command line flags and their descriptions in the format:
	flag<tab>required/not_required<tab>short_description<tab>long_description

nlp_engine.py
	the primary script for the natural language processing engine.  it requires a set of flagged command line arguments, as well as the command_line_flag file which gives their mappings, and input document(s)
(for not this is a tab delimited file in the format of the Amalga Import OBX table)

__init__.py 
	required for module imports

fhcrc_pathology
	directory of modules for processing pathology reports

make_text_output_directory.py
	a python script to create a directory for output text files (the directory location is expected to match the input file name location)

output_results.py
	output the final JSON object to the location specified by the command line -o flag
	