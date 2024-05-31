curl --insecure -XPUT "https://localhost:9200/pokemon" -H "Content-Type: application/json" -u 'admin:admin' --data-binary "@index.json"
