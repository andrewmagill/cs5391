* **main requirements**
    * **create an account**
        * input
            * unordered
                * firstname (required)
                * middle name (optional)
                * last name (required)
                * mailing address (required)
                * email address (required)
                * default credit card (required?)
                    * credit card type (required)
                    * credit card number (required)
                    * that number on back of the credit card (required)
                    * expiration date (required)
                * username (required)
                * password (required)
            * action
                * user must submit form when complete
        * result
            * account is created
    * **user profile page?**
        * see mileage?
        * see past purchases?
        * change password, etc.?
        * ...
    * **login**
        * input
            * unordered
                * username (required)
                * password (required)
            * action
                * user must submit form when complete
        * result
            * user is authenticated and logged in
        * constraints
            * user must have an account
        * exceptions
            * unknown username
            * bad password
    * **book a flight**
        * search for flight
            * input
                * unordered
                    * departing airport (required)
                    * departure date (required)
                    * destination airport (required)
                    * return date (required)
                    * number of passengers (required)
                * action
                    * user must submit form when complete
            * result
                * list of available flights given input parameters
                    * departings flights with overall cheapest cost
                        * cost of departing flight + cost of cheapest returning flight
                    * ~~*returning flights?*~~
            * constraints
                * *user must be logged in?*
            * exceptions
                * no available flights matching input parameters
            * misc
                * user may order flights
                    * by price
                    * by airline
        * select flights
            * ordered actions
                * select departing flight
                    * constraints
                        * *user must be logged in?*
                        * user must have searched for flights
                        * flights must be available
                * select returning flight
                    * constraints
                        * *user must be logged in?*
                        * user have selected departing flight
                * review and configm
                    * flight info and total cost displayed
                        * total cost = price of flight + taxes and fees
                            * price of flight = selected departure + return
                            * taxes and fees = 15% of price of flight
                    * user confirms or cancels booking
                        * if configm, directed to book flight page (or homepage)
                            * *asked to book hotel?*
                        * if cancel, return to flight search
                            * asked to verify cancel flight
        * book flight
            * constraints
                * *user must be logged in?*
                * user must have selected departing and returning flights
            * inputs
                * unordered
                    * first name (required)
                    * last name (required)
                    * middle name (optional)
                    * credit card type (required)
                    * credit card number (required)
                    * that number on back of the credit card (required)
                    * expiration date (required)
                * action
                    * user must submit form when complete
    * **book a hotel**
        * search for hotel
            * input
                * unordered
                    * city (required)
                    * check in date (required)
                    * check out date (required)
                    * number of rooms (required)
                    * number of guests (required)
                * action
                    * user must submit form when complete
            * result
                * list of available hotel rooms
            * constraints
                * *user must be logged in?*
            * exceptions
                * *no hotels available?*
            * misc
                * user may order flights
                    * by price
                    * by name
                    * by stars
        * select hotel
            * ordered actions
                * select hotel
                    * constraints
                        * *user must be logged in?*
                        * user must have searched hotels
                        * hotels must be available
                * review and configm
                    * hotel info and total cost displayed
                        * total price = price of hotel + taxes and fees - discount
                            * price of flight = selected departure + return
                            * discount = 20% of the price of the hotel
                                * **only if booking with flight**
                            * taxes and fees = 15% of price of flight
                    * user confirms or cancels booking
                        * if configm, directed to book hotel page
                        * if cancel, return to hotel search (or homepage)
                            * asked to verify cancel flight
        * book flight
            * constraints
                * *user must be logged in?*
                * user must have selected departing and returning flights
            * inputs
                * credit card payment
                    * unordered
                        * first name (required)
                        * last name (required)
                        * middle name (optional)
                        * credit card type (required)
                        * credit card number (required)
                        * that number on back of the credit card (required)
                        * expiration date (required)
                * pay with accumulated mileage (redeem mileage)
                    * constraints
                        * user must be logged in
                        * user must have sufficient miles
                            * 25,000 miles for domestic flight
                            * 50,000 miles for international
                    * action
                        * miles are subtracted from user's accumulated total
                * action
                    * user must submit form when complete
                    * user profile credited with flight mileage
                        * constraints
                            * user must be logged in
    * **book both a flight and a hotel**
        * see book a flight
        * pre tax discount of 20% applies
    * **check flight status**
        * input
            * unordered
                * flight number (required)
                * airline name (required)
                * departure date (required)
            * action
                * user must submit form when complete
        * result
            * flight status displayed
                * in flight
                * arrived
                * delayed
        * exceptions
            * *flight not found?*
    * **accumulate mileage**
        * see book flight
    * **redeem mileage**
        * see book a flight
    * **find deals**
        * input
            * unordered
                * departing airport (required)
                * departure date (required)
                * destination airport (required)
                * return date (required)
                * price range
            * action
                * user must submit form when complete
        * result
            * list of available *deals* given input parameters
        * exceptions
            * no available *deals* matching input parameters
        * misc
            * deals ordered by price
        * select and book
            * similar to booking flight
    * **provide feedback**
        * input
            * unordered
                * comments (optional)
                * rating 1-10 (optional)
        * action
            * user must submit form
