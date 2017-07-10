# Swagger\Client\CommentsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commentsCreate**](CommentsApi.md#commentsCreate) | **POST** /comments/ | API endpoint that allows comments to be viewed or edited.
[**commentsDelete**](CommentsApi.md#commentsDelete) | **DELETE** /comments/{id}/ | API endpoint that allows comments to be viewed or edited.
[**commentsList**](CommentsApi.md#commentsList) | **GET** /comments/ | API endpoint that allows comments to be viewed or edited.
[**commentsPartialUpdate**](CommentsApi.md#commentsPartialUpdate) | **PATCH** /comments/{id}/ | API endpoint that allows comments to be viewed or edited.
[**commentsRead**](CommentsApi.md#commentsRead) | **GET** /comments/{id}/ | API endpoint that allows comments to be viewed or edited.
[**commentsUpdate**](CommentsApi.md#commentsUpdate) | **PUT** /comments/{id}/ | API endpoint that allows comments to be viewed or edited.


# **commentsCreate**
> commentsCreate($data)

API endpoint that allows comments to be viewed or edited.

API endpoint that allows comments to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\CommentsApi();
$data = new \Swagger\Client\Model\Data(); // \Swagger\Client\Model\Data | 

try {
    $api_instance->commentsCreate($data);
} catch (Exception $e) {
    echo 'Exception when calling CommentsApi->commentsCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**\Swagger\Client\Model\Data**](../Model/\Swagger\Client\Model\Data.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **commentsDelete**
> commentsDelete($id)

API endpoint that allows comments to be viewed or edited.

API endpoint that allows comments to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\CommentsApi();
$id = 56; // int | A unique integer value identifying this comment.

try {
    $api_instance->commentsDelete($id);
} catch (Exception $e) {
    echo 'Exception when calling CommentsApi->commentsDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this comment. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **commentsList**
> commentsList()

API endpoint that allows comments to be viewed or edited.

API endpoint that allows comments to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\CommentsApi();

try {
    $api_instance->commentsList();
} catch (Exception $e) {
    echo 'Exception when calling CommentsApi->commentsList: ', $e->getMessage(), PHP_EOL;
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

# **commentsPartialUpdate**
> commentsPartialUpdate($id, $data)

API endpoint that allows comments to be viewed or edited.

API endpoint that allows comments to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\CommentsApi();
$id = 56; // int | A unique integer value identifying this comment.
$data = new \Swagger\Client\Model\Data2(); // \Swagger\Client\Model\Data2 | 

try {
    $api_instance->commentsPartialUpdate($id, $data);
} catch (Exception $e) {
    echo 'Exception when calling CommentsApi->commentsPartialUpdate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this comment. |
 **data** | [**\Swagger\Client\Model\Data2**](../Model/\Swagger\Client\Model\Data2.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **commentsRead**
> commentsRead($id)

API endpoint that allows comments to be viewed or edited.

API endpoint that allows comments to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\CommentsApi();
$id = 56; // int | A unique integer value identifying this comment.

try {
    $api_instance->commentsRead($id);
} catch (Exception $e) {
    echo 'Exception when calling CommentsApi->commentsRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this comment. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **commentsUpdate**
> commentsUpdate($id, $data)

API endpoint that allows comments to be viewed or edited.

API endpoint that allows comments to be viewed or edited.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$api_instance = new Swagger\Client\Api\CommentsApi();
$id = 56; // int | A unique integer value identifying this comment.
$data = new \Swagger\Client\Model\Data1(); // \Swagger\Client\Model\Data1 | 

try {
    $api_instance->commentsUpdate($id, $data);
} catch (Exception $e) {
    echo 'Exception when calling CommentsApi->commentsUpdate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this comment. |
 **data** | [**\Swagger\Client\Model\Data1**](../Model/\Swagger\Client\Model\Data1.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

