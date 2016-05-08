import rsa
import qrtools
import base64

def ff( string ):
	return string.strip('*\r\n ')

public = rsa.PublicKey.load_pkcs1( open('public').read() )

qr = qrtools.QR()

qr.decode("a.png")

C =  qr.data


URL = ff(C[:100])
signed = ff( C[100:500] )
org = ff( C[500:] )



print URL
print signed
print org
print public

print rsa.verify( URL , base64.decodestring(signed) , public )

