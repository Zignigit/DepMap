import pandas as pd
from DepMapModule2 import CellDict, Comparison

base_name = 'Protein_Array.csv'
proteomics = pd.read_csv(base_name)

list1_resistant = ['HEL', 'HL60', 'KASUMI1', 'ML2' 'MOLM13' 'THP1', 'U937']
resist_depmap_ids = {'ACH-000004': 'HEL', 'ACH-000002': 'HL60', 'ACH-000263': 'KASUMI1', 'ACH-002273': 'ML2', 'ACH-000362': 'MOLM13', 'ACH-000146': 'THP1', 'ACH-000406': 'U937'}
resist_genes_lst = []
sensitive_genes_lst = []
genes = proteomics.keys()
cell_ids = [i[0] for i in proteomics.values]

for i in cell_ids:
    if i in resist_depmap_ids:
        resist_genes_lst.append(resist_depmap_ids[i])

print(f'Из списка резистентных клеток от Вити в базе {base_name} были найдены клетки:')
print(*resist_genes_lst)

list2_sensitive = ['EOL1', 'KG1', 'MEG01', 'MOLM14', 'MOLM16', 'MV411', 'NOMO1', 'OCIAML2', 'RS411', 'SET2', 'SKNO1']
sensitive_depmap_ids = {'ACH-000198': 'EOL1', 'ACH-000386': 'KG1', 'ACH-000072': 'MEG01', 'ACH-001574': 'MOLM14', 'ACH-000369': 'MOLM16', 'ACH-000045': 'MV411', 'ACH-000168': 'NOMO1', 'ACH-000113': 'OCIAML2', 'ACH-000874': 'RS411', 'ACH-000195': 'SET2', 'ACH-001656': 'SKNO1'}
#sensitive_depmap_ids = {'ACH-000386': 'KG1', 'ACH-000072': 'MEG01', 'ACH-001574': 'MOLM14', 'ACH-000369': 'MOLM16', 'ACH-000045': 'MV411', 'ACH-000168': 'NOMO1', 'ACH-000113': 'OCIAML2', 'ACH-000874': 'RS411', 'ACH-000195': 'SET2', 'ACH-001656': 'SKNO1'}

for i in cell_ids:
    if i in sensitive_depmap_ids:
        sensitive_genes_lst.append(sensitive_depmap_ids[i])

print()
print(f'Из списка сенситивных клеток от Вити в базе {base_name} были найдены клетки:')
print(*sensitive_genes_lst)

print(proteomics.head())

sens_lst = list(sensitive_depmap_ids)
rest_lst = list(resist_depmap_ids)
print(sens_lst)
print(rest_lst)
gene_names = list(proteomics.keys())[1:]
proteomics_compare = Comparison(proteomics, sens_lst, rest_lst)

#proteomics_compare.show_median(min_value=0.4, max_value=0.5)
#proteomics_compare.show_values(min_value=0.3)
proteomics_compare.show_custom(cell='ACH-000707', attr='p90RSK_pT359_S363')


