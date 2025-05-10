def w_context_user_prompt(question, context):
    return f'Context: "{context}" Question: "{question}"'

def w_context_system_prompt():
    return 'You are a helpful assistant. Provide extremely short and factually correct answers based only on the given context. Limit your answer to just a few words. Avoid explanations or additional details.'

def wo_context_system_prompt():
    return 'You are a helpful assistant. Provide extremely short and factual answers. Limit your answer to just a few words. Respond with just the key fact, name, date, or relevant information in no more than a few words. Avoid any explanations, context, or additional details.'