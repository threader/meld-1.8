#! /usr/bin/env python2
# -*- coding: utf-8 -*-
#
# order is important here (for now)
import pygtk
pygtk.require('2.0')
import gtk

# string taken from pango examples directory and converted from utf8
# to python2 unicode string escapes
hellos = '''This is Pango (Παν語)

This is a list of ways to say hello in various languages.
Its purpose is to illustrate a number of scripts.

---------------------------------------------------------
Arabic	السَّلام عليكُم 
Bengali (বাঙ্লা)	ষাগতোম
Burmese မ္ရန္မာ
Cherokee (ᏣᎳᎩ)	ᎣᏏᏲ
Czech (česky)	Dobrý den
Danish (Dansk)	Hej, Goddag
English	Hello
Esperanto	Saluton
Estonian	Tere, Tervist
FORTRAN	PROGRAM
Finnish (Suomi)	Hei
French (Français)	Bonjour, Salut
German (Deutsch Nord)	Guten Tag
German (Deutsch Süd)	Grüß Gott
Georgian (ქართველი)	გამარჯობა
Gujarati	ગુજરાતિ
Greek (Ελληνικά)	Γειά σας
Hebrew	שלום
Hindi	नमस्ते, नमस्कार।
Italiano	Ciao, Buon giorno
IPA English (ɪŋglɪʃ)	hɛləʊ
Lao	ສບາຍດ
Maltese	Ċaw, Saħħa
Nederlands, Vlaams	Hallo, Dag
Norwegian (Norsk)	Hei, God dag
Punjabi	ਪੁਂਜਾਬਿ
Polish	Dzień dobry, Hej
Russian (Русский)	Здравствуйте!
Sinhala (සිංහල)	ආයුබෝවන්
Slovak	Dobrý deň
Spanish (Español)	¡Hola!
Swedish (Svenska)	Hej, Goddag
Thai (ภาษาไทย)	สวัสดีครับ, สวัสดีค่ะ
Tamil  (தமிழ்)	வணக்கம்
Turkish (Türkçe)	Merhaba
Vietnamese (Tiếng Việt)	Xin Chào
Yiddish (ײַדישע)‎	דאָס הײַזעלע 

Japanese (日本語)	こんにちは, ｺﾝﾆﾁﾊ
Chinese (中文,普通话,汉语)	你好
Cantonese (粵語,廣東話)	早晨, 你好
Korean (한글)	안녕하세요, 안녕하십니까

Difference among chinese characters in GB, JIS, KSC, BIG5:
 GB	--	元气	开发
 JIS	--	元気	開発
 KSC	--	元氣	開發
 BIG5	--	元氣	開發
'''

win = gtk.Window()
win.connect('destroy', gtk.main_quit)
win.set_default_size(600, 400)

swin = gtk.ScrolledWindow()
swin.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
win.add(swin)
swin.show()

l = gtk.Label(hellos)
swin.add_with_viewport(l)
l.show()

win.show()

gtk.main()
