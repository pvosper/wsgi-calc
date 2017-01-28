#!/usr/bin/env python

"""
For your homework this week, you'll be creating a wsgi application of your own.

You'll create an online calculator that can perform several operations

You'll need to support:

    Addition
    Subtraction
    Multiplication
    Division

Your users should be able to send appropriate requests and get back proper
    responses:

http://localhost:8080/multiply/3/5  => 15
http://localhost:8080/add/23/42     => 65
http://localhost:8080/divide/6/0    => HTTP "400 Bad Request"


christy [5:16 PM]
If you don't want to use regex, try something like this
`args = path.strip("/").split("/")`

"""

html_text = """<html>
<head>
<title>WSGI Calulator (Session 03 Homework)</title>
</head>
<body>
<p>Path Info: {print_path_info} Entries: {print_no_entries}</p>
<p>Operation: {print_operation} First Operand: {print_operand_1}
Second Operand: {print_operand_2}</p>
<h1>Result: {print_result}</h3>
<hr>
<h3>Examples</h3>
<p><a href="http://localhost:8080/multiply/3/5">multiply/3/5</a></p>
<p><a href="http://localhost:8080/add/23/42">add/23/42</a></p>
<p><a href="http://localhost:8080/divide/6/0">divide/6/0</a></p>
</body>
</html>"""


def application(environ, start_response):
    headers = [("Content-type", "text/html")]
    try:
        path_info = environ.get('PATH_INFO', None)
        if path_info is None:
            raise NameError
        args = resolve_path(path_info)
        if args[0].strip() == "multiply":
            result = int(args[1]) * int(args[2])
        elif args[0].strip() == "divide":
            result = int(args[1]) / int(args[2])
        elif args[0].strip() == "add":
            result = int(args[1]) + int(args[2])
        elif args[0].strip() == "subtract":
            result = int(args[1]) - int(args[2])
        else:
            result = "failer"
        body = html_text.format(
            print_path_info=path_info,
            print_no_entries=len(args),
            print_operation=args[0],
            print_operand_1=args[1],
            print_operand_2=args[2],
            print_result=result
        )
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body.encode('utf8')]


def resolve_path(path):
    args = path.strip("/").split("/")
    return args


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
