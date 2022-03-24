# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 23:56:26 2021

@author: PREDATOR
"""

import json
from flask import Flask,render_template,jsonify,send_file 
import sqlite3 

app = Flask(__name__)

@app.route("/")
def hello():
    return "<marquee style='background-color:black;color:yellow;'>Test</marquee>"

@app.route("/download2")
def from_db(): 
    with sqlite3.connect("fooddb.db") as con: 
            
            curr = con.cursor()
            sql_cmd = """
                                    
                                    SELECT * FROM USERFOOD; 
                                    """
                                    
            curr.execute(sql_cmd,)
            A = []
            x = "test"
            y = "name"
            result = """</table style='width:100%'>
            <tr>
                  <th>Person 1</th>
                  <th>Person 2</th>
             
            </tr>
            <tr>
                <td>{}</td>
                <td>{}</td>
            </tr>
            </table>
            """.format(x,y)
            # for row in curr.fetchall(): 
            #     result = result + "<tr><td>{}</td><td>{}</td></tr>\n".format(row[0],row[1])
            
            # result = result + "</table>"
            


    
    return result


if __name__ == '__main__': 
    app.run(debug=True,port=5000)
    
    
    
    
