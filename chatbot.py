from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the pre-trained model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []

def to_talk(input_text):
    """
    Process the input text and generate a response.
    
    Args:
        input_text (str): The input text from the user.
    
    Returns:
        str: The response generated by the chatbot.
    """
    # Combine the conversation history into a single string
    history_string = "\n".join(conversation_history)
    # Encode the input text and conversation history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    # Generate a response using the model
    outputs = model.generate(**inputs)
    # Decode the generated response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    # Update the conversation history with the input text and response
    conversation_history.append(input_text)
    conversation_history.append(response)
    return response
