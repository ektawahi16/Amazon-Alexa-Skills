def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "healthtips":
        return brain_teaser(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello! Namaste!"
    speechOutput =  "Hello, Welcome to all about health, " \
                    "You can ask me by saying give me some health tips,Thankyou"
    repromptText =  "You can ask me by saying give me some health tips"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def brain_teaser(intent, session):
    import random
    index = random.randint(0,len(brainteaser)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = brainteaser[index] 
    repromptText = "You can ask me workout by saying give me some health tips"
    shouldEndSession = True                    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using these healthy tips" \
                    "Have a great day , see you! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



brainteaser = [ "an apple a day keeps a doctor away" ,
                "Broccoli contains twice the vitamin C of an orange." ,
                "Avocado has highest protein content of all fruit" ,
                "Regular physical activity is important for the healthy growth, development and well-being of kids and teens." ,
                "They should get at least 60 minutes of physical activity every day, including vigorous activities that make them ‘huff and puff’ ",
                "Reduced fat milk for children over two years of age is a nutritious drink and a great source of calcium.",
                "Lemons contain more sugar than strawberries" ,
                "Ginger can reduce exercise-induced muscle pain by 25%",
                "Eating fruit and vegetables every day helps kids and teens grow and develop, boosts their vitality and can reduce the risk of many chronic diseases." ,
                "have fresh fruit available as a convenient snack and try to include fruit and vegies in every meal" ,
                "Aim to eat two serves of fruit and five serves of vegetables every day. (This varies for boys and girls at different ages.)" ,
                "Kids and teens should spend no more than 2 hours a day on ‘small screen’ entertainment." ,
                "Healthy snacks help kids and teens meet their daily nutritional needs.",
                "Snacks based on fruit and vegetables, reduced fat dairy products and whole grains are the healthiest choices. " ,
                "Water is the best way to quench your thirst – and it doesn’t come with the added sugar found in soft drinks, fruit juice drinks and other sweetened drinks." ,
                "Sedentary or ‘still’ time spent watching TV, surfing online or playing computer games is linked to kids becoming overweight or obese.",
                "Prioritize good sleep" ,
                "avoid drinking alcohol and smoking." ,
                "get lots of sleep and get regular exercise" ,
                "Set a regular sleep schedule, Don't count on weekend catch-up sleep, Don't ignore chronic sleep problems."
                ]
