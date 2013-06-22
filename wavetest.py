from __future__ import division
import math
import wave
import struct
richness = input('enter sound wave layers')
freq = input('enter frequency')
freqwidth = input('enter main freq layers')
widthtop = input('enter overtone frequency width')
widthbottom = input('enter undertone frequency width')
basetop = input('enter overtone frequency')
basebottom = input('enter undertone frequency')
frate = input('enter frame rate')
frate = float(frate)
data_size = 4000
pneglist = []
odd = 1

toprate = 1
bottomrate = 2
halfrich = abs(richness/2)
counter = 0
ratiolist = []
while counter < halfrich:
  ratio = toprate/bottomrate
	ratiolist.append(ratio)
	counter = counter + 1
	toprate = toprate + 1
	bottomrate = bottomrate + 1
harmonicseries = []
for item in ratiolist:
	harmonpoint = freq * item
	harmonicseries.append(harmonpoint)
harmonicseries.append(freq)
for item in ratiolist:
	harmonpoint = freq/item
	harmonicseries.append(harmonpoint)
print harmonicseries


if richness %2 == 0:
	splitlen = richness/4
else:
	splitlen = richness - 1
	splitlen = splitlen/4
undercount = 0
while undercount < splitlen:
	layer = basebottom - ((splitlen - undercount)*widthbottom)
	undercount = undercount + 1
	pneglist.append(layer)
undercount = 0
while undercount < splitlen:
	layer = basebottom +(undercount*widthbottom)
	undercount = undercount + 1
	pneglist.append(layer)
freqcount = 0
while freqcount < freqwidth:
	pneglist.append(freq)
	freqcount = freqcount + 1
overcount = 0
while overcount < splitlen:
	layer = basetop - ((splitlen - overcount)*widthtop)
	overcount = overcount + 1
	pneglist.append(layer)
overcount = 0
while overcount < splitlen:
	layer = basetop + (overcount*widthtop)
	overcount = overcount + 1
	pneglist.append(layer)

#add this line to make symmetrical harmonic series
pneglist = harmonicseries

newpneg = []
namelist = []

for item in pneglist:
	newitem = item
	if item == 0:
		newitem = -1
	newpneg.append(newitem)
	namelist.append(str(newitem))

fname = ''.join(namelist)
fname = fname +'.wav'
fname = 'wavefile.wav'

amp = 60400.0     # multiplier for amplitude

sine_list_x = []
for x in range(data_size): 
	for item in newpneg:
    		sine_list_x.append(math.sin(2*math.pi*item*(x/frate)))

wav_file = wave.open(fname, "w")

nchannels = 1
sampwidth = 2
framerate = int(frate)
nframes = data_size
comptype = "NONE"
compname = "not compressed"

wav_file.setparams((nchannels, sampwidth, framerate, nframes,
    comptype, compname))
for s in sine_list_x:
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))
print sine_list_x
wav_file.close()
