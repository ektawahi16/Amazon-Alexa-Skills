/* eslint-disable  func-names */
/* eslint-disable  no-console */

const Alexa = require('ask-sdk');

const GetNewFactHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'LaunchRequest'
      || (request.type === 'IntentRequest'
        && request.intent.name === 'GetNewFactIntent');
  },
  handle(handlerInput) {
    const factArr = data;
    const factIndex = Math.floor(Math.random() * factArr.length);
    const randomFact = factArr[factIndex];
    const speechOutput = GET_FACT_MESSAGE + randomFact;

    return handlerInput.responseBuilder
      .speak(speechOutput)
      .withSimpleCard(SKILL_NAME, randomFact)
      .getResponse();
  },
};

const HelpHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'IntentRequest'
      && request.intent.name === 'AMAZON.HelpIntent';
  },
  handle(handlerInput) {
    return handlerInput.responseBuilder
      .speak(HELP_MESSAGE)
      .reprompt(HELP_REPROMPT)
      .getResponse();
  },
};

const ExitHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'IntentRequest'
      && (request.intent.name === 'AMAZON.CancelIntent'
        || request.intent.name === 'AMAZON.StopIntent');
  },
  handle(handlerInput) {
    return handlerInput.responseBuilder
      .speak(STOP_MESSAGE)
      .getResponse();
  },
};

const SessionEndedRequestHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'SessionEndedRequest';
  },
  handle(handlerInput) {
    console.log(`Session ended with reason: ${handlerInput.requestEnvelope.request.reason}`);

    return handlerInput.responseBuilder.getResponse();
  },
};

const ErrorHandler = {
  canHandle() {
    return true;
  },
  handle(handlerInput, error) {
    console.log(`Error handled: ${error.message}`);

    return handlerInput.responseBuilder
      .speak('Sorry, an error occurred.')
      .reprompt('Sorry, an error occurred.')
      .getResponse();
  },
};

const SKILL_NAME = 'Marine Facts';
const GET_FACT_MESSAGE = 'Here\'s your marine fact: ';
const HELP_MESSAGE = 'You can say tell me a marine fact, or, you can say exit... What can I help you with?';
const HELP_REPROMPT = 'What can I help you with?';
const STOP_MESSAGE = 'Goodbye!';

const data = [
'Jellyfish Are 95% Water',
'Seahorses Have No Stomach',
'Clownfish Can Change Gender',
'Dolphins Rest Half of Their Brain at One Time',
'Sea Turtles “Cry” Salt',
'Jellyfish have been around for more than 650 million years, which means that they outdate both dinosaurs and sharks.',
'An Electric Eel is known to produce electricity sufficient enough to light up to 10 electric bulbs',
'At 188 decibels, the calls of blue whales is the loudest sound made by any animal on the planet.',
'Oysters can change from one gender to another and back again depending on which is best for mating.',
'Seahorses are the only animals in which the male, not the female, gives birth and care for their young.',
'A shrimps heart is in their head.',
'Sea sponges have no head, mouth, eyes, feelers, bones, heart, lungs, or brain, yet they are alive.',
'Turtles live on every continent except Antarctica.',
'Many fish are sequential hermaphrodites which are born as females and become male later on', 
'Clownfish are all male except the largest one which becomes a female',
'Parrot fish produce 85% of the sand that builds up reef islands like in the Maledives',
'Moray eels are not aggressive when they open and close their mouth, they are actually just breathing',
'Mimic octopus can imitated flounder, jelly fish, sting ray, sea snake, lionfish or just a rock/coral',
'Whales make the loudest sounds underwater with 188 dBs, the whistle can travel up to 500 miles',
];

const skillBuilder = Alexa.SkillBuilders.standard();

exports.handler = skillBuilder
  .addRequestHandlers(
    GetNewFactHandler,
    HelpHandler,
    ExitHandler,
    SessionEndedRequestHandler
  )
  .addErrorHandlers(ErrorHandler)
  .lambda();
