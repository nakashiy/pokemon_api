curl --insecure -XPUT "https://localhost:9200/pokemon/_mapping" -H "Content-Type: application/json" -u 'admin:admin' --data-binary "@add_field.json"
