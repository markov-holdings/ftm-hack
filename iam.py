import boto3
import json
import sys
import time
from botocore.config import Config
 
config = {
    # "aws_lambda_function_name": "roxie",
    "aws_region": "us-west-2",
    "aws_lex_bot_name": "matt-try",
    "aws_lex_role_arn": "arn:aws:iam::291406351574:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots",
    # "aws_lambda_environment_var_1": "10.8.107.34",
    # "aws_lambda_environment_var_2": "BIG_LONG_AUTH_TOKEN"
}
 
from botocore.config import Config
boto_config = Config(
    region_name = config['aws_region']
)
         
lex = boto3.client('lexv2-models', config=boto_config)
# lmda = boto3.client('lambda', config=boto_config)
 
print("Creating Bot")
response = lex.create_bot(
    botName=config['aws_lex_bot_name'],
    description="Roxie, Rubrik's intelligent personal assistant",
    dataPrivacy={
        'childDirected': False
    },
    idleSessionTTLInSeconds=300,
    roleArn = config['aws_lex_role_arn']
)
aws_lex_bot_id =  response["botId"]
 
print("Waiting for bot to be created...")
response = lex.describe_bot(
    botId=aws_lex_bot_id
)
bot_status = response['botStatus']
while bot_status != "Available":
    print("Bot status is "+ bot_status)
    time.sleep(2)
    response = lex.describe_bot(
        botId=aws_lex_bot_id
    )
    bot_status = response['botStatus']
response = lex.describe_bot(
    botId=aws_lex_bot_id
)
print ("Bot created...")
 
print("Creating en_US Bot Locale")
response = lex.create_bot_locale(
    botId=aws_lex_bot_id,
    botVersion = "DRAFT",
    localeId = "en_US",
    nluIntentConfidenceThreshold=0.40,
    voiceSettings={
        'voiceId': 'Ivy'
    }
)
 
response = lex.describe_bot_locale(
    botId = aws_lex_bot_id,
    botVersion = "DRAFT",
    localeId = "en_US"
)
locale_status = response['botLocaleStatus']
while locale_status != 'NotBuilt':
    print ("Bot Locale Status is " + locale_status)
    time.sleep(2)
    response = lex.describe_bot_locale(
        botId = aws_lex_bot_id,
        botVersion = "DRAFT",
        localeId = "en_US"
    )
    locale_status = response['botLocaleStatus']
print("Bot Locale en_US created!")
 
print("Creating Intents...")
with open('intents.json') as f:
    data = json.load(f)
 
for intent in data['Intents']:
    aws_lex_intent_utterances = intent['utterances']
    aws_lex_intent_name = intent['name']
    aws_lex_intent_description = intent['description']
    response = lex.create_intent(
        intentName=aws_lex_intent_name,
        description=aws_lex_intent_description,
        sampleUtterances=aws_lex_intent_utterances,
        fulfillmentCodeHook={
            'enabled': True
        },
        botId = aws_lex_bot_id,
        localeId="en_US",
        botVersion="DRAFT",
    )
print("Done adding intents!")
 
# print("Attaching Lex bot to Lambda function")
# response = lex.list_bot_aliases(
#     botId = aws_lex_bot_id
# )
# aws_lex_bot_alias_id = response['botAliasSummaries'][0]['botAliasId']
# aws_lex_bot_alias_name = response['botAliasSummaries'][0]['botAliasName']
 
# # Get lambda Arn
# response = lmda.get_function(
#     FunctionName=config['aws_lambda_function_name']
# )
# aws_lambda_function_arn = response['Configuration']['FunctionArn']
# # Update alias w/ Lambda
# response = lex.update_bot_alias(
#     botAliasId = aws_lex_bot_alias_id,
#     botAliasName = "TestBotAlias",
#     botVersion = "DRAFT",
#     botAliasLocaleSettings={
#         "en_US": {
#             "enabled": True,
#             "codeHookSpecification": {
#                 "lambdaCodeHook": {
#                     "lambdaARN": aws_lambda_function_arn,
#                     'codeHookInterfaceVersion': "1.0"
#                 }
#             }
#         }
#     },
#     botId = aws_lex_bot_id
# )
# print("Done attaching Lex to Lambda")
 
# print("Adding permission for Lex to call Lambda function")
# aws_account_id = boto3.client('sts').get_caller_identity().get('Account')
# aws_lex_bot_arn = "arn:aws:lex:{0}:{1}:bot-alias/{2}/{3}".format(config['aws_region'], aws_account_id,aws_lex_bot_id,aws_lex_bot_alias_id)
 
# response = lmda.add_permission(
#     FunctionName=config['aws_lambda_function_name'],
#     StatementId="AllowLexBot-"+config['aws_lex_bot_name']+"-AccessToLambdaFunction-"+config['aws_lambda_function_name'],
#     Action="lambda:InvokeFunction",
#     Principal="lexv2.amazonaws.com",
#     SourceArn=aws_lex_bot_arn
# )
# print("Done with permissions")
 
# print("Beginning initial build of bot")
# response = lex.build_bot_locale(
#     botId=aws_lex_bot_id,
#     botVersion="DRAFT",
#     localeId="en_US"
# )
# print("Build has began on bot.")