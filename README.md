## Email-Watch

Email-Watch assists defenders or curious researchers in identifying registered domains belonging to a specified email address.

Domains having the suspect email address in their WHOIS records are found courtesy of the WHOISXMLAPI. 

## Setup 

'''
Work in progress
'''

In addition to domains, Email-Watch will also attempt to find:

* DNS Records
* Certificate info
* Determine whether a selected domain is identified as malicious
* ...

Future versions of Email-Watch will include the ability to have all or some of the found domains ingested by ElasticSearch for 
records and research. 

## :clipboard: TODO:

* :white_check_mark:  Get certificate info (if applicable)
* :white_check_mark: Obtain Passive DNS information (using RiskIQ API)
* Screenshot subject domain (?)
* Obtain domain reputation
* Ingest emaill address and returned domains to ElasticSearch for further research
