from flask import Flask
# @app.route("/")
# def home():
#     return "Flaskda birinchi loyiha\nNamoz vaqtlari"
# app.run(debug=True)
# from flask import Flask
#
dastur = Flask("Namoz")
import requests

api_data = requests.get("https://islomapi.uz/api/present/day?region=Farg'ona")

# print(api_data.json())
saharlik = api_data.json().get("times").get('tong_saharlik')
quyosh = api_data.json().get("times").get('quyosh')
peshin = api_data.json().get("times").get('peshin')
asr = api_data.json().get("times").get('asr')
shom_iftor = api_data.json().get("times").get('shom_iftor')
hufton = api_data.json().get("times").get('hufton')


@dastur.route("/")
def home():
    return f"""
    <h1 style="color: green;"> Namoz vaqtlari </h1><hr>
    <ul style="color: teal;">
        <li>Saharlik: {saharlik}</li>
        <li>Quyosh: {quyosh}</li>
        <li>Peshin: {peshin}</li>
        <li>Asr: {asr}</li>
        <li>Shom: {shom_iftor}</li>
        <li>Xufton: {hufton}</li>
    </ul>
    """
#
#
dastur.run(debug=True)
app = Flask("Namoz vaqtlari")
import requests
from flask import Flask
dastur = Flask("Namoz")
import requests
import datetime
api_data_day = requests.get("https://islomapi.uz/api/present/day?region=Farg'ona")
api_data_week = requests.get("https://islomapi.uz/api/present/week?region=Farg'ona")


saharlik = api_data_day.json().get("times").get('tong_saharlik')
quyosh = api_data_day.json().get("times").get('quyosh')
peshin = api_data_day.json().get("times").get('peshin')
asr = api_data_day.json().get("times").get('asr')
shom_iftor = api_data_day.json().get("times").get('shom_iftor')
hufton = api_data_day.json().get("times").get('hufton')
#
#
@dastur.route("/")
def home():
    return f"""
    <h1 style="color: green;"> Namoz vaqtlari kunlik</h1><hr>
    <p style="color: teal;">{datetime.datetime.today().date()} uchun namoz vaqtlari:</p>
    <ul style="color: teal;">
        <li>Saharlik: {saharlik}</li>
        <li>Quyosh: {quyosh}</li>
        <li>Peshin: {peshin}</li>
        <li>Asr: {asr}</li>
        <li>Shom: {shom_iftor}</li>
        <li>Xufton: {hufton}</li>
    </ul>
    """


@dastur.route("/hafta-namoz-vaqtlari")
def hafta():
    template = f"""<h1 style="color: green;"> Namoz vaqtlari kunlik</h1>"""
    for kun in api_data_week.json():
        saharlik = kun.get('times').get('tong_saharlik')
        quyosh = kun.get('times').get('quyosh')
        peshin = kun.get('times').get('peshin')
        asr = kun.get('times').get('asr')
        shom_iftor = kun.get('times').get('shom_iftor')
        hufton = kun.get('times').get('hufton')

        template += f"""<hr>
        <p style="color: teal;">{kun.get('weekday')}</p>
        <ul style="color: teal; display: flex; flex-wrap: wrap; justify-content: center; gap: 25px;">
        <li>Saharlik: {saharlik}</li>
        <li>Quyosh: {quyosh}</li>
        <li>Peshin: {peshin}</li>
        <li>Asr: {asr}</li>
        <li>Shom: {shom_iftor}</li>
        <li>Xufton: {hufton}</li>
        </ul>
        """

#     return template
#
#
# dastur.run(debug=True)
#
# import requests
# api=requests.get(" https://islomapi.uz/api/present/day?region=Toshkent")
# print(api.json())

