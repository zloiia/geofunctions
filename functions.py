# -*- coding: utf-8 -*-
from math import ceil
def fromFloatToString(deg, htlm = True, repldots = True):
	deg = float(deg)
	floatPart = float(deg) - int(deg)
	minsec = floatPart * 60
	if htlm:
		res = "%d&deg %s'"%( int(deg), "{:.2f}".format(minsec))
	else:
		res = "%d %s"%( int(deg), "{:10.2f}".format(minsec))
	if repldots:
		return res.replace('.',',')
	return res

def fromFloatToList(deg):
	deg = float(deg)
	floatPart = float(deg) - int(deg)
	minsec = floatPart * 60
	return ( int(deg), int(minsec), int(ceil((minsec-int(minsec))*100)) )