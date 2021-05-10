## class to handle genetic algorithm

import numpy as np
import logics
import condGenerator
from random import choices
from itertools import islice 

rules = condGenerator.condGenerator()
new_logics= logics.logics()

class genetics:
    def __init__(self):
        pass

    def chromosome_label (self, typ, values):
        gene_label = []
        if typ == "logical":
            gene_label.append("TRUE")
            gene_label.append("FALSE")
        else:
            gene_label = gene_label+values
        return gene_label
    
    def chromosome(self, gene_label,len_gene,len_cnts, log_val):
        i=0
        gene=[]
        k=0
        while(i<len_gene):
            if (gene_label[i] == "TRUE" or gene_label[i] == "FALSE"):
                gene = gene + self.log_chromosome(log_val[k])
                k=k+1
                i=i+2
            else:
                gene = gene + self.cnts_chromosome(len_cnts-1)
                i=i+len_cnts
        return gene

    def log_chromosome(self, value):
        if(value == 'TRUE'):
            l_gene=[1,0]
        else:
            l_gene=[0,1]
        return l_gene

    def cnts_chromosome(self, len_cnts):
        c_gene =[]
        i=0
        c_gene =c_gene + self.rand_gene()
        for k in range(len_cnts):
            if(c_gene[i] == 1):
                z = self.zerolistmaker(len_cnts-k)
                c_gene = c_gene + z
                break
            else: 
                if(k== len_cnts-1):
                   c_gene = c_gene+ [1]
                else:
                    c_gene= c_gene+ self.rand_gene()
                    i=i+1
        return c_gene

    def rand_gene(self):
        return choices([0,1], k=1)

    def zerolistmaker(self, n):
        listofzeros = [0] * n
        return listofzeros

    def population(self, gene_label, len_cnts, pop_size,log_val):
        population =[]
        for p in range(pop_size):
            population.append(self.chromosome(gene_label, len(gene_label), len_cnts,log_val))
        return population

    def num_ex_covered(self, gene_label, gene, elements, operator):
        table= elements
        attrCount=0
        i=0
        for i in range(len(gene_label)):
            #print(gene)
            if (gene[i]==1):
                val = gene_label[i]
                if (gene_label[i] == "FALSE" or gene_label[i] == "TRUE"):
                    table, count = new_logics.getCountOfCoveredRecords(table,val,attrCount)
                    attrCount=attrCount+1
                else:
                    attrCount=attrCount+1
                    if operator == '<':
                        table = new_logics.recordsContLeft(table, val)
                        count= len(table)
                    else:
                        table = new_logics.recordsContRight(table, val)
                        count = len(table)
        return count

    def calc_completeness (self, num_ex_covered, num_elements):
        completeness = (num_ex_covered / num_elements)
        return completeness

    def consistency_degree (self, num_ex_covered, num_ex_uncovered) -> int:
        if (num_ex_uncovered == 0):
            consistency_degree = 1
        elif (num_ex_uncovered < num_ex_covered):
            consistency_degree = (num_ex_covered - num_ex_uncovered)/ num_ex_covered
        else:
            consistency_degree =0
        return consistency_degree

    def fitness (self,num_ex_covered, num_elements):
        num_ex_uncovered = num_elements - num_ex_covered
        completeness = self.calc_completeness(num_ex_covered, num_elements)
        consistency = self.consistency_degree(num_ex_covered, num_ex_uncovered)
        fitness = completeness * consistency
        return fitness

    def selection(self, population, fitness):
        return choices(
		population=population,
		weights=fitness,
		k=2  # this parameter draw states that we draw twice from our population to get a pair.
	) 
    
    def fitness_single(self, population, fitness):
        max_val = max(fitness)
        max_index = fitness.index(max_val)
        return population[max_index]
        #return population[max_index], operator[max_index]
    
    def split_gene(self, gene, gene_label, attr_typ, len_cnts):
        len_to_split=[]
        for j in range(len(attr_typ)):
            if (attr_typ[j]== "logical"):
                len_to_split.append(2)
            else:
                len_to_split.append(len_cnts)
        g = iter(gene)
        g_label = iter(gene_label)
        split_gene = [list(islice(g, elem)) 
          for elem in len_to_split] 
        split_gene_label= [list(islice(g_label, elem)) 
          for elem in len_to_split] 
        return split_gene, split_gene_label

    def gene_to_cond(self, gene_label, gene, attr_typ, attr_name, operator):
        rule=[]
        for i in range(len(gene)):
            index = gene[i].index(1)
            if (attr_typ[i]== "logical"):
                rule.append(rules.conditionGeneratorDiscrete(attr_name[i], gene_label[i][index]))
            else:
                rule.append(rules.conditionGeneratorNum(attr_name[i], str(gene_label[i][index]), operator))

        return(rule)




