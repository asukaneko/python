import openai
openai.api_key = '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'

response = openai.Completion.create(
  model='text-davinci-003',
  prompt='你好',#内容
  temperature=0.3,
  max_tokens=800,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

print(response.choices[0].text)