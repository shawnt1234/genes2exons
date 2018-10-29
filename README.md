# genes2exons
Requirements: BEDtools, BLAST, Python 2.7,reference genome, Target genes <br />
Takes target genes aligned to a reference genome and pulls out single copy genes split into exons. <br />
<br />
Input: modified BLAST output <br />
<br />
Scripts: <br />
splitBLAST.py <br />
rmgenes_multichrom.py <br />
rmgenes_multiloci.py <br />
makeexons.py <br />
combineexons.py <br />
<br />
Output: exons and coordinates <br />
<br />
Make BED file from output <br />
use BEDtools 'getfasta' command in order to get a exon fasta file <br />

Future work: rewrite scripts so that BLAST output doesn't need to be modified. Modify combine exons.py to create a BED file
