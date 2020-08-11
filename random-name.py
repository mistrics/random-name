import json

def random_name(event, context): 
    return {
        'statusCode': 200,
        'body': json.dumps({"name":"Random"})
    }    

