# README
# SFIA 2 Project - Robert W Siberry
## Fallout Pen and Paper Character Generator 

## Table of Contents
1. Project Brief
   - Requirements
   - Overview
2. Trello Board
3. Risk Assessment
4. Project Design
   - CI Pipeline
   - Database
   - App Design 
5. Deployment
6. Improvement

## Project Brief
### ___Requirements___
The requirements of the project are as follows:

- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- An Application fully integrated using the Feature-Branch model into a Version - Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application.
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

### ___Overview___
This app is a Fallout P&P Race and Role Generator.

Service 1 runs as the front end, displaying the output from Service 4. Service 4 gets a randomly generated race from Service 2, and a randomly generated role from Service 3, then concatenates them in Service 4 which then passes them back to  Service 1 gets them and displays them on the front end app.

![App](https://imgur.com/te0cb5u.png)


Below is an image of the Timeline showing the use of the Feature Branch model

![FeatureBranch](https://imgur.com/VUqZujr.png)

## Trello Board

A Trello Board is what I used to keep a track of my progress during project and also log errors.

In the below Trello Board you can see the progress as Sprints were completed and where there may be work carried onto the next Sprint. 

Errors logged that have not yet been moved over to the "Completed" section, are those that were not able to be completed.


![FinalTrello](https://imgur.com/YvHDIdV.png)

## Risk Assessment

Below you will see the risk assessment carried out for this project:

![Risk_Assessment](https://imgur.com/aLTThj0.png)


## Project Design
### ___CI Pipeline___

The Initial CI Pipeline design was made with fewer technologies in mind:

![CIPipelineOld](https://imgur.com/pkWKyI5.png)

### ___App Design___

This design implements the persisted data from previously generated Races/Roles:

![AppFinalDesign](https://media.discordapp.net/attachments/736223635676725341/743149880964546671/unknown.png)


## Deployment
The deployment of the app is automated and handled different tools such as Jenkins, Ansible and Docker. After committing any changes to my GitHub, Jenkins will trigger a pipeline job via a webhook set up through GitHub & Jenkins Configuration. The different stages of the pipeline are outlined in my Jenkinsfile, which for mine currently are:  
- Build Images 
- Deploy Stack 
- Clean 
 
In order to improve readability, each step refers to a script which handles a different stage of the pipeline. First, Jenkins will checkout the Github repo then it will initiate the Jenkinsfile stages.

Then, Jenkins will deploy the application from the swarm manager machine using docker stack. This will balance the load of the containers across the two machines, just before performing clean-up exercises on the Manager node.



If there is any failures in the pipeline jobs then it will be displayed as on the jenkins build page

## Retrospective
As each Sprint continued and more work was carried out, things that could have been done better were:
- Spending more time learning technologies
- Implement more seamless configuration management installations
- Further code testing could be implemented to ensure code works exactly as required

## Improvements

There could be some improvements made to the project, as stated below:
- Add a more asthetic design
- Also generate S.P.E.C.I.A.L stats for each character
- Add up Search Functionality to look up previously generated characters