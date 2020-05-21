#!/bin/bash
aws lambda invoke --function-name my-cli-function --payload '{"key": "value"}' out
sed -i'' -e 's/"//g' out
sleep 5
aws logs get-log-events --log-group-name /aws/lambda/my-cli-function --log-stream-name $(cat out) --limit 5
