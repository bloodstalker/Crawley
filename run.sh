#!/bin/bash 

rm ./data.json || true
"scrapy" runspider ./crawley.py -o ./data.json -s LOG_ENABLED=False
less ./data.json
