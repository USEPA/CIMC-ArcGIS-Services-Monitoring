#-------------------------------------------------------------------------------
# Name:        TestRestService
# Purpose:
#
# Author:      Jesse Adams
#
# Created:     02/08/2017
# Copyright:   US EPA
#-------------------------------------------------------------------------------

import csv
import urllib2
import json
import os

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def test_rest(baseURL):
    values = {
        'f' : 'json'}
    if baseURL.split("/")[-1:] != 'MapServer':
        values['where'] = '1=1'
        values['returnCountOnly'] = 'true'

    request = build_request(baseURL,values)
    response = urllib2.urlopen(request)
    data = json.load(response)

    if len(set(data.keys())&set(['count','layers'])) > 0:
        return True

def build_request(base_url,query_param_dict):
    if 'where' in query_param_dict.keys():
        query_str = '/query?'
    else:
        query_str = '/?'
    for param in query_param_dict.keys():
        query_str += '&{}={}'.format(param,query_param_dict[param])
    return base_url + query_str

def getURLs():

    csvData = []

    with open(os.path.join(os.path.dirname(__file__), 'RestServiceList.csv')) as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            csvData.append(row)

        return csvData

def sendEmails(toAddrList,subject,body):
    toaddr = toAddrList

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    part = MIMEBase('application', 'octet-stream')

    server = smtplib.SMTP('unixmail.rtpnc.epa.gov')

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def buildMessageString(badServices):
    messageString = 'The following rest services could not be reached:\n\n'

    for service in badServices:
        messageString += 'Rest Service: {0}\n'.format(service['NAME'])
        messageString += 'Rest Service URL: {0}\n'.format(service['URL'])
        messageString += 'Contact Organization: {0}\n'.format(service['CONTACT'])
        messageString += 'Contact Information: {0}\n\n'.format(service['EMAIL_URL'])

    return messageString

def main():

    badServices = []
    messageString = ''

    serviceInfo = getURLs()

    # toAddrList = [i['EMAIL'] for i in serviceInfo if len(i['EMAIL']) >0]

    for service in serviceInfo:
        if not test_rest(service['URL']):
            badServices.append(service)

    if badServices:
        messageString = buildMessageString(badServices)

        # for email in toAddrList:
        # sendEmails('CIMC_Services_Monitors@epa.gov','Rest Service Error', messageString)
        sendEmails('<Enter the email address you would like to notify>','Rest Service Error', messageString)

if __name__ == '__main__':
    # fromaddr = "adams.jesse@epa.gov"
    fromaddr = "<From email address>"
    fromaddrPass = "######"

    main()
