from django.shortcuts import render
import json
import requests

def generate_image_from_text(text):
    api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZmU4ZGM4MjUtMTU1ZS00YzUwLWJhYmItNTQ0Zjk5MWI1M2YwIiwidHlwZSI6ImFwaV90b2tlbiJ9.19V0juJi9RJBewzdDcD6CIvISos1YY3kWaKCGKCw2V0'
    url = 'https://api.edenai.run/v2/image/generation'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        "providers": "openai/dall-e-3",
        "text": text,
        "resolution": "1024x1024",
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        try:
            print("Full API response:", result)
            image_url = result['openai/dall-e-3']['items'][0]['image_resource_url']
            print("Image URL:", image_url)
            return image_url
        except KeyError as e:
            print(f"KeyError: {e}")
            return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


def image_generation_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        image_url = generate_image_from_text(text)
        if image_url:
            return render(request, 'result.html', {'image_url': image_url})
        else:
            return render(request, 'form.html', {'error': 'No image URL found. Please try again.'})
    return render(request, 'form.html')