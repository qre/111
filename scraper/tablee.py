import json2table
import json
#from ematiq import 'File.json'
infoFromJson = json.loads('File.json')
build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style": "width:100%"}
print(json2table.convert(infoFromJson, 
                         build_direction=build_direction, 
                         table_attributes=table_attributes))