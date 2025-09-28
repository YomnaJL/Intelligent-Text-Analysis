import os
from openai import OpenAI

def process_text(text: str, lang_choice: str, task: str) -> str:
    """
    Traite le texte en utilisant l'API NVIDIA.
    Cette fonction contient toute la logique métier.
    """
    api_key = os.getenv("NVIDIA_API_KEY")
    if not api_key:
        return "❌ Erreur de configuration : La clé API NVIDIA_API_KEY n'est pas définie."

    try:
        client = OpenAI(
          base_url = "https://integrate.api.nvidia.com/v1",
          api_key = api_key
        )
    except Exception as e:
        return f"Erreur de configuration du client API : {e}"

    lang_map = {"en": "English", "fr": "French", "ar": "Arabic"}
    target_lang = lang_map.get(lang_choice, "French")

    system_prompt = "You are a helpful assistant. Always reply in the requested language. Your responses should be direct and concise."

    prompts = {
        'translate': f"Translate the following text into {target_lang}. Only provide the translated text as a response, without any introductory phrases:\n{text}",
        'summary': f"Summarize the following text in {target_lang}:\n{text}",
        'keywords': f"Extract 3 to 5 keywords from this text in {target_lang}:\n{text}",
        'category': f"Classify this text into a topic category in {target_lang}:\n{text}",
        'simplify': f"Rewrite this text in a simple and accessible language in {target_lang}:\n{text}",
        'facts':    f"Extract factual information (dates, numbers, names) from this text in {target_lang}:\n{text}",
        'title':    f"Generate a short, informative title for this text in {target_lang}:\n{text}",
        'sentiment': f"Analyze the sentiment of this text in {target_lang} (positive, negative, neutral):\n{text}",
        'question_generation': f"Generate 3 relevant quiz questions and answers from this text in {target_lang}:\n{text}",
        'grammar_correction': f"Correct grammar and spelling errors in this text. Provide only the corrected text in {target_lang}:\n{text}",
        'text_completion': f"Complete the following text naturally in {target_lang}:\n{text}",
        'code_generation': f"Generate a code snippet based on this description. Provide only the code block:\n{text}"
    }

    user_prompt = prompts.get(task, prompts['summary'])
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]

    try:
        completion = client.chat.completions.create(
          model="meta/llama-3.1-70b-instruct",
          messages=messages,
          temperature=0.2, top_p=0.7, max_tokens=1024, stream=False
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Erreur lors de l'appel à l'API NVIDIA : {e}"