     client = openai.api_key = 'sk-2494c820a9dd448e868ec9973d3c2bb3'
        openai.base_url = "https://api.deepseek.com"

        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
        {"role": "user", "content": "How do I list all files in a directory using Python?"},
    ],
)

        print(completion.choices[0].message.content)