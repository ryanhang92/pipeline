# pipeline
deployment system

# Design Doc

1) Deployer

    a) build deploy code and program locally in container or via AWS on 1 machine or n machines


2) Deploy sentinel to handle any data logged during the deploy job and the final results, could be locally or https


3) Job Persistence to save any data generated, or pickled models in the cloud,


all 2/3 services shouold launch togeather with all deploy jobs
