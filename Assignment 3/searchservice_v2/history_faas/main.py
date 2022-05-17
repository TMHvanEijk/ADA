
def update_history(request):
    from flask import abort, json
    from google.cloud import bigquery

    client = bigquery.Client()

    table_id = "ada-search-service.searchhistory_db.search_history"

    request_json = request.get_json(silent=True)
    args = request.args


    if request_json and'search' in request_json:
        new_search = request_json['search']

        rows_to_insert = [{'search':new_search}]
        errors = client.insert_rows_json(table_id, rows_to_insert, row_ids=[None] * len(rows_to_insert))

        if errors != []:
            return abort(405)
        else:
            return json.dumps({'message': 'a search was added'}, sort_keys=False, indent=4), 200
    if args and 'search' in args:
        new_search = args['search']

        rows_to_insert = [{'search':new_search}]
        errors = client.insert_rows_json(table_id, rows_to_insert, row_ids=[None] * len(rows_to_insert))

        if errors != []:
            return abort(405)
        else:
            return json.dumps({'message': 'a search was added'}, sort_keys=False, indent=4), 200
    else:
        return json.dumps({'message': 'a search could not be added'}, sort_keys=False, indent=4), 200
