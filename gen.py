from sys import argv
import rsa

def main():
	if len(argv) < 2:
		print 'Format: enc.py <identifier>'
		exit(0)

	ID = argv[1]

	publickey , privatekey = rsa.newkeys(1024)

	with open('DB/'+ID+'.pub','w') as f:
		f.write( publickey.save_pkcs1() )

	with open(ID+'.pr','w') as f:
		f.write( privatekey.save_pkcs1() )



if __name__ == '__main__':
	main()