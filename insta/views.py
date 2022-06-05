from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def login(request):
  return render(request, 'index.html')  

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      username = form.cleaned_date.get('username')
      email = form.cleaned_data.get('email')
      password = form.cleaned_date('password')
      User.objects.create_user(username=username,email=email,password=passsword)
  else:
    form = SignupForm()
  context = {
    'form'==form
  }  
  return render(request, 'credentials/signup.html')