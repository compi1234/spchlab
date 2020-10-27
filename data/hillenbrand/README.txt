Hillenbrand Database 
====================
(c) 1995 James Hillenbrand
https://homepages.wmich.edu/~hillenbr/voweldata.html

vowdata.csv is a slightly modified rendering of the data in vowdata.dat combined with timedata.dat 
with following additional changes:
- column headers were added
- columns were added for file_id(fid) vowel_id(vid), gender_id(gid) and speaker_id(sid);
	these can be derived from filename, but to have them already processed is often handy
- the '0'-values representing 'Not Available' where modified to #N/A
- the csv separator is the standard ',' and all measurement data use standard floating point dot notation



Column Headers
==============
col1:4 		fid	vid	gid	sid
col5:10		dur	f0	F1	F2	F3	F4	
col11:18	F1-1	F2-1	F3-1	F1-2	F2-2	F3-2	F1-3	F2-3	F3-3	
col19:22	Start	End	Center1	Center2


Vowel ID
========
ae	had
ah	hod
aw	hawed
eh	head
er	heard
ei	haid
ih	hid
iy	heed
oa	hoat
oo	hood
uh	hud
uw	who'd



Gender ID
==========
m=man, w=woman, b=boy, g=girl


Speaker ID
==========
m01-m50, w01-w50, b01-b29, g01-g22



Reference
=========
The database was used to generate the results in:
Hillenbrand, Getty, Clark & Wheeler (1995). Acoustic characteristics of American English vowels. Journal of the Acoustical Society of America, 97, 3099-3111.

