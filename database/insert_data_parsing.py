import json
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="sbom",
    password="",
    database="sbom_data"
)
def insert(filename):
    with open(f'nvdcve-1.1-{filename}.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    cve_data_numberOfCVEs = data['CVE_data_numberOfCVEs']
    cve_data_numberOfCVEs = int(cve_data_numberOfCVEs)

    for i in range(cve_data_numberOfCVEs):
        cve_data_meta_id = data['CVE_Items'][i]['cve']['CVE_data_meta']['ID']
        CVE_Items = json.dumps(data['CVE_Items'][i], ensure_ascii=False, indent=3)

        cursor = connection.cursor()
        insert_query = "INSERT INTO CVE_DATA (CVE_ID, DATA) VALUES (%s, %s)"
        data_to_insert = (cve_data_meta_id, CVE_Items)
        cursor.execute(insert_query, data_to_insert)
        connection.commit()
        cursor.close()
        print(f'데이터 삽입 중 - ({i+1}/{cve_data_numberOfCVEs})')
    connection.close()
    print("데이터 삽입 완료")
