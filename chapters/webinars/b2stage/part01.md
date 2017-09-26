
# Webinars

## EUDAT-B2STAGE HTTP-API

Here there is the first part of the transcription for the webinar held 2017, September the 9th for the B2STAGE service I developed.

- Slides in `PDF` format are available on [google drive]()
- The recording is also accessible on 
[youtube](https://www.youtube.com/watch?v=6-55uOcqraA)

TODO: try to embed slides


---

### slide 01 - cover

Welcome everyone, this is Paolo D’Onorio De Meo speaking from CINECA, Italy.

(NOTE: senior software and architecture engineer 
for the Middleware subgroup in the SCAI department of [CINECA]()).

Today I would like to guide you through the project that I’ve been working on the past two years together with my colleague Roberto Mucci: the `B2STAGE RESTful HTTP-API`.

The project is getting closer to a final stable release. In fact we have just reached the second release candidate today.

What we want to share with you now is:

- why this application is important
- the initial requirements
- the decisions we made and the reasons behind
- how to deploy, use or develop the current release

Let’s start

---

### slide 02 - agenda

The webinar is divided into 4 main parts.

At first we will make an introduction to make sure that everyone may get confident with the context and all the terms involved.
To do so we will explain what is B2STAGE, the HTTP-API and the underlying framework called “*rapydo*”.

Then we will continue looking from the three different possible point of views when dealing with the project:

1. The EUDAT adminer which wants to deploy and host the project on his centre machines on top of B2SAFE
2. The Community user which wants to use different clients to interact with his data stored in B2SAFE
3. Finally how a developer can collaborate in moving the project forward

We start now with introducing the main concepts of the project.
And at the very beginning we can take a look 
at what the EUDAT B2STAGE service is intended for.

---

### slide 05 - introduction to B2STAGE services

B2STAGE is a reliable, efficient and easy-to-use service to transfer research data sets between EUDAT storage resources and high-performance computing (HPC) workspaces.

The service allows users to:
- transfer large data collections from EUDAT storage facilities to external HPC facilities for processing
- ingest computation results onto the EUDAT infrastructure
- access stored data sets through associated PIDs
- in conjunction with B2SAFE, replicate community data sets, ingesting them onto EUDAT storage resources for long-term preservation
- 
The B2STAGE service comprises two different packages:
- The GridFTP iRODS-DSI to enable fast data transfer through the GridFTP protocol which allows users to manage data on EUDAT nodes (iRODS) through any standard GridFTP client
- The B2STAGE HTTP-API

Since the HTTP protocol is not error-prone the recommended solution for moving large quantity of data is currently Grid-FTP.

A chunked upload feature for our HTTP API is planned, 
but due to limited effort compared to the list of things to be done we still haven’t got a chance to look at it.


---

### slide 06 - Integration with other EUDAT services

B2SAFE: 

B2SAFE is a service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner. It is the service used for long-term archiving and preservation.

B2HANDLE:

In order to access a data object stored in EUDAT, an associated PID is needed. B2HANDLE enables EUDAT services and user communities to assign PIDs to different kinds of managed objects stored in the EUDAT CDI. It also provides tool for the PIDs resolution.

B2ACCESS:

B2ACCESS is the Authentication and Authorization platform developed by EUDAT that can be integrate in any EUDAT service. 
When B2ACCESS is integrated with a given service, the user may log in by using different methods of authentication:
- Home organisation identity provider
- Google account
- EUDAT ID

I personally think that dealing with integration of different custom services which took their own path and decisions along the way
is probably the most complicated goal to achieve when working on an HTTP API interface layer.

---

### slide 07 - Introduction to HTTP API

Going on with the introduction we see the HTTP API word. 
This is currently a buzz word, everyone is talking about it. 

What does HTTP API really means?

Nowadays web applications are getting adopted more and more. 

To allow a common backend with multiple clients (for example desktop, web page, mobile application) the most common pattern used is the HTTP API server.

We have our principles and objectives.
The main endpoint is the [registered domain]().

---

### slide 12 - Introduction to RAPyDo

We complete this gentle introduction to the project by describing
the framework behind the B2STAGE HTTP API development, called “rapido”
(NOTE: It means 'fast' in italian).

When I first arrived in the EUDAT Work package 5 development team
I was asked to help providing a base Python code to harmonize HTTP API development in all EUDAT services 

Before arriving I was working with my colleague Mattia D’Antonio 
on a framework to be used as a base in CINECA for every project who needed HTTP API. So this two things collided and the work has grown with the EUDAT project eventually became this open source project we then called RAPyDo.

The name is the derivation of the main technologies used to build a generic HTTP API environment,
where every possible service can be plugged if respecting two main conditions:

- They have a working docker image
- They have a Python ORM or similar to map the service resources into Classes

The initial goal was to hide the complexity of docker and flask plugins needed for writing correct HTTP API while following standards from the start of a project.

We used Python because it's the EUDAT main programming language adopted so far while Docker avoided us difficulties in switching environments or falling into the hell of library versions.

---

### slide 16 - RAPyDo scheme


This is a simplified scheme of the B2STAGE HTTP API components on top of rapido. As you can see many containers are automatically spawned from the created configuration.

Many services are plugged to the Flask main server, which then in production is only reached by users through a proxy who’s providing the HTTPS interface.

Technologies used:

- Python3 language
- Flask web framework - http://flask.pocoo.org/
- Python iRODS Client extended to support GSI authentication and Python3 - https://github.com/irods/python-irodsclient/
- B2Handle Python library - https://github.com/EUDAT-B2SAFE/B2HANDLE
- Docker containers
- 
Production environment also starts:
- uWSGI - https://github.com/unbit/uwsgi (Uber)
- NGNIX HTTP and reverse proxy server - http://nginx.org/en/

The controller is the only component of rapido we must really know about,
because it allows us to do operations on any custom project based on the rapido templating.

We will have to install it as a base requirement in B2STAGE to have things working.



---

### slide 18 - Who adopted RAPyDO?

Since all currently working custom projects required different aspects to take care of, RAPyDo has grown since the very beginning a notable list of supported services and features.

As explained they usually are supported once a valid Docker image has been developed and tested in the whole environment.

So what it’s already working at the moment in the whole rapido box 
(and was added only thanks to these projects) are:

- Mongodb database (EPOS)
- Graphdb Neo4j database (Telethon)
- Pluggable javascript frontend based on Angular.js 1.6 (EPOS)
- Celery queues based on a Rabbit MQ broker (Telethon)
- FTP server (imediacities)
- Video sharing with Flask (imediacities)

To be included in the near future:

- Elasticsearch (Human Brain)
- Rancher APIs interaction: managing docker containers, images and volumes inside a Virtual Machine provider (seadatanet)


-- 

This is the end of the introductio of this webinar


