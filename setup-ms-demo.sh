#!/bin/bash

PROJECT_ID=ms-demo-2390
gcloud services enable container --project ${PROJECT_ID}

if [ ! -d "microservices-demo" ] ; 
then git clone https://github.com/CSCI-2390-Project/microservices-demo.git ;
else echo "directory microservices-demo exists in curent directory in gcloud (you're good to go)" ; 
fi ;

cd microservices-demo

ZONE=us-east1-b
gcloud container clusters create onlineboutique --project=${PROJECT_ID} --zone=${ZONE} --machine-type=e2-standard-2 --num-nodes=4

kubectl apply -f ./release/kubernetes-manifests.yaml

kubectl get pods

alias get-ip="kubectl get service frontend-external | awk '{print $4}'"
alias tear-down="gcloud container clusters delete onlineboutique --project=ms-demo-2390 --zone=us-east1-b"

echo "Once all the services listed above are ready, \
get the ip address of the frontend service with the following aliased command: 
get-ip
"

echo "Clean up the services when you are done so as not to waste GCP dollars!
Run the aliased command:
tear-down"
