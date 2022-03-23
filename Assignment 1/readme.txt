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
	-resources
		utility for the database inside of the docker container where for now the auction database is stored. Next this will be connected to the auctionservice
	-app.py
		This is used to create, fill, search the auction database through an API. From the GET, i.e. search, the http request is posted to the google cloud function.
	-Dockerfile
		defenition of the image to build
	-history_faas
		The function that is used by the google cloud to store the search history in bigquery upon a http request.