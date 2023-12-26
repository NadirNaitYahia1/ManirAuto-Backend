from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser 


class User(AbstractBaseUser):
    idUser= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    USERNAME_FIELD = 'idUser'
    REQUIRED_FIELDS = [
        'name',
        'surname',
        'password',
        'email',
        'phone',
    ]

    def __str__(self):
        return f"{self.name}"
    

 

class Car(models.Model):
    idCar = models.AutoField(primary_key=True)
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    annee = models.IntegerField()
    energie = models.CharField(max_length=50)
    couleur = models.CharField(max_length=50)
    kilometrage = models.IntegerField()
    description = models.TextField()
    prix = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    WILAYA_CHOICES = (
    ('01', 'Adrar'),
    ('02', 'Chlef'),
    ('03', 'Laghouat'),
    ('04', 'Oum El Bouaghi'),
    ('05', 'Batna'),
    ('06', 'Béjaïa'),
    ('07', 'Biskra'),
    ('08', 'Béchar'),
    ('09', 'Blida'),
    ('10', 'Bouira'),
    ('11', 'Tamanrasset'),
    ('12', 'Tébessa'),
    ('13', 'Tlemcen'),
    ('14', 'Tiaret'),
    ('15', 'Tizi Ouzou'),
    ('16', 'Alger'),
    ('17', 'Djelfa'),
    ('18', 'Jijel'),
    ('19', 'Sétif'),
    ('20', 'Saïda'),
    ('21', 'Skikda'),
    ('22', 'Sidi Bel Abbès'),
    ('23', 'Annaba'),
    ('24', 'Guelma'),
    ('25', 'Constantine'),
    ('26', 'Médéa'),
    ('27', 'Mostaganem'),
    ('28', 'MSila'),
    ('29', 'Mascara'),
    ('30', 'Ouargla'),
    ('31', 'Oran'),
    ('32', 'El Bayadh'),
    ('33', 'Illizi'),
    ('34', 'Bordj Bou Arreridj'),
    ('35', 'Boumerdès'),
    ('36', 'El Tarf'),
    ('37', 'Tindouf'),
    ('38', 'Tissemsilt'),
    ('39', 'El Oued'),
    ('40', 'Khenchela'),
    ('41', 'Souk Ahras'),
    ('42', 'Tipaza'),
    ('43', 'Mila'),
    ('44', 'Aïn Defla'),
    ('45', 'de Naâma'),
    ('46', 'Aïn Témouchent'),
    ('47', 'de Ghardaïa'),
    ('48', 'de Relizane'),
    ('49', 'de Timimoun'),
    ('50', 'de Bordj Badji Mokhtar'),
    ('51', 'Ouled Djellal'),
    ('52', 'de Béni Abbès'),
    ('53', 'In Salah'),
    ('54', 'In Guezzam'),
    ('55', 'de Touggourt'),
    ('56', 'de Djanet'),
    ('57', 'El MGhair'),
    ('58', 'El Menia'),
)
    wilaya = models.CharField(max_length=50, choices=WILAYA_CHOICES, default='Inconnu')
    puissanceFiscale = models.IntegerField()
    BOITE_VITESSE_CHOICES = (
        ('manuelle', 'Manuelle'),
        ('automatique', 'Automatique'),
    )
    boiteVitesse = models.CharField(max_length=50, choices=BOITE_VITESSE_CHOICES)
    nombrePortes = models.IntegerField()
    airbag = models.BooleanField(default=False)
    climatisation = models.BooleanField(default=False)
    abs = models.BooleanField(default=False)
    CDMP3Bluetooth = models.BooleanField(default=False)
    directionAssistee = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.mark} {self.model}"
    

class Image(models.Model):
    idImage = models.AutoField(primary_key=True)
    idCar = models.ForeignKey(Car, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return f"{self.image}"