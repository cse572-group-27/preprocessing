# Preprocessing helper code for Spotify Podcast Dataset

## json to transcript
```#TODO: copy from Ava code to here```

## textile_segment
Segment the txt file from transcript to segments using NLTK TextTiling
Usage:
```
python segment.py -ifp {FOLDER CONTAIN TRANSCRIPTS} -ofp {FOLDER TO SAVE SEGMENTS}
```

## segment to prelabel
Prelabel the segments to ad, non-ads label for segment-tool.
Usage:
```
python prelabel.py -ifp {FOLDER CONTAIN SEGMENTS} -ofp {FOLDER CONTAIN PRELABEL}
```
If we want to output everything to one big csv file:
```
python prelabel_onecsv.py -ifp {FOLDER CONTAIN SEGMENTS} -ofp {CSV FILE NAME (default to prelable.csv)}
```

