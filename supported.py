# -*- coding: utf-8 -*-

import sys
sys.path.append("resolvers")

import flickr
import gyazo
import hatena_fotolife
import imgly
import lockerz
import movapic
import niconico_seiga
import pckles
import photozou
import twipple
import twitgoo
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
	movapic.movapic(),
	niconico_seiga.niconicoSeiga(),
	pckles.pckles(),
	photozou.photozou(),
	twipple.twipple(),
	twitgoo.twitgoo(),
	twitpic.twitpic(),
	viame.viame(),
	yfrog.yfrog()
]
