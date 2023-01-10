#!/usr/bin/env python3
import json
import sys

# load data from json into dictionarz format, load template and load output file
json_file = open(sys.argv[1], 'r')
json_data = json.load(json_file)
output_file = open('output.cpp', 'w')
template = open('template.cpp', 'r')
    
# reading all lines from template
while True:

    # reading new line and add it into output_file
    line = template.readline()
    output_file.writelines(line)

    # if it gets on initItems it generate everzting needed from json file into initItems function
    if line.strip() == "void DeviceAB::initItems()" and template.readline().strip() == "{" :
        output_file.writelines("{\n")
        for i  in json_data:
            for j in json_data[i]:
                output_file.writelines("""    initDataItem(\"""" + str(j['name']) + """\", """ + str(j['tag']) + """, \"""" + str(j['type']) + """\", """ + str(j['size']) + """); \n""")

    # if it gets into initCollections it generates everything needed from json file into initCollections 
    if line.strip() == "std::shared_ptr<Iolink> Colection = Iolink::getInstance();":
        for i  in json_data:
            for j in json_data[i]:
                output_file.writelines("""    Colection.""" + i + """->push(\"""" + str(j['name']) + """\");\n""")
        
    # break on end of file
    if not line:
        break

output_file.close()