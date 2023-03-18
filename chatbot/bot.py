import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


class CreateBot:
    def __init__(self, system_prompt):
        self.system = system_prompt
        self.messages = [{'role': 'system', 'content': system_prompt}]

    def chat(self):
        print('to terminate type END')
        question = ''

        while question != "END":
            question = input("")
            print('\n')
            self.messages.append({'role': 'user', 'content': question})
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=self.messages
            )
            content = response['choices'][0]['message']['content']
            print('\n')
            print(content)
            print('\n')
            self.messages.append({'role': 'assistant', 'content': content})


eng = CreateBot(system_prompt='you are an engineer')
eng.chat()
