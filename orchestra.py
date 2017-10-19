# -*- coding: utf-8 -*-
from midiutil import MIDIFile
import pandas as pd

with open('pam30.txt') as f:
    table = pd.read_table(f, sep='\t', index_col=0, lineterminator='\n')
    
#          C4  Db4 D4  Eb4 E4  F4  Gb4 G4  Ab4 A4  Bb4 B4  C5  Db5 D5  Eb5 E5  F5  Gb5 G5  Ab5
degrees = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]

#salsa = [54, 56, 58, 51, 30, 60, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]

'''
C major          – C E G
C sharp major    – C♯ E♯ G♯
D major          – D F♯ A
E flat major     – E♭ G B♭
E major          – E G♯ B
F major          – F A C
F sharp major    – F♯ A♯ C♯
G major          – G B D
A flat major     – A♭ C E♭
A major          – A C♯ E
Bb major         – B♭ D F
B major          – B D♯ F♯

C minor          – C E♭ G
C sharp minor    – C♯ E G♯
D minor          – D F A
E flat minor     – E♭ G♭ B♭
E minor          – E G B
F minor          – F A♭ C
F sharp minor    – F♯ A C♯
G minor          – G B♭ D
A flat minor     – A♭ C♭(B) E♭
A minor          – A C E
B flat minor     – B♭ D♭ F
B minor          – B D F♯
'''

# Major chords - Cmaj to Bmaj
maj1 = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
maj2 = [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
maj3 = [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]

min1 = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
min2 = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
min3 = [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]

alignments = open('alignment.txt', 'r')
alignments = [line.strip() for line in alignments]

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
"-":100
}


#degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 440   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(17)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

'''
for i, pitch in enumerate(min1):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    MyMIDI.addNote(track, channel, min2[i], time + i, duration, volume)
    MyMIDI.addNote(track, channel, min3[i], time + i, duration, volume)
'''

def harmonize(position):
    nr_seqs = len(alignments)
    
    for num, alignment in enumerate(alignments):
        residue = alignment[position]
        pitch = aminos[residue]
        
        if nr_seqs > 3 and num > 2:
            pitch -= 12
        elif nr_seqs > 6 and num > 5:
            pitch -= 24

        MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    

for i in range(len(alignments[0])):
    harmonize(i)



with open("alignment-suite-in-Dm.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
