[app]
title = EnvChem Analyzer Pro
package.name = envchem
package.domain = org.envchem
source.dir = app
source.include_exts = py,png,jpg,kv,atlas,json,csv
version = 3.0

requirements = python3,kivy==2.3.0,numpy,pandas,scipy,scikit-learn,reportlab,openpyxl,pillow

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.logcat_filters = *:S python:D

android.presplash_color = #070d14
android.presplash_lottie = 

android.icon.filename = %(source.dir)s/../icons/icon.png
android.wakelock = False

[buildozer]
log_level = 2
warn_on_root = 1
