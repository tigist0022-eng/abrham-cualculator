[app]
title = Abraham Calculator
package.name = abrahamcalculator
package.domain = org.abraham
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
allow_bsd = True

[buildozer]
log_level = 2
warn_on_root = 1
