#Use this script to manually push a file to ELastic Search from any of EC2 instance or local machine that has connectivity to ElasticSearch
################################################
#  Install the dependenices if not installed already 
# pip install boto3 
# pip install requests
# pip install requests_aws4auth
# Modify the host endpoint
################################################
# import boto3
# import re
# import requests
# from requests_aws4auth import AWS4Auth
# import gzip
# import json
# region = 'us-east-1'
# service = 'es'
# credentials = boto3.Session().get_credentials()
# awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
# # Modify the host value here 
# host = 'https://search-public-tpzog6qiuogzhg3sjz52odvr5u.us-east-1.es.amazonaws.com'
# # Modify index value if required
# index = 'lambda-s3-index'
# # Modify type if required
# type = 'lambda-type'
# url = host + '/' + index + '/' + type
# headers = { "Content-Type": "application/json" }
# data = []
#version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status
import gzip 
with gzip.open('vpc.log.gz','rt') as f:
    lineCount=0
    for line in f:
        lineCount += 1
        if lineCount > 1:
            version = line.split(' ')[0]
            accountNumber = line.split(' ')[1]
            interfaceId = line.split(' ')[2]
            sourceAddress = line.split(' ')[3]
            destinationAddress = line.split(' ')[4]
            sourcePort = line.split(' ')[5]
            destinationPort = line.split(' ')[6]
            protocol = line.split(' ')[7]
            packets = line.split(' ')[8]
            totalBytes = line.split(' ')[9]
            startTime = line.split(' ')[10]
            endTime = line.split(' ')[11]
            action = line.split(' ')[12]
            logStatus = line.split(' ')[13]
            document = { "version": version, "accountNumber": accountNumber, "interfaceId":interfaceId, "sourceAddress": sourceAddress,"destinationAddress": destinationAddress, "sourcePort": sourcePort, "destinationPort": destinationPort, "protocol":protocol, "packets":packets, "totalBytes": totalBytes, "startTime": startTime, "endTime":endTime, "action":action, "logStatus": logStatus }
            print document
            

    
