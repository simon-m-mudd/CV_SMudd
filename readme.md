Simon M. Mudd CV
=============================

This is [my](http://www.geos.ed.ac.uk/homes/smudd) CV, based loosely on the format prepared by Dario Taraborelli
[URL](http://nitens.org/taraborelli/cvtex). 

You should complie with XeLaTeX.

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
This isn't a tex file!! It is tex-formatted text that can be intserted into the CV. 

