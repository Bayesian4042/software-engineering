# Introduction to API design
## What is API ?
API is an application programming interface. It is a way to communicate to the service/system/server. We expose specific api for a system which user can consume to interact with it. Basically, it is an entry point to communicate to the server. User doesn't need to know the internal details of the system. 

## Why should design API ?
It is good to determine all the nitty griity of an api before starting API development, else it is an effort to change things, can lead to many versioning and many iteration.

## Create new API
1. Capture metadata
    1. title: OpenAPI specification for LMS
    2. version: 1.0
    3. description: API specification document of the LMS System
    4. contact support: 

2. Identify type of API
    1. public
        1. Open APIs
    2. partner
        1. between two organization
    3. private
        1. used within a product

3. Identify the server base URL
    1. base URL of server: http://{hostname}:{port}/{directory}: http://localhost:3000/api

4. Identify the resources
5. Resource names as plural
    1. separate name using hypen -
6. Define the resource models
    1. attributes
7. Select identifies for each resource
    1. id

8. Identify the Association for each resource
9. Check for the URL complexity
10. Identify the operation for each resource
11. Identify the parametes required for the operation.
12. Identify the content type of request
13. Identify the request body
17. Handle errors for operation

# Overview of RESTful APIs

## How HTTP works ?
It is a standard protocol to communicate between client and server. 

## Parts of HTTP Request
1. Request Components
- Method: GET, PUT, POST, DELETE, PATCH
- URL: uniquely identify resource
- Headers: meta data of request
- Content: query parameters, body

2. Response Components
- Status Code: success 2xx; client-side error 4xx; server-side error 5xx
- Headers: meta data of response
- Content: response body

## What is REST (Representational State Transfer) ?
1. It is an approach to design the web services
2. Designed around resources
3. Platform Independent
4. Uniform Interface
5. Stateless: server treat every request as new request. 

## URL vs URI ?
1. URI: identify a web resource by location, name or both in internet
2. URL: identify a resource by location. 


# Designing API resources

## Resources should be Nouns
1. Resources are business entities
2. Needn't be based on physical data
3. resource should be nouns and not verbs: customers

## Non resource data should be query parameters
1. Filter: /colleges?sortBy=collegeName
2. Pagination: /colleges?page=10&size=20

# Designing Association between resources
## Defining Relationships between resources
    1. use URL navigation for sub objects
## URL shoudn't be complex
    1. collecton/item/collection
## Combine related resources: 
    1. combine multiple resources into one: for ex: /students/5/course and /students/5/hobbies to /students/5 and response body can have both courses and hobbies

# Designing API Operations

## Overview of HTTP operations/methods
    - Operations on resources:
        - GET
        - POST
        - PUT
        - PATCH
        - DELETE

## Idempotent = making multiple indentical request has the same effect as making a single request
    - GET, PUT and DELETE -> idempotent

# Designing API requests

## Designing Request Parameters
    - query param: passing additional values
    - path param: in the path of the url
    - headers: 
    - cookies: store certain information in cookie. 

## Designing Request Content
    - Content Type: application/json
    - request body: {}

# Designing API response
## HTTP Status Cdes
    - 2xx: success
    - 3xx: redirection
    - 4xx: client side error
    - 5xx: server side error


## Designing Error Handling
    - Client side errors
        - invalid credentials
        - incorrect parameters
        - invalid Ids
    - Server Side Errors
        - Exceptions
    - error Message format
        - code: common between server and client
        - message
        - details: 
        - innererror