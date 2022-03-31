# Movie Theater Seating Challenge
Language : python


## Program Description
This code reads the input file from commandline, reads the reservation request ans assigns available seats to the user requests

The algorithm implemented tries to minimize buffer space to accomadate maximum possible reservation requests.

To ensure Customer satisfation, seats in a given reservation are assigned in the same row
To ensure public safety, a buffer of three seats and one row around each reservation is enforced



## Assumptions 
* Priority of reservations is the same as their order in the input file
* All seats have the same value and customers are not concerned about what seat they are allocated
* Each reservation will have 0 < seats <= 20
* Seats once assigned for a reservation cannot be changed
* If a reservation cannot be accomadated, reservation output will be "cannot fulfill reservation"


## Steps to build and test the project
How to run project:
`./main.py -i \<inputfile> `

Run in Testing Mode
`./main.py -t`

How to run tests:
`pytest`


## Things to work on in the future
* If we can change the seats on the fly use backtracing to reorganize the seats. Similar to the N-Queens Problem.
* If there is preference for what seat a customer would like, allow the user to input it. Center Seats are normally more valuable in a movie theaters.
* Allow for reservations to be broken up for more optimized sitting