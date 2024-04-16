import json
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="sbom",
    password=" ",
    database="sbom_data"
)

with open(f'nvdcpematch-1.0.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
length = len(data['matches'])
count = 1
matches_list = data.get("matches", [])
for match in matches_list:
    
    cpe23Uri = match.get("cpe23Uri")
    versionStartIncluding = match.get("versionStartIncluding")
    versionStartExcluding = match.get("versionStartExcluding")
    versionEndIncluding = match.get("versionEndIncluding")
    versionEndExcluding = match.get("versionEndExcluding")
    cpe_name_list = match.get("cpe_name", [])

    output_str = '{' + '"cpe23Uri": ' + '"' + str(cpe23Uri) + '"'
    if versionStartIncluding is not None:
        output_str += ", " + '"versionStartIncluding": ' + '"' + str(versionStartIncluding) + '"'
    if versionStartExcluding is not None:
        output_str += ", " + '"versionStartExcluding": ' + '"' + str(versionStartExcluding) + '"'
    if versionEndIncluding is not None:
        output_str += ", " + '"versionEndIncluding": ' + '"' + str(versionEndIncluding) + '"'
    if versionEndExcluding is not None:
        output_str += ", " + '"versionEndExcluding": ' + '"' + str(versionEndExcluding) + '"'
    output_str += "}"

    cpe_name_uris = [item.get("cpe23Uri") for item in cpe_name_list]
    
    cursor = connection.cursor()
    insert_query = "INSERT INTO cpe_main_data (cpe_main, cpe_name) VALUES (%s, %s)"
    data_to_insert = (output_str, json.dumps(cpe_name_uris))
    cursor.execute(insert_query, data_to_insert)
    connection.commit()
    cursor.close()
    print(f'{count}/{length}')
    count += 1

 
