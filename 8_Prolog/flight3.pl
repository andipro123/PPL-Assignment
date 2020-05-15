:- initialisation(main)
main :- write('\nWelcome to flight management system!\n')

/*Facts of airports*/

airport(toronto, 50, 60).
airport(london, 75, 80).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).

/*Facts of flights*/

flight(toronto,aircanada,london,500,360).
flight(toronto,united,london,650,420).
flight(toronto,aircanada,madrid,900,480).
flight(toronto,united,madrid,950,540).
flight(toronto,iberia,madrid,800,480).
flight(madrid,aircanada,barcelona,100,60).
flight(madrid,iberia,barcelona,120,650).
flight(barcelona,iberia,london,220,240).
flight(madrid,iberia,valencia,40,50).
flight(barcelona,iberia,valencia,110,75).
flight(madrid,iberia,malaga,50,60).
flight(valencia,iberia,malaga,80,120).
flight(toulouse,united,paris,35,120).

/*Queries as per the questions*/

/*a. Is there a flight from Toronto to Madrid? checkFlight(toronto, madrid). */

checkFlight(A,B) :- flight(A, Airline, B, Price, Duration) ;  flight(B, Airline, A, Price, Duration).

/*b. A flight from city A to city B with airline C is cheap if its price is less than $400. */

isCheap(A, B, C) :- (flight(A, C, B, Price, Duration) ;  flight(B, C, A, Price, Duration)) , (Price < 400).

/*c. Is it possible to go from Toronto to Paris in two flights? */

hop(A,B) :- checkFlight(A,C), checkFlight(C,B).

/* A flight from city A to city B with airline C is preferred if it’s cheap (see (b)) or it’s with Air Canada.*/

preferred(A,B,C) :- isCheap(A,B,C) ; C = aircanada.

/* If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada */

un_ac(A,B) :-  (flight(A, united, B, Price, Duration) ;  flight(B, united, A, Price, Duration)) ->  
    (flight(A, aircanada, B, Price2, Duration2) ;  flight(B, aircanada, A, Price2, Duration2)).

/*function to print all files in database*/

printFlights(City1, City2) :- (flight(City1, Airline, City2, Price, Duration);
	flight(City1, Airline, City2, Price, Duration)),
	(printFlight(City1, Airline, City2, Price, Duration),
	printFlight(City2, Airline, City1, Price, Duration)).

/*function to print a flight from A to B*/
printFlight(City1, Airline, City2, Price, Duration):-
	write('Flight Name: '),
   	write(Airline),
	write('\tDeparture From: '),
   	write(City1),
   	write('\tArrival To: '),
   	write(City2),
   	write('\tPrice: '),
   	write(Price),
   	write('\tDuration: '),
   	write(Duration),
    write('\n').