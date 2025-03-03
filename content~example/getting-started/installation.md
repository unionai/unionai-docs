---
title: "Installation Guide"
date: 2023-01-01
draft: false
---

# Installation Guide

Follow these steps to install our software:

<div data-variant="java">

## Java Installation

```java
// Add this to your pom.xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>library</artifactId>
    <version>1.0.0</version>
</dependency>
```

</div>

<div data-variant="cpp">

## C++ Installation

```cpp
// Using CMake
add_subdirectory(library)
target_link_libraries(your_project library)
```

</div>

<div data-variant="go">

## Go Installation

```go
// Using Go modules
go get github.com/example/library
```

</div>