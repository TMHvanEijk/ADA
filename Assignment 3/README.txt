In the gateway_workflow folder in Assignment 3 a docker-compose.yml file can be found. 
From this folder one can build the containers in the cloud. 
In this folder a krakend folder is also found, which contains the krakend file for organizing the gateway API.

In Assignment 3 a workflows folder can be found. The YAML files for the relevant workflows are included here to be able to run in other virtual machines.

Finally a low resolution demo video is included in the Assignment 3 folder which shows the functionality. A higher resolution demo is available but could not be uploaded to github. It can be send to you if requested.

This assignment aims to focus on the core business process for marktplaats, which is the auctions. For this reason it contains the following functionality:
1. An auction can be created through the auction service.
2. An auction can be viewed through the auction service. Similar auctions will also be presented here by using a google workflow which gets these auctions from the search service. For now these similar auctions are mock ones, as no connection data storage in the cloud was implemented.
3. A bid can be placed through the auction service. This will envoke a google workflow as well, where it is checked whether the bid amount is sufficient by retrieving this information from the auction service. If this is the case a bid is places through the auction service and a conversation between the bidder and the seller is started through the message service. If the bid does not meet the requirements a message is returned which says so.
4. The message between the two parties can be viewed through the message service.
5. An auction can be deleted through the auction service.
6. A bid can be deleted through the auction service

Each of the through xxxxx service should be read as through the gatewayAPI which eaither connects to the service directly or to the service through a google workflow.