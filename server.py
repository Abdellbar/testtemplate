#!/usr/bin/python

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from flask import Flask,request
import flask
import json
from sparkapi import Sparkapi
import os
import vision_core 
import logging
import sys
from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI()
app = Flask(__name__)
sparkbot = Sparkapi(os.environ['WEBEX_TEAMS_ACCESS_TOKEN'])
sharedroomid = os.environ['shared_room_id']

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(logging.INFO)


@app.route('/webhook',methods=['POST'])
def webhook():
    app.logger.info('New reqest ---------------------------------')

    data = request.json
    msg_id = data['data']['id']
    roomId = data['data']['roomId']

    app.logger.info('reqester : %s',data['data']['personEmail'])
    app.logger.info('message id : %s',msg_id)
    app.logger.info('room id : %s',roomId)

    message_json = sparkbot.get_msg(str(msg_id))


    if 'webex.bot' in data['data']['personEmail']:# =='abdelbbot@sparkbot.io': #check if message is coming from the bot
      return "OK"
    else: #if "SHOW" in (message_json['text']).upper():
        i=0
        for file in message_json['files']:
            
            #read the pitcure and save it to file
            image_file = sparkbot.get_file(file)
            image_name = str(msg_id)+'.JPG'
            open(image_name, 'wb').write(image_file.content) 

            #Call ai to do analyses
            results = vision_core.face_joy_joy_likelihood(image_name)

            #how many faces in the picture
            faces_n=len(results['faces'])
            likelihood_name = ('UNKNOWN', 'VERY UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY LIKELY')
            if faces_n>=1:
                i=i+1
                analyses="### Image: "+str(i)+ "\n"
                analyses=analyses+"#### Detected faces : "+str(faces_n)+ "\n"
                for face in results['faces']:
                    analyses=analyses+"--- \n"
                    is_emotions=False
                    if face['joy_likelihood']>=2:
                        analyses=analyses+"#### Joy likelihood               :"+str(likelihood_name[face['joy_likelihood']])+ "\n"
                        is_emotions=True
                    if face['sorrow_likelihood']>=2:
                        analyses=analyses+"#### Sorrow likelihood            :"+str(likelihood_name[face['sorrow_likelihood']])+ "\n"
                        is_emotions=True
                    if face['anger_likelihood']>=2:
                        analyses=analyses+"#### Anger likelihood             :"+str(likelihood_name[face['anger_likelihood']])+ "\n"
                        is_emotions=True
                    if face['surprise_likelihood']>=2:
                        analyses=analyses+"#### Surprise likelihood          :"+str(likelihood_name[face['surprise_likelihood']])+ "\n"
                        is_emotions=True
                    if face['under_exposed_likelihood']>=2:
                        analyses=analyses+"#### Under exposed likelihood     :"+str(likelihood_name[face['under_exposed_likelihood']])+ "\n"
                        is_emotions=True
                    if face['blurred_likelihood']>=2:
                        analyses=analyses+"#### Blurred likelihood           :"+str(likelihood_name[face['blurred_likelihood']])+ "\n"
                        is_emotions=True
                    if face['headwear_likelihood']>=2:
                        analyses=analyses+"#### Headwear likelihood          :"+str(likelihood_name[face['headwear_likelihood']])+ "\n"
                        is_emotions=True
                    if is_emotions==False:
                        analyses=analyses+"#### Nothing detected !"
                    analyses=analyses+"#### Detection confidence         :"+str('{0:.0%}'.format(face['detection_confidence']))+ "\n"
                     
            else:
                analyses="## No faces detceted!"
            sparkbot.post_msg_markdown(str(roomId),analyses)
            
    app.logger.info('END of reqest ---------------------------------')        

    return 'OK'

@app.route('/signin')
def signin():
    usermail = request.args.get('email')
    print(usermail)
    #api.memberships.create(sharedroomid, personEmail=usermail)
    response = sparkbot.add_member_to_sapce(usermail,sharedroomid)
    return response.text.encode('utf8')

@app.route('/reset')
def reset():
    for webhook in api.webhooks.list():
        print(webhook.id)
        api.webhooks.delete(webhook.id)
    return 'ok'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)
