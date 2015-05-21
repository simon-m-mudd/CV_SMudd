#==============================================================================
# This function is for parsing a citations list from an RTF file in order to 
# generate a publications list for my Latex CV style. 
# 
# I generate the rtf using Zotero to make a bibliography. 
# You then need to go into the rtf using a text editor (not Word!!)
# and delete the codes at the beginning
# (i.e., {\rtf \li720 \fi-720 \sl240 \slmult1 \sa240 )
# and the closed bracket at the end. 
# Then feed this file into the code and out will come a formatted file, Parsed_refs.tex
# This isn't actually a tex file, you just need to insert it in a section
# of the CV
#==============================================================================
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:50:50 2015

@author: smudd
"""

# This is for parsing RTF files prodced by Zotero for ingestion into my tex cv
import re
import numpy as np


def read_rtf_references(filename):
    fi = open(filename, 'r')
    fo = open("Parsed_refs.tex",'w')
    lines = fi.readlines()
    newlines = []
    
    print "Lines are: "
    print lines

    for line in lines:
        print "line is: "
        
        line = line.replace('\uc0\u8220{}', '\'')
        line = line.replace('\uc0\u8217{}', '\'')
        line = line.replace('\uc0\u8216{}', '\'')
        line = line.replace('\uc0\u8211{}', '-')
        newlines.append(line)

    #reset the lines    
    lines = newlines
    newlines = []
    
    # now replace the rtf code for italics with the latex code
    for line in lines:
        p = re.compile('\\\\i( [^}]* )\\\\i0{}', re.VERBOSE)
        line = p.sub(r'textit{\1}',line)
        newlines.append(line)
        #print "line is: "
        #print line

    #reset the lines    
    lines = newlines
    newlines = []
    #print "lines are now: "
    #print lines

    # replace the dois with html links to doi.org
    for line in lines:
        p2 = re.compile('doi:( [^}]* ).\\\\', re.VERBOSE)
        line = p2.sub(r'href{http://doi.org/doi:\1}{doi:\1}.',line)
        newlines.append(line)
        #print "line is: "
        #print line

    #reset the lines    
    lines = newlines
    newlines = [] 

    
    # now get the year of the paper
    years = []    
    for line in lines:
        print "line is: "
        print line
        match = re.search('\d{4}', line).span()
        year= line[match[0]:match[1]]
        print "date is: "
        print year
        years.append(year) 
    
    # now sort the lines according to year 
    yeararray = np.asarray(years) 
    
    print "ya length: " + str(len(years))
    print "lines lenght: " + str(len(lines))
    
    # sort and get the indices    
    sorted_index = yeararray.ravel().argsort()
    #reverse this index
    
    print "sorted index is: "
    print sorted_index    
    
    reversed_arr = np.fliplr([sorted_index])[0]
    sorted_index = reversed_arr
    
    print "reversed sorted index is: "
    print sorted_index
    


    # now make the new list
    for i in sorted_index:
        newlines.append(lines[i])

    # now add the codes for hanging indent and the numbering at the beginning of
    # each line
    lines = newlines
    newlines = []
    for line in lines:
        line = '\\hangindent=0.7cm\\textbf{N.}'+line
        newlines.append(line)
        fo.write(line)
    
    
    
    #print out the lines to screen
    print "The newlines are: "
    print newlines    
    
    # Somme commented out code to test re
    #p = re.compile('\\\\i( [^}]* )\\\\i0{}', re.VERBOSE)
    #a = p.sub(r'subsection{\1}','\i Yo\i0{} \i{second}')    
    #print "a: " + a
    
    fi.close()
    fo.close()

if __name__ == "__main__":
    #fit_weibull_from_file(sys.argv[1])
    filename = 'c:\\Users\\smudd\\Documents\\Latex_projects\\CV\\test.rtf'
    
    read_rtf_references(filename) 
