- accountservice
the accountservice is there to create, view, and delete accounts; update account settings; update, and get login credentials
	- daos
		contains the data access objects for account, settings, and login.
	- openapi
		contains a yaml file for the openapi with seven microservice operations (create, get, put and delete) for both auction and bid
			- create, get, delete for account
			- put for settings
			- put, (2x) get for login
	- resources
		contains three python files that define the microservice operations
	- app.py
		python file that sets up the openapi when excecuted
	- db.py
		python file that reads or creates a database used in the microservice 
	- dockerfile
		definition of the image to build 		

- auctionservice
the auctionservice is there to create, view, delete and, update auctions and bids
	- daos
		contains the data access objects for auction and bid with the status data access objects for both 
	- openapi
		contains a yaml file for the openapi with eight microservice operations (create, get, put and delete) for both auction and bid
	- resources
		contains four python files that define the microservice operations
	- app.py
		python file that sets up the openapi when excecuted
	- db.py
		python file that reads or creates a database used in the microservice 
	- dockerfile
		definition of the image to build 		

- messageserviceopenapi
the messageserviceopenapi is there to create, view, delete and, update message
	-doas
		contains the data access objects for message with the status data access objects=
	- openapi
		contains a yaml file for the openapi with four microservice operations (create, get, put and delete) for message
	- resources 
		contains four python files that define the microservice operations
	- app.py
		python file that sets up the openapi when excecuted
	- db.py
		python file that reads or creates a database used in the microservice 
	- dockerfile
		definition of the image to build 
		
- searchservice
the search service is here to be able to search the auctions and store the search history
	-app.py
		This is to GET, i.e. search, in the auction bigquery. From here the search is posted to the google cloud function to trigger the http, which in turn stores the search in the dearch_history.
	-Dockerfile
		defenition of the image to build
	-history_faas
		The function that is used by the google cloud to store the search history in bigquery upon a http request.
	-CREDENTIALS
		This file is missing from the github as we don't like to share credentials. It is however used to connect to the bigquery.