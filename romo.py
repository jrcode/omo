#!/bin/env python3
################################
#Name:rOmO
#Author: JR Hernandez
#Version: 0.1
################################

#imports
import requests
import argparse

#script description and program name
parser = argparse.ArgumentParser(description='Submit Reserved Spots, default spots are 3,7,13,20', prog='Reserved Open Mic Ordinaire - rOmO')

#id argument
parser.add_argument('-i', '--id', type=int, required=True, help= 'Input ID')

#url argument
parser.add_argument('-u', '--url', required=True, help='Input The Permalink')

#spots argument
parser.add_argument('-s', '--Spots', nargs=4, default=['3','7','13','20'], metavar=('spot1','spot2', 'spot3', 'spot4'), help='Input Reserved Spots')

#variable to hold arguments
args = parser.parse_args()

#counter used to for number in the emails inperson#@gmail.com
count = 0

#loop 
for i in args.Spots:
    #increase the counter by 1
    count = count + 1
    
    #variable to hold the permalink 
    url = args.url + "?task_id=" + str(args.id + int(i))

    #variable to hold information
    payload = {'signup_firstname' : 'Reserved For In', 'signup_lastname' : 'Person Sign-up', 'signup_email' : 'inperson' + str(count) + '@gmail.com', 'signup_twitter_handle':'','signup_facebook_page':'','dlssus_submitted': str(args.id),'Submit': 'Sign me up!'}

    #variable to hold post request
    r = requests.post(url ,data=payload)
