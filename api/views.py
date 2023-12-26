from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Car, Image
from rest_framework.decorators import api_view
from rest_framework.response import Response
import jwt, datetime

@api_view(['POST'])
def register(request):
    name = request.data.get('name')
    surname = request.data.get('surname')
    password = request.data.get('password')
    email = request.data.get('email')
    phone = request.data.get('phone')
    print("azuk")
    try:
        user = User.objects.create(name=name, surname=surname, password=password, email=email, phone=phone)
        user.save()
    except:
        return Response({'error': 'email already exists'}, status='400')
    return Response({'success': 'user created successfully'}, status='200')


@api_view(['POST'])
def login(request):
    email    = request.data.get('email')
    password = request.data.get('password')
    try:
        user = User.objects.filter(email=email).first()
        if password != user.password:
            return Response({'error': 'password  is wrong'}, status='400')

    except:
        return Response({'error': 'email or password is wrong!'}, status='400')

    payload = {
        'email': user.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    # # Generate a random secret key
  
    token = jwt.encode(payload, 'secret', algorithm='HS256') 
    
    response = Response()
    # response.set_cookie('jwt', token, httponly=True, samesite='Strict')
    response.data = {   
        'message': 'Login successful',
        'jwt': token
    }
    return response


@api_view(['GET'])
def user(request):
    token = request.COOKIES.get('jwt')
    if not token:
        return Response({'error': 'not authenticated'}, status='400')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        return Response({'error': 'invalid credentials'}, status='400')
    user = User.objects.filter(email=payload['email']).first()
    user = {
        'name': user.name,
        'surname': user.surname,
        'email': user.email,
        'phone': user.phone,
    }
    return Response(user, status=200)

@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

def getUserById(id):
    user = User.objects.filter(idUser=id).first()
    user = {
        'name': user.name,
        'surname': user.surname,
        'email': user.email,
        'phone': user.phone,
    }
    return user



# ____________________________________________________________________
@api_view(['POST'])
def addCar(request):
    print("Request Data:", request.data)

    auth_header = request.headers.get('Authorization')
    if not auth_header or 'Bearer ' not in auth_header:
        return Response({'error': 'not authenticated'}, status='400')

    try:
        token = auth_header.split(' ')[1]
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user = User.objects.get(email=payload['email'])
        print("user", user)
    except jwt.ExpiredSignatureError:
        return Response({'error': 'session expired'}, status='400')
    except jwt.InvalidTokenError:
        return Response({'error': 'invalid token'}, status='400')
    except User.DoesNotExist:
        return Response({'error': 'user not found'}, status='400')

    try:
        mark = request.data.get('mark')
        model = request.data.get('model')
        annee = request.data.get('annee')
        energie = request.data.get('energie')
        couleur = request.data.get('couleur')
        kilometrage = request.data.get('kilometrage')
        description = request.data.get('description')
        prix = request.data.get('prix')
        wilaya = request.data.get('wilaya')
        puissanceFiscale = request.data.get('puissanceFiscale')
        boiteVitesse = request.data.get('boiteVitesse')
        nombrePortes = request.data.get('nombrePortes')
        airbag = request.data.get('airbag')
        abs_val = request.data.get('abs')
        climatisation = request.data.get('climatisation')
        CDMP3Bluetooth = request.data.get('CDMP3Bluetooth')
        directionAssistee = request.data.get('directionAssistee')
        photo_path = request.data.get('fileInput')  # Update the field name to match your form


        car = Car.objects.create(
            mark=mark, model=model, annee=annee, energie=energie, couleur=couleur,
            kilometrage=kilometrage, description=description, prix=prix, owner=user,
            wilaya=wilaya, puissanceFiscale=puissanceFiscale, boiteVitesse=boiteVitesse,
            nombrePortes=nombrePortes, airbag=airbag, abs=abs_val, climatisation=climatisation,
            CDMP3Bluetooth=CDMP3Bluetooth, directionAssistee=directionAssistee,
        )
        car.save()

        if photo_path is not None:
            try:
                image = Image.objects.create(idCar=car, image=photo_path)
                image.save()
            except Exception as e:
                print(f"Error: {e}")
                return Response({'error': 'image not saved'}, status='400')



        return Response({'success': 'car created successfully'}, status=200)

    except Exception as e:
        return Response({'error': str(e)}, status=400)
    

def getImageById(id):
    image = Image.objects.filter(idCar=id).first()
    return str(image.image.url) if image else None

@api_view(['GET'])
def getCars(request):
    cars = Car.objects.all()
    cars = list(cars.values())
    images = Image.objects.all()
    print(images)
    for car in cars:
        user = getUserById(car.get('owner_id'))
        imageById = getImageById(car.get('idCar'))
        phone = user['phone']
        cars[cars.index(car)]['image'] = str(imageById)
        cars[cars.index(car)]['phone'] = phone
    print(cars)

    return Response(cars, status=200)