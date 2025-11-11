## GCUA usage tutorial ## 
used GCUA(general codon usage analysis tool) to generate codon frequency/usage table
using the following command first   
``git clone https://github.com/mol-evol/gcua.git ``
``cd gcua ``    
``pip install -r requirements.txt.``
check installation with   
``python gcua.py --version ``  
run the interactive menu system of gcua by  
python gcua.py 

load the fasta file first via option, then export metrics, for our purposes, codon usage data and comprehensive metrics may be the most useful, I've done it on our Mimivirus refrence genome first. 
### bug fix! ### 
there is a bug in the GCUA original script, where the wrong name of export_base_comp() is called instead, navigate to line 5379 and change self._export_base_composition() to self._export_base_comp()

# citations # 
McInerney JO. GCUA: general codon usage analysis.
Bioinformatics. 1998;14(4):372-3.
doi: 10.1093/bioinformatics/14.4.372. PMID: 9632833. 