#import error_summary
from globals import global_patterns, global_messages


class WolffCampaign:
    def __init__(self):
        self.__campaign_allowed_parameters = []
    
    __campaign_allowed_parameters = [
        'CH',  # Channel
        'PR',  # Product
        'FL',  # Flight
        'DE',  # Device
        'KZ',  # Campaign goal
        'TI',  # Target group interest
        'LA',  # Country/Land
        'ID',  # Campaign id
        'TM',  # Test market
        'TP',  # Target group parent
        'V',   # Version
        'TR',  # Content keywords: Traffic route
        'TG',  # Target group gender
        'NW',  # Network
        'TA',  # Target age
        'FO',  # Format
        'GS',  # Bidding strategy
        'RT',  # Retargetting
        'OS',  # Operating system
        'ST',  # Content keyword: Setup type
        'CR',  # Creative route
        'CUA', # Creative sub category
        'C',   # Creative
    ]
    __campaign_present_parameters = []
    __error_summary =[]
    def is_last_value_empty(self,lst):
    # Check if the list is not empty and the last element is an empty string
        return len(lst) > 0 and lst[-1] == ""
   
    def validate_campaign(self, campaign_string):
        key = 'utm_campaign'
        #print(f"campaign_string {campaign_string}")
        
        values = campaign_string.split('|')  # split firma specific key value pairs are separated by pipe sign
        #print("compaign values",values)
        if len(values) > 1:  # skip checking firma  specific keywords if it contains only value
            #print('value length', len(values))
            if not self.is_last_value_empty(values): # check if string has pipe at the end
            #error_summary.append({value, messages["missing_pipe_at_end"]})
                self.__error_summary = global_messages[key]+ campaign_string + global_messages["missing_pipe_at_end"]
                #print("values",values) #values ['CH_OBB', 'PR_Alp-GreyAtt','']
                for val in values:
                    if val:
                        if '_' not in val:
                            self.__error_summary.append(global_messages["underscore_missing"])
                        else:
                            specialKey, specialValue = val.split('_')
                            if specialKey in self.__campaign_allowed_parameters:
                                if specialKey not in self.__campaign_present_parameters:
                                    self.__campaign_present_parameters.append(specialKey)
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
                if global_patterns[key].match(campaign_string) is None:
                    self.__error_summary.append(key + campaign_string+global_messages["pattern_mismatch"])
            else:
                self.__error_summary.append(key+global_messages["key_not_allowed"])
        
    def get_channel(self):
        return self.CH

    def set_channel(self, CH):
        if not self.CH:
            self.CH = CH

    def get_product(self):
        return self.PR

    def set_product(self, PR):
        if not self.PR:
            self.PR = PR

    def get_flight(self):
        return self.FL

    def set_flight(self, FL):
        if not self.FL:
            self.FL = FL

    def get_device(self):
        return self.DE

    def set_device(self, DE):
        if not self.DE:
            self.DE = DE

    def get_campaign_goal(self):
        return self.KZ

    def set_campaign_goal(self, KZ):
        if not self.KZ:
            self.KZ = KZ

    def get_target_group_interest(self):
        return self.TI

    def set_target_group_interest(self, TI):
        if not self.TI:
            self.TI = TI

    def get_country(self):
        return self.LA

    def set_country(self, LA):
        if not self.LA:
            self.LA = LA

    def get_campaign_id(self):
        return self.ID

    def set_campaign_id(self, ID):
        if not self.ID:
            self.ID = ID

    def get_test_market(self):
        return self.TM

    def set_test_market(self, TM):
        if not self.TM:
            self.TM = TM

    def get_target_group_parent(self):
        return self.TP

    def set_target_group_parent(self, TP):
        if not self.TP:
            self.TP = TP

    def get_version(self):
        return self.V

    def set_version(self, V):
        if not self.V:
            self.V = V
    def get_errors(self):
        return self.__error_summary
    def printErrors(self):
        for error in  self.__error_summary:
            print(f" {error}")   
    def reset(self):
        self.__error_summary = []
        self.__campaign_present_parameters = []
        