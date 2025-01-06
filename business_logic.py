import requests

def make_request(query: str, history: list) -> str:
    server_endpoint = 'https://crustbot-4d523fa27077.herokuapp.com/query'

    if len(history) > 5:
        history = history[-5:]

    payload = {
        "query": query,
        "history": history
    }


    try:
        response = requests.post(url=server_endpoint,
                                headers={'Content-Type': 'application/json'},
                                json=payload)
        
        response_json = response.json()
        return response_json
    except:
        return {"status": "failure", "error": "Some Error Occured. Please wait for a bit then try again!"}