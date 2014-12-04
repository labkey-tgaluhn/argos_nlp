#
# Copyright (c) 2014 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''
'''October 2014'''
__version__='find_stages_intersection1.0'

# take the intersection of staging results from the purely rules
# based program and the Naive Bayes multinomial event model

def get_intersection(rules,bayes,output_file):
    
    with open(output_file,'w') as f:
        for pt,stages in rules.items():
            
            rule_stage=stages[0]
            rule_confidence=float(stages[1])
            if pt in bayes:
                bayes_stage=bayes[pt][0]
                bayes_confidence=float(bayes[pt][1])
            else:
                bayes_stage='NOT FOUND'
                bayes_confidence=0.0
            
            if bayes_stage==rule_stage:                
                f.write(pt+'\t'+bayes_stage+'\t'+str((rule_confidence+bayes_confidence)/2)+'\n')                         
               
