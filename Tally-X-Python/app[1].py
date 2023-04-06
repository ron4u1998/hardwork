import json
from termcolor import colored
import xml.etree.ElementTree as Et
import requests


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# tally ip and port
url = "http://localhost:9000"
# XML body to send - Payload
with open('xml_flie/fetchledger.xml', 'r') as f:
    ledger_data = f.read()
# data = Et.parse('country_data.xml')
# make request
ledger_request = requests.post(url=url, data=ledger_data)
# parse response
# response = request.text.strip().replace("&amp;","and") #replace special char &
ledger_response = ledger_request.text.strip()
responseXML = Et.fromstring(ledger_response)
# loop through xmlnodes and get ledger names using Xpath
ledger_list = []
for data in responseXML.findall('./BODY/DATA/COLLECTION/LEDGER'):
    dataOFledger = data.get('NAME')
    ledger_list.append(dataOFledger)
# this will show the list of ledger available in Tally prime
# print(ledger_list)
f = open('json_file/4_3.json')
data = json.load(f)
led_name = data['COMP_NAME']
led_group = 'Sundry Debtors'
led_address = data['COMP_ADD']
led_country = 'India'
led_state = data['COMP_STATE']
led_mobile = '9987546523'
led_gst = data['COMP_GST']

if led_name in ledger_list:
    print(color.RED + color.BOLD + 'Ledger already exits')
else:
    # ledger creation
    data = '<ENVELOPE><HEADER><TALLYREQUEST>Import Data</TALLYREQUEST></HEADER><BODY>'
    data += '<IMPORTDATA><REQUESTDESC><REPORTNAME>All Masters</REPORTNAME></REQUESTDESC><REQUESTDATA>'
    data += '<TALLYMESSAGE xmlns:UDF="TallyUDF"><LEDGER Action="Create"><NAME>' + \
        led_name+'</NAME><PARENT>'+led_group
    data += '</PARENT><ADDRESS>'+led_address + \
        '</ADDRESS><COUNTRYOFRESIDENCE>'+led_country+'</COUNTRYOFRESIDENCE>'
    data += '<LEDSTATENAME>'+led_state+'</LEDSTATENAME><LEDGERMOBILE>' + \
        led_mobile+'</LEDGERMOBILE><PARTYGSTIN>'
    data += led_gst+'</PARTYGSTIN></LEDGER></TALLYMESSAGE></REQUESTDATA></IMPORTDATA></BODY></ENVELOPE>'

    # post the data into tally prime
    req = requests.post(url=url, data=data)


# with open('xml_flie/stockitems_fetch.xml', 'r') as f:
#     stock_data = f.read()

# stock_request = requests.post(url=url, data=stock_data)
# stock_response = stock_request.text.strip()
# responseXML = Et.fromstring(stock_response)

# stockitem_list = []
# for data in responseXML.findall('./BODY/DATA/COLLECTION/STOCKITEM'):
#     # data1 = list(data.get('NAME'))
#     dataOFstock = data.get('NAME')
#     stockitem_list.append(dataOFstock)
# print(color.GREEN, stockitem_list)

# f = open('json_file/stock_items.json')
# data = json.load(f)

# stock_data = '<ENVELOPE><HEADER><TALLYREQUEST>Import Data</TALLYREQUEST></HEADER><BODY>'
# stock_data += '<IMPORTDATA><REQUESTDESC><REPORTNAME>Stock Item</REPORTNAME></REQUESTDESC>'
# stock_data += '<REQUESTDATA ><TALLYMESSAGE xmlns: UDF = "TallyUDF" > \
#     <STOCKITEM NAME = "Product 1" ACTION = "Create" ><NAME > 40X2 ST Flow Solder Socket < /NAME ><BATCHALLOCATIONS.LIST >\
#         <AMOUNT > 2, 600.000 < /AMOUNT ></BATCHALLOCATIONS.LIST ></STOCKITEM ></TALLYMESSAGE></REQUESTDATA></IMPORTDATA></BODY></ENVELOPE>'

# req = requests.post(url=url, data=stock_data)
