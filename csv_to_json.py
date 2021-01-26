import csv
import json
import pprint

# json_list = []
# json_data = {}
#
# # CSVファイルのロード
# with open('jio.csv', 'r') as f:
#     # list of dictの作成
#     for line in csv.DictReader(f):
#         json_list.append(line)
#
# print(json.dumps(json_list, indent=2))

# Import JSON file into dict
# with open('config.json') as json_file:
#     data = json.load(json_file)
#     pprint.pprint(data)

# Re-export dict into JSON file
# with open('config2.json', 'w') as json_file2:
#     json.dump(data, json_file2, indent=2)

# # Not needed if the CSV file itself includes headers
# bgp_header = ['node','interface','vrf','ipv6','peer_address','remote_as','evpn_safi','ipv4','update_source']
# ip_addr_header = ['node','interface','vrf','primary_ipv4','secondary_ipv4','primary_ipv6','secondary_ipv6']

# with open('bgp.csv', 'r') as f:
#     for row in csv.DictReader(f):
#         print(row)
#
# with open('ip_addr.csv', 'r') as f:
#     for row in csv.DictReader(f):
#         print(row)

with open('bgp.csv', 'r') as f:
    bgp = csv.DictReader(f)
    for row in bgp:
        print(row)

with open('ip_addr.csv', 'r') as f:
    ip_addr = csv.DictReader(f)
    for row in ip_addr:
        print(row)

# Now I have opened BGP configuration and IP/interface configuration as 2 dict files.
# Now I need to create a third dict file which can be export into JSON