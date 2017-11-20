import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

evil = proxy.phone("Bert")

print(evil)