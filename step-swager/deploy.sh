#!/bin/bash

: "${STACK_NAME:=$1}"
: "${S3_BUCKET:=$2}"

if [[ -z ${STACK_NAME} ]] ; then
  echo "No stackname was provided."
  echo "Use: sh deploy.sh <STACK_NAME> <S3_BUCKET>"
  exit 2
fi

if [[ -z ${S3_BUCKET} ]] ; then
  echo "No S3 bucket defined, using 'pablo-email-test"
  S3_BUCKET="pablo-email-test"
fi

FILENAME=$(echo $RANDOM.${STACK_NAME} | openssl dgst -sha1 | sed 's/^.* //')
BUCKET="s3://$S3_BUCKET/$STACK_NAME/$FILENAME"

echo ${BUCKET}
echo ${FILENAME}


sam build --template-file cloudformation.yaml && sam package --output-template-file packaged.yaml --template-file cloudformation.yaml --s3-bucket ${S3_BUCKET} \
&& sam deploy --template-file packaged.yaml --capabilities CAPABILITY_NAMED_IAM --stack-name ${STACK_NAME}