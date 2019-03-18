### ** A python lib to interact with AcousticBrainz local server and AcousticBrainz.org database **

# Usage
Currently, to access the api you must edit and run `interact.py`

### Functions within interact.py

##### `getHLRecordings(mbids)`
* Args: * mbids is a list of MusicBrainz ids, which are strings
Returns json text of high-level data for recordings with all of the MusicBrainz ids passed into the function

##### `getHLRecording(mbid)`
* Args: * mbid is one MusicBrainz id, a string
Returns json text of high-level data the recording associated with the MusicBrainz id passed into the function

##### `getLLRecordings(mbids)`
* Args: * mbids is a list of MusicBrainz ids, which are strings
Returns json text of low-level data for recordings with all of the MusicBrainz ids passed into the function

##### `getLLRecording(mbid)`
* Args: * mbid is one MusicBrainz id, a string
Returns json text of low-level data the recording associated with the MusicBrainz id passed into the function
