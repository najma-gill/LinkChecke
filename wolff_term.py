#import error_summary
from globals import global_patterns, global_messages
class WolffTerm:
    """
    A class to represent a Wolff Term with various attributes.

    Attributes:
        ST (str): Setup type.
        CR (str): Creative route.
        CUA (str): Creative sub category.
        C (str): Creative.

    Methods:
        get_setup_type():
            Returns the setup type (ST).
        set_setup_type(ST):
            Sets the setup type (ST) if it is not already set.
        get_creative_route():
            Returns the creative route (CR).
        set_creative_route(CR):
            Sets the creative route (CR) if it is not already set.
        get_creative_subcategory():
            Returns the creative sub category (CUA).
        set_creative_subcategory(CUA):
            Sets the creative sub category (CUA) if it is not already set.
        get_creative():
            Returns the creative (C).
        set_creative(C):
            Sets the creative (C) if it is not already set.
    """
    """def __init__(self, ST="", CR="", CUA="", C=""):
        self.ST = ST  # Setup type
        self.CR = CR  # Creative route
        self.CUA = CUA  # Creative sub category
        self.C = C  # Creative"""
    def __init__(self):
        self.__term_allowed_parameters = []
    
    __term_present_parameters = []
    __error_summary =[]

    __term_allowed_parameters = [
        'ST',  # Term keyword: Setup type
        'CR',  # Creative route
        'CUA', # Creative sub category
        'C',   # Creative
        'V'    #version
    ]
    def is_last_value_empty(self,lst):
    # Check if the list is not empty and the last element is an empty string
        return len(lst) > 0 and lst[-1] == ""
   
    def validate_term(self, term_string):
        key = 'utm_term'
        
        values = term_string.split('|')  # split firma specific key value pairs are separated by pipe sign
        #print("compaign values",values)
        if len(values) > 1:  # skip checking firma  specific keywords if it contains only value
            #print('value length', len(values))
            if not self.is_last_value_empty(values): # check if string has pipe at the end
            #error_summary.append({value, messages["missing_pipe_at_end"]})
                self.__error_summary = global_messages[key]+ term_string + global_messages["missing_pipe_at_end"]
                #print("values",values) #values ['CH_OBB', 'PR_Alp-GreyAtt','']
                for val in values:
                    if val:
                        if '_' not in val:
                            self.__error_summary.append(global_messages["underscore_missing"])
                        else:
                            specialKey, specialValue = val.split('_')
                            if specialKey in self.__term_allowed_parameters:
                                if specialKey not in self.__term_present_parameters:
                                    self.__term_present_parameters.append(specialKey)
                                else:
                                    self.__error_summary.append(specialKey+global_messages["duplicate_key"])
                                
                            #print("specialKey "+specialKey,specialValue)
                            if specialKey in global_patterns:
                                if global_patterns[specialKey].match(specialValue) is None:
                                    self.__error_summary.append(val +global_messages["pattern_mismatch"])
                            else:
                                self.__error_summary.append(specialKey+global_messages["key_not_allowed"])
        else:
            if key in global_patterns:
                if global_patterns[key].match(term_string) is None:
                    self.__error_summary.append(global_messages[key] + term_string+ global_messages["pattern_mismatch"])
            else:
                self.__error_summary.append(global_messages[key] +global_messages["key_not_allowed"])


    def get_setup_type(self):
        return self.ST

    def set_setup_type(self, ST):
        if not self.ST:
            self.ST = ST

    def get_creative_route(self):
        return self.CR

    def set_creative_route(self, CR):
        if not self.CR:
            self.CR = CR

    def get_creative_subcategory(self):
        return self.CUA

    def set_creative_subcategory(self, CUA):
        if not self.CUA:
            self.CUA = CUA

    def get_creative(self):
        return self.C

    def set_creative(self, C):
        if not self.C:
            self.C = C
    def get_errors(self):
        return self.__error_summary
    def printErrors(self):
        for error in  self.__error_summary:
            print(f" {error}")   
    def reset(self):
        self.__error_summary = []
        self.__term_present_parameters = []
    