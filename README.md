

For your homework this week, you'll be creating a wsgi application of your own.

You'll create an online calculator that can perform several operations

You'll need to support:

    Addition
    Subtraction
    Multiplication
    Division

Your users should be able to send appropriate requests and get back proper responses:

http://localhost:8080/multiply/3/5  => 15
http://localhost:8080/add/23/42     => 65
http://localhost:8080/divide/6/0    => HTTP "400 Bad Request"

