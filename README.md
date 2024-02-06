# Web Server Application
## External Endpoints
1. REST API to communicate with the [telemetry device](https://github.com/mugabwa/Dwear-Arduino) and fetch\
   the collected data periodically using celery sheduled tasks.
2. REST API endpoints to send data to the [mobile application](https://github.com/mugabwa/DamageWear) once\
   they are polled to send data. This data is send via https between\
   the mobile application and the web server.
## Main Functionality
- Collect and store data from the telemetric devices. Use the collected\
data to perform analysis and send the feedback to the mobile\
application upon request.

- Provide an admin interface for the user interacting and managing the\
  web application.
