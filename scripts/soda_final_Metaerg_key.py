# Converted from soda_final_Metaerg_key.ipynb
# Clean Python script generated from the uploaded Jupyter notebook.
# Notebook outputs were removed from the cleaned .ipynb version.

# %% Cell 1
import os
import pandas as pd
from pandas import ExcelWriter

os.chdir(r"/Users/ruchitasolanki/Downloads/Cyano_paper/RNA_data_analysis")
print('Reading tpm file...')
names = pd.read_csv("/Users/ruchitasolanki/Downloads/Cyano_paper/RNA_data_analysis/name_to_keyword_mapping.csv")

print('Making categories...')
keyword_categories = {
    "Aminoacid biosynthesis": [
        r"Alanine transaminase", r"aminotransferase", r'Asparagine', r'Glutamate', r'Glutamine',
        r'Phosphoglycerate', r'Phosphoserine', r'Serine', r'Cysteine', r'Selenocysteine',
        r'serine hydroxymethyltransferase', r'Threonine aldolase', r'Acetolactate', r'Ketol-acid',
        r'Dihydroxyacid', r'transaminase', r'Isopropylmalate', r"MAG: imidazole glycerol phosphate synthase subunit HisH", 
        r"imidazole glycerol phosphate synthase subunit HisF", r"pyrroline-5-carboxylate reductase"
        r"aminopeptidase", r"metallopeptidase", r"carbamoylputrescine amidase", r"carboxyl-terminal protease",
        r"agmatine deiminase family protein", r"transcription termination/antitermination protein NusA",
        r"ribonucleoside-diphosphate reductase subunit alpha", r"AMP-binding protein",
        r"GTPase-activating protein", r"aspartate kinase", r"threonine-phosphate decarboxylase",    
        r"argininosuccinate lyase", r"histidine ammonia-lyase", 
        r"bifunctional GTP diphosphokinase/guanosine-3',5'-bis pyrophosphate 3'-pyrophosphohydrolase",
        r"Fic family protein", r"transcription antitermination factor NusB", r"diaminopimelate decarboxylase",
        r"N-succinylarginine", r"biosynthetic arginine decarboxylase", r"imidazolonepropionas", 
        r"urocanate hydratase", r"phenylalanine", r"oligopeptidase A"
        r"N-alpha-acetyl diaminobutyric acid deacetylase DoeB",
        r"ArgE/DapE family deacylase", r"tryptophan synthase subunit alpha", r"histidinol-phosphatase",     
        r"dihydrodipicolinate synthase family protein", r"ornithine cyclodeaminase", 
        r"2,3,4,5-tetrahydropyridine-2,6-dicarboxylate N-succinyltransferase",
        r"anthranilate synthase", r"ribosome recycling factor",
        r"ornithine carbamoyltransferase", r"MAG: adenosylmethionine decarboxylase", 
        r"gamma-glutamyltransferase", 
        r"dipeptidase", r"N-alpha-acetyl diaminobutyric acid deacetylase DoeB", r"MAG: GcvT family protein" 
    ],
    'Carbon fixation': [r'rbcL', r"rbcS", r"form I ribulose bisphosphate carboxylase large subunit", 
        r"ribulose bisphosphate carboxylase small subunit", r"rubredoxin", r"phosphoribulokinase"],
    "CCM": [r"CcmK", r"CcmL", r"carbonic anhydrase"],
    "Cell Envelope": [
        r"porin", r"D-alanine-D-alanine", r"Alanine racemase", r"Mur", r"Mra", r"Peptidoglycan",
        r"FtsX-like permease family protein", r"UDP-N-acetylglucosamine", r"TolB", r"LicD family protein",
        r"D-alanine--D-alanine ligase", r"LicD family protein", r"UDP-3", r"chain length", 
        r"primosomal replication protein", r"MinD/ParA family protein",
        r"cell division topological specificity factor MinE", r"sugar transferase", 
        r"DNA topoisomerase IV subunit A", r"rod shape-determining protein MreC", r"prolipoprotein diacylglyceryl transferase", 
        r"AsmA family protein", r"DNA polymerase III subunit alpha", r"choice-of-anchor K domain-containing protein", 
        r"penicillin-binding protein", r"D-alanyl-D-alanine carboxypeptidase", r"cardiolipin synthase", 
        r"cardiolipin synthase", r"lipid-A-disaccharide synthase", r"prolipoprotein diacylglyceryl transferase", 
        r"HU family DNA-binding protein", r"MAG: carbohydrate kinase"
    ],
    "Cell division": [
        r"septal", r"cell division protein", r"septum", r"MAG: chromosomal replication initiator protein DnaA",
        r"acetate--CoA ligase", r"septation protein IspZ", r"chromosome segregation protein SMC", 
        r"DNA polymerase III subunit delta", r"4-hydroxy-3-polyprenylbenzoate decarboxylase",
        r"glycerol-3-phosphate cytidylyltransferase", r"ParB/RepB/Spo0J family partition protein", 
        r"type I DNA topoisomerase"
    ],
    "Citric acid": [
        r"Pyruvate dehydrogenase", r"Pyruvate/2-oxoglutarate dehydrogenase", r'Citrate synthase',
        r'Aconitase', r'Isocitrate dehydrogenase', r'2-Oxoglutarate dehydrogenas', r'Succinyl-CoA synthetase',
        r'Succinate dehydrogenase', r'Fumarate hydratase', r'Malate', r'Isocitrate Lyase', r'Acetyl-CoA', r"NAD",
        r"aconitate hydratase AcnA", r"ADP-forming succinate",
        r"2-oxoacid:ferredoxin oxidoreductase subunit beta",
        r"NADP-dependent isocitrate dehydrogenase", r"pyruvate carboxylase", r"succinate--CoA ligase subunit alpha"
    ],
    "Cofactor: Menaquinol/Phylloquinol (Vitamin K)": [
        r"Menaquinol", r"Phylloquinol", r"menaquinone-specific isochorismate synthase", 
        r"2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate synthase",
        r"2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate synthase", r"o-succinylbenzoate synthase", 
        r"o-succinylbenzoate---CoA ligase", r"naphthoate synthase", r"1,4-dihydroxy-2-naphthoyl-CoA hydrolase",
        r"1,4-dihydroxy-2-naphthoate polyprenyltransferase", r"demethylmenaquinone methyltransferase",
        r"2-carboxy-1,4-naphthoquinone phytyltransferase", r"demethylphylloquinone reductase", 
        r"vitamin K epoxide reductase family protein",
        r"demethylphylloquinol methyltransferase", r"\bmen[A-G]\b", r"\bphylloquinone\b"
    ],
    "Cofactor: Ubiquinol (CoQ)": [
        r"Ubiquinol", r"chorismate lyase", r"chorismate lyase / 3-hydroxybenzoate synthase",
        r"4-hydroxybenzoate polyprenyltransferase", r"4-hydroxy-3-polyprenylbenzoate decarboxylase",
        r"2-polyprenylphenol 6-hydroxylase", 
        r"2-polyprenyl-6-hydroxyphenyl methylase / 3-demethylubiquinone-9 3-methyltransferase",
        r"2-octaprenyl-6-methoxyphenol hydroxylase", r"flavin prenyltransferase",
        r"3-demethoxyubiquinol 3-hydroxylase", 
        r"3-demethoxyubiquinol 3-hydroxylase", r"2-\(all-trans-polyprenyl\)phenol 6-hydroxylase \(prep\\henate\) UbiU",
        r"2-\(all-trans-polyprenyl\)phenol 6-hydroxylase \(prep\\henate\) accessory factor",
        r"\bUbi[ABCDEGHIKLMNOPQRX]\b", # General Ubi genes/terms
    ],
    "Cofactor: Tocopherol/Tocotrienol (Vitamin E)": [
        r"Tocopherol", r"Tocotrienol", r"homogentisate phytyltransferase", 
        r"homogentisate geranylgeranyltransferase", r"MPBQ/MSBQ methyltransferase", 
        r"tocopherol cyclase", r"tocopherol O-methyltransferas",
    ],
    "Cofactor: Heme/Siroheme": [
        r"Heme", r'Polyprenyltransferase', r"\bhem[A-Z]\b", r"\bporphyrin\b", 
        r"magnesium chelatase ATPase subunit I", r"5-aminolevulinate synthase", 
        r"glutamyl-tRNA reductase", r"glutamate-1-semialdehyde 2,1-aminomutase", 
        r"orphobilinogen synthase", r"hydroxymethylbilane synthase", r"uroporphyrinogen-III synthase", 
        r"uroporphyrinogen III methyltransferase / synthase", r"uroporphyrin-III C-methyltransferase", 
        r"hydrogen peroxide-dependent heme synthase", r"(2Fe-2S)-binding protein", 
        r"ferrochelatase\b", r"\bFC\s*H\b", r"magnesium-protoporphyrin IX monomethyl ester (oxidative) cyclase", 
        r"uroporphyrinogen decarboxylase", r"\bUroD\b", r"sirohydrochlorin chelatase", 
        r"protoporphyrinogen/coproporphyrinogen III oxidase", r"\b(Protoporphyrinogen|Coproporphyrinogen) oxidase\b",
        r"sirohydrochlorin ferrochelatase", r"precorrin-2 dehydrogenase", r"\bCysG\b", r"\bSirA\b",
        r"urobilinogen-III methylase", 
    ],
    "Cofactor: Cobalamin (Vitamin B12)": [
        r"\bcobalamin\b", r"\bB12\b", r"\bprecorrin\b|\bcbi|cob[A-Z]\b", 
        r"adenosylcobalamin-dependent ribonucleoside-diphosphate reductase",
        r"B12-binding domain-containing protein", r"cobalt-precorrin-6A reductase",
        r"sirohydrochlorin ferrochelatase", r"sirohydrochlorin cobaltochelatase",
        r"sirohydrochlorin cobalt/nickelchelatase", r"cobaltochelatase\s*CobN\b",
        r"uroporphyrinogen III methyltransferase / synthase", r"uroporphyrin-III C-methyltransferase",
        r"precorrin-2 dehydrogenase", r"precorrin-2 C20-methyltransferase", r"precorrin-3B synthase",
        r"precorrin-3B C17-methyltransferase", r"cobalt-precorrin 5A hydrolase", 
        r"cobalt-factor III methyltransferase", r"precorrin-4/cobalt-precorrin-4 C11-methyltransferase",
        r"precorrin-6A/cobalt-precorrin-6A reductase", 
        r"precorrin-6B C5,C15-methyltransferase", r"cobalt-precorrin-8 methylmutase",
        r"cobyrinic acid a,c-diamide synthase",
        r"cob\(I\)alamin adenosyltransferase", r"adenosylcobyrinic acid synthase",
        r"adenosylcobinamide-phosphate synthase", r"cobalamin biosynthesis protein CobC",
        r"adenosylcobinamide kinase / adenosylcobinamide-phosphate guanylyltransferase",
        r"nicotinate-nucleotide--dimethylbenzimidazole phosphoribosyltransferase",
        r"alpha-ribazole phosphatase", r"adenosylcobinamide-GDP ribazoletransferase",
    ],
    "Cofactor: Riboflavin (Vitamin B2)": [
        r"GTP cyclohydrolase II", r"3,4-dihydroxy 2-butanone 4-phosphate synthase / GTP cyclohydrolase II",
        r"diaminohydroxyphosphoribosylamino-pyrimidine deaminase", r"phosphoribosyltransferase",
        r"5-amino-6-(5-phosphoribosylamino)uracil reductase", r"aspartate carbamoyltransferase catalytic subunit", 
        r"5-amino-6-(5-phospho-D-ribitylamino)uracil phosphatase",
        r"FMN hydrolase", r"riboflavin kinase / FMN adenylyltransferase", r"FAD synthetase",
        r'6,7-?dimethyl-8-?ribityllumazine synthase|\bRibE\b|\briboflavin\b',
        r'\bRib[A-D]\b', r'FAD:protein FMN transferase', 
        r"2,5-diamino-6-\(ribosylamino\)-4\(3H\)-pyrimidinone 5'-phosphate reductase",
        r"tRNA pseudouridine32 synthase"
    ],
    "Cofactor: Folates": [
        r"GTP cyclohydrolase I[A-B]?", r"3,4-dihydroxy 2-butanone 4-phosphate synthase / GTP cyclohydrolase II",
        r"2,5-diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one isomerase/dehydratase",
        r"alkaline phosphatase", r"dihydroneopterin triphosphate diphosphatase", 
        r"dihydroneopterin triphosphate pyrophosphohydrolase", r"dihydroneopterin aldolase", 
        r"7,8-dihydroneopterin aldolase/epimerase/oxygenase", r"dihydrofolate synthase / folylpolyglutamate synthase",
        r"dihydrofolate reductase", r"thymidylate synthase", r"6-pyruvoyl-tetrahydropterin/6-carboxy-tetrahydropterin synthase",
        r"sepiapterin reductase", r"2-amino-4-hydroxy-6-hydroxymethyldihydropteridine diphosphokinase",
        r"\bfol[A-Z]\b", r"dihydropteroate synthase", r"dihydroneopterin aldolase", 
        r"formate--tetrahydrofolate ligase", r"5-formyltetrahydrofolate cyclo-ligase", 
        r"5,10-methylenetetrahydrofolate reductase", r"L-threoTetrafolate", r"\bPTPS-III\b"
    ],
    "Cofactor: Pyrroloquinoline Quinone (PQQ)": [
        r"pyrroloquinoline quinone", r"\bPQQ\b", r"\bQue[DEF]\b|\bpreQ0\b|\b7-?carboxy-7-?deazaguanine\b", 
        r"MAG: 6-carboxytetrahydropterin synthase"
    ],
    "Cofactor: NAD (Niacin/Vitamin B3)": [
        r"\bNAD\b", r"\bNADH\b", r"\bNADP\b", r"nicotinate-nucleotide", r"nicotinamide mononucleotide",
        r"tryptophan 2,3-dioxygenase", r"indoleamine 2,3-dioxygenase", r"arylformamidase", 
        r"kynurenine formamidase", r"kynurenine 3-monooxygenase", r"kynureninase", 
        r"3-hydroxyanthranilate 3,4-dioxygenase", r"nicotinate-nucleotide pyrophosphorylase \(carboxylating\)",
        r"nicotinate-nucleotide adenylyltransferase", r"nicotinamide mononucleotide adenylyltransferase", 
        r"NAD\+ synthase \(glutamine- hydrolysing\)", r"NAD\+ synthase", r"tryptophan synthase"
    ],
    "Cofactor: Thiamine (Vitamin B1)": [
        r"\bthi[A-Z]\b", r"\bthiamine\b", r"thiazole synthase", r"sulfur carrier protein ThiS adenylyltransferase",
        r"sulfur carrier protein", r"tRNA uracil 4-sulfurtransferase", r"2-iminoacetate synthase",
        r"phosphomethylpyrimidine synthase", r"hydroxymethylpyrimidine/phosphomethylpyrimidine kinase",
        r"thiamine-phosphate pyrophosphorylase", r"thiamine-monophosphate kinase",
        r"glycine oxidase", r"thiazole tautomerase", r"sulfide-dependent adenosine diphosphate thiazole synthase",
        r"thiamine-phosphate diphosphorylase", r"hydroxyethylthiazole kinase", r"rhodanese-like domain-containing protein"
    ],
    "Cofactor: Pyridoxine (Vitamin B6)": [
        r"\bpdx[A-Z]\b", r"\bpyridoxine\b",
        r"D-erythrose 4-phosphate dehydrogenase", r"erythronate-4-phosphate dehydrogenase",
        r"phosphoserine aminotransferase", r"4-hydroxythreonine-4-phosphate dehydrogenase",
        r"pyridoxine 5-phosphate synthase", r"pyridoxamine 5'-phosphate oxidase",
    ],
    "Cofactor: Coenzyme F420": [
        r"\bcoenzyme F420\b|\bfbi[ABCDE]\b|\bcof[GH]\b|\bF\ *420\b|\bF420 hydrogenase\b",
    ],
    "Cofactor: Biotin": [
        r"\bbio[A-Z]\b", r"bifunctional biotin", r"biotin-dependent carboxyltransferase",
    ],
    "Cofactor: Pantothenate/CoA": [
        r"\bpan[A-Z]\b", r"\bpantothenate\b", r"\bcoa[A-Z]\b", r"\bcoenzyme A\b", r"formate C-acetyltransferase", 
        r"pantetheine", r"N-acetyltransferase", r"pantetheine-phosphate adenylyltransferase", 
        r"4'-phosphopantetheinyl transferase superfamily protein", r"dephospho-CoA kinase",
    ],
    "Cofactor: Lipoic Acid": [
        r"\blip[A-L]\b", r"\blipoic acid\b", r"lipoyl synthase",
    ],
    "Cofactor: Molybdenum Cofactor (MoCo)": [
        r"\bmoe[A-Z]\b", r"\bmog[A-Z]\b", r"\bmob[A-Z]\b", r"\bmolybdenum cofactor\b",
        r"MOCO", r"molybdopterin adenylyltransferase", r"molybdopterin-dependent oxidoreductase", 
        r"Gfo/Idh/MocA family oxidoreductase", r"GTP 3',8-cyclase MoaA", 
        r"cyclic pyranopterin monophosphate synthase MoaC", r"molybdopterin-binding protein",
    ],
    "Precursor: Shikimate/Aromatic": [
        r"\bshikimate\b|\bAro[ABCDEFG]\b|\bchorismate\b",
        r"3-?deoxy-7-?phosphoheptulonate|\bDAHP\b", r"aminodeoxychorismate synthase component I",
        r"3-phosphoshikimate 1-carboxyvinyltransferase",
    ],
    "Precursor: Purine/Pyrimidine": [
        r"\bpreQ1\b", r"\btruB\b", r"dUTP diphosphatase", r"dTMP kinase", 
        r"carboxylating nicotinate-nucleotide diphosphorylase", r"orotate phosphoribosyltransferase", 
        r"phosphoribosylformylglycinamidine cyclo-ligase", r"phosphoribosylamine--glycine ligase",
        r"5-(carboxyamino)imidazole ribonucleotide synthase", r"adenylosuccinate lyase", 
        r"phosphoribosylglycinamide formyltransferase", r"ykkC-yxkD Guanidine-I riboswitch", 
        r"phosphoribosylaminoimidazolesuccinocarboxamide synthase", r"ydaO-yuaA ydaO/yuaA leader", 
        r"anaerobic ribonucleoside-triphosphate reductase",
        r"LOG family protein", r"adenine phosphoribosyltransferase", r"amidophosphoribosyltransferase",
        r"adenylosuccinate synthase", r"thymidylate synthase",
    ],
    "Cofactor: Others": [
        r"component of SufBCD complex", r"hydrogenase formation protein HypD", 
        r"dehydrogenase\b",
        r"\bHpsN\b", r"inorganic diphosphatase", r"Fe-S biogenesis protein NfuA",
        r"Fe-S cluster assembly protein SufD", r"dipeptidase PepE", r"bifunctional salicylyl-CoA", 
        r"ibonucleotide reductase subunit alpha",
        r"2_alkali_proteins.clustering.xlsxadenosine deaminase family protein",
        r"adenosylhomocysteinase", 
    ],
    "Defense": [
        r"Defense", r"cas", r"CRISPR", r"RAMP superfamily", r"viral", r"excinuclease ABC",
        r"extracellular endonuclease", r"TraB/GumN family protein", r"gamma-glutamylcyclotransferase",
        r"RluA family pseudouridine synthase", r"DNA polymerase III subunit epsilon", 
        r"DNA mismatch repair endonuclease MutL", r"excinuclease ABC subunit UvrB", r"peroxiredoxin", 
        r"peroxide stress", r"DNA recombination protein", r"reverse transcriptase domain-containing protein, partial", 
        r"LON peptidase substrate-binding domain-containing protein", r"CHAT domain-containing protein", 
        r"SOS response-associated peptidase", r"glutathione S-transferase (GST) family protein", 
        r"bifunctional DNA-formamidopyrimidine glycosylase/DNA-(apurinic or apyrimidinic site) lyase",
        r"Holliday junction branch migration protein RuvA", r"glyoxalase-like domain protein", 
        r"recombinase family protein", r"restriction endonuclease subunit S", 
        r"TPA: type I restriction endonuclease subunit R", r"MIR1437 MIR1437 microRNA precursor family", 
        r"bifunctional DNA-formamidopyrimidine glycosylase", r"Mu-like prophage major head subunit gpT family protein", 
        r"alpha-2-macroglobulin family protein", r"phage holin family protein", 
        r"ATP-dependent endonuclease", r"MAG: glutathione S-transferase family protein",    
        r"glutathione peroxidase", r"arsenate reductase", r"tellurium resistance protein",
        r"recombinase RecA", r"DNA mismatch repair protein MutS", r"Holliday junction resolvase RuvX", r"double-strand break repair protein AddB",
        r"DNA primase", r"deoxyribodipyrimidine photo-lyase", r"transcriptional repressor LexA", 
        r"virulence factor", r"Mu-like prophage major head subunit gpT family protein",
        r"ATP-dependent endonuclease", r"glutathione S-transferase", r"arsenical resistance protein ArsH",  
        r"DNA alkylation repair protein", r"uracil-DNA glycosylase", 
        r"cisplatin damage response ATP-dependent DNA ligase", 
        r"DNA starvation/stationary phase protection protein", r"recombination mediator RecR", r"recombinase/integrase",
        r"Holliday junction resolvase RuvX", r"endonuclease/exonuclease/phosphatase family protein"
    ],
    "Ectoine": [
        r"ectoine", r"diaminobutyrate", r"Dab", r"Ect[A-C]", r"ectoine synthase"
    ],
    "EPS": [
        r"PEP-CTERM", r"alginate export family protein", r"arginine N-succinyltransferase", r"alginate export family protein"],
    "Fatty acid": [
        r"acyl-carrier-protein", r'C-acyltransferase',
        r'Fatty', r"beta-ketoacyl-ACP synthase",
        r"cyl-CoA dehydrogenase C-terminal domain-containing protein", r"DNA repair protein RadA", r"lipase",
        r"acyl-CoA carboxylase subunit beta"],
    "Glycolysis": [
        r"Hexokinase", r"glucokinase", r'Glucose-6-phosphate-isomerase', r'Phosphofructokinase',
        r'Fructose-bisphosphate', r'Triosephosphate isomerase', r'Glyceraldehyde-3-phosphate', r'Phosphoglycerate',
        r'Phosphopyruvate', r'Pyruvate', r"sugar-phosphate isomerase", r"1,4-alpha-glucan branching protein GlgB",
        r"protein phosphatase CheZ", r"alpha-amylase family", r"glycerol kinase GlpK", r"RpiA",
        r"Ldh family oxidoreductase", r"transketolase", r"triose-phosphate isomerase", 
        r"glucan biosynthesis protein D", r"glucose-1-phosphate adenylyltransferase", 
        r"glucans biosynthesis glucosyltransferase MdoH", 
        r"class II fructose-bisphosphatase" 
    ],
    "Hypothetical protein": [r"hypothetical"],
    "Hydrogen oxidation": [
        r'NiFe Hydrogenase', r"FeFe Hydrogenase", r'hox', r'ech Hydrogenase', r"HupU protein", 
        r"nickel-dependent hydrogenase large subunit", r"hydrogenase nickel incorporation protein HypB"],
    "Inositol_phosphate_biosynthesis": [
        r"Phosphoinositide phospholipase", r"Inositol", r'Triosephosphate', r'Fructose-1,6-bisphosphate',
        r'Phospholipase', r'phosphocholine', r"endonuclease III"],
    "Iron storage": [
        r"Bacterioferritin", r"Ferritin"],
    "Methylation": [
        r"SAM-dependent", r"50S ribosomal protein L11 methyltransferase", r"protein meaA",
        r"TrmD", r"16S rRNA (uracil(1498)-N(3))-methyltransferase",
        r"RNA methyltransferase", r"methyltransferase", r"sulfotransferase", r"adenosyltransferase"],
    "Modifying enzymes": [
        r"\bcytochrome P450\b|\bCYP\d+", r"antibiotic biosynthesis monooxygenase",
        r"2OG-?Fe\(II\) oxygenase", r"\bSDR family oxidoreductase\b",
        r"\bFAD-?dependent (hydroxylase|monooxygenase)\b",
        r"glycosyltransferase( family)?", 
        r"\bO-?methyltransferase\b|\bN-?methyltransferase\b|\bC-?methyltransferase\b",
        r"epimerase\b", r"halogenase|flavin-?dependent halogenase|prnA|rebH|thaL",
        r"Baeyer-?Villiger monooxygenase|BVMO",
        r"acyl-CoA ligase|AMP-?dependent synthetase", r"YciK family oxidoreductas", 
        r"signal peptidase", r"GNAT family", r"CoA transferase subunit", r"propionyl-CoA", 
        r"trans-2-enoyl-CoA reductase family protein", r"peptide-methionine", r"exo-alpha-sialidase",
        r"glycosyl hydrolase family 3", r"methionine gamma-lyase family protein", 
        r"CoA transferase", r"acyl-CoA synthetase", r"glycosyl transferase",
        r"transglutaminase family protein", r"phosphoglucosamine mutase", 
        r"alpha-D-glucose phosphate-specific phosphoglucomutase", r"alpha-D-glucose phosphate-specific phosphoglucomutase", 
        r"glycerophosphodiester phosphodiesterase", r"LarC family nickel insertion protein", 
        r"glyceride hydrolase family 15 protein",
        r"gamma-glutamyltransferase",
        r"hydrolase", r"acetate/propionate family kinase", r"alpha-hydroxy-acid oxidizing protein", r"amidase", 
        r"creatininase family protein", r"crotonyl-CoA carboxylase/reductase", 
        r"carboxyltransferase domain-containing protein", r"thymidine phosphorylase", r"phosphoglycolate phosphatase"
    ],
    "Motility": [
        r"Flagellar", r"flagellin", r'pilin', r'Pilus', r'PilM', r"chemotaxis protein", r"FtsE"],
    "Nitrogen cycle": [
        r"Hydrazine", r"nitrate", r'Nitrite', r'Heme-copper', r'nitric', r'Nitrous', r"Circadian oscillating protein COP23", 
        r'Pmo', r'Smmo', r'hao', r'Nitrogenase', r'Urease', r'Urea', r'Cyanate lyase', r"COP23 domain-containing protein", 
        r'Nitrile', r'nif', r'ure', r'urt', r'nap', r'octR', r'nrf', r"global nitrogen regulator NtcA", 
        r"nitrogen regulation protein", r"NnrS", r"nitrilase"], 
    "Non-ribisomal peptide synthetase": [
        r"\bNRPS\b", r"\bPKS\b", r"prodigiosin",
        r"amino acid adenylation domain", r"\bAdenylation\b|\bA\s*domain\b",
        r"\bcondensation\b|\bC\s*domain\b", r"betalactone",
        r"\bPCP\b|\bpeptidyl carrier protein\b",
        r"thioesterase\b|\bTE\s*domain\b",
        r"\bACP\b|\bacyl carrier protein\b",
        r"\bKS\b|\bketosynthase\b",
        r"beta-?ketoacyl-?ACP", r"\bKR\b|\bketoreductase\b",
        r"\bDH\b|\bdehydratase\b", r"\bER\b|\benoylreductase\b",
        r"\bAT\b|\bacyltransferase\b", r"\bTE\b|\bthioesterase\b",
        r"\btrans-AT\b|\bstandalone acyltransferase\b",
        r"thioester reductase\b|\bR\s*domain\b",
        r"starter unit( acyltransferase)?",
        r"acyltransferases", r"pre-peptidase C-terminal domain-containing protein",
        r"hydroxymethylglutaryl-CoA lyase",
        r"type I polyketide synthase", r"non-ribosomal peptide synthetase"
    ], 
    "Other elements": [
        r"Arsenite", r'Tetrachloroethene', r'PceA', r'Rdh', r'2-Haloacid', r"Decaheme", r'DMSO',
        r'Selenate', r'chlorate', r'selenate', r"UMP kinase", r"(d)CMP kinase", 
        r"polyphosphate kinase 2", r"5-oxoprolinase", r"allantoinase PuuE", r"D-lyxose/D-mannose family sugar isomerase",
        r"3-carboxy-cis,cis-muconate cycloisomerase",
        r"protocatechuate 3,4-dioxygenase subunit alpha",
        r"carboxymuconolactone decarboxylase family protein",
        r"intradiol ring-cleavage dioxygenase", r"guanine deaminase", r"nucleoside-diphosphate kinase", 
        r"adenylate kinase", r"ribose-phosphate pyrophosphokinase", r"phenylacetic acid catabolic", 
        r"phenylacetate-CoA oxygenase subunit PaaJ family protein", r"fumarylacetoacetase", 
        r"aromatic ring-hydroxylating dioxygenase subunit alpha",
        r"deoxyguanosinetriphosphate triphosphohydrolase", 
        r"ribose-phosphate pyrophosphokinase", 
        r"3-alpha,7-alpha,12-alpha-trihydroxy-5-beta-choles t-24-enoyl-CoA hydratase", 
        r"maleylacetoacetate isomerase", 
        r"HutD family protein"
    ],
    "Peptidoglycan Remodeling": [
        r"RlpA", r"peptidase M23", r"L,D-transpeptidase", r"4-hydroxy-tetrahydrodipicolinate synthase"],
    "Phycocynin": [
        r"phycocyanin", r"phycobilisome", r"allophycocyanin", r"phycocyanin subunit alpha", 
        r"cyanophycinase", r"phycobiliprotein lyase"],
    "Photosystems": [
        r"Photosystem", r"Bacteriorhodopsin", r"psb", r"psa", r"petA", r"petB", r"photosynthesis system II assembly factor Ycf48", 
        r"petC", r"petD", r"petE", r"petF", r"petH", r"ferredoxin", r"photosynthetic", r"MAG: Rieske (2Fe-2S) protein", 
        r"c-type cytochrome biogenesis protein CcsB", r"cytochrome c biogenesis protein CcdA",
        r"puhA", r"pufA", r"pufB", r"pufC", r"pufM", r"pufL", r"chlorophyll", r"cytochrome b559", r"Calvin cycle protein CP12"],
    "Quorum Sensing": [
        r"N-acyl homoserine lactones", r"\bAHL\b", r"\bLuxI\b", r"\bLuxR\b", r"quorum sensing"
    ],
    "Regulatory & Transport Genes": [
        r"\bTetR/AcrR\b|\bTetR\b", r"\bSARP\b", r"\bLAL regulator\b|\bLuxR-like\b|\bLuxR\b",
        r"\bMarR\b|\bMerR\b|\bLysR\b|\bAraC\b|\bXRE\b|\bsigma factor\b", r"RNA-guided endonuclease TnpB family protein", 
        r"diguanylate cyclase|GGDEF|EAL domain", r"ComF family protein",
        r"\bMFS transporter\b|\bABC transporter\b|\bRND efflux\b|\bMATE\b|\bSMR\b|\bpermease\b|\befflux pump\b",
        r"\bTonB-?dependent receptor\b", r"pca operon transcription factor PcaQ",
        r"\bPhzF family phenazine\b", r"PAS domain-containing protein", r"GTP-binding proteins",
        r"GntR family transcriptional regulator", r"PilZ", r"BolA family transcriptional regulator",
        r"integration host factor subunit beta", r"H-NS histone family protein", r"AAA family ATPase",
        r"transcriptional regulator", r"sigma D regulator", r"sigma E", r"DeoR", r"HAMP domain", 
        r"TraR/DksA C4", r"DNA-binding protein HU-beta", r"ntegration host", r"DksA",
        r"histidine kinase", r"GcrA cell cycle regulator", r"PAS domain S-box protein", 
        r"cyclic nucleotide-binding domain-containing protein", r"transcriptional repressor", 
        r"PAS domain-containing sensor histidine kinase", r"magnesium chelatase ATPase subunit D",
        r"MAG: Sensor protein FixL", r"heterocyst differentiation master regulator HetR",
        r"AbrB/MazE/SpoVT family DNA-binding domain-containing protein", r"oxidoreductase"
        r"CopG family ribbon-helix-helix protein", r"PatU", r"phosphohistidine phosphatase SixA",
        r"ATP phosphoribosyltransferase regulatory subunit", r"ATP-dependent Clp protease ATP-binding subunit", 
        r"ribbon-helix-helix domain-containing protein", r"NsiR1 Nitrogen stress-induced RNA 1", 
        r"nodulation protein NfeD", r"histone deacetylase", r"metalloregulator ArsR/SmtB family transcription factor", 
        r"DNA topoisomerase (ATP-hydrolyzing) subunit A", r"protease complex subunit PrcB family protein", 
    ],
    "Resistance Genes": [
        r"macrolide 2'-?phosphotransferase",
        r"aminoglycoside (acetyltransferase|phosphotransferase|nucleotidyltransferase)",
        r"\bvan[HAXYZW]\b", r"\bble\b|\bbleomycin resistance\b",
        r"\bdrrA\b|\bdrrB\b|\bdrrAB\b", r"pentapeptide repeat-containing protein",
        r"target protection|self-?resistance|antibiotic resistance protein"],
    "Respiration": [
        r"F0F1", r"Vacuolar", r'ATP synthase', r'NADH:ubiquinone', r"cofactor assembly of complex C subunit B", 
        r'Cytochrome b6/f', r'Plastocyanin', r'Rieske Fe-S', r"cytochrome-c peroxidase",
        r'quinol dependent', r'Heme/copper oxidase', r'Cyrochrome bd', r"group 1 truncated hemoglobin",
        r'Electron transport', r'Proton/sodium translocating pyrophosphatase',
        r"ndh", r"nuo", r"nqr", r"cytochrome c oxidase", r"cytochrome c1", r"cytochrome c", 
        r"cytochrome ubiquinol oxidase subunit I", r"ETC complex I subunit", r"quinoprotein", 
        r"cytochrome-c", r"cbb3-type subunit I",  r"cytochrome B6", r"apocytochrome f",
        r"cytochrome b6-f complex iron-sulfur subunit", r"cytochrome B6-F complex subunit VI (PetL)",
        r"c-type cytochrome",  r"cytochrome bd-I oxidase subunit CydX", r"ssl1498 family light-harvesting-like protein", 
        r"electron transfer flavoprotein subunit beta/FixA family protein"
    ],
    "Retrotransposon": [r"LTR retrotransposon"],
    "Ribosomal Proteins": [
        r"Ribosomal protein", r"ribosome modulation factor", r"ribosome maturation factor RimM",r"ribosome biogenesis GTPase Der",
        r"translation initiation factor IF-3", r"ABC-F family ATPase0", r"ribosome biogenesis GTPase YlqF",
        r"elongation factor Tu", r"translational GTPase TypA", r"elongation factor", r"cytochrome B", 
        r"energy-dependent translational throttle protein EttA", r"translation initiation", r"ribosome silencing factor", 
        r"RNA-binding S4 domain-containing protein", r"ribosome small subunit-dependent GTPase A", 
        r"GTPase ObgE", r"GTPase Era", r"GTPase HflX", r"16S rRNA processing protein RimM", r"HEARO", 
        r"HPF/RaiA family ribosome-associated protein",  r"peptide chain release factor 3", 
        r"peptide deformylase"],
    "Ribozyme Activity": [
        r"RNase P RNA component class A"],
    "Ribosomally synthesized and post-translationally modified peptide": [
        r"\bRiPP\b", r"\bprecursor peptide\b", r"\bleader peptide\b", 
        r"tRNA-dependent cyclodipeptide synthases", r"\bCDPS\b",
        r"lanthipeptide|Lan(B|C|M|A|K)|class [I-V] lanthipeptide",
        r"lasso ?peptide|lasso cyclase|Lpt[BCE]",
        r"thiopeptide|Tcl|ThiF|YcaO|TfuA",
        r"sactipeptide|radical SAM|rSAM",
        r"linaridin|LinM|LinD", r"cupin-like domain-containing protein", 
        r"microviridin|Mdn", r"metalloprotease TldD", 
        r"cyanobactin|Pat[A-E]|Tru[A-E]",
        r"LAP\b|linear azol(in|)e-?containing",
        r"bottromycin|Btm",
        r"glycocin|bacteriocin|\bTIGR\d+",
        r"RiPP precursor", r"TldD/PmbA", r"family peptidase", r"YcaO-like family protein",
        r"lantibiotic dehydratase",
    ],
    "RNA processing": [
        r"ribonuclease", r"bifunctional 2',3'-cyclic-nucleotide 2'-phosphodiesterase/3'-nucleotidase",
        r"RNA polymerase-associated", r"RNA chaperone", r"translation elongation factor",
        r"YqgE/AlgH family protein",  r"RNA pseudouridine synthase", 
        r"multifunctional 2',3'-cyclic-nucleotide 2'-phosphodiesterase/5'-nucleotidase/3'-nucleotidase",
        r"DNA polymerase III subunit gamma/tau", r"23S rRNA pseudouridine", r"DNA-directed RNA polymerase",
        r"NusG", r"polyribonucleotide nucleotidyltransferase", 
        r"2'-5' RNA ligase family protein", 
        r"rRNA pseudouridine synthase", 
        r"mRNA interferase MazF", 
        r"EndoU domain-containing protein", 
        r"Uma2 family endonuclease"],
    "rRNA": [
        r"23S ribosomal RNA", r"5S ribosomal RNA", r"16S ribosomal RNA"],
    "Siderophore": [
        r"\bsiderophore\b", r"SidA|IucD|PvdA", r"\bisochorismate\b|\bEntC\b|\bMenF\b",
        r"\benterobactin\b|\bEnt[A-F]\b|\bFep[ABCDG]\b",
        r"\bpvd[A-Z]\b|\bpch[A-Z]\b", r"\bybt[A-Z]\b|\byersiniabactin\b",
        r"\bNIS\b|\biuc[ABC]\b", r"TonB-?dependent receptor", r"\bFhu|Fec|Fep\b",
        r"\bdes[A-F]\b", r"\bFur\b"
    ],
    "Stress response": [
        r"DnaK", r"response regulator", r"CBS", r"GroES", r"GroEL", r"tyrosine-protein kinase domain-containing protein",
        r"alcohol dehydrogenase", r"HtpG", r"ClpB", r"HslO", r"DnaJ", r"RbcX chaperonin protein", 
        r"CsbD", r"Crp/Fnr", r"CHASE2", r"GrpE", r"thioredoxin", r"MAG: ATP-dependent Clp protease ATP-binding subunit ClpA",
        r"ATP-dependent protease ATPase subunit HslU", r"RNA polymerase factor sigma-32", r"chloride channel protein", 
        r"Hsp70", r"GerMN", r"VOCs", r"universal stress protein", r"HpsJ family protein", r"Hpt domain-containing protein", 
        r"mechanosensitive ion channel", r"STAS domain-containing protein", r"HEAT", r"metallothionein", 
        r"co-chaperone GroES", r"MAG: chaperonin GroEL", r"IsrR Antisense RNA which regulates isiA expression", 
        r"metallophosphoesterase", r"putative addiction module antidote protein", r"YraN family protein", 
        r"SpoIIE", r"VOC", r"Ppx/GppA", r"HtpG", r"FtsH", r"MAG: glycoside hydrolase family 65 protein",
        r"DNA-binding transcriptional regulator Fis", r"30S ribosome-binding factor RbfA", r"MAG: OstA family protein", 
        r"MAG: HslU--HslV peptidase ATPase subunit", r"co-chaperone DjlA", r"superoxide dismutase",
        r"FKBP-type peptidyl-prolyl cis-trans isomerase", r"YbjN domain-containing protein", 
        r"trypsin-like peptidase domain-containing protein",
        r"putative pyridoxal-dependent aspartate 1-decarboxylase", r"peptidylprolyl isomerase", r"cold shock", r"cold-shock",
        r"stress response", r"trigger factor", r"molec7ular chaperone", r"TorD family protein", r"PspA/IM30 family protein",
        r"peptidylprolyl isomerase", r"cspA cspA thermoregulator", r"CPP1-like family protein", r"PD40 domain-containing protein", 
        r"TerB family tellurite resistance protein", r"site-2 protease family protein", r"CPBP family intramembrane metalloprotease", 
        r"low molecular weight phosphotyrosine protein phosphatase", r"ATP-dependent Clp protease, protease subunit",
        r"MAPEG family protein", r"heavy-metal-associated domain-containing protein", r"protein phosphatase 2C domain-containing protein"
    ],
    "Sulfur cycle": [
        r"Adenylylsulfate", r"Sulfate", r"3-phosphoadenosine", r"phosphosulfate", r"Sulfite", r"Sulfur",
        r"Thiosulfate", r"Sulfide", r"Thiosulfohydrolase", r"S-disulfanyl-L-cysteine", r"Thiosulfate",
        r"Quinoprotein dehydrogenase", r'apr', r'dsr', r'sqr', r'fcc', r'sox', r"TauD/TfdA family dioxygenase"],
    "Terpenoids": [
        r"\bterpene\b|\bterpenoid\b", r"\bisoprenoid\b",
        r"GGPP|GGPPS|geranylgeranyl( diphosphate)? (synthase|reductase)",
        r"FPP|FPPS|farnesyl diphosphate synthase",
        r"\bidi\b|\bIPP isomerase\b|\bIsp[DFGH]\b|\bDXS\b|\bDXR\b|\bMEP\b|\bMVA pathway\b",
        r"phytoene (synthase|desaturase)|\bcrt(B|I|Y|E)\b|\bcarotenoid\b|\bcarotene\b",
        r"tocopherol cyclase", r"squalene|phytoene|hydroxysqualene",
        r"Red carotenoid-binding protein", r"\borange\b", r"4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol kinase", 
        r"4-hydroxy-3-methylbut-2-enyl diphosphate reductase", 
        r"flavodoxin-dependent (E)-4-hydroxy-3-methylbut-2-enyl-diphosphate synthase",
        r"polyprenyl synthetase family protein",
        r"2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase",
        r"isopentenyl-diphosphate Delta-isomerase", r"geranylgeranyl diphosphate synthase, type II", 
        r"15-cis-Phytoene Synthase", r"15-cis-Phytoene Desaturase", r"Zeta-Carotene Isomerase", 
        r"Zeta-Carotene Desaturase", r"Prolycopene Isomerase", r"Lycopene Cyclase", 
        r"Beta-Carotene Hydroxylase", r"\bcarotenoid\b", r"\bphytoene\b", r"\blycopene\b",
        r"diterpenoid", r"(E)-4-hydroxy-3-methylbut-2-enyl-diphosphate synthase", 
    ],
    "tmRNA": [r"transfer-messenger"],
    "Toxin antitoxin": [
        r"antitoxin", r"killer suppression", r"toxin-antitoxin", r"MAG: DNA gyrase inhibitor YacG", r"PilN domain-containing protein", 
        r"HigA family addiction module antitoxin", r"RebB like protein", r"ParE toxin", r"nuclear transport factor 2 family protein"],
    "Toxin/Cyanide": [
        r"hydrogen cyanide", r"HCN", r"FAD-binding oxidoreductase", r"FAD/NAD(P)-binding oxidoreductase",
        r"NAD(P)/FAD-dependent oxidoreductase", r"(2Fe-2S)-binding protein"
    ],
    "Transposase": [r"transposase", r"site-specific integrase", r"IS66 family", 
        r"IS200/IS605 family accessory protein TnpB-related protein"],
    "Transport": [
        r"Twin arginine-target", r"translocase", r"Signal recognition", r"TolC", r"Periplasmic linker", r"HlyB",
        r"Autotransported effector", r"secretion", r"Periplasmic", r"ExbB", r"cyanoexosortase B system-associated protein", 
        r"TonB", r"ExbD", r'porter', r"protein-export chaperone", r"AMIN domain-containing protein", 
        r"cation-transporting", r"outer membrane", r"GspE/PulE family protein", r"CDP-glycerol0", 
        r"Na+/H+ antiporter", r"antiporter", r"ntermembrane transport protein", r"CopD family protein",
        r"ABC transporter permease", r"CvpA family protein", r"LysE family translocator", 
        r"metabolite traffic protein EboE", r"MAG: FtsW/RodA/SpoVE family cell cycle protein", 
        r"DMT family protein", r"twin-arginine translocation signal domain-containing protein", 
        r"ABC-type transport auxiliary lipoprotein family protein", r"PH domain-containing protein", 
        r"LysE family translocator", r"ATP-dependent protease ATP-binding subunit ClpX", 
        r"transferrin-binding protein-like solute binding protein", r"PRC-barrel domain-containing protein", 
        r"heavy metal translocating P-type ATPase", r"tol-pal system protein YbgF", 
        r"translocation/assembly module TamB domain-containing protein",
        r"CDP-alcohol phosphatidyltransferase family protein", r"membrane protein insertion efficiency factor YidD"
        r"YidD", r"OmpA family protein",
        r"extracellular solute-binding protein", 
        r"SurA N-terminal domain-containing protein", 
        r"Tim44/TimA family putative adaptor protein"],
    "tRNA": [r"tRNA"],
    "Unknown": [
        r"DUF", r"Uncharacterized", r"YbaN family protein", r"cupin domain-containing protein", r"META domain",
        r"membrane protein insertase YidC", r"MAG: AAA-like domain-containing protein", 
        r"D-tagatose-bisphosphate aldolase, class II, non-catalytic subunit",
        r"fumarylacetoacetate", r"YaiI/YqxD", r"tetratricopeptide", r"Wzz/FepE/Etk N",
        r"class II aldolase/adducin family protein", r"P-II family nitrogen regulator",
        r"helix-turn-helix", r"metabolite traffic protein EboE", r"MAG: BMP family protein", 
        r"type III PLP-dependent enzyme", r"flavin reductase family protein", r"FAD-dependent oxidoreductase",
        r"4-hydroxybenzoate 3-monooxygenase", r"bifunctional salicylyl-CoA 5-hydroxylase/oxidoreductase",
        r"MAG: nitronate monooxygenase", r"CatB-related O-acetyltransferase", r"lipid-binding SYLF domain-containing protein", 
        r"EI24 domain-containing protein", r"EVE domain-containing protein", r"host attachment family protein", 
        r"N-acetylneuraminate synthase", r"carbon-nitrogen hydrolase family protein", r"edox-regulated ATPase YchF", 
        r"histidine phosphatase family protein", r"UDPGP type", r"AHH domain-containing protein", 
        r"PepSY domain-containing protein", r"histidine phosphatase family protein", 
        r"hydantoinase/oxoprolinase family protein", r"MoxR family ATPase", r"ribbon", r"YdcH family protein", 
        r"GSCFA domain-containing protein", r"FCD domain-containing protein", 
        r"right-handed parallel beta-helix repeat-containing protein", r"calcium-binding protein",
        r"NYN domain-containing protein", r"fasciclin domain-containing protein", 
        r"ridA family protein", r"2,4-dihydroxyhept-2-ene-1,7-dioic acid aldolase", 
        r"GTP-binding protein", r"globin domain-containing protein", 
        r"sensor domain-containing phosphodiesterase", r"YeeE/YedE family protein", r"MAG: Stealth CR1 domain-containing protein", 
        r"BON domain-containing protein", r"CAP domain-containing protein", r"SH3 domain-containing protein",
        r"MAG: VPEID-CTERM sorting domain-containing protein", r"Ycf66 family protein", 
        r"PIN domain-containing protein", r"FIST C-terminal domain-containing protein",
        r"MAG: BMP family protein", r"type III PLP-dependent enzyme",
        r"CinA family protein", r"LLM class flavin-dependent oxidoreductase",
        r"YIP1 family protein", r"sarcosine oxidase subunit beta family protein",
        r"MAG: methylmalonyl-CoA mutase", r"MAG: acetyl/propionyl/methylcrotonyl-CoA carboxylase subunit alpha",
        r"Hly-III family protein", r"B12-binding domain-containing protein", r"Hint domain-containing protein",
        r"aldol/keto reductase", r"penicillin acylase family protein", r"glycine zipper 2TM domain-containing protein",
        r"toprim domain-containing protein", r"GTP-binding protein", r"Mrp/NBP35 family ATP-binding protein", 
        r"cetyl/propionyl/methylcrotonyl-CoA carboxylase subunit alpha", r"flotillin", r"VWA domain-containing protein",
        r"ROK family protein", r"extensin family protein", r"Mth938-like domain-containing protein", r"TIM barrel protein",
        r"PhoH family protein", r"MOSC domain-containing protein",r"protein GlxC", r"phasin family protein", 
        r"UPF0262 family protein", r"YihY/virulence factor BrkB family protein",
        r"ATP-binding protein", r"circularly permuted type 2 ATP-grasp protein"
    ],
}
print('Saving resluts...')
results = {}
for category, keywords in keyword_categories.items():
    pattern = '|'.join(keywords)
    results[category] = names[names['#Name'].str.contains(pattern, case=False, na=False)]

# with ExcelWriter("name_categories.xlsx", engine='openpyxl') as writer:
#     for category, df in results.items():
#         if not df.empty:
#             df.to_excel(writer, sheet_name=category, index=False)
#         else:
#             print(f"{category} skipped.")

# print(f"Detailed data has been saved to name_categories.xlsx!")

# data = pd.DataFrame(columns=["Category"] + names.columns[1:].tolist())  
# for category, keywords in keyword_categories.items():
#     pattern = '|'.join(keywords)
#     filtered_df = names[names['#Name'].str.contains(pattern, case=False, na=False)]
#     row_data = {"Category": category}
#     for col in names.columns[1:]:  
#         row_data[col] = filtered_df[col].sum()

#     data = pd.concat([data, pd.DataFrame([row_data])], ignore_index=True)

# data.to_excel(f"keyword_category_sums.xlsx", index=False)
# print(f"Summaries has been saved to keyword_category_sums.xlsx")
    
# print(results)
# name_categories = pd.DataFrame.from_dict(results, orient="index")
# output_file = "name_categories.csv"
# name_categories.to_csv(output_file)

# Step 1: Create a list to hold the DataFrames with their category information
df_list = []

# Step 2: Iterate through the 'results' dictionary
for category_name, df_content in results.items():
    if not df_content.empty: # Only add if the DataFrame is not empty
        df_content['Category'] = category_name # Add the 'Category' column
        df_list.append(df_content)

# Step 3: Concatenate all DataFrames in the list
if df_list: # Check if the list is not empty before concatenating
    final_df = pd.concat(df_list, ignore_index=True)
else:
    final_df = pd.DataFrame() # Create an empty DataFrame if no results were found

# Display the resulting DataFrame
# print(final_df)
output_file = "Soda_newfinal_categories_wSMs.csv"
final_df.to_csv(output_file)
