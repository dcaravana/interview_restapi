[![Build Status](https://travis-ci.org/dcaravana/interview_restapi.svg?branch=master)](https://travis-ci.org/dcaravana/interview_restapi)

# Interview Coding Test

This repo contains my execution of a coding test about implementing a RESTful API.

The code I wrote goes a bit beyond what was requested as I considered it as an
interesting opportunity to study python a bit more.


## Test Description

1. Write a simple Restful API that takes and stores comments identified by an SKU.

2. The API should have a way in which the comment has been analysed to tell us whether the
comment is positive or not. To do this, you'll use the Watson Tone Analyser for emotional tone.
https://watson-api-explorer.mybluemix.net/apis/tone-analyzer-v3#!/tone/GetTone
The test isn't about Watson, but it makes the problem a little more interesting.

3. The code will need to scale, tell me about how it'll be deployed and built to achieve this.

4. The code must be restful, tell me what makes your API restful.

5. Your code should be well structured, what approach have you taken, and how would you
explain it to another developer?

6. The API must be documented. How have you documented your API?

7. Lastly, any core development approaches should be evident in code.

8. I would also like client examples of it working. Acceptable languages for the test are Python, Java, PHP.


### Questions/doubts about the test

- About 1: comment entity primary key? is it SKU? autogenerated?
- About 7: what does it mean "core development"?


## Test Execution

I learned a bit more python conventions and I tried to use it here since I know
how much they are considered important by the python community.

Interesting places are [The Hitchhiker’s Guide to Python](http://python-guide-pt-br.readthedocs.io/en/latest/) and
[Sample module for Python-Guide.org](https://github.com/kennethreitz/samplemod).

To enforce this, I've configured my editor (Atom) to respect more python
conventions (like automatically removing trailing whitespaces).
More importantly, I've installed and used python linters (`pylint` and
`pycodestyle` seemed good options but opinions are contrasting): with their
help, I've managed to go from 2.35/10 grade on `/sku` python files up to 6.73/10.
A perfect score hardly makes sense in all cases with linters, but they can be
of great help when dealing with readability.

I learned also a bit more about the differences between python 2.x and 3.x and
they boils down to a few important ones: in this case I've chosen python 2.x as
it was immediately available, the ecosystem is a bit more complete and stable.

I also packaged the project as a proper python library that can be distributed
and installed using well-known python package managers like `pip` but more importantly
this brings clarity and autonomy to the project.

Using `virtualenv` is also considered fundamental and I agree since it removes
one of the most fundamental and long-standing issues of software programming:
dependency hell.

The project currently only runs locally but since the test requires scalability
I have planned to write the corresponding code, things that I have not yet done
since it goes beyond the test requirements (but I'll do it since I still want
to learn more python.)

In my mind the project should run in a completely seamless way both locally and
on the cloud (AWS) using automated cloud configuration tools.

Last but not least, I had to chose if to use a framework and also select one.

Going without a framework is an interesting idea but it's clearly beyond the scope of the
this test, even if implementing a WSGI toy framework (or even a web server) is
something I want to try in future.

After a quick research, I selected Django REST Framework for a number of reasons,
but basically because of Django (it seems to be an important skill) and
of its numerous capabilities included out of the box.


### Setup

Just execute `bootstrap.sh` then follow the instructions at the end.

I report them here for completeness:

```
source ~/.virtualenvs/interview_restapi-python/bin/activate
./manage.py migrate
./manage.py createsuperuser --username admin --email admin@nowhere.no
[enter "admin001" as password]
./manage.py runserver
```

Also you need to provide `WATSON_USERNAME` and `WATSON_PASSWORD` (as ENV variables
or in `local_settings.py` file) corresponding to the credentials of the IBM
Watson Tone service.


### Django REST Framework

Just followed a couple of pages:

- https://github.com/encode/django-rest-framework#example
- http://www.django-rest-framework.org/tutorial/quickstart/

This let me create an API in literally no time, complete with authentication and
a load of other features. By the way I have enabled authentication which is
clearly out of spec but makes things a bit more realistic, for example with the
client libraries.

In Diango terms, `skucommentsentimentapi` folder contains the project,
while `sku` is the app.

Even adding the new Comment entity required little time.

For now it's just `/comments` but it may be also `/sku/XXX/commments` depending
on the definition of the entity itself.

It has just a few attributes and no PK:

```
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    tone = models.TextField(blank=True)

    ...
```

I've added some tests as of here http://www.django-rest-framework.org/api-guide/testing/.

I've created very simple tests for models and API.

They can be run with `./manage.py test`.

TODO Add more tests.

While I was at it, I leveraged the awesome Travis CI services adding builds
for python 2.x and 3.x (just fixing a minor syntax error) that executes the
same command.


### API Documentation

The framework has good support to generate API documentation automatically.
It's even interactive.

See http://www.django-rest-framework.org/topics/documenting-your-api/.

I've also added Swagger support but more for automatic client code generation
(see below).

See https://django-rest-swagger.readthedocs.io/en/latest/.

TODO complete endpoints descriptions and regenerate clients/docs if any.

Have a look of the docs here:
 - http://127.0.0.1:8000/
 - http://127.0.0.1:8000/docs/
 - http://127.0.0.1:8000/swagger/ (read below)


If you don't log in with the admin user we created previously, it will only show
read-only operations.


### Tone Analysis

I've learned that ViewSet are just like Controllers in MVC so the right place
were to implement initial non-scalable call to sentiment analysis.
See http://www.django-rest-framework.org/api-guide/viewsets/.

After resurrecting my IBM account, I was able to use the tone service again with
the Watson SDK for python https://github.com/watson-developer-cloud/python-sdk.

The API returns a single meaningful result (as requested) named `tone_is_positive`
associated with each comment. I have defined "positiveness" as a bit arbitrary
(just `joy > 0.5`).

I have implemented this as a virtual/calculated attribute of the Comment entity
just to check how it worked; in a production environment, this value should be
stored for efficiency's sake.

The API also stores and returns the entire analysis result for completeness,
but it's probably something to be encapsulated as an internal detail because
it discloses a detail of the underlaying tools which may make upgrades/evolution
more difficult as users will start relying on it.

I have used ENV variables and `local_settings.py` file to set credentials
(they can be useful in e.g. AWS Beanstalk) as a security best practice.

After a bit of wandering around, I've found an ideal way to add behaviour to
models through signals (`pre_save` in this case), which is great so there is
no need to alter the default View and to keep the logic together with the
corresponding model (in this case `Comment` and the call to tone analyser).


### Scalability

Making scalable this kind of application is about delivering it on
the right infrastructure configured in the right way.

I'm going to consider AWS but any other cloud provider
would probably do well.

Let's consider some aspects:

 - Web tier: AWS Beanstalk is the simplest solution here, it's just about
    creating a new app/env with autoscaling enabled and properly configured;
    this may require a bit of fiddling with the values the trigger the
    autoscaling mechanism, together with a tool that can simulate virtual users.
 - Database tier: database can easily become the single point of failure
    for scalability, but we can start with a non-trivial RDS MySQL/Aurora instance then
    proceed from there by scaling vertically (resizing the instance), scaling
    horizontally (adding read-only replicas), or switching to a more scalable database
    (e.g. DynamoDB, or Cassandra, depending on the overall purpose of the API).
    As an afterthought, actually DynamoDB may be ideal if the API remains quite
    simple like it is now.
 - Caching: caching responses and/or database objects in the web tier (maybe
    using memcached) can do wonders but it depends more on the read/write ratio
    of the app: in this case, being related to comments, reads should be much more
    then writes so a cache could be very helpful here.
 - Decoupling services: since we don't have any control on the external service
    that provides the tone analysis, we must assume we need to decouple the call
    to this service from the API call that actually creates a new comment instance.
    Clearly having the service call our API back would be awesome, but lacking that,
    we can think to a traditional queuing paradigm (implemented using e.g. `rq` or
    AWS SQS), or even better a serverless solution which is much easier to
    implement on e.g. AWS Lambda service. To complete the loop, this decoupled
    element of the architecture should call back the API when done to update
    the `tone` field of the corresponding SKU. This makes a things a bit more
    complicated when developing as the API dev environment should be reachable
    through the Internet if local. (TODO Add code)

In this way, every tier of the solution can scale and be tuned for scalability
independently from each other while the API usage grows. This translates in
simplicity and effectiveness of a product that can grow with the business in
a lean way.

Another completely different take would have been using something like
AWS API Gateway + Lamdba which can guarantee a scalability but using a
completely different toolset.

### Other Architectural Aspects

#### Deployment

If we adopt AWS Beanstalk it's very easy from the command line, just running
`eb deploy`. In combination with extensions, it's possible to configure completely
an environment.
See http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html.

TODO More in general I would like to try with e.g. ansible or AWS CodeDeploy.

#### Monitoring

Monitoring your app is always a fundamental aspect of its life since you cannot
decide if you don't measure.

Using AWS console may be enough for monitoring, but using dedicated dashboard
software can be really much more effective. For example I recently used
https://grafana.com/ just mirroring counters coming out from CloudWatch.

The experience is entirely different since you can group together all the
counters that matter to your app/role, enabling easy and quick discovery of issues
and/or adding an information radiator to your organisation/team.

#### Logging

Django supports logging (I've added an example call) with full
configurability https://docs.djangoproject.com/en/1.11/topics/logging/.

An very useful option here is configuring it to send the logs in a central
location like AWS CloudWatch, as it makes very simple and immediate to search
for anything in logs coming from a potentially high number of machines.


### Client Libraries and Examples

I think that auto-generating client libraries could be a good idea because it
brings efficiency, uniformity and hopefully more quality.

Anyway I've written and included also a python client developed manually with
`requests` library.

I've written a Java client with Retrofit http://square.github.io/retrofit/
because I wanted to try it: at this level of complexity is not
worth using it, but client code looks natural and simple.

TODO Add a Java client implemented at a lower-level e.g. with
http://square.github.io/okhttp/.

Clients for some languagues are immediately available thanks to
http://www.coreapi.org/.

See http://www.django-rest-framework.org/topics/api-clients/.

See `clients` folder here in the repo.

Python and Javascript clients are trivial with coreapi.

Run the browser test with e.g. `python -m SimpleHTTPServer 8001` after changing
dir in the folder.
A CORS issue with the browser resolved trivially by installing an extension.

TODO node.js coreapi sadly not working right now.

To generate a client with Swagger, install Swagger Codegen then run e.g. for PHP:

`swagger-codegen generate -i http://127.0.0.1:8000/swagger/v2/swagger.json?format=openapi -l php -o ./php/ -a "Authorization:Basic YWRtaW46YWRtaW4wMDE="`

See https://swagger.io/swagger-codegen/.
See https://stackoverflow.com/a/42137322/384336 for authorization encoding.

I've included Swagger PHP client and example in this repo for completeness.

Turns out API schema generation is a bit buggy so clients must be manually
patched for now, see https://github.com/marcgibbons/django-rest-swagger/issues/595.
