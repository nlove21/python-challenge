import pandas as pd 


df=pd.read_csv("employee_data1.csv")

ed=pd.read_csv("employee_data2.csv")

frame = [df,ed]

employee_table= pd.concat(frame) 

list=employee_table['Name'].str.split(' ',expand=True)       

employee_table['First Name']=list[0] 

employee_table['Last Name']=list[1] 

del employee_table['Name'] 

employee_table['DOB'] = pd.to_datetime(employee_table.DOB) 

employee_table['DOB'] = employee_table['DOB'].dt.strftime("%m/%d/%Y")  

employee_table['SSN']= "***-**-"+employee_table['SSN'].str[7:11]

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

state_abbrev = [us_state_abbrev[i] for i in employee_table['State']]

state_abbrev = pd.Series(state_abbrev) 

employee_table['State'] = state_abbrev 

neworder= ['Emp ID','First Name','Last Name','DOB','SSN','State']

employee_table = employee_table.reindex(columns=neworder)  

employee_table.to_csv("PyBoss.csv",index=False, header=True) 