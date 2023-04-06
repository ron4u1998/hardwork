import json
from xml.etree.ElementTree import Element

# Load the JSON data from a string
data = json.loads('''
{
  "HEADER": {
    "TALLYREQUEST": "Import Data"
  },
  "BODY": {
    "IMPORTDATA": {
      "REQUESTDESC": {
        "REPORTNAME": "All Masters"
      },
      "REQUESTDATA": {
        "TALLYMESSAGE": {
          "LEDGER": {
            "Action": "Create",
            "NAME": "Name",
            "PARENT": "Sundry Creditors",
            "ADDRESS": "Address",
            "COUNTRYOFRESIDENCE": "Country",
            "LEDSTATENAME": "State",
            "LEDGERMOBILE": "Mobile",
            "PARTYGSTIN": "GSTIN"
          }
        }
      }
    }
  }
}
''')

# Define a function to convert a dictionary to an XML element
def dict_to_xml(tag, d):
    # Create an element with the given tag name
    elem = Element(tag)

    # If the dictionary is empty, return the element
    if not d:
        return elem

    # Iterate over the dictionary items
    for key, value in d.items():
        # If the value is a dictionary, recursively convert it to an XML element and add it as a child
        # of the current element.
        if isinstance(value, dict):
            elem.append(dict_to_xml(key, value))
        # If the value is a list, convert each item in the list to an XML element and add them as
        # children of the current element.
        elif isinstance(value, list):
            for item in value:
                elem.append(dict_to_xml(key, item))
        # Otherwise, add the key-value pair as an attribute of the current element.
        else:
            elem.set(key, value)

    # Return the element
    return elem

# Convert the dictionary to an XML element
root = dict_to_xml('ENVELOPE', data)

# Print the XML element
print(Element.tostring(root, encoding='unicode'))
