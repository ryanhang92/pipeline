# Pipeline
deployment system

# Design Doc

Modules:

Builder: Build Docker Images (from dev environment) put it remote and put data sets in s3 (or other store)

Installer: Install needed packges on host machines (docker) and set up data sets?

Contoller: Orchestrate and launch processes (Ansible)
    1) Use Builder 
    2) Procure Comput Resources, Use Installed to set up
    3) Initialize Start compute tasks
    4) Clean-up when done

Monitor (Sentinel)
    1) Monitor experiment progress and results and costs usages, send logs on crash?
    2) Have small library make HTTPS calls to sentinel (maybe auth?) to transmit data 

Store (Could be S3 interface or some DB server)
    1) Store experiment results such as weight
    2) Store training data

