'''
Created on 27-May-2017

@author: venkat
'''

SLEEP_TIME = 1

data={
    'invalid_name' : '1234fdesr',
    'valid_name' : 'rain',
    'address' : 'shop-16',
    'invalid_city': '1245dsfer',
    'valid_city' : 'nandyal',
    'invalid_phone_number_with_alphabets' : 'abcdert1234',
    'invalid_phone_number_length' : '12345678',
    'valid_phone_number' : '9620074979'
 }


errors= {
'name_error':'name should contain only alphabets',
'city_error' :'city should contain only alphabets',
'phone_number_error':'Phone number should contain only 10 numbers'
}