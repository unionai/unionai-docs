---
title: flytekit.core.artifact_utils
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.artifact_utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`LabelValue`](.././flytekit.core.artifact_utils#flytekitcoreartifact_utilslabelvalue) | A ProtocolMessage. |
| [`Partitions`](.././flytekit.core.artifact_utils#flytekitcoreartifact_utilspartitions) | A ProtocolMessage. |
| [`TimePartition`](.././flytekit.core.artifact_utils#flytekitcoreartifact_utilstimepartition) | A ProtocolMessage. |
| [`Timestamp`](.././flytekit.core.artifact_utils#flytekitcoreartifact_utilstimestamp) | A ProtocolMessage. |
| [`datetime`](.././flytekit.core.artifact_utils#flytekitcoreartifact_utilsdatetime) | datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |

## flytekit.core.artifact_utils.LabelValue

A ProtocolMessage


## flytekit.core.artifact_utils.Partitions

A ProtocolMessage


## flytekit.core.artifact_utils.TimePartition

A ProtocolMessage


## flytekit.core.artifact_utils.Timestamp

A ProtocolMessage


### Methods

| Method | Description |
|-|-|
| [`FromDatetime()`](#fromdatetime) | Converts datetime to Timestamp |
| [`FromJsonString()`](#fromjsonstring) | Parse a RFC 3339 date string format to Timestamp |
| [`FromMicroseconds()`](#frommicroseconds) | Converts microseconds since epoch to Timestamp |
| [`FromMilliseconds()`](#frommilliseconds) | Converts milliseconds since epoch to Timestamp |
| [`FromNanoseconds()`](#fromnanoseconds) | Converts nanoseconds since epoch to Timestamp |
| [`FromSeconds()`](#fromseconds) | Converts seconds since epoch to Timestamp |
| [`GetCurrentTime()`](#getcurrenttime) | Get the current UTC into Timestamp |
| [`ToDatetime()`](#todatetime) | Converts Timestamp to a datetime |
| [`ToJsonString()`](#tojsonstring) | Converts Timestamp to RFC 3339 date string format |
| [`ToMicroseconds()`](#tomicroseconds) | Converts Timestamp to microseconds since epoch |
| [`ToMilliseconds()`](#tomilliseconds) | Converts Timestamp to milliseconds since epoch |
| [`ToNanoseconds()`](#tonanoseconds) | Converts Timestamp to nanoseconds since epoch |
| [`ToSeconds()`](#toseconds) | Converts Timestamp to seconds since epoch |


#### FromDatetime()

```python
def FromDatetime(
    dt,
):
```
Converts datetime to Timestamp.



| Parameter | Type |
|-|-|
| `dt` |  |

#### FromJsonString()

```python
def FromJsonString(
    value,
):
```
Parse a RFC 3339 date string format to Timestamp.



| Parameter | Type |
|-|-|
| `value` |  |

#### FromMicroseconds()

```python
def FromMicroseconds(
    micros,
):
```
Converts microseconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `micros` |  |

#### FromMilliseconds()

```python
def FromMilliseconds(
    millis,
):
```
Converts milliseconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `millis` |  |

#### FromNanoseconds()

```python
def FromNanoseconds(
    nanos,
):
```
Converts nanoseconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `nanos` |  |

#### FromSeconds()

```python
def FromSeconds(
    seconds,
):
```
Converts seconds since epoch to Timestamp.


| Parameter | Type |
|-|-|
| `seconds` |  |

#### GetCurrentTime()

```python
def GetCurrentTime()
```
Get the current UTC into Timestamp.


#### ToDatetime()

```python
def ToDatetime(
    tzinfo,
):
```
Converts Timestamp to a datetime.



| Parameter | Type |
|-|-|
| `tzinfo` |  |

#### ToJsonString()

```python
def ToJsonString()
```
Converts Timestamp to RFC 3339 date string format.

Returns:
A string converted from timestamp. The string is always Z-normalized
and uses 3, 6 or 9 fractional digits as required to represent the
exact time. Example of the return format: '1972-01-01T10:00:20.021Z'


#### ToMicroseconds()

```python
def ToMicroseconds()
```
Converts Timestamp to microseconds since epoch.


#### ToMilliseconds()

```python
def ToMilliseconds()
```
Converts Timestamp to milliseconds since epoch.


#### ToNanoseconds()

```python
def ToNanoseconds()
```
Converts Timestamp to nanoseconds since epoch.


#### ToSeconds()

```python
def ToSeconds()
```
Converts Timestamp to seconds since epoch.


## flytekit.core.artifact_utils.datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.


