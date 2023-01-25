# service layer for calling 3rd party API 

import boto3
import time
from botocore.config import Config


class LexFactoryService:
    def __init__(self, input: dict):
        self.input = input # dict from Chatbot model

        self.config = {
            "aws_region": "us-west-2",
            "aws_lex_bot_name": self.input["name"],
            "aws_lex_role_arn": "arn:aws:iam::117410643577:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots_E7271B1Z2V9",
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

        self.create_bot()
        time.sleep(2)

        self.create_locale()
        time.sleep(2)

        self.create_intents()
        time.sleep(2)

        return self

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
                    'enabled': False
                },
                botId = self.aws_bot_id,
                localeId="en_US",
                botVersion="DRAFT",
            )

            intent_id = response["intentId"]
            elicit_slot = None
            slot_priorities = []
            priority_rank = 0
            for slot in slots:
                slot_name = slot["name"]
                if elicit_slot == None:
                    elicit_slot = slot_name

                ## testing
                slot["options"] = ["small", "medium", "large"]
                ## end testing

                enum_options = slot["options"]
                resp = self.lex.create_slot_type(
                    botId = self.aws_bot_id,
                    localeId="en_US",
                    botVersion="DRAFT",
                    slotTypeName = slot_name,
                    slotTypeValues = [{"sampleValue": {'value': value} for value in enum_options}],   
                    valueSelectionSetting={
                        'resolutionStrategy': 'OriginalValue',
                    }
                )            

                slot_type_id = resp["slotTypeId"]

                resp = self.lex.create_slot(
                    botId = self.aws_bot_id,
                    localeId="en_US",
                    botVersion="DRAFT",
                    intentId=intent_id,
                    slotName=slot_name,
                    slotTypeId=slot_type_id,
                    valueElicitationSetting={ 
                        "slotConstraint": "Required",    
                        "promptSpecification": {
                            "maxRetries": 3,
                            "messageGroups": [
                                {"message": {"plainTextMessage": {"value": slot["content"]}}},
                            ],
                        },
                    },
                )

                slot_id = resp["slotId"]
                slot_priorities.append({"priority": priority_rank, "slotId": slot_id})

                self.lex.update_intent(
                    botId = self.aws_bot_id,
                    localeId="en_US",
                    botVersion="DRAFT",
                    intentName=name,
                    intentId=intent_id,
                    sampleUtterances=utterances,
                    initialResponseSetting={
                        "initialResponse": {"messageGroups": [{"message": {"plainTextMessage": {"value": "Sure, I can help with that."}}}]},
                        "nextStep": {
                            "dialogAction": {
                                "slotToElicit": elicit_slot,
                                "suppressNextMessage": False,
                                "type": "ElicitSlot"
                            },
                        }                                                                  
                    },
                    slotPriorities=slot_priorities
                )             
                
                priority_rank += 1   

        
        return self