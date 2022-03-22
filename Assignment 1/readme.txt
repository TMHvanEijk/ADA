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
