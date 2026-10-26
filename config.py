''' Bot Config: '''
# Bot Name, will show up in the chat header
BOT_NAME = "Assistant"                         

# First Message a User sees when using the chatbot
GREETING = "Hi! Ask me anything about this site."   

''' Retrieval Config: '''
# Number of Chunks retrieved by the RAG Algorithm
# which will be sent to the LLM per query
# 3 to 5 is used usually
# Going above this range makes it slower and costlier without a significant rise in accuracy
# Going below this range kills accuracy though making it extremely fast and cheap
TOP_K = 4      

# Tokens per chunk, Reduce it to increase precision
CHUNK_SIZE = 400    

# Tokens shared between neighbouring chunks to keep context
OVERLAP = 50           

# DONE