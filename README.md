## Test Description


Write a simple Restful API that takes and stores comments identified by an SKU.

The API should have a way in which the comment has been analysed to tell us whether the
comment is positive or not. To do this, you'll use the Watson Tone Analyser for emotional tone.
https://watson-api-explorer.mybluemix.net/apis/tone-analyzer-v3#!/tone/GetTone

The test isn't about Watson, but it makes the problem a little more interesting.

The code will need to scale, tell me about how it'll be deployed and built to achieve this.

The code must be restful, tell me what makes your API restful.

Your code should be well structured, what approach have you taken, and how would you
explain it to another developer?

The API must be documented. How have you documented your API?

Lastly, any core development approaches should be evident in code.

I would also like client examples of it working. Acceptable languages for the test are Python, Java, PHP.


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
