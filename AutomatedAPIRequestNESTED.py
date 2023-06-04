# -*- coding: utf-8 -*-
"""
Created on Wed May 31 10:24:52 2023

@author: hakany
"""


import requests
import json
import sys

# Open a file to redirect the output
with open('ReportOutput.txt', 'w') as file:
    # Save the current sys.stdout for later use
    original_stdout = sys.stdout
    # Redirect the console output to the file
    sys.stdout = file
    try:
        # Your code here
        file_path = "input.txt"  # Replace with your file path
    
        # Read the file
        with open(file_path, "r") as file:
            lines = file.readlines()
    
        # Process the lines and store them as an array
        data_array = []
        for line in lines:
            # Remove newline characters and any leading/trailing whitespace
            cleaned_line = line.strip()
            # Append the cleaned line to the data array
            data_array.append(cleaned_line)
    
    
    
        # Get the length of the data
        data_length = len(data_array)
    
    
        # api-endpoint
        URL = "URLtoGetToken"
    
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {
        "grant_type":"password",
        "scope":"",
        "user_id":"",
        "password":"",
        }
          
        # sending get request and saving the response as response object
        r = requests.post(URL,json=PARAMS)
    
    
        x = r.content
        y = json.loads(x)
        Bearers = y["access_token"]
    
        #print(y["access_token"])
        countA = 0
    
        #Request for loop
        for index in range(data_length):
            
    
            SecondURL = "SecondURLtoMainlyUseWithToken"
            
            userID = data_array[index]
            UserAdditionParam = {
              "UserId":userID,
            }
            
            
            
            hed = {'Authorization': 'Bearer ' + Bearers}
            d = requests.post(SecondURL, json=UserAdditionParam, headers=hed)
            
            responseofServ= d.status_code
            xb = d.content
            print(responseofServ)
            if responseofServ == 200:
               print("User Addition Successfully Done for" + data_array[index])
               print(xb)
               countA = countA + 1
    
            else:
               print("User Addition failed for " + data_array[index]) 
               print(xb)
        #Printing succesfull request count       
        print(countA)
       
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Stopping execution.")
    # Restore the original sys.stdout
    sys.stdout = original_stdout

    
           
           
           


