from fastapi import FastAPI
from pydantic import BaseModel
import requests
from moneyone_api import moneyone_headers,moneyone_endpoints
from firebase import customers_collection


app=FastAPI()


vua = "1999999999@onemoney"
accountID = "NAD1234"


class ConsentRequest(BaseModel):
    mobile:str
    consentTypeID:str


@app.get('/')
def index():
    return {"message":'Hello'}


# def get_customers_collection():
#     return customers_collection

@app.post('/requestconsent')
def request_consent(data:ConsentRequest, ):
    """
    Send consent request and update the consent data for the user
    """
    
    #Consent request
    requestConsentPayload = {
    "partyIdentifierType": "MOBILE",
    "partyIdentifierValue": data.mobile,
    "productID": data.consentTypeID,
    "accountID":  accountID,
    "vua": vua
    }
    
    response = requests.request("POST", moneyone_endpoints['requestConsentUrl'], headers=moneyone_headers, json = requestConsentPayload)

    if response.json()['status'] !='success':
        return response.json()
    else:
        getConsentListPayload = {
        "partyIdentifierType": "MOBILE",
        "partyIdentifierValue": data.mobile,
        "productID": data.consentTypeID,
        "accountID":  accountID,
        }

        response = requests.request("POST", moneyone_endpoints['getConsentListUrl'], headers=moneyone_headers, json = getConsentListPayload)

        if response.json()['status'] !='success':
            return response.json()
        else:
            consents_data = response.json()['data']
            #Check if document exists
            if customers_collection.document(data.mobile).get().exists:
                customers_collection.document(data.mobile).update({'consents':consents_data})
            #Create document if it doesn't exist
            else:
                customers_collection.document(data.mobile).set({'consents':consents_data})

            return {"status":"success"}


        






