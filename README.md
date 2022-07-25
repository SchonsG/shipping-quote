# SHIPPING-QUOTE

Service related to obtaining shipping quote information

### How to use?

To install all requirements, run:
```
make install
```

#### Testing the code:

```
make test
make coverage
```

#### Running a flask server:

```
make run
```

cURL example:

```
curl -d '{"dimensao":{"altura":80, "largura":13}, "peso":400}' -H "Content-Type: application/json" -X POST http://localhost:5000/shipping-quote
```


All documentation is included in swagger file. I recommend an extension or a web viewer to get all the information.
