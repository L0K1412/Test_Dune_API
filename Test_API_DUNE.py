from requests import get, post
import pandas as pd
import time

# input API Key
API_KEY = "LU3LdU4ChI1TnCpKsHpPlvqVIs5Agcb8"
HEADER = {"x-dune-api-key" : API_KEY}

# Simplifying URL generation
BASE_URL = "https://api.dune.com/api/v1/"

def make_api_url(module, action, ID):
    """
    We shall use this function to generate a URL to call the API.
    """

    url = BASE_URL + module + "/" + ID + "/" + action

    return url

# Wrapping API endpoints in functions

# execute query with no param or default params
def execute_query(query_id, engine="medium"):
    """
    Takes in the query ID and engine size.
    Specifying the engine size will change how quickly your query runs. 
    The default is "medium" which spends 10 credits, while "large" spends 20 credits.
    Calls the API to execute the query.
    Returns the execution ID of the instance which is executing the query.
    """

    url = make_api_url("query", "execute", query_id)
    params = {
        "performance": engine,
    }
    response = post(url, headers=HEADER, params=params)
    execution_id = response.json()['execution_id']

    return execution_id

# execute query with params
def execute_query_with_params(query_id, param_dict):
    """
    Takes in the query ID. And a dictionary containing parameter values.
    Calls the API to execute the query.
    Returns the execution ID of the instance which is executing the query.
    """

    url = make_api_url("query", "execute", query_id)
    response = post(url, headers=HEADER, json={"query_parameters" : param_dict})
    execution_id = response.json()['execution_id']

    return execution_id

def get_query_status(execution_id):
    """
    Takes in an execution ID.
    Fetches the status of query execution using the API
    Returns the status response object
    """

    url = make_api_url("execution", "status", execution_id)
    response = get(url, headers=HEADER)
    status = response.json()

    return status

def get_query_results(execution_id):
    """
    Takes in an execution ID.
    Fetches the results returned from the query using the API
    Returns the results response object
    """

    url = make_api_url("execution", "results", execution_id)
    response = get(url, headers=HEADER)

    return response

def cancel_query_execution(execution_id):
    """
    Takes in an execution ID.
    Cancels the ongoing execution of the query.
    Returns the response object.
    """

    url = make_api_url("execution", "cancel", execution_id)
    response = get(url, headers=HEADER)

    return response

def run_query():
    # Last transactions of address (Test query: 2619279)
    execution_id = execute_query("2619279","medium")
    # print(execution_id)

    response_status = get_query_status(execution_id)
    
    # Check state of query
    while response_status["state"] != "QUERY_STATE_COMPLETED":
        # wait 30 seconds then check again
        time.sleep(30)
        response_status = get_query_status(execution_id)

    response_result = get_query_results(execution_id)
    array_data = list(response_result.json()['result']['rows'])
    
    # sort order of columns
    new_array_data =[
        {'time': item['time'],
        'from': item['from'],
        'to': item['to'],
        'hash': item['tx_hash'],
        'symbol': item['symbol'],
        'amount': item['amount']}
        for item in array_data
    ]
    
    for item in new_array_data:
        print(item)
        
def run_query_with_params():
    # Last transactions of address (Test query: 2619279)
    # initialize list params
    parameters = {"last_txs" : "30", "wallet_address" : "0x412B7f53613Be5d29E112e5a23f8D52b1E77eeb6"}
    execution_id = execute_query_with_params("2619279", parameters)
    # print(execution_id)

    response_status = get_query_status(execution_id)
    
    # Check state of query
    while response_status["state"] != "QUERY_STATE_COMPLETED":
        # wait 30 seconds then check again
        time.sleep(30)
        response_status = get_query_status(execution_id)

    response_result = get_query_results(execution_id)
    array_data = list(response_result.json()['result']['rows'])
    
    # sort order of columns
    new_array_data =[
        {'time': item['time'],
        'from': item['from'],
        'to': item['to'],
        'hash': item['tx_hash'],
        'symbol': item['symbol'],
        'amount': item['amount']}
        for item in array_data
    ]
    
    for item in new_array_data:
        print(item)
        
# run query with default params
#run_query()

# run query with params
run_query_with_params()