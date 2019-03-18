<h6>A python lib to interact with AcousticBrainz local server and AcousticBrainz.org database</h6>

<h4>Usage</h4>
<p>Currently, to access the api you must edit and run `interact.py` </p>

<h5>Functions within interact.py</h5>

<h6>`getHLRecordings(mbids)`</h6>
<p>Args: mbids is a list of MusicBrainz ids, which are strings</p>
<p>Returns json text of high-level data for recordings with all of the MusicBrainz ids passed into the function</p>

<h6>`getHLRecording(mbid)`</h6>
<p>Args: mbid is one MusicBrainz id, a string</p>
<p>Returns json text of high-level data the recording associated with the MusicBrainz id passed into the function</p>

<h6>`getLLRecordings(mbids)`</h6>
<p>Args: mbids is a list of MusicBrainz ids, which are strings</p>
<p>Returns json text of low-level data for recordings with all of the MusicBrainz ids passed into the function</p>

<h6>`getLLRecording(mbid)`</h6>
<p>Args: mbid is one MusicBrainz id, a string</p>
<p>Returns json text of low-level data the recording associated with the MusicBrainz id passed into the function</p>
