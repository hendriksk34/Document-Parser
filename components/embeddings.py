import openai

class AdaEmbeddingGenerator:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_embedding(self, text: str):
        """
        Generate a vector embedding using OpenAI's ADA model.
        Args:
            text (str): The input text to generate embeddings for.
        Returns:
            list: Embedding vector.
        """
        response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
        return response['data'][0]['embedding']