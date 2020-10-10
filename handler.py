
def hello(event, context):
    # TODO implement
    firstName = event['first']
    
    lastName = event['last']
    
    return 'Hello, ' + firstName + ' ' + lastName + '!'
        #'statusCode': 200,
