# thingsboard_client.EntityViewControllerApi

All URIs are relative to *//localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_entity_view_to_customer_using_post**](EntityViewControllerApi.md#assign_entity_view_to_customer_using_post) | **POST** /api/customer/{customerId}/entityView/{entityViewId} | assignEntityViewToCustomer
[**assign_entity_view_to_public_customer_using_post**](EntityViewControllerApi.md#assign_entity_view_to_public_customer_using_post) | **POST** /api/customer/public/entityView/{entityViewId} | assignEntityViewToPublicCustomer
[**delete_entity_view_using_delete**](EntityViewControllerApi.md#delete_entity_view_using_delete) | **DELETE** /api/entityView/{entityViewId} | deleteEntityView
[**find_by_query_using_post3**](EntityViewControllerApi.md#find_by_query_using_post3) | **POST** /api/entityViews | findByQuery
[**get_customer_entity_views_using_get**](EntityViewControllerApi.md#get_customer_entity_views_using_get) | **GET** /api/customer/{customerId}/entityViews{?type,textSearch,idOffset,textOffset,limit} | getCustomerEntityViews
[**get_entity_view_by_id_using_get**](EntityViewControllerApi.md#get_entity_view_by_id_using_get) | **GET** /api/entityView/{entityViewId} | getEntityViewById
[**get_entity_view_types_using_get**](EntityViewControllerApi.md#get_entity_view_types_using_get) | **GET** /api/entityView/types | getEntityViewTypes
[**get_tenant_entity_view_using_get**](EntityViewControllerApi.md#get_tenant_entity_view_using_get) | **GET** /api/tenant/entityViews{?entityViewName} | getTenantEntityView
[**get_tenant_entity_views_using_get**](EntityViewControllerApi.md#get_tenant_entity_views_using_get) | **GET** /api/tenant/entityViews{?type,textSearch,idOffset,textOffset,limit} | getTenantEntityViews
[**save_entity_view_using_post**](EntityViewControllerApi.md#save_entity_view_using_post) | **POST** /api/entityView | saveEntityView
[**unassign_entity_view_from_customer_using_delete**](EntityViewControllerApi.md#unassign_entity_view_from_customer_using_delete) | **DELETE** /api/customer/entityView/{entityViewId} | unassignEntityViewFromCustomer

# **assign_entity_view_to_customer_using_post**
> EntityView assign_entity_view_to_customer_using_post(customer_id, entity_view_id)

assignEntityViewToCustomer

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
entity_view_id = 'entity_view_id_example' # str | entityViewId

try:
    # assignEntityViewToCustomer
    api_response = api_instance.assign_entity_view_to_customer_using_post(customer_id, entity_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->assign_entity_view_to_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **entity_view_id** | **str**| entityViewId | 

### Return type

[**EntityView**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_entity_view_to_public_customer_using_post**
> EntityView assign_entity_view_to_public_customer_using_post(entity_view_id)

assignEntityViewToPublicCustomer

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
entity_view_id = 'entity_view_id_example' # str | entityViewId

try:
    # assignEntityViewToPublicCustomer
    api_response = api_instance.assign_entity_view_to_public_customer_using_post(entity_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->assign_entity_view_to_public_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_view_id** | **str**| entityViewId | 

### Return type

[**EntityView**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_view_using_delete**
> delete_entity_view_using_delete(entity_view_id)

deleteEntityView

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
entity_view_id = 'entity_view_id_example' # str | entityViewId

try:
    # deleteEntityView
    api_instance.delete_entity_view_using_delete(entity_view_id)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->delete_entity_view_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_view_id** | **str**| entityViewId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_query_using_post3**
> list[EntityView] find_by_query_using_post3(body)

findByQuery

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
body = thingsboard_client.EntityViewSearchQuery() # EntityViewSearchQuery | query

try:
    # findByQuery
    api_response = api_instance.find_by_query_using_post3(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->find_by_query_using_post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityViewSearchQuery**](EntityViewSearchQuery.md)| query | 

### Return type

[**list[EntityView]**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_entity_views_using_get**
> TextPageDataEntityView get_customer_entity_views_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getCustomerEntityViews

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getCustomerEntityViews
    api_response = api_instance.get_customer_entity_views_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_customer_entity_views_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **limit** | **str**| limit | 
 **type** | **str**| type | [optional] 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataEntityView**](TextPageDataEntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_view_by_id_using_get**
> EntityView get_entity_view_by_id_using_get(entity_view_id)

getEntityViewById

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
entity_view_id = 'entity_view_id_example' # str | entityViewId

try:
    # getEntityViewById
    api_response = api_instance.get_entity_view_by_id_using_get(entity_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_entity_view_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_view_id** | **str**| entityViewId | 

### Return type

[**EntityView**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_view_types_using_get**
> list[EntitySubtype] get_entity_view_types_using_get()

getEntityViewTypes

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))

try:
    # getEntityViewTypes
    api_response = api_instance.get_entity_view_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_entity_view_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EntitySubtype]**](EntitySubtype.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_entity_view_using_get**
> EntityView get_tenant_entity_view_using_get(entity_view_name)

getTenantEntityView

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
entity_view_name = 'entity_view_name_example' # str | entityViewName

try:
    # getTenantEntityView
    api_response = api_instance.get_tenant_entity_view_using_get(entity_view_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_tenant_entity_view_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_view_name** | **str**| entityViewName | 

### Return type

[**EntityView**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_entity_views_using_get**
> TextPageDataEntityView get_tenant_entity_views_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantEntityViews

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getTenantEntityViews
    api_response = api_instance.get_tenant_entity_views_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_tenant_entity_views_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **type** | **str**| type | [optional] 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataEntityView**](TextPageDataEntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_entity_view_using_post**
> EntityView save_entity_view_using_post(body)

saveEntityView

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
body = thingsboard_client.EntityView() # EntityView | entityView

try:
    # saveEntityView
    api_response = api_instance.save_entity_view_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->save_entity_view_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityView**](EntityView.md)| entityView | 

### Return type

[**EntityView**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_entity_view_from_customer_using_delete**
> EntityView unassign_entity_view_from_customer_using_delete(entity_view_id)

unassignEntityViewFromCustomer

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
api_instance = thingsboard_client.EntityViewControllerApi(thingsboard_client.ApiClient(configuration))
entity_view_id = 'entity_view_id_example' # str | entityViewId

try:
    # unassignEntityViewFromCustomer
    api_response = api_instance.unassign_entity_view_from_customer_using_delete(entity_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->unassign_entity_view_from_customer_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_view_id** | **str**| entityViewId | 

### Return type

[**EntityView**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

