#!/bin/bash
heroku apps:destroy visionbotai2
heroku create visionbotai2 #create a new app 
git init
heroku git:remote -a visionbotai2
git add .
git commit -am "make it better"
git push heroku master
heroku config:set GOOGLE_APPLICATION_CREDENTIALS='/app/gservice.json'
heroku config:set shared_room_id='Y2lzY29zcGFyazovL3VzL1JPT00vNGQ0Yzg2YjAtNWQyNy0xMWVhLWE5OGQtMWY1MWU3NzdkOGRm'
heroku config:set WEBEX_TEAMS_ACCESS_TOKEN='MzMwYjYwZmEtYjE0MS00N2NkLTgyOTEtODkxMDFlMDVlNDgxMTk3NjYxMmUtNWQx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
heroku ps:scale web=1
heroku logs -t # display logs