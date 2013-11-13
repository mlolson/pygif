import sys, os, time, Image

im = Image.open(sys.argv[1])
width, height = im.size
fwidth = 200
fheight = int(height * (0.4 * fwidth / width))
lines = [[" " for i in range(fwidth)] for j in range(fheight)]

while 1:
	try:
	    while 1:
			os.system('cls' if os.name=='nt' else 'clear')
			frame = im.tell()
			img = im.resize((fwidth, fheight))
			pix = img.load()
			maximum = 1.0*img.getextrema()[1]

			for y in xrange(0,fheight):
				l = ""
				for x in xrange(0,fwidth):

					pixel = pix[x,y]

					if pixel < 255.0:
						alpha = pixel/maximum
						if alpha < 0.1:
							l = l + " "
						elif alpha < 0.2:
							l = l + " "
						elif alpha < 0.3:
							l = l + "."
						elif alpha < 0.4:
							l = l + ":"
						elif alpha < 0.5:
							l = l + "*"
						elif alpha < 0.6:
							l = l + "%"
						elif alpha < 0.7:
							l = l + "O"
						elif alpha < 0.8:
							l = l + "@"
						else:
							l = l + u"\u2588"
					else:
						l = l + lines[y][x]

				lines[y] = l
				print l
			time.sleep(0.1)
			im.seek(frame+1)

	except EOFError:
		im.seek(0)