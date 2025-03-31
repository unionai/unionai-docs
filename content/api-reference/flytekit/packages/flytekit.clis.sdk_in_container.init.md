---
title: flytekit.clis.sdk_in_container.init
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.init

## Directory

### Classes

| Class | Description |
|-|-|
| [`BytesIO`](.././flytekit.clis.sdk_in_container.init#flytekitclissdk_in_containerinitbytesio) | Buffered I/O implementation using an in-memory bytes buffer. |
| [`ZipFile`](.././flytekit.clis.sdk_in_container.init#flytekitclissdk_in_containerinitzipfile) | Class with methods to open, read, write, close, list zip files. |

## flytekit.clis.sdk_in_container.init.BytesIO

Buffered I/O implementation using an in-memory bytes buffer.


## flytekit.clis.sdk_in_container.init.ZipFile

Class with methods to open, read, write, close, list zip files.

z = ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=True,
compresslevel=None)

file: Either the path to the file, or a file-like object.
If it is a path, the file will be opened and closed by ZipFile.
mode: The mode can be either read 'r', write 'w', exclusive create 'x',
or append 'a'.
compression: ZIP_STORED (no compression), ZIP_DEFLATED (requires zlib),
ZIP_BZIP2 (requires bz2) or ZIP_LZMA (requires lzma).
allowZip64: if True ZipFile will create files with ZIP64 extensions when
needed, otherwise it will raise an exception when this would
be necessary.
compresslevel: None (default for the given compression type) or an integer
specifying the level to pass to the compressor.
When using ZIP_STORED or ZIP_LZMA this keyword has no effect.
When using ZIP_DEFLATED integers 0 through 9 are accepted.
When using ZIP_BZIP2 integers 1 through 9 are accepted.


```python
class ZipFile(
    file,
    mode,
    compression,
    allowZip64,
    compresslevel,
    strict_timestamps,
    metadata_encoding,
)
```
Open the ZIP file with mode read 'r', write 'w', exclusive create 'x',
or append 'a'.


| Parameter | Type |
|-|-|
| `file` |  |
| `mode` |  |
| `compression` |  |
| `allowZip64` |  |
| `compresslevel` |  |
| `strict_timestamps` |  |
| `metadata_encoding` |  |

### Methods

| Method | Description |
|-|-|
| [`close()`](#close) | Close the file, and for mode 'w', 'x' and 'a' write the ending. |
| [`extract()`](#extract) | Extract a member from the archive to the current working directory,. |
| [`extractall()`](#extractall) | Extract all members from the archive to the current working. |
| [`getinfo()`](#getinfo) | Return the instance of ZipInfo given 'name'. |
| [`infolist()`](#infolist) | Return a list of class ZipInfo instances for files in the. |
| [`mkdir()`](#mkdir) | Creates a directory inside the zip archive. |
| [`namelist()`](#namelist) | Return a list of file names in the archive. |
| [`open()`](#open) | Return file-like object for 'name'. |
| [`printdir()`](#printdir) | Print a table of contents for the zip file. |
| [`read()`](#read) | Return file bytes for name. |
| [`setpassword()`](#setpassword) | Set default password for encrypted files. |
| [`testzip()`](#testzip) | Read all the files and check the CRC. |
| [`write()`](#write) | Put the bytes from filename into the archive under the name. |
| [`writestr()`](#writestr) | Write a file into the archive. |


#### close()

```python
def close()
```
Close the file, and for mode 'w', 'x' and 'a' write the ending
records.


#### extract()

```python
def extract(
    member,
    path,
    pwd,
)
```
Extract a member from the archive to the current working directory,
using its full name. Its file information is extracted as accurately
as possible. `member' may be a filename or a ZipInfo object. You can
specify a different directory using `path'. You can specify the
password to decrypt the file using 'pwd'.


| Parameter | Type |
|-|-|
| `member` |  |
| `path` |  |
| `pwd` |  |

#### extractall()

```python
def extractall(
    path,
    members,
    pwd,
)
```
Extract all members from the archive to the current working
directory. `path' specifies a different directory to extract to.
`members' is optional and must be a subset of the list returned
by namelist(). You can specify the password to decrypt all files
using 'pwd'.


| Parameter | Type |
|-|-|
| `path` |  |
| `members` |  |
| `pwd` |  |

#### getinfo()

```python
def getinfo(
    name,
)
```
Return the instance of ZipInfo given 'name'.


| Parameter | Type |
|-|-|
| `name` |  |

#### infolist()

```python
def infolist()
```
Return a list of class ZipInfo instances for files in the
archive.


#### mkdir()

```python
def mkdir(
    zinfo_or_directory_name,
    mode,
)
```
Creates a directory inside the zip archive.


| Parameter | Type |
|-|-|
| `zinfo_or_directory_name` |  |
| `mode` |  |

#### namelist()

```python
def namelist()
```
Return a list of file names in the archive.


#### open()

```python
def open(
    name,
    mode,
    pwd,
    force_zip64,
)
```
Return file-like object for 'name'.

name is a string for the file name within the ZIP file, or a ZipInfo
object.

mode should be 'r' to read a file already in the ZIP file, or 'w' to
write to a file newly added to the archive.

pwd is the password to decrypt files (only used for reading).

When writing, if the file size is not known in advance but may exceed
2 GiB, pass force_zip64 to use the ZIP64 format, which can handle large
files.  If the size is known in advance, it is best to pass a ZipInfo
instance for name, with zinfo.file_size set.


| Parameter | Type |
|-|-|
| `name` |  |
| `mode` |  |
| `pwd` |  |
| `force_zip64` |  |

#### printdir()

```python
def printdir(
    file,
)
```
Print a table of contents for the zip file.


| Parameter | Type |
|-|-|
| `file` |  |

#### read()

```python
def read(
    name,
    pwd,
)
```
Return file bytes for name. 'pwd' is the password to decrypt
encrypted files.


| Parameter | Type |
|-|-|
| `name` |  |
| `pwd` |  |

#### setpassword()

```python
def setpassword(
    pwd,
)
```
Set default password for encrypted files.


| Parameter | Type |
|-|-|
| `pwd` |  |

#### testzip()

```python
def testzip()
```
Read all the files and check the CRC.

Return None if all files could be read successfully, or the name
of the offending file otherwise.


#### write()

```python
def write(
    filename,
    arcname,
    compress_type,
    compresslevel,
)
```
Put the bytes from filename into the archive under the name
arcname.


| Parameter | Type |
|-|-|
| `filename` |  |
| `arcname` |  |
| `compress_type` |  |
| `compresslevel` |  |

#### writestr()

```python
def writestr(
    zinfo_or_arcname,
    data,
    compress_type,
    compresslevel,
)
```
Write a file into the archive.  The contents is 'data', which
may be either a 'str' or a 'bytes' instance; if it is a 'str',
it is encoded as UTF-8 first.
'zinfo_or_arcname' is either a ZipInfo instance or
the name of the file in the archive.


| Parameter | Type |
|-|-|
| `zinfo_or_arcname` |  |
| `data` |  |
| `compress_type` |  |
| `compresslevel` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `comment` |  | {{< multiline >}}The comment text associated with the ZIP file.
{{< /multiline >}} |

