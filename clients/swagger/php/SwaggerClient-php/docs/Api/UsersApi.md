# Swagger\Client\UsersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersCreate**](UsersApi.md#usersCreate) | **POST** /users/ | API endpoint that allows users to be viewed or edited.
[**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /users/{id}/ | API endpoint that allows users to be viewed or edited.
[**usersList**](UsersApi.md#usersList) | **GET** /users/ | API endpoint that allows users to be viewed or edited.
[**usersPartialUpdate**](UsersApi.md#usersPartialUpdate) | **PATCH** /users/{id}/ | API endpoint that allows users to be viewed or edited.
[**usersRead**](UsersApi.md#usersRead) | **GET** /users/{id}/ | API endpoint that allows users to be viewed or edited.
[**usersUpdate**](UsersApi.md#usersUpdate) | **PUT** /users/{id}/ | API endpoint that allows users to be viewed or edited.


# **usersCreate**
> usersCreate($data)

API endpoint that allows users to be viewed or edited.

API endpoint that allows users to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\UsersApi();
$data = new \Swagger\Client\Model\Data6(); // \Swagger\Client\Model\Data6 | 

try {
    $api_instance->usersCreate($data);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->usersCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**\Swagger\Client\Model\Data6**](../Model/\Swagger\Client\Model\Data6.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **usersDelete**
> usersDelete($id)

API endpoint that allows users to be viewed or edited.

API endpoint that allows users to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\UsersApi();
$id = 56; // int | A unique integer value identifying this user.

try {
    $api_instance->usersDelete($id);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->usersDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **usersList**
> usersList()

API endpoint that allows users to be viewed or edited.

API endpoint that allows users to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\UsersApi();

try {
    $api_instance->usersList();
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->usersList: ', $e->getMessage(), PHP_EOL;
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

# **usersPartialUpdate**
> usersPartialUpdate($id, $data)

API endpoint that allows users to be viewed or edited.

API endpoint that allows users to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\UsersApi();
$id = 56; // int | A unique integer value identifying this user.
$data = new \Swagger\Client\Model\Data8(); // \Swagger\Client\Model\Data8 | 

try {
    $api_instance->usersPartialUpdate($id, $data);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->usersPartialUpdate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. |
 **data** | [**\Swagger\Client\Model\Data8**](../Model/\Swagger\Client\Model\Data8.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **usersRead**
> usersRead($id)

API endpoint that allows users to be viewed or edited.

API endpoint that allows users to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\UsersApi();
$id = 56; // int | A unique integer value identifying this user.

try {
    $api_instance->usersRead($id);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->usersRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **usersUpdate**
> usersUpdate($id, $data)

API endpoint that allows users to be viewed or edited.

API endpoint that allows users to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\UsersApi();
$id = 56; // int | A unique integer value identifying this user.
$data = new \Swagger\Client\Model\Data7(); // \Swagger\Client\Model\Data7 | 

try {
    $api_instance->usersUpdate($id, $data);
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->usersUpdate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. |
 **data** | [**\Swagger\Client\Model\Data7**](../Model/\Swagger\Client\Model\Data7.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

