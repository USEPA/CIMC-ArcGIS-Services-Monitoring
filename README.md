# CIMC ArcGIS Services Monitor Script (SMS)

CIMC SMS is a services monitoring script that was originally designed for the Cleanups in My Community (CIMC) application.  The two main requirements for this script are Python that reads a CSV list of services required by the CIMC application and an SMTP mail server connection.  The software includes the capability to:

- Monitor services utilized by the application by reading the services listed in the CSV file
- Cycles through each data layer
- Queries the map service
- Tests that results are being returned
- Emails a SMTP distribution group if no response was received from the service

For more information, go to https://www.epa.gov/cleanups/cimc-web-map-service

## License
The script was developed by Jesse Adams for the US Environmental Protection Agency for Cleanups In My Community.  His contact information is below.
## Organization
The SMS is a python script that reads from a CSV file.
#### Files

- RestServiceList.csv – which contains the email distributions and the services verified by the script
- Python script – TestRestService_EPA.py – The python script that contains the logic for querying, testing, and emailing if issues existing with the REST services specified in the CSV file.  Ensure that the SMTP configuration is setup correctly so the script will email the specified user or users

```python
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

if __name__ == '__main__':
    # fromaddr = "adams.jesse@epa.gov"
    fromaddr = "<From email address>"
    fromaddrPass = "######"

    main()

```

## Contact

- Lisa Jenkins, US Environment Protection Agency, Jenkins.Lisa@epa.gov
- Jesse Adams, North Point Geographic Solutions (NPGS), adams.jesse@epa.gov

## EPA Disclaimer
The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use. EPA has relinquished control of the information and no longer has responsibility to protect the integrity, confidentiality, or availability of the information. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA. The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government.