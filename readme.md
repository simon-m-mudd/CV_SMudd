Simon M. Mudd CV
=============================

This is [my](http://www.geos.ed.ac.uk/homes/smudd) CV, based loosely on the format prepared by Dario Taraborelli
[URL](http://nitens.org/taraborelli/cvtex). 

You should compile with XeLaTeX.

To get this to work you will need some free fonts; the URL of these fonts is in the source code. 

NOTE: Fo reasons that I have not been fully able to diagnose, this tex file results in quite a few errors.
However, it produces a pdf with a nice-looking cv so I just ignore all the errors. 

There are also some python scripts for automating generation of the components of the cv. 

Convert_rtf_references.py
----------------------------------
The tex document does not use a bibliography: you have to give it formatted references. 
Preparing these can be a pain (I did it by hand the first time around--it took ages!!). 
This script should save you the trouble. 

First, you should have a citation engine like [Zotero](https://www.zotero.org/). 
I grabbed all my citations from (Web of Science](https://www.webofscience.com/) and imported them into a collection.
The first time I tried this I grabbed everything from Google Scholar: don't do this!! It gives jumbled, malformatted reference records. 
For example, the zotero conversions from Google Scholar seem to be missing the doi information, and the doi is used to make html links to papers. 

Once you have your collection in Zotero, you can dowload your favourite [stylesheet](https://www.zotero.org/styles) and format a bibliography. 
Save the bibliography in rtf format. 

Then, in a text editor (not Word!!), open the rtf and get rid of the codes at the beginning of the file before the first reference (they might look like this: {\rtf \li720 \fi-720 \sl240 \slmult1 \sa240 ) and the curly bracket at the end. 
Save this file and then use this filename as the input to the rtf converter. 

The rtf converter will then spit out another file, called 'Parsed_refs.tex'. 
This isn't a tex file!! It is tex-formatted text that can be inserted into the CV. 

Attempting to get the fonts to work
---------------------------------------------------------

Okay, so this template is a little bit finicky. 
I've tried to get it working with the docker latex container, which has all the necessary bells and whistles for latex but only the most basic fonts. 


For getting the docker container working, the steps are:
1. `docker pull blang/latex`
2. `docker run -it -v C:\Path\to\repo:/data blang/latex`
3. `pdflatex book.tex`
4. `bibtex book`
5. `pdflatex book.tex`
6. `pdflatex book.tex`

For Simon's laptop computer the docker call is:
`docker run -it -v C:\Users\smudd\Documents\papers_latex\CV_SMudd:/data blang/latex`

For Simon's desktop computer the docker call is:
`docker run -it -v C:\Users\smudd\local_latex\CV_SMudd:/data blang/latex`

To install the font (in this case the test is the Font Hack)

Update: I am putting the font in the repo so you don't have to do steps 1-4.

1. The blang/latex container doesn't have all the stuff you need to get the font, so first run `apt-get update`
2. Then `apt-get install wget`
3. Download the font `wget https://www.fontsquirrel.com/fonts/download/heuristica`
4. Unzip it: `unzip heuristica`
4. Go into the heirstica directory `cd heuristica`
5. Make a directory in your fonts folder: `mkdir /usr/share/fonts/opentype/heuristica`
6. Copy the fonts across
7. `cp Heuristica-Bold.otf /usr/share/fonts/opentype/heuristica/Heuristica-Bold.otf`
8. `cp Heuristica-BoldItalic.otf /usr/share/fonts/opentype/heuristica/Heuristica-BoldItalic.otf`
9. `cp Heuristica-Italic.otf /usr/share/fonts/opentype/heuristica/Heuristica-Italic.otf`
10. `cp Heuristica-Regular.otf /usr/share/fonts/opentype/heuristica/Heuristica-Regular.otf`
11. Update the fonts cache: `fc-cache -f -v`
12. Done! That was easy, wasn't it!
13. Now run the cv with `xelatex MuddCV_August2016.tex`
