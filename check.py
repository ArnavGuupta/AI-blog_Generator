import together

# Initialize client with API key manually
client = together.Together(api_key="afca9f0c32da0aea06e032084fc471d96cc1adbdefa5df8a975101d7604d37e1")

# List available models
print(client.models.list())


