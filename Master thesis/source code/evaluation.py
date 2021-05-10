## class to evaluate the learned planning domain model

from collections import Counter

class evaluation:

    def __init__(self):
        pass

## function to separate precondition's and effects' fluents from file
    def separate_fluents(self):
        ref_domain = open("source code/Evaluation/Ref domain predicates.txt", "r")
        learned_domain = open("source code/Evaluation/LearnedPredicates.txt", "r")
        ref_pre=[]
        ref_eff=[]
        for line in ref_domain:
            l=line.strip()
            if "precondition" in l:
                l1= l.split(":")
                ref_pre = ref_pre + (l1[1].split())
            elif "effect" in l:
                l1= l.split(":")
                ref_eff = ref_eff + (l1[1].split())
        ref_fluents = ref_pre+ref_eff

        learned_pre=[]
        learned_eff=[]
        for line in learned_domain:
            l=line.strip()
            if "precondition" in l:
                l1= l.split(":")
                learned_pre = learned_pre + (l1[1].split())
            elif "effect" in l:
                l1= l.split(":")
                learned_eff = learned_eff + (l1[1].split())

        learned_fluents = learned_pre+learned_eff
        return ref_fluents, learned_fluents

## function to find difference in list (missing and extra fluents)  
    def list_difference(self,a,b):
        c = a
        for item in b:
            try:
                c.remove(item)  
            except ValueError:
                pass  
        return c

## function to find domain error rate
    def domain_error_rate(self):
        ref_fluents, learned_fluents = self.separate_fluents()
        len_ref = len(ref_fluents)
        missing_fluents = self.list_difference(ref_fluents, learned_fluents)
        ref_fluents, learned_fluents = self.separate_fluents()
        extra_fluents = self.list_difference(learned_fluents, ref_fluents)
        # print(missing_fluents)
        # print(extra_fluents)
        domain_error = (len(extra_fluents) + len(missing_fluents)) / (len_ref)
        print("Domain error rate:", domain_error, "\n")
        return domain_error

## function to find accuracy of numerical information
    def extract_num_info(self):
        num_info = open("source code/Evaluation/ numericalInformation.txt", "r")
        ref_pre_num =[]
        ref_eff_num =[]
        l_pre_num =[]
        l_eff_num =[]
        for line in num_info:
            l=line.strip()
            if "ref_precondition" in l:
                l1= l.split(":")
                ref_pre_num = ref_pre_num + (l1[1].split(","))
            elif "ref_effect" in l:
                l1= l.split(":")
                ref_eff_num = ref_eff_num + (l1[1].split(","))
            elif "learned_precondition" in l:
                l1= l.split(":")
                l_pre_num = l_pre_num + (l1[1].split(","))
            elif "learned_effect" in l:
                l1= l.split(":")
                l_eff_num = l_eff_num + (l1[1].split(","))
        
        return ref_pre_num, ref_eff_num,l_pre_num, l_eff_num
        
    def tot_deviation(self):
        ref_pre_num, ref_eff_num,l_pre_num, l_eff_num = self.extract_num_info()
        
        num_actions = len(ref_pre_num)
        pre_d=0
        for i in range (num_actions):
            expected = ref_pre_num[i]
            learned = l_pre_num[i]
            pre_d = pre_d + (abs(float(expected) - float(learned)) / float(expected))
        
        pre_deviation = pre_d/num_actions

        eff_d=0
        for i in range (num_actions):
            expected = ref_eff_num[i]
            learned = l_eff_num[i]
            eff_d = eff_d+ (abs(float(expected) - float(learned)) / float(expected))
        eff_deviation = eff_d/num_actions
        
        avg_deviation = (pre_deviation + eff_deviation) / 2
        print("Calculating accuracy in numerical information")
        print("Deviation in preconditions in %:", (pre_deviation*100))
        print("Deviation in effects in %:", (eff_deviation*100))
        print("Deviation in domain in %:", (avg_deviation*100), "\n")


# t = evaluation()
# t.domain_error_rate()
# t.tot_deviation()

