import openai

openai.api_key = "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"

while True:

  prompt = input("\nIntroduce una pregunta: ")

  if prompt == "exit":
    break

  completion = openai.Completion.create(engine     = "text-davinci-003",
                                        prompt     = prompt,
                                        max_tokens = 2048)

  print(completion.choices[0].text)