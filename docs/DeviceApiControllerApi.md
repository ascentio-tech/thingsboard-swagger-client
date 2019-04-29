# thingsboard_client.DeviceApiControllerApi

All URIs are relative to *//localhosT:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_attributes_using_get**](DeviceApiControllerApi.md#get_device_attributes_using_get) | **GET** /api/v1/{deviceToken}/attributes | getDeviceAttributes
[**post_device_attributes_using_post**](DeviceApiControllerApi.md#post_device_attributes_using_post) | **POST** /api/v1/{deviceToken}/attributes | postDeviceAttributes
[**post_rpc_request_using_post**](DeviceApiControllerApi.md#post_rpc_request_using_post) | **POST** /api/v1/{deviceToken}/rpc | postRpcRequest
[**post_telemetry_using_post**](DeviceApiControllerApi.md#post_telemetry_using_post) | **POST** /api/v1/{deviceToken}/telemetry | postTelemetry
[**reply_to_command_using_post**](DeviceApiControllerApi.md#reply_to_command_using_post) | **POST** /api/v1/{deviceToken}/rpc/{requestId} | replyToCommand
[**subscribe_to_attributes_using_get**](DeviceApiControllerApi.md#subscribe_to_attributes_using_get) | **GET** /api/v1/{deviceToken}/attributes/updates | subscribeToAttributes
[**subscribe_to_commands_using_get**](DeviceApiControllerApi.md#subscribe_to_commands_using_get) | **GET** /api/v1/{deviceToken}/rpc | subscribeToCommands

# **get_device_attributes_using_get**
> DeferredResultResponseEntity get_device_attributes_using_get(device_token, client_keys=client_keys, shared_keys=shared_keys)

getDeviceAttributes

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
api_instance = thingsboard_client.DeviceApiControllerApi(thingsboard_client.ApiClient(configuration))
device_token = 'device_token_example' # str | deviceToken
client_keys = 'client_keys_example' # str | clientKeys (optional)
shared_keys = 'shared_keys_example' # str | sharedKeys (optional)

try:
    # getDeviceAttributes
    api_response = api_instance.get_device_attributes_using_get(device_token, client_keys=client_keys, shared_keys=shared_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApiControllerApi->get_device_attributes_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_token** | **str**| deviceToken | 
 **client_keys** | **str**| clientKeys | [optional] 
 **shared_keys** | **str**| sharedKeys | [optional] 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_device_attributes_using_post**
> DeferredResultResponseEntity post_device_attributes_using_post(body, device_token)

postDeviceAttributes

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
api_instance = thingsboard_client.DeviceApiControllerApi(thingsboard_client.ApiClient(configuration))
body = 'body_example' # str | json
device_token = 'device_token_example' # str | deviceToken

try:
    # postDeviceAttributes
    api_response = api_instance.post_device_attributes_using_post(body, device_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApiControllerApi->post_device_attributes_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| json | 
 **device_token** | **str**| deviceToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rpc_request_using_post**
> DeferredResultResponseEntity post_rpc_request_using_post(body, device_token)

postRpcRequest

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
api_instance = thingsboard_client.DeviceApiControllerApi(thingsboard_client.ApiClient(configuration))
body = 'body_example' # str | json
device_token = 'device_token_example' # str | deviceToken

try:
    # postRpcRequest
    api_response = api_instance.post_rpc_request_using_post(body, device_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApiControllerApi->post_rpc_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| json | 
 **device_token** | **str**| deviceToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_telemetry_using_post**
> DeferredResultResponseEntity post_telemetry_using_post(body, device_token)

postTelemetry

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
api_instance = thingsboard_client.DeviceApiControllerApi(thingsboard_client.ApiClient(configuration))
body = 'body_example' # str | json
device_token = 'device_token_example' # str | deviceToken

try:
    # postTelemetry
    api_response = api_instance.post_telemetry_using_post(body, device_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApiControllerApi->post_telemetry_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| json | 
 **device_token** | **str**| deviceToken | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_to_command_using_post**
> DeferredResultResponseEntity reply_to_command_using_post(body, device_token, request_id)

replyToCommand

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
api_instance = thingsboard_client.DeviceApiControllerApi(thingsboard_client.ApiClient(configuration))
body = 'body_example' # str | json
device_token = 'device_token_example' # str | deviceToken
request_id = 56 # int | requestId

try:
    # replyToCommand
    api_response = api_instance.reply_to_command_using_post(body, device_token, request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApiControllerApi->reply_to_command_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| json | 
 **device_token** | **str**| deviceToken | 
 **request_id** | **int**| requestId | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_attributes_using_get**
> DeferredResultResponseEntity subscribe_to_attributes_using_get(device_token, timeout=timeout)

subscribeToAttributes

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
api_instance = thingsboard_client.DeviceApiControllerApi(thingsboard_client.ApiClient(configuration))
device_token = 'device_token_example' # str | deviceToken
timeout = 789 # int | timeout (optional)

try:
    # subscribeToAttributes
    api_response = api_instance.subscribe_to_attributes_using_get(device_token, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApiControllerApi->subscribe_to_attributes_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_token** | **str**| deviceToken | 
 **timeout** | **int**| timeout | [optional] 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_commands_using_get**
> DeferredResultResponseEntity subscribe_to_commands_using_get(device_token, timeout=timeout)

subscribeToCommands

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
api_instance = thingsboard_client.DeviceApiControllerApi(thingsboard_client.ApiClient(configuration))
device_token = 'device_token_example' # str | deviceToken
timeout = 789 # int | timeout (optional)

try:
    # subscribeToCommands
    api_response = api_instance.subscribe_to_commands_using_get(device_token, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApiControllerApi->subscribe_to_commands_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_token** | **str**| deviceToken | 
 **timeout** | **int**| timeout | [optional] 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

