# thingsboard_client.DashboardControllerApi

All URIs are relative to *//localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dashboard_customers_using_post**](DashboardControllerApi.md#add_dashboard_customers_using_post) | **POST** /api/dashboard/{dashboardId}/customers/add | addDashboardCustomers
[**assign_dashboard_to_customer_using_post**](DashboardControllerApi.md#assign_dashboard_to_customer_using_post) | **POST** /api/customer/{customerId}/dashboard/{dashboardId} | assignDashboardToCustomer
[**assign_dashboard_to_public_customer_using_post**](DashboardControllerApi.md#assign_dashboard_to_public_customer_using_post) | **POST** /api/customer/public/dashboard/{dashboardId} | assignDashboardToPublicCustomer
[**delete_dashboard_using_delete**](DashboardControllerApi.md#delete_dashboard_using_delete) | **DELETE** /api/dashboard/{dashboardId} | deleteDashboard
[**get_customer_dashboards_using_get**](DashboardControllerApi.md#get_customer_dashboards_using_get) | **GET** /api/customer/{customerId}/dashboards | getCustomerDashboards
[**get_dashboard_by_id_using_get**](DashboardControllerApi.md#get_dashboard_by_id_using_get) | **GET** /api/dashboard/{dashboardId} | getDashboardById
[**get_dashboard_info_by_id_using_get**](DashboardControllerApi.md#get_dashboard_info_by_id_using_get) | **GET** /api/dashboard/info/{dashboardId} | getDashboardInfoById
[**get_max_datapoints_limit_using_get**](DashboardControllerApi.md#get_max_datapoints_limit_using_get) | **GET** /api/dashboard/maxDatapointsLimit | getMaxDatapointsLimit
[**get_server_time_using_get**](DashboardControllerApi.md#get_server_time_using_get) | **GET** /api/dashboard/serverTime | getServerTime
[**get_tenant_dashboards_using_get**](DashboardControllerApi.md#get_tenant_dashboards_using_get) | **GET** /api/tenant/dashboards | getTenantDashboards
[**get_tenant_dashboards_using_get1**](DashboardControllerApi.md#get_tenant_dashboards_using_get1) | **GET** /api/tenant/{tenantId}/dashboards | getTenantDashboards
[**remove_dashboard_customers_using_post**](DashboardControllerApi.md#remove_dashboard_customers_using_post) | **POST** /api/dashboard/{dashboardId}/customers/remove | removeDashboardCustomers
[**save_dashboard_using_post**](DashboardControllerApi.md#save_dashboard_using_post) | **POST** /api/dashboard | saveDashboard
[**unassign_dashboard_from_customer_using_delete**](DashboardControllerApi.md#unassign_dashboard_from_customer_using_delete) | **DELETE** /api/customer/{customerId}/dashboard/{dashboardId} | unassignDashboardFromCustomer
[**unassign_dashboard_from_public_customer_using_delete**](DashboardControllerApi.md#unassign_dashboard_from_public_customer_using_delete) | **DELETE** /api/customer/public/dashboard/{dashboardId} | unassignDashboardFromPublicCustomer
[**update_dashboard_customers_using_post**](DashboardControllerApi.md#update_dashboard_customers_using_post) | **POST** /api/dashboard/{dashboardId}/customers | updateDashboardCustomers

# **add_dashboard_customers_using_post**
> Dashboard add_dashboard_customers_using_post(body, dashboard_id)

addDashboardCustomers

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
body = ['body_example'] # list[str] | strCustomerIds
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # addDashboardCustomers
    api_response = api_instance.add_dashboard_customers_using_post(body, dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->add_dashboard_customers_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| strCustomerIds | 
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_dashboard_to_customer_using_post**
> Dashboard assign_dashboard_to_customer_using_post(customer_id, dashboard_id)

assignDashboardToCustomer

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # assignDashboardToCustomer
    api_response = api_instance.assign_dashboard_to_customer_using_post(customer_id, dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->assign_dashboard_to_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_dashboard_to_public_customer_using_post**
> Dashboard assign_dashboard_to_public_customer_using_post(dashboard_id)

assignDashboardToPublicCustomer

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # assignDashboardToPublicCustomer
    api_response = api_instance.assign_dashboard_to_public_customer_using_post(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->assign_dashboard_to_public_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_using_delete**
> delete_dashboard_using_delete(dashboard_id)

deleteDashboard

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # deleteDashboard
    api_instance.delete_dashboard_using_delete(dashboard_id)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->delete_dashboard_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| dashboardId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_dashboards_using_get**
> TimePageDataDashboardInfo get_customer_dashboards_using_get(customer_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getCustomerDashboards

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = false # bool | ascOrder (optional) (default to false)
offset = 'offset_example' # str | offset (optional)

try:
    # getCustomerDashboards
    api_response = api_instance.get_customer_dashboards_using_get(customer_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_customer_dashboards_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **limit** | **str**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] [default to false]
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataDashboardInfo**](TimePageDataDashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_by_id_using_get**
> Dashboard get_dashboard_by_id_using_get(dashboard_id)

getDashboardById

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # getDashboardById
    api_response = api_instance.get_dashboard_by_id_using_get(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_dashboard_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_info_by_id_using_get**
> DashboardInfo get_dashboard_info_by_id_using_get(dashboard_id)

getDashboardInfoById

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # getDashboardInfoById
    api_response = api_instance.get_dashboard_info_by_id_using_get(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_dashboard_info_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**DashboardInfo**](DashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_max_datapoints_limit_using_get**
> int get_max_datapoints_limit_using_get()

getMaxDatapointsLimit

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))

try:
    # getMaxDatapointsLimit
    api_response = api_instance.get_max_datapoints_limit_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_max_datapoints_limit_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_time_using_get**
> int get_server_time_using_get()

getServerTime

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))

try:
    # getServerTime
    api_response = api_instance.get_server_time_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_server_time_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_dashboards_using_get**
> TextPageDataDashboardInfo get_tenant_dashboards_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantDashboards

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getTenantDashboards
    api_response = api_instance.get_tenant_dashboards_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_tenant_dashboards_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataDashboardInfo**](TextPageDataDashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_dashboards_using_get1**
> TextPageDataDashboardInfo get_tenant_dashboards_using_get1(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantDashboards

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | tenantId
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getTenantDashboards
    api_response = api_instance.get_tenant_dashboards_using_get1(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_tenant_dashboards_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenantId | 
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataDashboardInfo**](TextPageDataDashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dashboard_customers_using_post**
> Dashboard remove_dashboard_customers_using_post(body, dashboard_id)

removeDashboardCustomers

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
body = ['body_example'] # list[str] | strCustomerIds
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # removeDashboardCustomers
    api_response = api_instance.remove_dashboard_customers_using_post(body, dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->remove_dashboard_customers_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| strCustomerIds | 
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_dashboard_using_post**
> Dashboard save_dashboard_using_post(body)

saveDashboard

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
body = thingsboard_client.Dashboard() # Dashboard | dashboard

try:
    # saveDashboard
    api_response = api_instance.save_dashboard_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->save_dashboard_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| dashboard | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_dashboard_from_customer_using_delete**
> Dashboard unassign_dashboard_from_customer_using_delete(customer_id, dashboard_id)

unassignDashboardFromCustomer

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # unassignDashboardFromCustomer
    api_response = api_instance.unassign_dashboard_from_customer_using_delete(customer_id, dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->unassign_dashboard_from_customer_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_dashboard_from_public_customer_using_delete**
> Dashboard unassign_dashboard_from_public_customer_using_delete(dashboard_id)

unassignDashboardFromPublicCustomer

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # unassignDashboardFromPublicCustomer
    api_response = api_instance.unassign_dashboard_from_public_customer_using_delete(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->unassign_dashboard_from_public_customer_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_customers_using_post**
> Dashboard update_dashboard_customers_using_post(body, dashboard_id)

updateDashboardCustomers

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
api_instance = thingsboard_client.DashboardControllerApi(thingsboard_client.ApiClient(configuration))
body = ['body_example'] # list[str] | strCustomerIds
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # updateDashboardCustomers
    api_response = api_instance.update_dashboard_customers_using_post(body, dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->update_dashboard_customers_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| strCustomerIds | 
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

