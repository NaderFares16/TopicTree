from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
  # CAN REALIZE USER LOGOUT
  logout(request)
  return HttpResponseRedirect(reverse('index'))
