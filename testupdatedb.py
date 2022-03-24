# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:16:01 2021

@author: PREDATOR
"""

import sqlite3 


with sqlite3.connect("fooddb.db") as con: 
    
    curr = con.cursor()
    sql_cmd = """
    
    SELECT * FROM FOOD; 
    """
    
    food_nut_detail = []
    for row in curr.execute(sql_cmd):
        food_nut_detail.append(row)
    print(food_nut_detail)
    
# with sqlite3.connect("fooddb.db") as con: 
#     curr = con.cursor()

#     sql_cmd = """
            
#             SELECT * FROM USERFOOD WHERE user_id == ? and date == ?;
            
#             """

#     date_input = ""
#     user_id = ""
#     food = curr.execute(sql_cmd,(user_id,date_input))

#     food_name_portion = []
#     sum_protein = 0 
#     sum_carbo = 0 
#     sum_fat = 0 