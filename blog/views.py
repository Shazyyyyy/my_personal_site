from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import User, Skills, About, Accomplishments
from .forms import ContactMeForm

def index(request):
    # form = ContactMeForm()
    user = User.objects.get(id=1)
    user_skills = user.skills.all()
    about = About.objects.get(id=1)
    accomplishments = Accomplishments.objects.all()
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_message = f"Имя: {name}\n\nЭл.почта: {email}\n\nСообщение: {message}"
            print(f'{name} - {email} - {subject} - {message}')
            send_mail(subject, email_message, 'korvaloool1@yahoo.com', recipient_list=['korvaloool1@yahoo.com'], fail_silently=False)
            return redirect('index')
    else:
        form = ContactMeForm()

    context = {
        'user': user,
        'skills': user_skills,
        'info': about,
        'accomplishments': accomplishments,
        'form': form
    }

    return render(request, 'blog/index.html', context)




