# Generated by Django 4.1.4 on 2023-12-26 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('idCar', models.AutoField(primary_key=True, serialize=False)),
                ('mark', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('annee', models.IntegerField()),
                ('energie', models.CharField(max_length=50)),
                ('couleur', models.CharField(max_length=50)),
                ('kilometrage', models.IntegerField()),
                ('description', models.TextField()),
                ('prix', models.IntegerField()),
                ('wilaya', models.CharField(choices=[('01', 'Adrar'), ('02', 'Chlef'), ('03', 'Laghouat'), ('04', 'Oum El Bouaghi'), ('05', 'Batna'), ('06', 'Béjaïa'), ('07', 'Biskra'), ('08', 'Béchar'), ('09', 'Blida'), ('10', 'Bouira'), ('11', 'Tamanrasset'), ('12', 'Tébessa'), ('13', 'Tlemcen'), ('14', 'Tiaret'), ('15', 'Tizi Ouzou'), ('16', 'Alger'), ('17', 'Djelfa'), ('18', 'Jijel'), ('19', 'Sétif'), ('20', 'Saïda'), ('21', 'Skikda'), ('22', 'Sidi Bel Abbès'), ('23', 'Annaba'), ('24', 'Guelma'), ('25', 'Constantine'), ('26', 'Médéa'), ('27', 'Mostaganem'), ('28', 'MSila'), ('29', 'Mascara'), ('30', 'Ouargla'), ('31', 'Oran'), ('32', 'El Bayadh'), ('33', 'Illizi'), ('34', 'Bordj Bou Arreridj'), ('35', 'Boumerdès'), ('36', 'El Tarf'), ('37', 'Tindouf'), ('38', 'Tissemsilt'), ('39', 'El Oued'), ('40', 'Khenchela'), ('41', 'Souk Ahras'), ('42', 'Tipaza'), ('43', 'Mila'), ('44', 'Aïn Defla'), ('45', 'de Naâma'), ('46', 'Aïn Témouchent'), ('47', 'de Ghardaïa'), ('48', 'de Relizane'), ('49', 'de Timimoun'), ('50', 'de Bordj Badji Mokhtar'), ('51', 'Ouled Djellal'), ('52', 'de Béni Abbès'), ('53', 'In Salah'), ('54', 'In Guezzam'), ('55', 'de Touggourt'), ('56', 'de Djanet'), ('57', 'El MGhair'), ('58', 'El Menia')], default='Inconnu', max_length=50)),
                ('puissanceFiscale', models.IntegerField()),
                ('boiteVitesse', models.CharField(choices=[('manuelle', 'Manuelle'), ('automatique', 'Automatique')], max_length=50)),
                ('nombrePortes', models.IntegerField()),
                ('airbag', models.BooleanField(default=False)),
                ('climatisation', models.BooleanField(default=False)),
                ('abs', models.BooleanField(default=False)),
                ('CDMP3Bluetooth', models.BooleanField(default=False)),
                ('directionAssistee', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('idUser', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('idImage', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('idCar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
