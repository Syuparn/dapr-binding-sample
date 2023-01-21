# dapr-binding-sample
Dapr binding sample (only for experiments)

# run

```bash
$ kind create cluster
$ skaffold run
```

# experiment

## invoke

```bash
$ kubectl port-forward svc/app 3500:3500
$ curl -XPOST -i http://localhost:3500/v1.0/bindings/myevent -d '{"data": {}, "operation": "create"}'
HTTP/1.1 204 No Content
Server: fasthttp
Date: Sat, 21 Jan 2023 04:31:40 GMT
Traceparent: 00-00000000000000000000000000000000-0000000000000000-00
```

## crash app

```bash
$ kubectl port-forward svc/app 8080:8080

$ curl -XPOST -i http://localhost:8080/crash
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.10.7
Date: Sat, 21 Jan 2023 04:57:38 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 20
Connection: close

healthz will hang up

$ kubectl get po app-cd8ddc45-hbhm4 -o json | jq '[.spec.containers,.status.containerStatuses] | transpose | .[] | {"name": .[0].name, "res
tartCount": .[1].restartCount}'
{
  "name": "myapp",
  "restartCount": 0
}
{
  "name": "daprd",
  "restartCount": 1
}
```
