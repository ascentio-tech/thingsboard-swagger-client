# thingsboard_client.WidgetTypeControllerApi

All URIs are relative to *//localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_widget_type_using_delete**](WidgetTypeControllerApi.md#delete_widget_type_using_delete) | **DELETE** /api/widgetType/{widgetTypeId} | deleteWidgetType
[**get_bundle_widget_types_using_get**](WidgetTypeControllerApi.md#get_bundle_widget_types_using_get) | **GET** /api/widgetTypes{?isSystem,bundleAlias} | getBundleWidgetTypes
[**get_widget_type_by_id_using_get**](WidgetTypeControllerApi.md#get_widget_type_by_id_using_get) | **GET** /api/widgetType/{widgetTypeId} | getWidgetTypeById
[**get_widget_type_using_get**](WidgetTypeControllerApi.md#get_widget_type_using_get) | **GET** /api/widgetType{?isSystem,bundleAlias,alias} | getWidgetType
[**save_widget_type_using_post**](WidgetTypeControllerApi.md#save_widget_type_using_post) | **POST** /api/widgetType | saveWidgetType

# **delete_widget_type_using_delete**
> delete_widget_type_using_delete(widget_type_id)

deleteWidgetType

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
api_instance = thingsboard_client.WidgetTypeControllerApi(thingsboard_client.ApiClient(configuration))
widget_type_id = 'widget_type_id_example' # str | widgetTypeId

try:
    # deleteWidgetType
    api_instance.delete_widget_type_using_delete(widget_type_id)
except ApiException as e:
    print("Exception when calling WidgetTypeControllerApi->delete_widget_type_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_type_id** | **str**| widgetTypeId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_widget_types_using_get**
> list[WidgetType] get_bundle_widget_types_using_get(is_system, bundle_alias)

getBundleWidgetTypes

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
api_instance = thingsboard_client.WidgetTypeControllerApi(thingsboard_client.ApiClient(configuration))
is_system = 'is_system_example' # str | isSystem
bundle_alias = 'bundle_alias_example' # str | bundleAlias

try:
    # getBundleWidgetTypes
    api_response = api_instance.get_bundle_widget_types_using_get(is_system, bundle_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetTypeControllerApi->get_bundle_widget_types_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_system** | **str**| isSystem | 
 **bundle_alias** | **str**| bundleAlias | 

### Return type

[**list[WidgetType]**](WidgetType.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_type_by_id_using_get**
> WidgetType get_widget_type_by_id_using_get(widget_type_id)

getWidgetTypeById

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
api_instance = thingsboard_client.WidgetTypeControllerApi(thingsboard_client.ApiClient(configuration))
widget_type_id = 'widget_type_id_example' # str | widgetTypeId

try:
    # getWidgetTypeById
    api_response = api_instance.get_widget_type_by_id_using_get(widget_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetTypeControllerApi->get_widget_type_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_type_id** | **str**| widgetTypeId | 

### Return type

[**WidgetType**](WidgetType.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_type_using_get**
> WidgetType get_widget_type_using_get(is_system, bundle_alias, alias)

getWidgetType

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
api_instance = thingsboard_client.WidgetTypeControllerApi(thingsboard_client.ApiClient(configuration))
is_system = 'is_system_example' # str | isSystem
bundle_alias = 'bundle_alias_example' # str | bundleAlias
alias = 'alias_example' # str | alias

try:
    # getWidgetType
    api_response = api_instance.get_widget_type_using_get(is_system, bundle_alias, alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetTypeControllerApi->get_widget_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_system** | **str**| isSystem | 
 **bundle_alias** | **str**| bundleAlias | 
 **alias** | **str**| alias | 

### Return type

[**WidgetType**](WidgetType.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_widget_type_using_post**
> WidgetType save_widget_type_using_post(body)

saveWidgetType

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
api_instance = thingsboard_client.WidgetTypeControllerApi(thingsboard_client.ApiClient(configuration))
body = thingsboard_client.WidgetType() # WidgetType | widgetType

try:
    # saveWidgetType
    api_response = api_instance.save_widget_type_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WidgetTypeControllerApi->save_widget_type_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WidgetType**](WidgetType.md)| widgetType | 

### Return type

[**WidgetType**](WidgetType.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

