from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pytube import YouTube
from django.conf import settings
import json
import os
import assemblyai as ai
from .models import BlogPost
import yt_dlp
import together

# Home Page
@login_required
def index(request):
    return render(request, "index.html")

# Generate Blog from YouTube Video
@csrf_exempt
def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            yt_link = data['link']
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data sent'}, status=400)


        # get yt title
        title = yt_title(yt_link)

        # get transcript
        transcription = get_transcription(yt_link)
        if not transcription:
            return JsonResponse({'error': " Failed to get transcript"}, status=500)


        # use OpenAI to generate the blog
        blog_content = generated_blog_from_transcription(transcription)
        if not blog_content:
            return JsonResponse({'error': " Failed to generate blog article"}, status=500)

        # save blog article to database
        new_blog_article = BlogPost.objects.create(
            user=request.user,
            youtube_title=title,
            youtube_link=yt_link,
            generated_content=blog_content,
        )
        new_blog_article.save()

        # return blog article as a response
        return JsonResponse({'content': blog_content})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Get YouTube Video Title
def yt_title(link):
    yt = YouTube(link)
    return yt

def download_audio(link):
    with yt_dlp.YoutubeDL({"format": "bestaudio", "outtmpl": "audio.webm"}) as ydl:
        ydl.download([link])

    if not os.path.exists("audio.webm"):
        raise FileNotFoundError("Audio file not found after download!")

    return "audio.webm"

# Transcribe Audio using AssemblyAI
def get_transcription(yt_link):
    ai.settings.api_key = "268e81bca6274d74be0d1bdf3cca35e9"
    audio_file = "audio.webm"  # Check if this file exists
    print("Checking audio file:", audio_file)

    if not os.path.exists(audio_file):
        print("Error: File not found!", audio_file)
        return "Error: Audio file not found."
    transcriber = ai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    return transcript


# Generate Blog using OpenAI
def generated_blog_from_transcription(transcription):
    together.api_key = "afca9f0c32da0aea06e032084fc471d96cc1adbdefa5df8a975101d7604d37e1"  # Replace with your free Together AI key

    prompt = f"Write a detailed and professional blog article based on the following transcript. Ensure it reads like a proper blog post and not like a video transcript:\n\n{transcription}\n\nArticle:"


    response = together.Complete.create(
    prompt=prompt,
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo-p",  # Use a valid model


    
)
    generated_content = response['choices'][0]['text'].strip()
    return generated_content

# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            error_message = "Invalid username or password"
            return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")

# User Signup
def user_signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repeatpassword = request.POST["repeatpassword"]

        if password == repeatpassword:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)
                return redirect("/")
            except:
                error_message = "Error creating account"
                return render(request, "signup.html", {"error_message": error_message})
        else:
            error_message = "Passwords do not match"
            return render(request, "signup.html", {"error_message": error_message})

    return render(request, "signup.html")

# User Logout
def user_logout(request):
    logout(request)
    return redirect("/")
