# thingsboard_client.BillingControllerApi

All URIs are relative to *//localhosT:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_cycle_using_post**](BillingControllerApi.md#create_billing_cycle_using_post) | **POST** /api/billing/cycle | createBillingCycle

# **create_billing_cycle_using_post**
> BillingInfoResponse create_billing_cycle_using_post()

createBillingCycle

### Example
```python
from __future__ import print_function
import time
import thingsboard_client
from thingsboard_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
configuration = thingsboard_client.Configuration()
configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = thingsboard_client.BillingControllerApi(thingsboard_client.ApiClient(configuration))

try:
    # createBillingCycle
    api_response = api_instance.create_billing_cycle_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingControllerApi->create_billing_cycle_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BillingInfoResponse**](BillingInfoResponse.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

