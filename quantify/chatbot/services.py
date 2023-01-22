# service layer for calling 3rd party API 

import boto3
import json
import sys
import time
from botocore.config import Config


class LexFactoryService:
    def __init__(self, input: dict):
        self.input = input # dict from Chatbot model

        self.config = {
            "aws_region": "us-west-2",
            "aws_lex_bot_name": self.input["name"],
            "aws_lex_role_arn": "arn:aws:iam::291406351574:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots",
        }
 
        self.boto_config = Config(
            region_name = self.config['aws_region']
        )
        
        self.lex = boto3.client('lexv2-models', config=self.boto_config)
        self.aws_bot_id = None

    def get_aws_bot_id(self) -> str:
        if self.aws_bot_id == None:
            raise Exception("Bot not built yet")
        
        return str(self.aws_bot_id)

    def run(self) -> 'LexFactoryService':
        # TODO: change to event based await instead of time.sleep 

        self.aws_bot_id = str(12345) # for demo purposes
        return self
        
        '''
        self.create_bot()
        time.sleep(2)

        self.create_locale()
        time.sleep(2)

        self.create_intents()
        time.sleep(2)

        return self
        '''

    def create_bot(self) -> 'LexFactoryService':
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
    
    def create_locale(self) -> 'LexFactoryService':
        if self.aws_bot_id == None:
            raise Exception("Bot is not created yet!")
        else:
            response = self.lex.create_bot_locale(
                botId = self.aws_bot_id,
                botVersion = "DRAFT",
                localeId = "en_US",
                nluIntentConfidenceThreshold=0.40,
                voiceSettings={
                    'voiceId': 'Ivy'
                }
            )
        
        return self 
    
    def create_intents(self) -> 'LexFactoryService':
        for intent in self.input["chatbot_intents"]:
            name = intent["name"]
            description = intent["description"]
            utterances = intent["utterances"]
            slots = intent["slots"]
            
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