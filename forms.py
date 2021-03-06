#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte
import wtforms

import sys

reload(sys)
sys.setdefaultencoding("utf8")

class RegistrationForm(wtforms.Form):
    nome = wtforms.StringField('Nome', [wtforms.validators.Length(min=4, max=25)])
    forca = wtforms.IntegerField('Força', [wtforms.validators.Required()])
    inteligencia = wtforms.IntegerField('Inteligência')
    rapidez = wtforms.IntegerField('Rapidez')
