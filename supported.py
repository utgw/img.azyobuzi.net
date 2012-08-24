# -*- coding: utf-8 -*-

import sys
sys.path.append("resolvers")

import flickr
import gyazo
import hatena_fotolife
import imgly
import lockerz
import niconico_seiga
import pckles
import photozou
import twitpic
import viame
import yfrog

#アルファベット順

services = [
	flickr.flickr(),
	gyazo.gyazo(),
	hatena_fotolife.hatenaFotolife(),
	imgly.imgly(),
	lockerz.lockerz(),
	niconico_seiga.niconicoSeiga(),
	pckles.pckles(),
	photozou.photozou(),
	twitpic.twitpic(),
	viame.viame(),
	yfrog.yfrog()
]
