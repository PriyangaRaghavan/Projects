import ReadFiles
import Attributes
import genetic
import Records
import condGenerator
import outputRule
import preprocessing
import logics
import evaluation
import ruleToPDDL
import writeToFile

actions = ['on-heater', 'off-heater','open', 'close', 'on-light','off-light']
read = ReadFiles.ReadFile()

allActions=0
numerical_precondition=[]
numerical_effect=[]

for action in actions:
  allActions= allActions+1
  actionOut =0
  lines = read.readAttrFile(action)
  elements = read.readTrainFile(action)

  new_records = Records.Records()
  train_data = new_records.getRecordElements(elements)
  size = new_records.sizeOfRecords(elements)
  classAttributes = new_records.classAttributes(train_data)

  attr = Attributes. Attributes()
  num_attr = attr.numberOfAttributes(lines)
  attr_table = attr.AttributeTable(lines)

  new_genetic = genetic.genetics()
  new_preprocessing = preprocessing.preprocessing()

  new_rules = condGenerator.condGenerator()
  new_logics= logics.logics()
  new_evaluation= evaluation.evaluation()

  outRule = outputRule.output()
  toPDDL = ruleToPDDL.ruleToPDDL()
  outFile = writeToFile.fileWrite()
  
  ##preprocessing to find diff in prestate and poststate values
  num_val=[]
  for i in range(len(attr_table)):
    if (attr_table[i]['type'] == "numerical"):
      for j in range(1,len(train_data)):
        if train_data[j][i] == "NA":
          train_data[j][i] = '0'
          num_val.append(train_data[j][i])
  operator, function = new_preprocessing.diff_in_numerical_attr(num_val)
  
  elementList =[[] for x in range (len(classAttributes))]
  for x in range(0,len(classAttributes)):
    for j in range(1,new_records.sizeOfRecords(elements)):
            category = new_records.classAttributeAtIndex(elements, j)
            if category==classAttributes[x]:
              elementList[x].append(new_records.getRecordElementsAtIndex(elements,j))
    
    attr_typ=[]
    attr_name=[]
    for n in range(len(attr_table)-1):
       attr_typ.append(attr_table[n]['type'])
       attr_name.append(attr_table[n]['name'])

    gene_label =[]
    log_val=[]
    check_cnts=0
    for i in range(num_attr-1): 
        typ = attr.getType(lines, i)
        values=[]
        val=[]
       
        if (attr_typ[i]== "numerical"):
          check_cnts=1
          for j in range(new_records.sizeOfRecords(elementList[x])):
              if new_records.getRecordValueAtIndex(elementList[x], j, i) != '0':
                val.append(new_records.getRecordValueAtIndex(elementList[x], j, i))
          values = (new_preprocessing.discretize(val, 9))
          len_cnts = len(values)

        else:
            for j in range(new_records.sizeOfRecords(elementList[x])):
               values.append(new_records.getRecordValueAtIndex(elementList[x], j, i))
            log_val.append(values[0])
    
        g = new_genetic.chromosome_label(typ, values)
        gene_label = gene_label + g
    
    if check_cnts==0:
        len_cnts=0
        function = "None"

    fitness=[]
    population = new_genetic.population(gene_label, len_cnts, 10, log_val)
    if x==1:
        if(operator == '<'):
          operator='>='
        else:
          operator='<'
    
    for i in range(len(population)):
       cover = new_genetic.num_ex_covered(gene_label, population[i], elementList[x], operator)
       fitness.append(new_genetic.fitness(cover, len(elementList[x])))
    best_fit = new_genetic.fitness_single(population, fitness)
    split_gene, split_gene_label= new_genetic.split_gene(best_fit,gene_label,attr_typ, len_cnts)
    rule = new_genetic.gene_to_cond(split_gene_label, split_gene,attr_typ, attr_name, operator)
    outrule = outRule.rule(rule, classAttributes[x])  

    ## Write extracted rules to file
    if actionOut ==0:
      actionOut =1
      outFile.writeRule("\n"+"Extracted rules for action "+ action +":"+ "\n")
      outFile.writePDDL("\n"+"PDDL precondition and effect of "+ action +":"+ "\n")
      outFile.writeLearnedPredicates("\n"+ action +":"+ "\n")
    outFile.writeRule(outrule)


    if classAttributes[x] == "prestate":
        prestate_rule = rule
        PDDL, fluents,num = toPDDL.prestate(rule)
        if (action == "off-heater" or action == "close" or action == "off-light"):
          PDDL=toPDDL.toReplace(PDDL)
          fluents=toPDDL.toReplace(fluents)
        numerical_precondition=numerical_precondition+num

    elif classAttributes[x] == "poststate":
      PDDL, fluents,num = toPDDL.poststate(prestate_rule, rule, function)
      if (action == "off-heater" or action == "close" or action == "off-light"):
          PDDL=toPDDL.toReplace(PDDL)
          fluents=toPDDL.toReplace(fluents)
      numerical_effect=numerical_effect+num
    
    # # Write PDDL code to file
    outFile.writePDDL(PDDL)
    outFile.writePDDL("\n")

    # # Write fluents to file for evaluation using domain error
    outFile.writeLearnedPredicates(fluents)
    outFile.writeLearnedPredicates("\n")

    # # Write numerical information into file for evaluation of numerical info

    if allActions>(len(actions)-1) and x==1:
      num_pre=new_logics.listToString(numerical_precondition)
      num_eff=new_logics.listToString(numerical_effect)
      outFile.writeNumericalInformation("\n\nlearned_precondition :")
      outFile.writeNumericalInformation(num_pre)
      outFile.writeNumericalInformation("\nlearned_effect: ")
      outFile.writeNumericalInformation(num_eff)
      print("Output of extracted rules and coverted code are created in folder- outputFiles ")
    
    ## evaluation
      new_evaluation.domain_error_rate()
      new_evaluation.tot_deviation()
      
