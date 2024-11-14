import numpy as np

# Define the function that counts spam words in a message
def spam_word_count(message):
    # Define the spam-related keywords
    spam_keywords = [
        "win", "winner", "prize", "congratulations", "cash", "reward", "bonus", "award",
        "claim", "free", "won", "money", "lottery", "urgent", "offer", "exclusive", 
        "buy", "purchase", "discount", "save", "clearance", "deal", "bargain", "limited", 
        "cheap", "apply now", "subscribe", "voucher", "call now", "click", "reply", "final", 
        "guarantee", "important", "reminder", "limited time", "expire soon", "contact", 
        "phone", "sms", "text", "claim code", "PIN", "access code"
    ]
    
    # Convert message to lowercase to make the search case-insensitive
    message = message.lower()
    
    # Count occurrences of spam keywords in the message
    count = 0
    """ Code Logic 
    """
    for keyword in spam_keywords:
        if keyword in message:
            count +=1 

    return count

# Main program to classify SMS messages from a file
def classify_messages(file_path, threshold=2):
    actuals, predictions = [], []
    
    # read the file with SMS messages, as a list of SMS
    messages = []
    
    """Code Logic 
    """
    try :
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                
                if line:
                    parts = line.split(maxsplit=1)
                    
                    if len(parts) == 2:
                        label, msg = parts
                        messages.append((label, msg))
                    
        #print("Messages:", messages)
        #print("labels:", actuals)        
    except FileNotFoundError:
        print(f"Error : The File at {file_path} was not foud. ")
        
    except Exception as e:
        print(f"An error occured: {e}")
        
    
    # Loop through each message and classify based on spam word count
    for label,msg in messages:
        msg = msg.lower()

        # split the msg into actual classification and the SMS text
        # actual class is the first part before tab character, rest is SMS text      
        
        actual = True if label=='spam' else False
        actuals.append(actual)

        spam_count = spam_word_count(msg)
        spam = True if spam_count >= threshold else False
        predictions.append(spam)

    # compute accuracy as an integer between 0 and 100
    actuals, predictions = np.array(actuals), np.array(predictions)
    correct_predictions = np.sum(actuals == predictions)
    acc = (correct_predictions / len(actuals)) *100

    print(f"Accuracy: {acc:.2f} for threshold: {threshold}")
    return(acc)    