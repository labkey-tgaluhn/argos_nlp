#
# Copyright (c) 2014-2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''
'''
    written October 2014, updates:
    December 2014 - added table_name to return dictionary
'''
__version__='PathStageT1.0'
import re
import global_strings

def get(disease_group,dictionary):
    try:
      
        '''
        extract the PathStageT (size/location of tumor)from normal cased text of the pathology report        
        '''
        full_text=dictionary[(-1,'FullText',0,None)]        
        return_dictionary={global_strings.NAME:"PathStageT",global_strings.VALUE:None,global_strings.CONFIDENCE:0.0,global_strings.VERSION:__version__,
                           global_strings.STARTSTOPS:[],global_strings.TABLE:global_strings.STAGE_GRADE_TABLE}
        
        
        t_stage=re.match('.*(pT[012345][abc]?).*',full_text,re.DOTALL)        
       
        if t_stage:
            return_dictionary[global_strings.VALUE]=t_stage.group(1)
            return_dictionary[global_strings.STARTSTOPS].append({global_strings.START:t_stage.start(),global_strings.STOP:t_stage.end()})
        return ([return_dictionary],list)
    except:
        return ({global_strings.ERR_TYPE:'Warning',global_strings.ERR_STR:'ERROR in PathStageT module.'},Exception)
