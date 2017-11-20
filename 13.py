import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

methods = proxy.system.listMethods()
print(methods)

evil = proxy.phone("Bert")

print(evil)