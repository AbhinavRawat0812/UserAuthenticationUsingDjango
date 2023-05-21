import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializer,UserRegistrationSerializer

# @csrf_exempt
# def create_user(request):
#     if request.method == 'POST':
#         # Get the user data from the request
#         data = json.loads(request.body)
#         username = data.get('username')
#         password = data.get('password')
#         mobile = data.get('mobile')
#         name = data.get('name')
#         address = data.get('address')
#         email = data.get('email')

#         # Validate the user data
#         if not (username.isalpha() and username.isalnum() and len(username) <= 100):
#             return JsonResponse({'error': 'Invalid username'}, status=400)
#         if not (len(password) >= 6 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password)):
#             return JsonResponse({'error': 'Invalid password'}, status=400)
#         if not (isinstance(mobile, int) and len(str(mobile)) == 10):
#             return JsonResponse({'error': 'Invalid mobile'}, status=400)
#         if not email:
#             return JsonResponse({'error': 'Invalid email'}, status=400)

#         # Save the user to the database
#         user = User(username=username, password=password, mobile=mobile, name=name, address=address, email=email)
#         user.save()

#         # Send email to the user
#         send_mail(
#             'User Registration',
#             f'Your account has been created. Your password is: {password}',
#             'sender@example.com',
#             [email],
#             fail_silently=False,
#         )

#         # Return the generated user ID
#         return JsonResponse({'user_id': user.id},status=200)

# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         # Get the login data from the request
#         data = json.loads(request.body)
#         username = data.get('username')
#         password = data.get('password')

#         # Check if the user exists in the database
#         try:
#             user = User.objects.get(username=username, password=password)
#             return JsonResponse({'status': 'success'})
#         except User.DoesNotExist:
#             return JsonResponse({'status': 'failure'}, status=400)

# def select_users(request):
#     if request.method == 'GET':
#         # Get all users from the database
#         users = User.objects.all()

#         # Convert users to JSON format
#         user_list = [{'username': user.username, 'password': user.password, 'mobile': user.mobile, 'name': user.name, 'address': user.address, 'email': user.email} for user in users]

#         # Return the users


class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
         serializer = UserLoginSerializer(data = request.data)
         if serializer.is_valid(raise_exception=True):
             email=serializer.data.get('email')
             password =serializer.data.get('password')
             user = authenticate(email=email, password=password)
             if user is not None:
                    return Response({'msg':'Successful Login'},
                                    status=status.HTTP_200_OK)
             else:
                  return Response({'errors':{'non_field_errors':['Email or password is not valid']}},
                                  status=status.HTTP_404_NOT_FOUND)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Successful'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

