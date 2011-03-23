from partfinder import alignment

def test_phylip():
    test_alignment = r"""16 13
Aalksfj GCCGGCGGGGA-A
	Bla	GCCGGCGGGGAAA
	Ca	GCCGGCGGGGAAG
	D	GCCAGCGGGGAAG
E	GCCCGGGGGGAAG
	F	GCCCGTGGGGAAG
	G	GCCGGCGAGGAAG
	H	GCCAGCGGGGAAA
	I	GCCGGCGGGGAAG
	J	GCC GGCGGGGAAG
	K	GCCGGCGGGGAAT
	L	GCCGGCGGGGAAA
	M	GTCGGCGGGGAAA
	N	GCCGGCGGGGAAA
	O	GCCGGCGGGGAAA
	P	GCC GGCGGGGAAT
"""
    print alignment.parse(test_alignment)

# def test_fasta():
    # test_alignment = r"""
# >spp1
# ATTGAGGTTCAGAATGGTAATGAA------GTGCTGG
# >spp2
# CTTGAGGTACAAAATGGTAATGAG------AGCCTGG
# >spp3
# CTTGAGGTACAGAATAACAGCGAG------AAGCTGG
# >spp4
# ATCGAGGTGAAAAATGGTGATGCT------CGTCTGG
    # """
    # a = alignment.parse(test_alignment)
    # print a