# thingsboard_client.EntityRelationControllerApi

All URIs are relative to *//localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_relation_using_delete**](EntityRelationControllerApi.md#delete_relation_using_delete) | **DELETE** /api/relation | deleteRelation
[**find_by_to_using_get**](EntityRelationControllerApi.md#find_by_to_using_get) | **GET** /api/relations | findByTo
[**find_info_by_to_using_get**](EntityRelationControllerApi.md#find_info_by_to_using_get) | **GET** /api/relations/info | findInfoByTo
[**get_relation_using_get**](EntityRelationControllerApi.md#get_relation_using_get) | **GET** /api/relation | getRelation

# **delete_relation_using_delete**
> delete_relation_using_delete(from_id, from_type, relation_type, to_id, to_type, relation_type_group=relation_type_group)

deleteRelation

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
api_instance = thingsboard_client.EntityRelationControllerApi(thingsboard_client.ApiClient(configuration))
from_id = 'from_id_example' # str | fromId
from_type = 'from_type_example' # str | fromType
relation_type = 'relation_type_example' # str | relationType
to_id = 'to_id_example' # str | toId
to_type = 'to_type_example' # str | toType
relation_type_group = 'relation_type_group_example' # str | relationTypeGroup (optional)

try:
    # deleteRelation
    api_instance.delete_relation_using_delete(from_id, from_type, relation_type, to_id, to_type, relation_type_group=relation_type_group)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->delete_relation_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_id** | **str**| fromId | 
 **from_type** | **str**| fromType | 
 **relation_type** | **str**| relationType | 
 **to_id** | **str**| toId | 
 **to_type** | **str**| toType | 
 **relation_type_group** | **str**| relationTypeGroup | [optional] 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_to_using_get**
> list[EntityRelation] find_by_to_using_get(to_id, to_type, relation_type_group=relation_type_group)

findByTo

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
api_instance = thingsboard_client.EntityRelationControllerApi(thingsboard_client.ApiClient(configuration))
to_id = 'to_id_example' # str | toId
to_type = 'to_type_example' # str | toType
relation_type_group = 'relation_type_group_example' # str | relationTypeGroup (optional)

try:
    # findByTo
    api_response = api_instance.find_by_to_using_get(to_id, to_type, relation_type_group=relation_type_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->find_by_to_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_id** | **str**| toId | 
 **to_type** | **str**| toType | 
 **relation_type_group** | **str**| relationTypeGroup | [optional] 

### Return type

[**list[EntityRelation]**](EntityRelation.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_info_by_to_using_get**
> list[EntityRelationInfo] find_info_by_to_using_get(to_id, to_type, relation_type_group=relation_type_group)

findInfoByTo

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
api_instance = thingsboard_client.EntityRelationControllerApi(thingsboard_client.ApiClient(configuration))
to_id = 'to_id_example' # str | toId
to_type = 'to_type_example' # str | toType
relation_type_group = 'relation_type_group_example' # str | relationTypeGroup (optional)

try:
    # findInfoByTo
    api_response = api_instance.find_info_by_to_using_get(to_id, to_type, relation_type_group=relation_type_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->find_info_by_to_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_id** | **str**| toId | 
 **to_type** | **str**| toType | 
 **relation_type_group** | **str**| relationTypeGroup | [optional] 

### Return type

[**list[EntityRelationInfo]**](EntityRelationInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation_using_get**
> EntityRelation get_relation_using_get(from_id, from_type, relation_type, to_id, to_type, relation_type_group=relation_type_group)

getRelation

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
api_instance = thingsboard_client.EntityRelationControllerApi(thingsboard_client.ApiClient(configuration))
from_id = 'from_id_example' # str | fromId
from_type = 'from_type_example' # str | fromType
relation_type = 'relation_type_example' # str | relationType
to_id = 'to_id_example' # str | toId
to_type = 'to_type_example' # str | toType
relation_type_group = 'relation_type_group_example' # str | relationTypeGroup (optional)

try:
    # getRelation
    api_response = api_instance.get_relation_using_get(from_id, from_type, relation_type, to_id, to_type, relation_type_group=relation_type_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->get_relation_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_id** | **str**| fromId | 
 **from_type** | **str**| fromType | 
 **relation_type** | **str**| relationType | 
 **to_id** | **str**| toId | 
 **to_type** | **str**| toType | 
 **relation_type_group** | **str**| relationTypeGroup | [optional] 

### Return type

[**EntityRelation**](EntityRelation.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

