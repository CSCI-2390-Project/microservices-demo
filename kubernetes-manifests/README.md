# ./kubernetes-manifests

:warning: Kubernetes manifests provided in this directory are not directly
deployable to a cluster. They are meant to be used with `skaffold` command to
insert the correct `image:` tags.

Use the manifests in [/release](/release) directory which are configured with
pre-built public images.

## Collecting Traces from Jaegar

A single product fetch!
```
http://<address of jaeger-query>/api/traces?limit=20&lookback=1h&operation=Recv.%2Fproduct%2F0PUK6V6EV0&service=frontend
```

This is what a single trace looks like - the results you get back from the above will have many more array elements in `data`. Note that the full duration of the request is the span whose `references` array is empty, and that units are in microseconds (not milliseconds!).
```
{
  "data": [
    {
      "traceID": "f29361adb116fedd18f240496e8927cf",
      "spans": [
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "21186f1ecc9af6f2",
          "flags": 1,
          "operationName": "Sent.hipstershop.ProductCatalogService.GetProduct",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433019035,
          "duration": 987,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "4ba6499b2e8cbf94",
          "flags": 1,
          "operationName": "Sent.hipstershop.CartService.GetCart",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433021404,
          "duration": 1027,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "60edb6d9df04a465",
          "flags": 1,
          "operationName": "Sent.hipstershop.CurrencyService.Convert",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433022460,
          "duration": 1021,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "365fdc5c7d13dbc3",
          "flags": 1,
          "operationName": "Sent.hipstershop.CurrencyService.GetSupportedCurrencies",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433020040,
          "duration": 780,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "75342418917d8836",
          "flags": 1,
          "operationName": "Sent.hipstershop.RecommendationService.ListRecommendations",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433023516,
          "duration": 6505,
          "tags": [
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "8a7b915642f66c07",
          "flags": 1,
          "operationName": "Sent.hipstershop.ProductCatalogService.GetProduct",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433030402,
          "duration": 2038,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "9fc2fe94f36e51d8",
          "flags": 1,
          "operationName": "Sent.hipstershop.ProductCatalogService.GetProduct",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433032799,
          "duration": 1046,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "b4096cd3a4e735a9",
          "flags": 1,
          "operationName": "Sent.hipstershop.ProductCatalogService.GetProduct",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433034037,
          "duration": 1071,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "de97465007d9fe4a",
          "flags": 1,
          "operationName": "Sent.hipstershop.ProductCatalogService.GetProduct",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433036455,
          "duration": 867,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "c950d91156601a7a",
          "flags": 1,
          "operationName": "Sent.hipstershop.ProductCatalogService.GetProduct",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433035371,
          "duration": 891,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "f3deb38eb851e31b",
          "flags": 1,
          "operationName": "Sent.hipstershop.AdService.GetAds",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "0cd101e01a221222"
            }
          ],
          "startTime": 1607283433037683,
          "duration": 2822,
          "tags": [
            {
              "key": "Client",
              "type": "bool",
              "value": true
            },
            {
              "key": "FailFast",
              "type": "bool",
              "value": true
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": ""
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "0cd101e01a221222",
          "flags": 1,
          "operationName": "Recv./product/1YMWWN1N4O",
          "references": [],
          "startTime": 1607283433018919,
          "duration": 22380,
          "tags": [
            {
              "key": "http.method",
              "type": "string",
              "value": "GET"
            },
            {
              "key": "http.user_agent",
              "type": "string",
              "value": "python-requests/2.21.0"
            },
            {
              "key": "http.status_code",
              "type": "int64",
              "value": 200
            },
            {
              "key": "http.path",
              "type": "string",
              "value": "/product/1YMWWN1N4O"
            },
            {
              "key": "http.url",
              "type": "string",
              "value": "/product/1YMWWN1N4O"
            },
            {
              "key": "http.host",
              "type": "string",
              "value": "frontend"
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "status.message",
              "type": "string",
              "value": "OK"
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [],
          "processID": "p1",
          "warnings": null
        },
        {
          "traceID": "f29361adb116fedd18f240496e8927cf",
          "spanID": "c0042eb6bc13c69d",
          "flags": 1,
          "operationName": "Recv.hipstershop.AdService.GetAds",
          "references": [
            {
              "refType": "CHILD_OF",
              "traceID": "f29361adb116fedd18f240496e8927cf",
              "spanID": "f3deb38eb851e31b"
            }
          ],
          "startTime": 1607283433038000,
          "duration": 2285,
          "tags": [
            {
              "key": "method",
              "type": "string",
              "value": "getAds"
            },
            {
              "key": "status.code",
              "type": "int64",
              "value": 0
            },
            {
              "key": "internal.span.format",
              "type": "string",
              "value": "jaeger"
            }
          ],
          "logs": [
            {
              "timestamp": 1607283433039088,
              "fields": [
                {
                  "key": "Context Keys",
                  "type": "string",
                  "value": "[cookware]"
                },
                {
                  "key": "Context Keys length",
                  "type": "int64",
                  "value": 1
                },
                {
                  "key": "message",
                  "type": "string",
                  "value": "Constructing Ads using context"
                }
              ]
            },
            {
              "timestamp": 1607283433038391,
              "fields": [
                {
                  "key": "compressed_size",
                  "type": "int64",
                  "value": 10
                },
                {
                  "key": "id",
                  "type": "int64",
                  "value": 0
                },
                {
                  "key": "message",
                  "type": "string",
                  "value": "received message"
                },
                {
                  "key": "uncompressed_size",
                  "type": "int64",
                  "value": 0
                }
              ]
            },
            {
              "timestamp": 1607283433039424,
              "fields": [
                {
                  "key": "compressed_size",
                  "type": "int64",
                  "value": 92
                },
                {
                  "key": "id",
                  "type": "int64",
                  "value": 0
                },
                {
                  "key": "message",
                  "type": "string",
                  "value": "sent message"
                },
                {
                  "key": "uncompressed_size",
                  "type": "int64",
                  "value": 92
                }
              ]
            }
          ],
          "processID": "p2",
          "warnings": null
        }
      ],
      "processes": {
        "p1": {
          "serviceName": "frontend",
          "tags": []
        },
        "p2": {
          "serviceName": "adservice",
          "tags": []
        }
      },
      "warnings": null
    }
  ],
  "total": 0,
  "limit": 0,
  "offset": 0,
  "errors": null
}
```