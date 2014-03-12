# -*- coding: utf-8 -*-
def fromFloatToString(deg, htlm = True, repldots = True):
	floatPart = float(deg) - int(deg)
	minsec = floatPart * 60
	if htlm:
		res = "%d&deg %s'"%( int(deg), "{:.2f}".format(minsec))
	else:
		res = "%d deg %s"%( int(deg), "{:10.2f}".format(minsec))
	if repldots:
		return res.replace('.',',')
	return res

print fromFloatToString(55.547000)