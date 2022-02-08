#!/bin/bash

curl -vX POST http://localhost:8069/decryptMessage -d @payload.json --header "Content-Type: application/json"