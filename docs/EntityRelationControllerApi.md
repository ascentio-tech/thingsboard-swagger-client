# thingsboard_client.EntityRelationControllerApi

All URIs are relative to *//localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_relation_using_delete**](EntityRelationControllerApi.md#delete_relation_using_delete) | **DELETE** /api/relation{?relationTypeGroup,fromId,fromType,relationType,toId,toType} | deleteRelation
[**delete_relations_using_delete**](EntityRelationControllerApi.md#delete_relations_using_delete) | **DELETE** /api/relations{?entityId,entityType,id,type} | deleteRelations
[**find_by_from_using_get**](EntityRelationControllerApi.md#find_by_from_using_get) | **GET** /api/relations{?relationTypeGroup,fromId,fromType,relationType} | findByFrom
[**find_by_from_using_get1**](EntityRelationControllerApi.md#find_by_from_using_get1) | **GET** /api/relations{?relationTypeGroup,fromId,fromType} | findByFrom
[**find_by_query_using_post2**](EntityRelationControllerApi.md#find_by_query_using_post2) | **POST** /api/relations | findByQuery
[**find_by_to_using_get**](EntityRelationControllerApi.md#find_by_to_using_get) | **GET** /api/relations{?relationTypeGroup,toId,toType} | findByTo
[**find_by_to_using_get1**](EntityRelationControllerApi.md#find_by_to_using_get1) | **GET** /api/relations{?relationTypeGroup,toId,toType,relationType} | findByTo
[**find_info_by_from_using_get**](EntityRelationControllerApi.md#find_info_by_from_using_get) | **GET** /api/relations/info{?relationTypeGroup,fromId,fromType} | findInfoByFrom
[**find_info_by_query_using_post**](EntityRelationControllerApi.md#find_info_by_query_using_post) | **POST** /api/relations/info | findInfoByQuery
[**find_info_by_to_using_get**](EntityRelationControllerApi.md#find_info_by_to_using_get) | **GET** /api/relations/info{?relationTypeGroup,toId,toType} | findInfoByTo
[**get_relation_using_get**](EntityRelationControllerApi.md#get_relation_using_get) | **GET** /api/relation{?relationTypeGroup,fromId,fromType,relationType,toId,toType} | getRelation
[**save_relation_using_post**](EntityRelationControllerApi.md#save_relation_using_post) | **POST** /api/relation | saveRelation

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

# **delete_relations_using_delete**
> delete_relations_using_delete(entity_id, entity_type, id, type)

deleteRelations

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
entity_id = 'entity_id_example' # str | entityId
entity_type = 'entity_type_example' # str | entityType
id = 'id_example' # str | 
type = 'type_example' # str | 

try:
    # deleteRelations
    api_instance.delete_relations_using_delete(entity_id, entity_type, id, type)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->delete_relations_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| entityId | 
 **entity_type** | **str**| entityType | 
 **id** | **str**|  | 
 **type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_from_using_get**
> list[EntityRelation] find_by_from_using_get(from_id, from_type, relation_type, relation_type_group=relation_type_group)

findByFrom

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
relation_type_group = 'relation_type_group_example' # str | relationTypeGroup (optional)

try:
    # findByFrom
    api_response = api_instance.find_by_from_using_get(from_id, from_type, relation_type, relation_type_group=relation_type_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->find_by_from_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_id** | **str**| fromId | 
 **from_type** | **str**| fromType | 
 **relation_type** | **str**| relationType | 
 **relation_type_group** | **str**| relationTypeGroup | [optional] 

### Return type

[**list[EntityRelation]**](EntityRelation.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_from_using_get1**
> list[EntityRelation] find_by_from_using_get1(from_id, from_type, relation_type_group=relation_type_group)

findByFrom

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
relation_type_group = 'relation_type_group_example' # str | relationTypeGroup (optional)

try:
    # findByFrom
    api_response = api_instance.find_by_from_using_get1(from_id, from_type, relation_type_group=relation_type_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->find_by_from_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_id** | **str**| fromId | 
 **from_type** | **str**| fromType | 
 **relation_type_group** | **str**| relationTypeGroup | [optional] 

### Return type

[**list[EntityRelation]**](EntityRelation.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_query_using_post2**
> list[EntityRelation] find_by_query_using_post2(body)

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
api_instance = thingsboard_client.EntityRelationControllerApi(thingsboard_client.ApiClient(configuration))
body = thingsboard_client.EntityRelationsQuery() # EntityRelationsQuery | query

try:
    # findByQuery
    api_response = api_instance.find_by_query_using_post2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->find_by_query_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityRelationsQuery**](EntityRelationsQuery.md)| query | 

### Return type

[**list[EntityRelation]**](EntityRelation.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

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

# **find_by_to_using_get1**
> list[EntityRelation] find_by_to_using_get1(to_id, to_type, relation_type, relation_type_group=relation_type_group)

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
relation_type = 'relation_type_example' # str | relationType
relation_type_group = 'relation_type_group_example' # str | relationTypeGroup (optional)

try:
    # findByTo
    api_response = api_instance.find_by_to_using_get1(to_id, to_type, relation_type, relation_type_group=relation_type_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->find_by_to_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_id** | **str**| toId | 
 **to_type** | **str**| toType | 
 **relation_type** | **str**| relationType | 
 **relation_type_group** | **str**| relationTypeGroup | [optional] 

### Return type

[**list[EntityRelation]**](EntityRelation.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_info_by_from_using_get**
> list[EntityRelationInfo] find_info_by_from_using_get(from_id, from_type, relation_type_group=relation_type_group)

findInfoByFrom

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
relation_type_group = 'relation_type_group_example' # str | relationTypeGroup (optional)

try:
    # findInfoByFrom
    api_response = api_instance.find_info_by_from_using_get(from_id, from_type, relation_type_group=relation_type_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->find_info_by_from_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_id** | **str**| fromId | 
 **from_type** | **str**| fromType | 
 **relation_type_group** | **str**| relationTypeGroup | [optional] 

### Return type

[**list[EntityRelationInfo]**](EntityRelationInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_info_by_query_using_post**
> list[EntityRelationInfo] find_info_by_query_using_post(body)

findInfoByQuery

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
body = thingsboard_client.EntityRelationsQuery() # EntityRelationsQuery | query

try:
    # findInfoByQuery
    api_response = api_instance.find_info_by_query_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->find_info_by_query_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityRelationsQuery**](EntityRelationsQuery.md)| query | 

### Return type

[**list[EntityRelationInfo]**](EntityRelationInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
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

# **save_relation_using_post**
> save_relation_using_post(body)

saveRelation

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
body = thingsboard_client.EntityRelation() # EntityRelation | relation

try:
    # saveRelation
    api_instance.save_relation_using_post(body)
except ApiException as e:
    print("Exception when calling EntityRelationControllerApi->save_relation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityRelation**](EntityRelation.md)| relation | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

