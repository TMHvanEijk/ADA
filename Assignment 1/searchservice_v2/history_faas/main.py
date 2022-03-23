
def update_history(request):
    from flask import abort
    from google.cloud import bigquery

    table_id = "ada-search-service.searchhistory_db.search_history"

    if request['search']:
        new_search = request['search']

        row_to_insert = {'search':search}
        errors = client.insert_rows_json(table_id, rows_to_insert, row_ids=[None] * len(rows_to_insert))

        if errors != []:
            return abort(405)
        else:
            return json.dumps({'message': 'a search was added'}, sort_keys=False, indent=4), 200

    else:
        return json.dumps({'message': 'a search could not be added'}, sort_keys=False, indent=4), 400
