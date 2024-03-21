import string
import random
import numpy as np
import pandas as pd

# LAB-107, LAB-108
def fetch_epa(key):  
    '''
    Imports EPA data from adacert github and creates a dictionary with three keys:
        state: a list of the states
        county: a list of the counties
        aqi: a list of the aqi
    
    Returns the values at a given key.
    '''
    epa = pd.read_csv('https://raw.githubusercontent.com/adacert/EPA/main/c2_epa_air_quality.csv')
    state = epa['state_name'].to_list()
    county = epa['county_name'].to_list()
    aqi = epa['aqi'].to_list()
    epa_dict = dict(state = state,
                    county = county,
                    aqi = aqi)
    
    return epa_dict[key]


# LAB-099, LAB-100
def id_gen(n_chars_id, n_samples):  
    '''
    Return a list of `n_samples` elements where each element is a string 
    of len(`n_chars_id`) random lowercase characters and digits. 
    '''
    ids = []
    seed = 0
    for i in range(n_samples):
        random.seed(seed)
        id = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=n_chars_id))
        ids.append(id)
        seed+=1
    return ids


# LAB-099, LAB-100
def lists_gen(n_chars_id, n_pool, n_feedback_ids, n_verified_ids):  
    '''
    Return two lists: `verified_ids` and `feedback_ids`
    '''
    seed = 0
    pool = id_gen(n_chars_id, n_pool) 
    verified_ids = random.sample(pool, k=n_verified_ids)
    feedback_ids = random.sample(pool, k=n_feedback_ids)
    return verified_ids, feedback_ids


# LAB-099, LAB-100
def sales_data_generator(n_customers, seed):
    '''
    Returns a list of sales prices for n customers.
    Each customer has 0-6 purchases in their list.
    '''
    random.seed(seed)
    sales = []      
    for customer in range(n_customers):
        customer_sales = []
        n_sales = random.randint(0, 6)  # Random 0-6 number of sales for each cust.
        for sale in range(n_sales):     # Each sale price random from a lognormal dist.
            customer_sales.append(round(random.lognormvariate(2.5, 1.5), 2))
        sales.append(customer_sales)
    
    return sales
