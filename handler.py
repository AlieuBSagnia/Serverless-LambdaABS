
def hello(event, context):
    firstName = event['first']
    lastName = event['last']
    
    if firstName == "" or lastName == "":
        return 'Hello, you need to enter a first/last name'
    else:
        return f'Hello, {firstName} {lastName}!'
        #'statusCode': 200,

