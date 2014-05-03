import os
import json




data_obj = {}
data_obj['a'] = 'a'

if os.path.isfile("john.json"):
    fp = open("john.json", 'r+')
else:
    fp = open("john.json", 'w+')
    json.dump(data_obj, fp)
    
    fp.close()
    fp = open("john.json", 'r+')

    #print "fp contents"
    #print fp.read()
json_obj = json.loads(fp.read())
fp.close()

print json_obj


# Now try to change json_obj, and write it back to the file
json_obj['b'] = 'b'

fp = open("john.json", 'w+')
json.dump(json_obj, fp)

fp.close()
fp = open("john.json", 'r+')
json_obj = json.loads(fp.read())
fp.close()

print json_obj