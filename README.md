# Sentimentor bot lab
In this lab, we will put togather a webexteams bot that can analyse your selfies and tell you how you feel in the photos, this prototype is using google mahine learning cloud for photo analyses, the bot code is hosted in heroku and almsot ready to be used, in this lab you will need to create a webhook for the bot to comunicate with webexteams and test it using webexteams app on the laptop or on your smart phone app.


![Wiring photo][flow]

[flow]:./flow.png "flow photo"

## Setup :

#### Webexteams Account :
If you dont have a webexteams account, you can create one for free here [Link](https://teams.webex.com/), once you have your webexteams account loging on the laptop or on your mobile to webexteams app.

#### Access the shared teams space:
For each laptope a bot has been created on the hosting servie heroku find the one for your laptop and assigne your email address used to create webexteams account:
* laptop1 : ```https://visionbotai1.herokuapp.com/signin?email=your@email.com```
* laptop2 : ```https://visionbotai2.herokuapp.com/signin?email=your@email.com```
* ...
![Wiring photo][email]

[email]:./email.png "sigin to the space"

Check if you got access to webexteams space 'DeveNet Sentimentor Bot Lab - Cisco connect Riyadh 2020' you should see somthing lik this when you open the webexteams app.

![Wiring photo][space]

[space]:./space.png "webxteams space"

#### Reset you heroku app:
before starting the lab, you need to reset your heorku app, you can do that by accessing the link provided for your laptop:
* laptop1 : https://visionbotai1.herokuapp.com/reset
* laptop2 : https://visionbotai2.herokuapp.com/reset
* ...
![Wiring photo][reset]

[reset]:./reset.png "reset heroku app"

## Set up the webhook :
The webhook is a reverse API call, that will tell our bot when a message has been posted in our shared space. 
to setup the webhook we need to loging to the webexteams developer portal, and create a webhook for our bot in this [Link](https://developer.webex.com/docs/api/v1/webhooks/create-a-webhook)
*  make sure to copy the api token of your bot in the Authorisation field  
	* laptop 1 token : ```NGIzMTc2YTMtMGU0Ny00ZjNjLTk5YzUtZjY4YzZlNWVjZDgwODc2NzA5MGYtMzAz_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f```
	* laptop 2 token : ```MzMwYjYwZmEtYjE0MS00N2NkLTgyOTEtODkxMDFlMDVlNDgxMTk3NjYxMmUtNWQx_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f```
*  copy the target url for your assigned for your laptop bot :
	* laptop 1 : ```https://visionbotai1.herokuapp.com/webhook```
	* laptop 2 : ```https://visionbotai2.herokuapp.com/webhook```
	* ...

![Wiring photo][webhook]

[webhook]:./webhook.png "set up webhook in portal"

Once done compare the results with the screen shot;
![Wiring photo][webhookreturn]

[webhookreturn]:./webhookreturn.png "webhookreturn"

## Test the sentimentor bot:
Now that you have setup the webhook for your bot succesfully, you can test it by sending a photo or a selfie and tagging the bot on the shared teams space 'DeveNet Sentimentor Bot Lab - Cisco connect Riyadh 2020' from the lapop or using you smartphone.

![Wiring photo][test]

[test]:./test.png "photo"





