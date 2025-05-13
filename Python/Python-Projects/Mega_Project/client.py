# # from openai import OpenAI
# # client = OpenAI(api_key="pk-jzXUzkRGfoGgBSohhbXrYoSpuazgJvUBlAfUGStgQXiemaky")

# # completion = client.chat.completions.create(
# #     model="gpt-3.5-turbo",
# #     messages=[
# #         {"role": "system", "content": "You are a helpful assistant."},
# #         {
# #             "role": "user",
# #             "content": "Write a haiku about recursion in programming."
# #         }
# #     ]
# # )

# # print(completion.choices[0].message.content)
# import openai

# openai.api_key = 'pk-AGUMDlQraXLZGKUgYaodcQuhDCQqocNKAtEULYgWRUtHQjrE'
# openai.base_url = "https://api.pawan.krd/v1/chat/completions"

# completion = openai.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content": "How do I list all files in a directory using Python?"},
#     ],
# )

# print(completion.choices[0].message.content)


# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-2494c820a9dd448e868ec9973d3c2bb3", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)


