import json
from sqlalchemy import create_engine,text
from sqlalchemy.exc import OperationalError, ProgrammingError, SQLAlchemyError
import pandas as pd
import base64
import re
import tkinter as tk
from tkinter import simpledialog
import time
 
 
json_temp = {
        "question" : "",
        "card_id" : "",
        "title" : "",
        "board_id" : "",
        "enable_change" : False
    }
 
with open("config.json","r") as file:
    config = json.load(file)
 
def get_conn(port:int):
    try:
        postgres_engine = create_engine(
            'postgresql://' + base64.b64decode('cG9zdGdyZXM=').decode("ascii") + ':' + base64.b64decode(
                'd2hpenVzZXI=').decode("ascii") + '@' + 'localhost' + ':' + str(port) + '/' + 'sda')
        return postgres_engine
    except OperationalError as e:
        print("Operational Error : Could not connect to the database.")
        print(f"Error details : {e}")
    except SQLAlchemyError as e:
        print("SqlAlChemy error occured.")
        print(f"Error details : {e}")
    except Exception as e:
        print("An unexpected error occured.")
        print(f"Error details : {e}")
 
def update_config():
    with open("config.json",'w') as f:
        json.dump(config,f,indent=4)
 
 
def alter_kbq_data():
    try:
        dicts_list = []
        root=tk.Tk()
        root.withdraw()
        # port = simpledialog.askstring("Input","Enter Your Port Number : ")
        # report_name = simpledialog.askstring("Input","Enter Report Name : ")
        # whiz_board_id = simpledialog.askstring("Input","Enter Pinboard Id Number : ")
        port = 20903
        report_names = ['ONC KBQ Report OS']
        whiz_board_ids = ['8945','7720']
        conn= get_conn(port)
        for report in report_names:
            for board_id in whiz_board_ids:
                cards_sql_query = f"""select distinct wc.id, wc.title
                                    from whiz_cards wc  
                                    left join whiz_boards wb on wc.whiz_board_id  = wb.id where whiz_board_id in
                                    (select distinct whiz_board_id from whiz_board_links wbl where link_owner_id = 49 and owner = true)
                                    and whiz_board_id = '{board_id}'"""
                print(f"Executing the Whiz Cards Query for board_id:{board_id}")
                cards_df = pd.read_sql_query(cards_sql_query, conn)
                if cards_df.empty:
                    print(f"Whiz Cards Query returned 0 Records for the given board id : {board_id}: Aborting the Next steps")
                    return 0
                for index,row in cards_df.iterrows():
                    for conf_item in config:
                        if row['title'] == conf_item.get('title') and conf_item.get('board_id') == board_id:
                            conf_item['card_id'] = str(row['id'])
                            conf_item['enable_change'] = True
 
                print("Updating the Config Json With new Pincard Id")
                update_config()
                time.sleep(2)
 
                reg_sql_query = f"select action from registries where name = '{report}'"
                print(f"Executing the Registries Query for Report:{report}")
                reg_df = pd.read_sql_query(reg_sql_query, conn)
                if reg_df.empty:
                    print(f"Registries Query returned 0 Records for the given Report Name : {report}: Aborting the Next steps")
                    return 0
                reg_res = reg_df['action'].to_json()
                res = json.loads(reg_res)
                questions = []
                for section in res['0']['attributes']['sections']:
                    questions.append(section['data'])
                conf_qtns = config
                enbl_qtns = {i.get("question"):i.get("card_id") for i in conf_qtns if i.get("enable_change")}
                for section in questions:
                    for j in section:
                        if j['name']['en'] in list(enbl_qtns.keys()):
                            print("Question >",j['name']['en'])
                            url = j.get('url')
                            new_card_id = enbl_qtns.get(j['name']['en'])
                            updated_url = re.sub(r"(dialog:card/)\d+",lambda match: match.group(1)+new_card_id,url)
                            j['url']= updated_url
                action_res = res.get('0')
                result = json.dumps(action_res)
                print("Executing the Update Query for Registries table")
                update_query = f"Update registries SET action = '{result}'::json where name = '{report}'"
                with conn.connect() as con:
                    con.execute(text(update_query))
                    con.commit()
                for i in config:
                    if i.get("enable_change"):
                        i['enable_change'] = False
                update_config()
                time.sleep(2)
        return {"Success" : "KBQ PinCard Updated Successfully"}
    except ProgrammingError as e:
        print("Programming error: There may be an issue with your SQL query or schema.")
        print(f"Error details : {e}")
    except Exception as e:
        print("An unexpected error occured.")
        print(f"Error details : {e}")
 
if __name__ == "__main__":
    alter_kbq_data()
 
