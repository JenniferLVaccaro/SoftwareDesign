# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Jenny Vaccaro
"""

# you may find it useful to import these variables (although you are not required to use them)
import amino_acids
from amino_acids import aa, codons

startCodon = 'ATG'
stopCodon = ['TAA', 'TAG', 'TGA']

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    L = []
    r = int(len(dna))/3    # no need to cast to an int :-)
    for i in range(r):
        # a shorthand: codon = dna[3*i:3*(i+1)]
        codon = str(dna[3*i]) + str(dna[3*i+1]) + str(dna[3*i+2])
        for i in range(len(codons)):     # use different variables for nested loops!
            if codon in codons[i]:
                yolo = i
                break
        print yolo
        L.append(aa[yolo])
    return collapse(L)

'''
Love the parameter name, yolo!

A suggestion for simpler logic:

for i in range(r):
    codon = dna[3*i:3*(i+1)]
    for j in range(len(codons)):
        if codon in codons[j]:
            L.append(aa[j])
return collapse(L)
'''

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    dna = 'AGCGCG'
    print coding_strand_to_AA(dna)

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    R = []
    for i in range(len(dna)):
        if dna[i] == 'A':
            R.append('T')
        elif dna[i] == 'T':
            R.append('A')
        elif dna[i] == 'C':
            R.append('G')
        elif dna[i] == 'G':
            R.append('C')
        else:
            print 'Invalid Entry: not A T G or C you gave me' + str(dna[i])     # Great error catching! Look below for more comments!
    R.reverse()
    return collapse(R)
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    A = 'TATACGCG'
    B = 'TATAGC'    
    print get_reverse_complement(A) 
    """The answer should be: ATATGCGC"""
    print get_reverse_complement(B) 
    """The answer should be 'ATATCG'"""       

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    R = []
    for i in range((int(len(dna))/3)):
        q = str(dna[3*i]) + str(dna[3*i+1]) + str(dna[3*i+2])     
        if  q in stopCodon:
            return collapse(R)
        else:
            R.append(q)
    return collapse()

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    abc = 'ATA'+'GCG'+'CGC'+ stopCodon[1]
    print rest_of_ORF(abc)     
    """ the response should be sipmly ATAGCGCGC"""
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    L = []         
    for i in range(len(dna)/3):
         q = str(dna[3*i]) + str(dna[3*i+1]) + str(dna[3*i+2])
         if q == startCodon:
             K = []
             for j in range(i,len(dna)/3):
                 p = str(dna[3*j]) + str(dna[3*j+1]) + str(dna[3*j+2])
                 if p in stopCodon:
                     L.append(collapse(K))
                     break
                 else:
                     K.append(p)
    return L       
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    abc = 'AAT' + startCodon + 'AGC' + 'ATA' + str(stopCodon[1]) + 'AA' + startCodon + 'GAC' + collapse(stopCodon)
    print find_all_ORFs_oneframe(abc)

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    L = []
    L.extend(find_all_ORFs_oneframe(dna))
    L.extend(find_all_ORFs_oneframe(dna[1:]))
    L.extend(find_all_ORFs_oneframe(dna[2:]))
    return L
    
def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    abc = 'AAT' + startCodon + 'AGC' + 'ATA' + str(stopCodon[1]) + 'AA' + startCodon + 'GAC' + collapse(stopCodon)
    print find_all_ORFs(abc)

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    L = []
    L.extend(find_all_ORFs(dna))
    abc = get_reverse_complement(dna)
    L.extend(find_all_ORFs(abc))
    return L

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    print find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    # returns ['ATGCGAATG', 'ATGCTACATTCGCAT']


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    L = find_all_ORFs_both_strands(dna)
    A = L[0]
    for i in range(len(L)):
        if len(L[i]) > A:       # I think you meant if len(L[i]) > len(A): ...
            A = L[i]
    return A
    
def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """
    print longest_ORF("ATGCGAATGTAGCATCAAA")
    

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    DNA = list(dna)
    import random
    J = 'ABCD'                  # What's 'ABCD'..??!?!?!
    for i in range(num_trials):
        L = ''        
        dna = collapse(DNA)
        L = longest_ORF(dna)        
        if len(L) > len(J):
            J = L
            print len(J)
        DNA = list(dna)
        random.shuffle(DNA)
    return len(J)
        
def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    A = []
    R = []
    L = find_all_ORFs_both_strands(dna)
    for i in range(len(L)):
        if len(L[i]) > threshold:
            A.append(L[i])
    for i in range(len(A)):
        b = coding_strand_to_AA(A[i])
        R.append(b)
    return R

'''
As always, great work, Jenny!

A few comments I have are:
    - You don't need to type cast unnecessarily. When in doubt, always try running `type(...)` 
      of whatever you have questions about!
    - Huge kudos to you for realizing that you should raise a flag when a user types in something
      that's not one of the nucleotides! Search for 'python raise exception' for more information
      on these, or feel free to check out the codes in my hw3 folder on https://github.com/abekim/softdes
'''
