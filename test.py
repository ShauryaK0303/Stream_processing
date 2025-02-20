import gradio as gr
import numpy as np
from keras.models import load_model

# Load your Keras model
model = load_model(r"D:\JSHII\DIV\model_1.keras")
# Define the questions and their corresponding indices
questions = ["If one of us apologizes when our discussion deteriorates, the discussion ends.",
                  "I know we can ignore our differences, even if things get hard sometimes.",
                  "When we need it, we can take our discussions with my spouse from the beginning and correct it.",
                  "When I discuss with my spouse, to contact him will eventually work.",
                  "The time I spent with my wife is special for us.",
                  "We don't have time at home as partners.",
                  "We are like two strangers who share the same environment at home rather than family.",
                  "I enjoy our holidays with my wife.",
                  "I enjoy traveling with my wife.",
                  "Most of our goals are common to my spouse.",
                  "I think that one day in the future, when I look back, I see that my spouse and I have been in harmony with each other.",
                  "My spouse and I have similar values in terms of personal freedom.",
                  "My spouse and I have similar sense of entertainment.",
                  "Most of our goals for people (children, friends, etc.) are the same.",
                  "Our dreams with my spouse are similar and harmonious.",
                  "We're compatible with my spouse about what love should be.",
                  "We share the same views about being happy in our life with my spouse",
                  "My spouse and I have similar ideas about how marriage should be",
                  "My spouse and I have similar ideas about how roles should be in marriage",
                  "My spouse and I have similar values in trust.",
                  "I know exactly what my wife likes",
                  "I know how my spouse wants to be taken care of when she/he sick.",
                  "I know my spouse's favorite food.",
                  "I can tell you what kind of stress my spouse is facing in her/his life.",
                  "I have knowledge of my spouse's inner world.",
                  "I know my spouse's basic anxieties.",
                  "I know what my spouse's current sources of stress are.",
                  "I know my spouse's hopes and wishes.",
                  "I know my spouse very well.",
                  "I know my spouse's friends and their social relationships.",
                  "I feel aggressive when I argue with my spouse.",
                  "When discussing with my spouse, I usually use expressions such as ‘you always’ or ‘you never’.",
                  "I can use negative statements about my spouse's personality during our discussions.",
                  "I can use offensive expressions during our discussions.",
                  "I can insult my spouse during our discussions.",
                  "I can be humiliating when we discussions.",
                  "My discussion with my spouse is not calm.",
                  "Our discussions often occur suddenly.",
                  "I hate my spouse's way of open a subject.",
                  "We're just starting a discussion before I know what's going on.",
                  "When I talk to my spouse about something, my calm suddenly breaks.",
                  "When I argue with my spouse, ı only go out and I don't say a word.",
                  "I mostly stay silent to calm the environment a little bit.",
                  "Sometimes I think it's good for me to leave home for a while.",
                  "I'd rather stay silent than discuss with my spouse.",
                  "Even if I'm right in the discussion, I stay silent to hurt my spouse.",
                  "When I discuss with my spouse, I stay silent because I am afraid of not being able to control my anger.",
                  "I feel right in our discussions.",
                  "I have nothing to do with what I've been accused of.",
                  "I'm not actually the one who's guilty about what I'm accused of.",
                  "I'm not the one who's wrong about problems at home.",
                  "I wouldn't hesitate to tell my spouse about her/his inadequacy.",
                  "When I discuss, I remind my spouse of her/his inadequacy.",
                  "I'm not afraid to tell my spouse about her/his incompetence."
    # Add more questions here...
]

# Define the Gradio interface
inputs = []
for i, question in enumerate(questions):
    inputs.append(gr.CheckboxGroup([question], label=str(i)))

def divorce_predictor(*args):
    # Convert user responses to numerical values
    responses = [0 if not arg else arg[0] for arg in args]
    # Pass responses to the model and get the prediction
    prediction = np.mean(responses)  # For demonstration purposes, just averaging the responses
    return "High risk of divorce" if prediction > 2.5 else "Low risk of divorce"

output = gr.Textbox()

# Create the Gradio interface
gr.Interface(fn=divorce_predictor, inputs=inputs, outputs=output, title="Divorce Predictor").launch()

