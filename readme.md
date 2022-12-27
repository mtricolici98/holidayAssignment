# Assignment

## Fork or download the current repository, and work on your own.

After completeng the assingment, send me the link to your github repository with the solution.

**You are already provided with all the necessary solutions for data storage**

## Topic

We are creating a console application for a small car rental company. The rental company only leases the car for one day. The car rental company wants to have the following functionality. 

* Register cars in the system
    *  Required fields are: Make, Model, VIN Number, Plate Number, Color, Year of production ***information is stored in a `dict`***
* Register customers in the system
    * Required fields are: First Name, Last Name, IDNP, Date of Birth (as string)
* Create a reservations for a car for a specific customer
    * Reservations are created using the `Plate Number` of the car, the user should also provide a Date, Month, and Year of the reservation 
* Check reservations for a car, using the `plate number`:
    * Should show all **upcoming** reservations for a car displaying all the reservation where the date is **higher** than a date input from the console. 
    * Should show all **current** reservations for a car, where the date equals the date input from a console.
    * Should show all **past** reservations for a car, where the date is lower than the date input from a console.
* Show reservations for all cars for the day input from console.

### Requirements

* Dates are tuples of (DAY, MONTH, YEAR)
* Implement everything that is necessary in the `data_access` package.
* Do not use python date/datetime libraries. Make an algorithm to compare the dates yourself.
* Separate your logic into functions as you see fit.
* Read the documentation from the `data` package, how you can access and modify the saved data.
* Improvise, add functionality if you feel like some is missing.
* All the functionality should start by starting `main.py` file. 




