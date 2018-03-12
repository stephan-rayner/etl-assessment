#!/bin/bash 

submit_crash_report(){
    curl -X POST \
    http://159.65.76.76/ \
    -H 'cache-control: no-cache' \
    -H 'content-type: application/json' \
    -d '{
        
        "event_name": "crash_report",
        "user_id": 1,
        "timestamp": 1483228810,
        "message": "Stuff went really well!"
    }'
}

submit_purchase(){
    curl -X POST \
    http://159.65.76.76/ \
    -H 'cache-control: no-cache' \
    -H 'content-type: application/json' \
    -d '{
        
        "event_name": "purchase",
        "user_id": 1,
        "timestamp": 1483228810,
        "sku": "com.iugome.knights.52gold"
    }'
}

submit_install(){
    curl -X POST \
    http://159.65.76.76/ \
    -H 'cache-control: no-cache' \
    -H 'content-type: application/json' \
    -H 'postman-token: 72491d61-e7e6-237e-e46c-f9180e71104b' \
    -d '{
        
        "event_name": "install",
        "user_id": 2,
        "timestamp": 1483228800
    }'
}

main(){
    COUNTER=0
    while [  $COUNTER -lt 100000 ]; do
        submit_crash_report
        submit_purchase
        submit_install
        let COUNTER=COUNTER+1 
    done
}

main