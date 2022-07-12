# N3


## Requirements


* Python3
* pip3


## Installation


`pip3 install -r requirements.txt`


## Usage


### gen.py
```bash 
./gen.py --help
```

*Example usage*

```bash 
./gen.py --rows 20 --output-path ./data/ --column-data "('int_data', 'integer'), ('string_data', 'string')"
```


### api.py
```bash 
./api.py
```

*Example API calls*

GET:
```bash 
curl http://127.0.0.1:5000/file
```

POST:
```bash 
curl http://127.0.0.1:5000/file -d '{"data": "test"}' -H "Content-Type: application/json" -X POST
```


## Tests


```bash 
pytest
```


