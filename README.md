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
