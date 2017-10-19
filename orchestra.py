# -*- coding: utf-8 -*-

from midiutil import MIDIFile
import pandas as pd

with open('pam30.txt') as f:
    table = pd.read_table(f, sep='\t', index_col=0, lineterminator='\n')
    
#          C4  Db4 D4  Eb4 E4  F4  Gb4 G4  Ab4 A4  Bb4 B4  C5  Db5 D5  Eb5 E5  F5  Gb5 G5  Ab5
#degrees = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]

#salsa = [54, 56, 58, 51, 30, 60, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]

alignment = open('alignment.txt', 'r')
alignment = [line.strip() for line in alignment]


aminos = {
"A":60,
"B":61,
"C":62,
"D":63,
"E":64,
"F":65,
"G":66,
"H":67,
"I":68,
"J":69,
"K":70,
"L":71,
"M":72,
"N":73,
"O":74,
"P":75,
"Q":76,
"R":77,
"S":78,
"T":79,
"U":80,
"V":81,
"W":82,
"X":83,
"Y":84,
"-":85
}


#degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(17)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(alignment[0]):
    MyMIDI.addNote(track, channel, aminos[pitch]-12, time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[1][i]]-12, time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[2][i]]-12, time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[3][i]]-12, time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[4][i]]-12, time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[5][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[6][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[7][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[8][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[9][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[10][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[11][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[12][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[13][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[14][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[15][i]], time + i, duration, volume)
    MyMIDI.addNote(track, channel, aminos[alignment[16][i]], time + i, duration, volume)
    
with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
