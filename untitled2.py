# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 00:16:52 2021

@author: PREDATOR
"""

import sqlite3 
with sqlite3.connect("fooddb.db") as con: 
        
        curr = con.cursor()
        sql_cmd = """
                                
                                SELECT * FROM USERFOOD; 
                                """
                                
        curr.execute(sql_cmd,)
        A = []
        result = "</table><tr><th>User</th><th>Food</th></tr>"
        for row in curr.fetchall(): 
            result = result + "<tr><td>{}</td><td>{}</td></tr>".format(row[0],row[1])
        
        result = result + "</table>"
        print(result)
        
        