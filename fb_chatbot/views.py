    #!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, requests, random, re
from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

PAGE_ACCESS_TOKEN = 'EAAP4kUPM8oQBALU0LzGDXu8IETF9ALwohbpKJ5gZAXnnQDq8uV1fsiP1mQ6t8wGv8LAGyk06K2pZCzQfAGSUHiltl6GZBN5hEACFHXCN5yoEIgpf8ybJZCo5cEgKuVcIeZBxTyPMJz07s5zR3LxcT13Uh6gCekl43ezEPcOmtVQZDZD'
VERIFY_TOKEN = '8447789934m'


def post_facebook_message(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN

    if recevied_message.startswith('/machineid'):
        response_msg1 = json.dumps(
                {
                  "recipient":{
                    "id":fbid
                  },
                  "message":{
                      "attachment":{
                        "type":"template",
                        "payload":{
                          "template_type":"button",
                          "text":"Thanks, the current address we have is ... Is this address correct ?",
                          "buttons":[
                            {
                              "type":"postback",
                              "title":"yes",
                              "payload":"ADDRESS_YES"
                            },
                            {
                              "type":"postback",
                              "title":"no",
                              "payload":"ADDRESS_NO"
                            }
                          ]
                        }
                      }
                    }
                }
            )
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg1)
        return

    if recevied_message.startswith('/address'):
        response_text = 'Thanks, we have updated your address and logged a ticket, someone will be ther shortly.'
        response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":response_text}})
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
        return

    response_msg5 = json.dumps(
            {
              "recipient":{
                "id":fbid
              },
              "message":{
                  "attachment":{
                    "type":"template",
                    "payload":{
                      "template_type":"button",
                      "text":"Hi user, how may I help you today ?",
                      "buttons":[
                        {
                          "type":"postback",
                          "title":"POS problem",
                          "payload":"NOT_ACCEPTING"
                        },
                        {
                          "type":"postback",
                          "title":"ticket status",
                          "payload":"TICKET_STATUS"
                        }
                      ]
                    }
                  }
                }
            }
        )

    #status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg3)
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg5)
    return

def render_postback(fbid,payload):
  post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
  print '%s\n%s\n%s'%('&'*20,payload,'&'*20)
  
  if payload == 'NOT_ACCEPTING':
      response_text = 'I am sorry for that. Please share your maching ID as follows: /machineid 123********'
  if payload == 'TICKET_STATUS':
      response_text = 'Your request is being worked on, and someone will reach out to you very shortly.'
  if payload == 'ADDRESS_YES':
      response_text = 'We have logged a ticket, someone will be there soon.'
  if payload == 'ADDRESS_NO':
      response_text = 'Please enter new address as follows: /address <your address>'

  try:
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":response_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
  except Exception as e:
    print 'POSTBACK-ERROR:%s\n%s\n%s'%('%'*20,e,'%'*20)

class MyQuoteBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']: 
                if 'postback' in message:
                    print '%s\n%s\n%s'%('$'*20,message,'$'*20)
                    render_postback(message['sender']['id'],message['postback']['payload'])

                if 'message' in message:
                    print '%s\n%s\n%s'%('*'*20,message,'*'*20)
                    try:  
                        post_facebook_message(message['sender']['id'], message['message']['text'])
                    except Exception as e:
                        print '%s\n%s\n%s'%('%'*20,e,'%'*20)
                        post_facebook_message(message['sender']['id'], 'Please send a valid text for emoji search.')


        return HttpResponse()    



def index(request):
    search_string = request.GET.get("text")
    return HttpResponse(text)



