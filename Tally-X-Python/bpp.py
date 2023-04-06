import json
import requests
import xml.etree.ElementTree as Et
from termcolor import colored
url = "http://localhost:9000"

f = open('json_file\\1210.json')
ledger_data = json.load(f)
led_name = ledger_data['COMP_NAME']
led_group = 'Sundry Debtors'
led_address = ledger_data['COMP_ADD']
led_country = 'India'
led_state = ledger_data['COMP_STATE']
led_mobile = '9987546523'
led_gst = ledger_data['COMP_GST']
led_total = ledger_data['TOTAL']
total_gst = ledger_data['TAX_AMOUNT']

f = open('json_file\\1210_table.json')
stock_data = json.load(f)
stock_desc = stock_data['Description of Goods']
print(stock_desc)
stock_qty = stock_data['Quantity']
print(stock_qty)
stock_rate = stock_data['Rate']
print(stock_rate)
stock_amt = stock_data['Amount']
print(stock_amt)
stock_per = stock_data['per']
print(stock_per)


data = '<ENVELOPE><HEADER><TALLYREQUEST>Import Data</TALLYREQUEST></HEADER><BODY>'
data += '<IMPORTDATA><REQUESTDESC><REPORTNAME>Vouchers</REPORTNAME><STATICVARIABLES><SVCURRENTCOMPANY>Samyak Infotech Pvt Ltd</SVCURRENTCOMPANY></STATICVARIABLES>'
data += '</REQUESTDESC><REQUESTDATA><TALLYMESSAGE xmlns:UDF="TallyUDF"><VOUCHER VCHTYPE="Purchase" ACTION="Create" OBJVIEW="Invoice Voucher View">'
data += '<ADDRESS.LIST TYPE="String"><ADDRESS>None</ADDRESS></ADDRESS.LIST><BASICBUYERADDRESS.LIST TYPE="String"><BASICBUYERADDRESS>Memnagar</BASICBUYERADDRESS>'
data += '</BASICBUYERADDRESS.LIST><OLDAUDITENTRYIDS.LIST TYPE="Number"><OLDAUDITENTRYIDS>-1</OLDAUDITENTRYIDS></OLDAUDITENTRYIDS.LIST><DATE>20220401</DATE>'
data += '<REFERENCEDATE>20220401</REFERENCEDATE><GUID>ec393735-c49b-42c2-83a4-9daceb111ab5-00000009</GUID><VATDEALERTYPE/><STATENAME>Gujarat</STATENAME><VOUCHERTYPENAME>Purchase</VOUCHERTYPENAME>'
data += '<COUNTRYOFRESIDENCE>India</COUNTRYOFRESIDENCE><PARTYGSTIN>24AACFI8730P1Z0</PARTYGSTIN><PLACEOFSUPPLY>Gujarat</PLACEOFSUPPLY><PARTYNAME>' + \
    led_name+'</PARTYNAME><PARTYLEDGERNAME>'+led_name+'</PARTYLEDGERNAME>'
data += '<REFERENCE>1210/2122</REFERENCE><PARTYMAILINGNAME>'+led_name + \
    '</PARTYMAILINGNAME><CONSIGNEEMAILINGNAME>Samyak Infotech Pvt Ltd</CONSIGNEEMAILINGNAME><CONSIGNEESTATENAME>Gujarat</CONSIGNEESTATENAME>'
data += '<VOUCHERNUMBER>1</VOUCHERNUMBER><BASICBASEPARTYNAME>'+led_name + \
    '</BASICBASEPARTYNAME><CSTFORMISSUETYPE/><CSTFORMRECVTYPE/><FBTPAYMENTTYPE>Default</FBTPAYMENTTYPE><PERSISTEDVIEW>Invoice Voucher View</PERSISTEDVIEW>'
data += '<BASICBUYERNAME>Samyak Infotech Pvt Ltd</BASICBUYERNAME><CONSIGNEECOUNTRYNAME>India</CONSIGNEECOUNTRYNAME><VCHGSTCLASS/><VCHENTRYMODE>Item Invoice</VCHENTRYMODE><DIFFACTUALQTY>No</DIFFACTUALQTY><ISMSTFROMSYNC>No</ISMSTFROMSYNC><ISDELETED>No</ISDELETED><ISSECURITYONWHENENTERED>No</ISSECURITYONWHENENTERED><ASORIGINAL>No</ASORIGINAL><AUDITED>No</AUDITED><FORJOBCOSTING>No</FORJOBCOSTING><ISOPTIONAL>No</ISOPTIONAL><EFFECTIVEDATE>20220401</EFFECTIVEDATE><USEFOREXCISE>No</USEFOREXCISE><ISFORJOBWORKIN>No</ISFORJOBWORKIN><ALLOWCONSUMPTION>No</ALLOWCONSUMPTION><USEFORINTEREST>No</USEFORINTEREST><USEFORGAINLOSS>No</USEFORGAINLOSS><USEFORGODOWNTRANSFER>No</USEFORGODOWNTRANSFER><USEFORCOMPOUND>No</USEFORCOMPOUND><USEFORSERVICETAX>No</USEFORSERVICETAX><ISONHOLD>No</ISONHOLD><ISBOENOTAPPLICABLE>No</ISBOENOTAPPLICABLE><ISGSTSECSEVENAPPLICABLE>No</ISGSTSECSEVENAPPLICABLE><ISEXCISEVOUCHER>No</ISEXCISEVOUCHER><EXCISETAXOVERRIDE>No</EXCISETAXOVERRIDE><USEFORTAXUNITTRANSFER>No</USEFORTAXUNITTRANSFER><IGNOREPOSVALIDATION>No</IGNOREPOSVALIDATION><EXCISEOPENING>No</EXCISEOPENING><USEFORFINALPRODUCTION>No</USEFORFINALPRODUCTION><ISTDSOVERRIDDEN>No</ISTDSOVERRIDDEN><ISTCSOVERRIDDEN>No</ISTCSOVERRIDDEN><ISTDSTCSCASHVCH>No</ISTDSTCSCASHVCH><INCLUDEADVPYMTVCH>No</INCLUDEADVPYMTVCH><ISSUBWORKSCONTRACT>No</ISSUBWORKSCONTRACT><ISVATOVERRIDDEN>No</ISVATOVERRIDDEN><IGNOREORIGVCHDATE>No</IGNOREORIGVCHDATE><ISVATPAIDATCUSTOMS>No</ISVATPAIDATCUSTOMS><ISDECLAREDTOCUSTOMS>No</ISDECLAREDTOCUSTOMS><ISSERVICETAXOVERRIDDEN>No</ISSERVICETAXOVERRIDDEN><ISISDVOUCHER>No</ISISDVOUCHER><ISEXCISEOVERRIDDEN>No</ISEXCISEOVERRIDDEN><ISEXCISESUPPLYVCH>No</ISEXCISESUPPLYVCH><ISGSTOVERRIDDEN>No</ISGSTOVERRIDDEN><GSTNOTEXPORTED>No</GSTNOTEXPORTED><IGNOREGSTINVALIDATION>No</IGNOREGSTINVALIDATION><ISGSTREFUND>No</ISGSTREFUND><OVRDNEWAYBILLAPPLICABILITY>No</OVRDNEWAYBILLAPPLICABILITY><ISVATPRINCIPALACCOUNT>No</ISVATPRINCIPALACCOUNT><IGNOREEINVVALIDATION>No</IGNOREEINVVALIDATION><IRNJSONEXPORTED>No</IRNJSONEXPORTED><IRNCANCELLED>No</IRNCANCELLED><ISSHIPPINGWITHINSTATE>No</ISSHIPPINGWITHINSTATE><ISOVERSEASTOURISTTRANS>No</ISOVERSEASTOURISTTRANS><ISDESIGNATEDZONEPARTY>No</ISDESIGNATEDZONEPARTY><ISCANCELLED>No</ISCANCELLED><HASCASHFLOW>No</HASCASHFLOW><ISPOSTDATED>No</ISPOSTDATED><USETRACKINGNUMBER>No</USETRACKINGNUMBER><ISINVOICE>Yes</ISINVOICE><MFGJOURNAL>No</MFGJOURNAL><HASDISCOUNTS>No</HASDISCOUNTS><ASPAYSLIP>No</ASPAYSLIP><ISCOSTCENTRE>No</ISCOSTCENTRE><ISSTXNONREALIZEDVCH>No</ISSTXNONREALIZEDVCH><ISEXCISEMANUFACTURERON>No</ISEXCISEMANUFACTURERON><ISBLANKCHEQUE>No</ISBLANKCHEQUE><ISVOID>No</ISVOID><ORDERLINESTATUS>No</ORDERLINESTATUS><VATISAGNSTCANCSALES>No</VATISAGNSTCANCSALES><VATISPURCEXEMPTED>No</VATISPURCEXEMPTED><ISVATRESTAXINVOICE>No</ISVATRESTAXINVOICE><VATISASSESABLECALCVCH>No</VATISASSESABLECALCVCH><ISVATDUTYPAID>Yes</ISVATDUTYPAID><ISDELIVERYSAMEASCONSIGNEE>No</ISDELIVERYSAMEASCONSIGNEE><ISDISPATCHSAMEASCONSIGNOR>No</ISDISPATCHSAMEASCONSIGNOR><ISDELETEDVCHRETAINED>No</ISDELETEDVCHRETAINED><CHANGEVCHMODE>No</CHANGEVCHMODE><RESETIRNQRCODE>No</RESETIRNQRCODE><ALTERID> 18</ALTERID><MASTERID> 9</MASTERID><VOUCHERKEY>191774584733704</VOUCHERKEY><EWAYBILLDETAILS.LIST></EWAYBILLDETAILS.LIST><EXCLUDEDTAXATIONS.LIST></EXCLUDEDTAXATIONS.LIST><OLDAUDITENTRIES.LIST></OLDAUDITENTRIES.LIST><ACCOUNTAUDITENTRIES.LIST></ACCOUNTAUDITENTRIES.LIST><AUDITENTRIES.LIST></AUDITENTRIES.LIST><DUTYHEADDETAILS.LIST></DUTYHEADDETAILS.LIST>'
data += '<ALLINVENTORYENTRIES.LIST><STOCKITEMNAME>'+stock_desc + \
    '</STOCKITEMNAME><ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE>'
data += '<ISLASTDEEMEDPOSITIVE>Yes</ISLASTDEEMEDPOSITIVE><ISAUTONEGATE>No</ISAUTONEGATE><ISCUSTOMSCLEARANCE>No</ISCUSTOMSCLEARANCE><ISTRACKCOMPONENT>No</ISTRACKCOMPONENT><ISTRACKPRODUCTION>No</ISTRACKPRODUCTION><ISPRIMARYITEM>No</ISPRIMARYITEM><ISSCRAP>No</ISSCRAP>'
data += '<RATE>'+stock_rate+'</RATE><AMOUNT>'"-"+stock_amt+'</AMOUNT><ACTUALQTY> ' + \
    stock_qty+'</ACTUALQTY><BILLEDQTY> '+stock_qty + \
        '</BILLEDQTY><BATCHALLOCATIONS.LIST>'
data += '<GODOWNNAME>Main Location</GODOWNNAME><BATCHNAME>Primary Batch</BATCHNAME><INDENTNO/><ORDERNO/><TRACKINGNUMBER/><DYNAMICCSTISCLEARED>No</DYNAMICCSTISCLEARED>'
data += '<AMOUNT>'"-"+stock_amt+'</AMOUNT><ACTUALQTY> '+stock_qty+'</ACTUALQTY><BILLEDQTY> '+stock_qty + \
    '</BILLEDQTY><ADDITIONALDETAILS.LIST></ADDITIONALDETAILS.LIST><VOUCHERCOMPONENTLIST.LIST></VOUCHERCOMPONENTLIST.LIST></BATCHALLOCATIONS.LIST><ACCOUNTINGALLOCATIONS.LIST><OLDAUDITENTRYIDS.LIST TYPE="Number"><OLDAUDITENTRYIDS>-1</OLDAUDITENTRYIDS></OLDAUDITENTRYIDS.LIST>'
data += '<LEDGERNAME>Purchase GST</LEDGERNAME><GSTCLASS/><ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE><LEDGERFROMITEM>No</LEDGERFROMITEM><REMOVEZEROENTRIES>No</REMOVEZEROENTRIES><ISPARTYLEDGER>No</ISPARTYLEDGER><ISLASTDEEMEDPOSITIVE>Yes</ISLASTDEEMEDPOSITIVE><ISCAPVATTAXALTERED>No</ISCAPVATTAXALTERED><ISCAPVATNOTCLAIMED>No</ISCAPVATNOTCLAIMED>'
data += '<AMOUNT>'"-"+stock_amt+'</AMOUNT><SERVICETAXDETAILS.LIST></SERVICETAXDETAILS.LIST><BANKALLOCATIONS.LIST></BANKALLOCATIONS.LIST><BILLALLOCATIONS.LIST></BILLALLOCATIONS.LIST><INTERESTCOLLECTION.LIST></INTERESTCOLLECTION.LIST><OLDAUDITENTRIES.LIST></OLDAUDITENTRIES.LIST><ACCOUNTAUDITENTRIES.LIST></ACCOUNTAUDITENTRIES.LIST><AUDITENTRIES.LIST></AUDITENTRIES.LIST><INPUTCRALLOCS.LIST></INPUTCRALLOCS.LIST><DUTYHEADDETAILS.LIST></DUTYHEADDETAILS.LIST><EXCISEDUTYHEADDETAILS.LIST></EXCISEDUTYHEADDETAILS.LIST><RATEDETAILS.LIST></RATEDETAILS.LIST><SUMMARYALLOCS.LIST></SUMMARYALLOCS.LIST><STPYMTDETAILS.LIST></STPYMTDETAILS.LIST><EXCISEPAYMENTALLOCATIONS.LIST></EXCISEPAYMENTALLOCATIONS.LIST><TAXBILLALLOCATIONS.LIST></TAXBILLALLOCATIONS.LIST><TAXOBJECTALLOCATIONS.LIST></TAXOBJECTALLOCATIONS.LIST><TDSEXPENSEALLOCATIONS.LIST></TDSEXPENSEALLOCATIONS.LIST><VATSTATUTORYDETAILS.LIST></VATSTATUTORYDETAILS.LIST><COSTTRACKALLOCATIONS.LIST></COSTTRACKALLOCATIONS.LIST><REFVOUCHERDETAILS.LIST></REFVOUCHERDETAILS.LIST><INVOICEWISEDETAILS.LIST></INVOICEWISEDETAILS.LIST><VATITCDETAILS.LIST></VATITCDETAILS.LIST><ADVANCETAXDETAILS.LIST></ADVANCETAXDETAILS.LIST></ACCOUNTINGALLOCATIONS.LIST><DUTYHEADDETAILS.LIST></DUTYHEADDETAILS.LIST><SUPPLEMENTARYDUTYHEADDETAILS.LIST></SUPPLEMENTARYDUTYHEADDETAILS.LIST><TAXOBJECTALLOCATIONS.LIST></TAXOBJECTALLOCATIONS.LIST><REFVOUCHERDETAILS.LIST></REFVOUCHERDETAILS.LIST><EXCISEALLOCATIONS.LIST></EXCISEALLOCATIONS.LIST><EXPENSEALLOCATIONS.LIST></EXPENSEALLOCATIONS.LIST></ALLINVENTORYENTRIES.LIST><SUPPLEMENTARYDUTYHEADDETAILS.LIST></SUPPLEMENTARYDUTYHEADDETAILS.LIST><EWAYBILLERRORLIST.LIST></EWAYBILLERRORLIST.LIST><IRNERRORLIST.LIST></IRNERRORLIST.LIST><INVOICEDELNOTES.LIST></INVOICEDELNOTES.LIST><INVOICEORDERLIST.LIST></INVOICEORDERLIST.LIST><INVOICEINDENTLIST.LIST></INVOICEINDENTLIST.LIST><ATTENDANCEENTRIES.LIST></ATTENDANCEENTRIES.LIST><ORIGINVOICEDETAILS.LIST></ORIGINVOICEDETAILS.LIST><INVOICEEXPORTLIST.LIST></INVOICEEXPORTLIST.LIST><LEDGERENTRIES.LIST><OLDAUDITENTRYIDS.LIST TYPE="Number"><OLDAUDITENTRYIDS>-1</OLDAUDITENTRYIDS></OLDAUDITENTRYIDS.LIST>'
data += '<LEDGERNAME>'+led_name+'</LEDGERNAME><GSTCLASS/><ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE><LEDGERFROMITEM>No</LEDGERFROMITEM><REMOVEZEROENTRIES>No</REMOVEZEROENTRIES><ISPARTYLEDGER>Yes</ISPARTYLEDGER><ISLASTDEEMEDPOSITIVE>No</ISLASTDEEMEDPOSITIVE><ISCAPVATTAXALTERED>No</ISCAPVATTAXALTERED><ISCAPVATNOTCLAIMED>No</ISCAPVATNOTCLAIMED>'
data += '<AMOUNT>'+led_total + \
    '</AMOUNT><SERVICETAXDETAILS.LIST></SERVICETAXDETAILS.LIST><BANKALLOCATIONS.LIST></BANKALLOCATIONS.LIST><BILLALLOCATIONS.LIST>'
data += '<NAME>1210/2122</NAME><BILLTYPE>New Ref</BILLTYPE><TDSDEDUCTEEISSPECIALRATE>No</TDSDEDUCTEEISSPECIALRATE><AMOUNT>'+led_total+'</AMOUNT><INTERESTCOLLECTION.LIST></INTERESTCOLLECTION.LIST><STBILLCATEGORIES.LIST></STBILLCATEGORIES.LIST></BILLALLOCATIONS.LIST><INTERESTCOLLECTION.LIST></INTERESTCOLLECTION.LIST><OLDAUDITENTRIES.LIST></OLDAUDITENTRIES.LIST><ACCOUNTAUDITENTRIES.LIST></ACCOUNTAUDITENTRIES.LIST><AUDITENTRIES.LIST></AUDITENTRIES.LIST><INPUTCRALLOCS.LIST></INPUTCRALLOCS.LIST><DUTYHEADDETAILS.LIST></DUTYHEADDETAILS.LIST><EXCISEDUTYHEADDETAILS.LIST></EXCISEDUTYHEADDETAILS.LIST><RATEDETAILS.LIST></RATEDETAILS.LIST><SUMMARYALLOCS.LIST></SUMMARYALLOCS.LIST><STPYMTDETAILS.LIST></STPYMTDETAILS.LIST><EXCISEPAYMENTALLOCATIONS.LIST></EXCISEPAYMENTALLOCATIONS.LIST><TAXBILLALLOCATIONS.LIST></TAXBILLALLOCATIONS.LIST><TAXOBJECTALLOCATIONS.LIST></TAXOBJECTALLOCATIONS.LIST><TDSEXPENSEALLOCATIONS.LIST></TDSEXPENSEALLOCATIONS.LIST><VATSTATUTORYDETAILS.LIST></VATSTATUTORYDETAILS.LIST><COSTTRACKALLOCATIONS.LIST></COSTTRACKALLOCATIONS.LIST><REFVOUCHERDETAILS.LIST></REFVOUCHERDETAILS.LIST><INVOICEWISEDETAILS.LIST></INVOICEWISEDETAILS.LIST><VATITCDETAILS.LIST></VATITCDETAILS.LIST><ADVANCETAXDETAILS.LIST></ADVANCETAXDETAILS.LIST></LEDGERENTRIES.LIST><LEDGERENTRIES.LIST><OLDAUDITENTRYIDS.LIST TYPE="Number"><OLDAUDITENTRYIDS>-1</OLDAUDITENTRYIDS></OLDAUDITENTRYIDS.LIST><ROUNDTYPE/>'
data += '<LEDGERENTRIES.LIST><OLDAUDITENTRYIDS.LIST TYPE="Number"><OLDAUDITENTRYIDS>-1</OLDAUDITENTRYIDS></OLDAUDITENTRYIDS.LIST><LEDGERNAME>IGST</LEDGERNAME><GSTCLASS/><ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE><LEDGERFROMITEM>No</LEDGERFROMITEM><REMOVEZEROENTRIES>No</REMOVEZEROENTRIES><ISPARTYLEDGER>No</ISPARTYLEDGER><ISLASTDEEMEDPOSITIVE>Yes</ISLASTDEEMEDPOSITIVE><ISCAPVATTAXALTERED>No</ISCAPVATTAXALTERED><ISCAPVATNOTCLAIMED>No</ISCAPVATNOTCLAIMED>'
data += '<AMOUNT>'"-"+total_gst+'</AMOUNT><VATEXPAMOUNT>'"-"+total_gst+'</VATEXPAMOUNT><SERVICETAXDETAILS.LIST></SERVICETAXDETAILS.LIST><BANKALLOCATIONS.LIST></BANKALLOCATIONS.LIST><BILLALLOCATIONS.LIST></BILLALLOCATIONS.LIST><INTERESTCOLLECTION.LIST></INTERESTCOLLECTION.LIST><OLDAUDITENTRIES.LIST></OLDAUDITENTRIES.LIST><ACCOUNTAUDITENTRIES.LIST></ACCOUNTAUDITENTRIES.LIST><AUDITENTRIES.LIST></AUDITENTRIES.LIST><INPUTCRALLOCS.LIST></INPUTCRALLOCS.LIST><DUTYHEADDETAILS.LIST></DUTYHEADDETAILS.LIST><EXCISEDUTYHEADDETAILS.LIST></EXCISEDUTYHEADDETAILS.LIST><RATEDETAILS.LIST></RATEDETAILS.LIST><SUMMARYALLOCS.LIST></SUMMARYALLOCS.LIST><STPYMTDETAILS.LIST></STPYMTDETAILS.LIST><EXCISEPAYMENTALLOCATIONS.LIST></EXCISEPAYMENTALLOCATIONS.LIST><TAXBILLALLOCATIONS.LIST></TAXBILLALLOCATIONS.LIST><TAXOBJECTALLOCATIONS.LIST></TAXOBJECTALLOCATIONS.LIST><TDSEXPENSEALLOCATIONS.LIST></TDSEXPENSEALLOCATIONS.LIST><VATSTATUTORYDETAILS.LIST></VATSTATUTORYDETAILS.LIST><COSTTRACKALLOCATIONS.LIST></COSTTRACKALLOCATIONS.LIST><REFVOUCHERDETAILS.LIST></REFVOUCHERDETAILS.LIST><INVOICEWISEDETAILS.LIST></INVOICEWISEDETAILS.LIST><VATITCDETAILS.LIST></VATITCDETAILS.LIST><ADVANCETAXDETAILS.LIST></ADVANCETAXDETAILS.LIST></LEDGERENTRIES.LIST>'
data += '<LEDGERNAME>Freight Sales Gst</LEDGERNAME><GSTCLASS/><ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE><LEDGERFROMITEM>No</LEDGERFROMITEM><REMOVEZEROENTRIES>No</REMOVEZEROENTRIES><ISPARTYLEDGER>No</ISPARTYLEDGER><ISLASTDEEMEDPOSITIVE>Yes</ISLASTDEEMEDPOSITIVE><ISCAPVATTAXALTERED>No</ISCAPVATTAXALTERED><ISCAPVATNOTCLAIMED>No</ISCAPVATNOTCLAIMED>'
data += '<AMOUNT>-50.00</AMOUNT><VATEXPAMOUNT>-50.00</VATEXPAMOUNT><SERVICETAXDETAILS.LIST></SERVICETAXDETAILS.LIST><BANKALLOCATIONS.LIST></BANKALLOCATIONS.LIST><BILLALLOCATIONS.LIST></BILLALLOCATIONS.LIST><INTERESTCOLLECTION.LIST></INTERESTCOLLECTION.LIST><OLDAUDITENTRIES.LIST></OLDAUDITENTRIES.LIST><ACCOUNTAUDITENTRIES.LIST></ACCOUNTAUDITENTRIES.LIST><AUDITENTRIES.LIST></AUDITENTRIES.LIST><INPUTCRALLOCS.LIST></INPUTCRALLOCS.LIST><DUTYHEADDETAILS.LIST></DUTYHEADDETAILS.LIST><EXCISEDUTYHEADDETAILS.LIST></EXCISEDUTYHEADDETAILS.LIST><RATEDETAILS.LIST></RATEDETAILS.LIST><SUMMARYALLOCS.LIST></SUMMARYALLOCS.LIST><STPYMTDETAILS.LIST></STPYMTDETAILS.LIST><EXCISEPAYMENTALLOCATIONS.LIST></EXCISEPAYMENTALLOCATIONS.LIST><TAXBILLALLOCATIONS.LIST></TAXBILLALLOCATIONS.LIST><TAXOBJECTALLOCATIONS.LIST></TAXOBJECTALLOCATIONS.LIST><TDSEXPENSEALLOCATIONS.LIST></TDSEXPENSEALLOCATIONS.LIST><VATSTATUTORYDETAILS.LIST></VATSTATUTORYDETAILS.LIST><COSTTRACKALLOCATIONS.LIST></COSTTRACKALLOCATIONS.LIST><REFVOUCHERDETAILS.LIST></REFVOUCHERDETAILS.LIST><INVOICEWISEDETAILS.LIST></INVOICEWISEDETAILS.LIST><VATITCDETAILS.LIST></VATITCDETAILS.LIST><ADVANCETAXDETAILS.LIST></ADVANCETAXDETAILS.LIST></LEDGERENTRIES.LIST><PAYROLLMODEOFPAYMENT.LIST></PAYROLLMODEOFPAYMENT.LIST><ATTDRECORDS.LIST></ATTDRECORDS.LIST><GSTEWAYCONSIGNORADDRESS.LIST></GSTEWAYCONSIGNORADDRESS.LIST><GSTEWAYCONSIGNEEADDRESS.LIST></GSTEWAYCONSIGNEEADDRESS.LIST><TEMPGSTRATEDETAILS.LIST></TEMPGSTRATEDETAILS.LIST></VOUCHER></TALLYMESSAGE></REQUESTDATA></IMPORTDATA></BODY></ENVELOPE>'
# print(data)
req = requests.post(url=url, data=data)

# if req == 1 :
#     print('ok')
# else:
#     print('no')
