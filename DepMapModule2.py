import pandas as pd
from statistics import median


class CellDict:
    def __init__(self, pandas_csv, cell_lst):
        self.pandas_csv = pandas_csv
        self.cell_lst = cell_lst
        self.base_attribute = list(self.pandas_csv.keys())[1:]
        self.celldict = {}

        for i in self.pandas_csv.values:
            if i[0] in self.cell_lst:
                for j in range(len(self.base_attribute)):
                    if i[0] in self.celldict:
                        self.celldict[i[0]].append([self.base_attribute[j], i[j+1]])
                    else:
                        self.celldict[i[0]] = [[self.base_attribute[j], i[j+1]]]

    def __str__(self):
        return str(self.celldict)


class Comparison:
    def __init__(self, csv, list1, list2):
        self.csv = csv
        self.list1 = list1
        self.list2 = list2
        self.base_attribute = list(csv.keys())[1:]
        self.cd1 = CellDict(csv, self.list1)
        self.cd2 = CellDict(csv, self.list2)
        self.sorted_attr_lst1 = self.sort_attr(self.base_attribute, self.cd1)
        self.sorted_attr_lst2 = self.sort_attr(self.base_attribute, self.cd2, sort='rev')

    @staticmethod
    def sort_attr(base_attribute, celldict, sort=True):
        attr_dict = {}
        for index in range(len(base_attribute)):
            minmaxlst = []
            for i in range(len(list(celldict.celldict.values()))):
                minmaxlst.append([list(celldict.celldict.keys())[i], list(celldict.celldict.values())[i][index][1]])
            if sort is True:
                minmaxlst = sorted(minmaxlst, key=lambda x: x[1])
            if sort in ('rev', 'reverse', 'Reverse'):
                minmaxlst = sorted(minmaxlst, key=lambda x: x[1], reverse=True)
            for i in minmaxlst:
                if base_attribute[index] in attr_dict:
                    attr_dict[base_attribute[index]].append(i)
                else:
                    attr_dict[base_attribute[index]] = [i]
        return attr_dict

    def compare_median(self):
        comparison_dict = {}
        for attr_index in range(len(self.sorted_attr_lst1)):
            median1 = median([x[1] for x in list(self.sorted_attr_lst1.values())[attr_index]])
            median2 = median([x[1] for x in list(self.sorted_attr_lst2.values())[attr_index]])
            comparison_dict[list(self.sorted_attr_lst1)[attr_index]] = [abs(median1 - median2), f'median1={median1}', f'median2={median2}']
        return comparison_dict

    def compare_values(self):
        comparison_dict = {}
        for attr_index in range(len(self.sorted_attr_lst1)):
            for i in range(len(list(self.sorted_attr_lst1.values())[attr_index])):
                if list(self.sorted_attr_lst1)[attr_index] in comparison_dict:
                    try:
                        comparison_dict[list(self.sorted_attr_lst1)[attr_index]].append([abs(list(self.sorted_attr_lst1.values())[attr_index][i][1] - list(self.sorted_attr_lst2.values())[attr_index][i][1]), list(self.sorted_attr_lst1.values())[attr_index][i][0], list(self.sorted_attr_lst2.values())[attr_index][i][0]])
                    except:
                        pass
                else:
                    comparison_dict[list(self.sorted_attr_lst1)[attr_index]] = [[abs(list(self.sorted_attr_lst1.values())[attr_index][i][1] - list(self.sorted_attr_lst2.values())[attr_index][i][1]), list(self.sorted_attr_lst1.values())[attr_index][i][0], list(self.sorted_attr_lst2.values())[attr_index][i][0]]]
        sorted_comp_dict = {key: sorted(item, key=lambda x: x[:][0], reverse=True) for key, item in comparison_dict.items()}
        return sorted_comp_dict

    def show_values(self, n=10, min_value=0, max_value=1000):
        res = self.compare_values()
        res_lst = []
        for key in res:
            if min_value <= res[key][0][0] <= max_value:
                res_lst.append([key, *res[key]])
        sorted_res_lst = sorted(res_lst, key=lambda x: x[1][0], reverse=True)
        for i in range(min(n, len(sorted_res_lst))):
            print(*sorted_res_lst[i])

    def show_median(self, n=10, min_value=0, max_value=1000):
        res_lst = []
        for key, item in self.compare_median().items():
            if min_value <= item[0] <= max_value:
                res_lst.append([key, item])
        for i in range(min(n, len(res_lst))):
            print(sorted(res_lst, key=lambda x: x[1][0], reverse=True)[i])

    def show_custom(self, cell=None, attr=None):
        for row in self.csv.values:
            if row[0] == cell:
                print('Cells:', cell, end=' ')
                for attr_index in range(len(self.csv.keys())):
                    if list(self.csv.keys())[attr_index] == attr:
                        print('Attr:', list(self.csv.keys())[attr_index], end=' ')
                print('value =',row[attr_index-1])




tester = pd.read_csv('scv test.scv')
print(tester.head())
#
# gene_names = list(tester.keys())[1:]
tester_lst1 = ['cell1', 'cell2', 'cell5']
tester_lst2 = ['cell3', 'cell4', 'cell6']
test_compare = Comparison(tester, tester_lst1, tester_lst2)
test_compare.show_median(min_value=0, max_value=1000)

# Женя дурак сделал не то,
# сравнить медианы и вывести разницу медиан
# сделать статистику
# сделать волкано плот
# сделать виолин плот
# объеденить модули, переименовать атрибуты