from sys import argv
from rsa import PrivateKey,sign
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L

def padding( string , size ):
	return ( size - len(string) ) * '*'  + string


def main():
	if len(argv) < 3:
		print 'Format: enc.py <identifier> <message>'
		return

	ID = argv[1] # Identifier of origin
	MESSAGE = argv[2] 

	# Read private key of origin
	with open(ID+'.pr','r') as f:
		privatekey = PrivateKey.load_pkcs1( f.read() )

	# Sign message with private key
	SIGN = sign( MESSAGE , privatekey , 'SHA-256' ).encode('hex')

	# Concatenate message, signature and identifier
	TEXT = padding( MESSAGE , 100 ) +   padding( SIGN , 400 )  +  padding( ID ,100 )


	# Create QR code
	qr = QRCode(
		version=1,
		error_correction=ERROR_CORRECT_L,
		box_size=10,
		border=4,
		)

	qr.add_data( TEXT )
	qr.make(fit=True)

	img = qr.make_image()
	img.save(ID + '.png')


if __name__ == '__main__':
	main()

