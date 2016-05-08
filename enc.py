import rsa
import qrcode
import base64





URL = 'http://google.com/asdqwe'

def f( string , size ):
	print '---->',string
	if size > len(string):
		return ( size - len(string) ) * '*'  + string

( public , private ) = rsa.newkeys(1024)

signature = rsa.sign( URL , private , 'SHA-256' )

signature = base64.encodestring(signature)

C = f( URL , 100 ) +  f( signature , 400 )  + f('GOOGLE',100 )

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data( C )
qr.make(fit=True)

img = qr.make_image()
img.save('a.png')

open('public','w').write( public.save_pkcs1() )


