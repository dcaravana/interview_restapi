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


## Test Execution



- interesting opportunity to study python a bit more
- actually use python conventions
- python 2 vs 3
- packaging
- virtualenv
- framework: django, flask, ???
- local (dev) mode
- scalable mode: AWS, database, SQS
- trying djangorestframework

### djangorestframework

Just followed

- https://github.com/encode/django-rest-framework#example
- http://www.django-rest-framework.org/tutorial/quickstart/

Created an API in no time.

For now it's just `/comments` but it may be also `/sku/XXX/commments`.

TODO return a single meaningful result as requested.

Documentation is cool TODO complete endpoints descriptions http://www.django-rest-framework.org/topics/documenting-your-api/

API clients automatically generated for some languages http://www.django-rest-framework.org/topics/api-clients/

Learned that ViewSet are just like Controllers in MVC so the right place
were to implement initial non-scalable call to sentiment analysis. See 
http://www.django-rest-framework.org/api-guide/viewsets/

After resurrecting my IBM account, I can use the tone service again with
the Watson SDK for python https://github.com/watson-developer-cloud/python-sdk

Used ENV vars and `local_settings.py` to set credentials (first can be useful
  in e.g. AWS Beanstalk).

After a bit of wandering around, I've found an ideal way to add behaviour to
models through signals (`pre_save` in this case), which is great so there is 
no need to alter the default View and to keep the logic together with the
corresponding model (in this case `Comment` and the call to tone analyser).

Adding tests as of here http://www.django-rest-framework.org/api-guide/testing/
Created tests for models and API.
TODO complete.

Scalability: making scalable this kind of application is about delivering it on
the right infrastructure. I'm going to consider AWS but any other cloud provider 
would probably do well.

 - web tier: AWS Beanstalk is the simplest solution here, it's just about 
    creating a new app/env with autoscaling enabled and properly configured
 - database tier: database can easily become the single point of failure even
    for scalability, but we can start with a non-trivial RDS MySQL/Aurora instance then
    start from there by scaling vertically (resizing the instance), scaling
    horizontally (adding read-only replicas), switching to a more scalable database
    (e.g. DynamoDB, or Cassandra, depending on the overall purpose of the API).
    As an afterthought, actually DynamoDB may be ideal if the API remains quite
    simple.
 - caching: caching responses and/or database objects in the web tier (maybe
    using memcached) can do wonders but it depends more on the read/write ratio
    of the app: in this case, being related to comments, reads should be much more
    then writes so a cache is helpful
 - decoupling services: since we don't have any control on the external service 
    that provides the tone analysis, we must assume we need to decouple the call
    to this service from the API call that actually creates a new comment instance.
    Clearly having the service call our API back would be awesome, but lacking that,
    we can think to a traditional queue paradigm (implemented using `rq` or 
    AWS SQS), or even better a serverless solution which is much easier to
    implement on e.g. AWS Lambda service. (TODO code)
    
So basically every tier of the solution can scale and be scaled independently
while the API usage grows, which translates in simplicity and effectiveness of
a product that can grow with the business.
Another completely different take would have implied using AWS API Gateway + Lamdba.

CI: leverage github and related services? not done yet, but started with CI in
2004, and more recently used Jenkins.

Deployment: if we adopt AWS Beanstalk it's very easy from the command line 
`eb deploy` in combination with extensions http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html
More in general with e.g. ansible.

Monitoring: using AWS console may be enough, but using dedicated dashboard
software can be really much more effective. For example I recently used 
https://grafana.com/ just mirroring counters coming out from CloudWatch.
The experience is entirely different since you can group together all the 
counters that matter to your app/role, enabling easy and quick discovery of issues
and/or adding an information radiator to your organisation/team.
