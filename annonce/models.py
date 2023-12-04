from django.db import models
from user_api.models import AppUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Option(models.Model):
    climatisation = models.BooleanField(default=False)
    toit_ouvrant = models.BooleanField(default=False)
    radio = models.BooleanField(default=False)
    retroviseurs_electrique = models.BooleanField(default=False)
    alarm = models.BooleanField(default=False)
    boite_auto = models.BooleanField(default=False)


class Photo(models.Model):
    image = models.ImageField(upload_to='voiture_photo/')
    #voiture = models.ForeignKey('Voiture', on_delete=models.CASCADE, related_name='voiture_photos')


class Voiture(models.Model):
    id = models.AutoField(primary_key=True)
    mark = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    annee = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(1980),
            MaxValueValidator(2023),
        ],
    )
    ENERGIE_CHOICES = (
        ('diesel', 'Diesel'),
        ('essence', 'Essence'),
        ('gpl', 'GPL'),
    )
    energie = models.CharField(max_length=10, choices=ENERGIE_CHOICES)
    couleur = models.CharField(max_length=50)
    kilometrage = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0),
        ],
    )
    photos = models.ManyToManyField(Photo, related_name='voiture_photos')
    description = models.TextField()
    prix = models.IntegerField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20000000),
        ],
    )
    options = models.ManyToManyField(Option)
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
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

    def __str__(self):
        return f"{self.mark} {self.model} ({self.annee})"


#https://drawsql.app/teams/arab/diagrams/manirauto


