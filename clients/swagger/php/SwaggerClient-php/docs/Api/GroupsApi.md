# Swagger\Client\GroupsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupsCreate**](GroupsApi.md#groupsCreate) | **POST** /groups/ | API endpoint that allows groups to be viewed or edited.
[**groupsDelete**](GroupsApi.md#groupsDelete) | **DELETE** /groups/{id}/ | API endpoint that allows groups to be viewed or edited.
[**groupsList**](GroupsApi.md#groupsList) | **GET** /groups/ | API endpoint that allows groups to be viewed or edited.
[**groupsPartialUpdate**](GroupsApi.md#groupsPartialUpdate) | **PATCH** /groups/{id}/ | API endpoint that allows groups to be viewed or edited.
[**groupsRead**](GroupsApi.md#groupsRead) | **GET** /groups/{id}/ | API endpoint that allows groups to be viewed or edited.
[**groupsUpdate**](GroupsApi.md#groupsUpdate) | **PUT** /groups/{id}/ | API endpoint that allows groups to be viewed or edited.


# **groupsCreate**
> groupsCreate($data)

API endpoint that allows groups to be viewed or edited.

API endpoint that allows groups to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\GroupsApi();
$data = new \Swagger\Client\Model\Data3(); // \Swagger\Client\Model\Data3 | 

try {
    $api_instance->groupsCreate($data);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->groupsCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**\Swagger\Client\Model\Data3**](../Model/\Swagger\Client\Model\Data3.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **groupsDelete**
> groupsDelete($id)

API endpoint that allows groups to be viewed or edited.

API endpoint that allows groups to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\GroupsApi();
$id = 56; // int | A unique integer value identifying this group.

try {
    $api_instance->groupsDelete($id);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->groupsDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this group. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **groupsList**
> groupsList()

API endpoint that allows groups to be viewed or edited.

API endpoint that allows groups to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\GroupsApi();

try {
    $api_instance->groupsList();
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->groupsList: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **groupsPartialUpdate**
> groupsPartialUpdate($id, $data)

API endpoint that allows groups to be viewed or edited.

API endpoint that allows groups to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\GroupsApi();
$id = 56; // int | A unique integer value identifying this group.
$data = new \Swagger\Client\Model\Data5(); // \Swagger\Client\Model\Data5 | 

try {
    $api_instance->groupsPartialUpdate($id, $data);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->groupsPartialUpdate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this group. |
 **data** | [**\Swagger\Client\Model\Data5**](../Model/\Swagger\Client\Model\Data5.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **groupsRead**
> groupsRead($id)

API endpoint that allows groups to be viewed or edited.

API endpoint that allows groups to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\GroupsApi();
$id = 56; // int | A unique integer value identifying this group.

try {
    $api_instance->groupsRead($id);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->groupsRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this group. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **groupsUpdate**
> groupsUpdate($id, $data)

API endpoint that allows groups to be viewed or edited.

API endpoint that allows groups to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\GroupsApi();
$id = 56; // int | A unique integer value identifying this group.
$data = new \Swagger\Client\Model\Data4(); // \Swagger\Client\Model\Data4 | 

try {
    $api_instance->groupsUpdate($id, $data);
} catch (Exception $e) {
    echo 'Exception when calling GroupsApi->groupsUpdate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this group. |
 **data** | [**\Swagger\Client\Model\Data4**](../Model/\Swagger\Client\Model\Data4.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

