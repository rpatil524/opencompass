from opencompass.models import OpenAISDKStreaming

api_meta_template = dict(round=[
    dict(role='HUMAN', api_role='HUMAN'),
    dict(role='BOT', api_role='BOT', generate=True),
], )

models = [
    dict(
        abbr='DeepSeek-R1-0528',
        type=OpenAISDKStreaming,
        path='deepseek-reasoner',
        key='',  # DeepSeek API key
        meta_template=api_meta_template,
        query_per_second=1,
        openai_api_base='https://api.deepseek.com/v1', # check https://api-docs.deepseek.com/ 
        batch_size=1,
        temperature=1,
        max_seq_len=163840,
        retry=10,
        stream=True,  # Enable streaming output
        verbose=True,  # Enable detailed logging to see real-time streaming output
        stream_chunk_size=1,  # Streaming chunk size
        ),
] 