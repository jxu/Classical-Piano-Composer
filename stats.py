from music21 import *
import glob
from collections import Counter
import matplotlib.pyplot as plt


note_lengths = Counter()
intervals = Counter()

for file in glob.glob("dur2.mid"):
    midi = converter.parse(file)

    print("Parsing %s" % file)

    notes_to_parse = midi.flat.notes

    for element in notes_to_parse:
        note_lengths[element.duration.quarterLength] += 1

    for i in range(len(notes_to_parse)-1):
        if isinstance(notes_to_parse[i], note.Note) and isinstance(notes_to_parse[i+1], note.Note):

            iv = interval.Interval(noteStart = notes_to_parse[i], noteEnd = notes_to_parse[i+1])
            intervals[iv.semitones] += 1
    

print(note_lengths)
print(intervals)

plt.bar(list(intervals.keys()), intervals.values())
plt.xlabel("Pitch interval (semitones)")
plt.ylabel("Count")
plt.show()
