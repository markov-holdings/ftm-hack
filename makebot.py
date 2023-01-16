# Wrapper over AWS LexV2 API

import boto3
import json
import sys
import time
from botocore.config import Config


class LexFactory:
    def __init__(self, input):
        self.config = {
            "aws_region": "us-west-2",
            "aws_lex_bot_name": "florist-bot",
            "aws_lex_role_arn": "arn:aws:iam::291406351574:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots",
        }
 
        self.boto_config = Config(
            region_name = self.config['aws_region']
        )
        
        self.lex = boto3.client('lexv2-models', config=self.boto_config)
        self.input = input # json / dict from Chatbot Model
        self.aws_bot_id = None
    
    def create_bot(self):
        response = self.lex.create_bot(
            botName = self.config['aws_lex_bot_name'],
            description = self.input["description"],
            dataPrivacy={
                'childDirected': False
            },
            idleSessionTTLInSeconds=300,
            roleArn = self.config['aws_lex_role_arn'],
        )
        self.aws_bot_id = response["botId"]
        
        return self
    
    def create_locale(self):
        if self.aws_bot_id == None:
            raise Exception("Bot is not created yet!")
        else:
            response = self.lex.create_bot_locale(
                botId = self.aws_lex_bot_id,
                botVersion = "DRAFT",
                localeId = "en_US",
                nluIntentConfidenceThreshold=0.40,
                voiceSettings={
                    'voiceId': 'Ivy'
                }
            )
            return self 
    
    def create_intents(self):
        for intent in self.input["chatbot_intents"]:
            name = intent["name"]
            description = intent["description"]
            utterances = [d["content"] for d in intent["utterances"]]
            #slots = intent["slots"]
            
            response = self.lex.create_intent(
                intentName=name,
                description=description,
                sampleUtterances=utterances,
                fulfillmentCodeHook={
                    'enabled': True
                },
                botId = self.aws_bot_id,
                localeId="en_US",
                botVersion="DRAFT",
            )
        
        return self
 
if __name__ == "__main__":
    # sample api usage
    f = open('sample.json')
    data = json.load(f)
    f.close()
    
    factory = LexFactory(data)
    factory.create_bot().create_locale().create_intents()
    print("Bot created successfully")