import requests

moneyone_clent_id = 'fp_test_99c6b457064afe2b3d1d64d8ba4552729dcfd5a8'
moneyone_client_secret = '1fc2fd75ceafcae2b2005cc7f31f1684344f9761f19a16e872cb75d28982ad5f70c7df56'
appIdentifier = 'https://www.example.com'
organisationId = 'NAD0163'

moneyone_headers = {
    'Content-Type': 'application/json',
    'client_id': moneyone_clent_id,
    'client_secret': moneyone_client_secret,
    'organisationId': organisationId,
    'appIdentifier': appIdentifier
    }


moneyone_endpoints = {
    'requestConsentUrl':'https://sandbox.moneyone.in/finpro_sandbox/v2/requestconsent',
    'getConsentListUrl' : 'https://sandbox.moneyone.in/finpro_sandbox/v2/getconsentslist',
    'revokeConsentUrl' : 'https://sandbox.moneyone.in/finpro_sandbox/revokeconsent',
    'getFiDataUrl' : 'https://sandbox.moneyone.in/finpro_sandbox/getfidata',
    'getAllFiDataUrl' : 'https://sandbox.moneyone.in/finpro_sandbox/getallfidata',
    'getFiBalanceUrl' : 'https://sandbox.moneyone.in/finpro_sandbox/getfibalance',
    'getGstDataUrl' : 'https://sandbox.moneyone.in/finpro_sandbox/getGSTdata'
}








