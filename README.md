## Laboratory work for network programming class
### Client Service Server
___ 
To start the project make sure you have the Dining Hall Server running and then run the  Client Service Server using the 
```docker-compose up``` command</br>

The basic idea of food ordering simulation is to have multiple clients ordering food from multiple restaurants. The goal is to
adopt the restaurant implementation to be able to integrate with some "third" party services such as Food Ordering service.

`Client service` represents component which simulates end clients of the system, which want just to order and pick up food from
restaurant.
`Client service` have to generate end users orders and send orders to `Food Ordering service`. `Client service` consists of
clients which will actually generates orders and represents abstraction of a real system client.

