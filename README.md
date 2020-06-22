### Story one 

```text
Story one took long. I tried to model the database based on the information I had. I am still not sure if the database 
I modelled is accurate. I then dockerised the app and using docker-compose to run the services together. Wrote the test cases
to check the config and planning to use monkeypatching for the remaining ones.

I configured the setup.cfg basically asking the Flake8 to stick to some rules and coveragerc to omit the app/tests folder
and set the branching to true to check if the conditions in the if/else is correct.

I wrote unit tests for the configuration and a test for the endpoint to make sure the project is working. Which is a test api


I declared a method which is calc test and it returns nothing
```

### Story 2 
```text
In the story 2 I declared BookType as an enum along with its respected book price and seeded the database.
```
### Story 3
```text
I basically wrote the logic for the calculator. And created the Dockerfile and deployed it on Heroku.
```

If I was to scale the app I will use celery for the asynchronous task and let the calculations happen. 
Secondly, I would not have one database for all the services and probably would have focused more on microservices architecture
and use rabbit mq or any other event queue to exchange events. 
Also, 