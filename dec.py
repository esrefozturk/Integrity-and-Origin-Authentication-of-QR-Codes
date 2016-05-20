from rsa import PublicKey,verify
from qrtools import QR
from sys import argv

def main():
	if len(argv) < 2:
		print 'Format: enc.py <image>'
		return

	qr = QR()
	qr.decode(argv[1])

	TEXT =  qr.data


	MESSAGE = TEXT[:100].strip('*\r\n')
	SIGN = TEXT[100:500].strip('*\r\n').decode('hex')
	ID = TEXT[500:].strip('*\r\n')

	publickey = PublicKey.load_pkcs1( open('DB/'+ID+'.pub').read() )

	if verify( MESSAGE , SIGN , publickey ):
		print MESSAGE
	else:
		print 'VERIFICATION FAILED!'

if __name__ == '__main__':
	main()
