#import error_summary
from globals import global_patterns, global_messages
class WolffContent: #Adset class
    def __init__(self):
        self.__content_allowed_parameters = []
    """
    A class to represent a Wolff Content with various attributes.

    Attributes:
        TR (str): Traffic route.
        TG (str): Target group gender.
        NW (str): Network.
        TA (str): Target age.
        FO (str): Format.
        GS (str): Bidding strategy.
        RT (str): Retargeting.
        OS (str): Operating system.

    Methods:
        get_traffic_route(): Returns the traffic route.
        set_traffic_route(TR): Sets the traffic route if it is not already set.
        get_target_group_gender(): Returns the target group gender.
        set_target_group_gender(TG): Sets the target group gender if it is not already set.
        get_network(): Returns the network.
        set_network(NW): Sets the network if it is not already set.
        get_target_age(): Returns the target age.
        set_target_age(TA): Sets the target age if it is not already set.
        get_format(): Returns the format.
        set_format(FO): Sets the format if it is not already set.
        get_bidding_strategy(): Returns the bidding strategy.
        set_bidding_strategy(GS): Sets the bidding strategy if it is not already set.
        get_retargetting(): Returns the retargeting.
        set_retargetting(RT): Sets the retargeting if it is not already set.
        get_operating_system(): Returns the operating system.
        set_operating_system(OS): Sets the operating system if it is not already set.
    """
    __content_allowed_parameters = [
        'TR',  # Content keywords: Traffic route
        'TG',  # Target group gender
        'NW',  # Network
        'TA',  # Target age
        'FO',  # Format
        'GS',  # Bidding strategy
        'RT',  # Retargetting
        'OS',  # Operating system
    ]
    """def __init__(self, TR="", TG="", NW="", TA="", FO="", GS="", RT="", OS=""):
        self.TR = TR  # Traffic route
        self.TG = TG  # Target group gender
        self.NW = NW  # Network
        self.TA = TA  # Target age
        self.FO = FO  # Format
        self.GS = GS  # Bidding strategy
        self.RT = RT  # Retargetting
        self.OS = OS  # Operating system"""
    __content_present_parameters = []
    __error_summary =[]
    def is_last_value_empty(self,lst):
    # Check if the list is not empty and the last element is an empty string
        return len(lst) > 0 and lst[-1] == ""
   
    def validate_content(self, content_string):
        #print(f"content_string {content_string}")
        key = 'utm_content'
        values = content_string.split('|')  # split firma specific key value pairs are separated by pipe sign
        #print("compaign values",values)
        if len(values) > 1:  # skip checking firma  specific keywords if it contains only value
            #print('value length', len(values))
            if not self.is_last_value_empty(values): # check if string has pipe at the end
            #error_summary.append({value, messages["missing_pipe_at_end"]})
                self.__error_summary = global_messages[key]+ content_string + global_messages["missing_pipe_at_end"]
                #print("values",values) #values ['CH_OBB', 'PR_Alp-GreyAtt','']
                for val in values:
                    if val:
                        if '_' not in val:
                            self.__error_summary.append(global_messages["underscore_missing"])
                        else:
                            specialKey, specialValue = val.split('_')
                            if specialKey in self.__content_allowed_parameters:
                                if specialKey not in self.__content_present_parameters:
                                    self.__content_present_parameters.append(specialKey)
                                else:
                                    self.__error_summary.append(specialKey+global_messages["duplicate_key"])
                                
                            #print("specialKey "+specialKey,specialValue)
                            if specialKey in global_patterns:
                                if global_patterns[specialKey].match(specialValue) is None:
                                    self.__error_summary.append(specialValue +global_messages["pattern_mismatch"])
                            else:
                                self.__error_summary.append(specialKey+global_messages["key_not_allowed"])
        else:
            if key in global_patterns:
                if global_patterns[key].match(content_string) is None:
                    self.__error_summary.append(key+ content_string+global_messages["pattern_mismatch"])
            else:
                self.__error_summary.append(key+global_messages["key_not_allowed"])

    def get_traffic_route(self):
        return self.TR

    def set_traffic_route(self, TR):
        if not self.TR:
            self.TR = TR

    def get_target_group_gender(self):
        return self.TG

    def set_target_group_gender(self, TG):
        if not self.TG:
            self.TG = TG

    def get_network(self):
        return self.NW

    def set_network(self, NW):
        if not self.NW:
            self.NW = NW

    def get_target_age(self):
        return self.TA

    def set_target_age(self, TA):
        if not self.TA:
            self.TA = TA

    def get_format(self):
        return self.FO

    def set_format(self, FO):
        if not self.FO:
            self.FO = FO

    def get_bidding_strategy(self):
        return self.GS

    def set_bidding_strategy(self, GS):
        if not self.GS:
            self.GS = GS

    def get_retargetting(self):
        return self.RT

    def set_retargetting(self, RT):
        if not self.RT:
            self.RT = RT

    def get_operating_system(self):
        return self.OS

    def set_operating_system(self, OS):
        if not self.OS:
            self.OS = OS
    def get_errors(self):
        return self.__error_summary
    def printErrors(self):
        for error in  self.__error_summary:
            print(f" {error}")   
    def reset(self):
        self.__content_present_parameters = []
        self.__error_summary =[]