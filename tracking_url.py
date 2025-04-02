from urllib.parse import urlparse, parse_qs
import urllib
from wolff_campaign import WolffCampaign #import the WolffCampaign class file name and then class name
from wolff_content import WolffContent #import the WolffContent class
from wolff_term import WolffTerm #import the WolffTerm class
from globals import global_patterns, global_messages

class TrackingUrl:
    def __init__(self):
        self._utm_params = {}
        self.utm_present_parameters = {}
        
    utm_allowed_parameters = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term']
    reserved_characters = [':', '/', '?', '#', '[', ']', '@', '$', '&', ',', ';', '=']#'+'
    __error_summary =[]
    def validate_tracking_url(self, url):
         
        #self.extract_utm_params(url)
         # Parse the URL
        un_encodedurl = urllib.parse.unquote(url)
        parsed_url = urlparse(un_encodedurl)
        #print(f"process data ",parsed_url)
        #print(f"query ",parsed_url.query)
        query_string = parsed_url.query
        # Parse the query string into a dictionary
        #query_params = parse_qs(parsed_url.query)
        query_params = query_string.split('&')
        for parameter in query_params:
            print(f"{parameter}")
            
            if '=' not in parameter:
                self.__error_summary.append(parameter+global_messages["equal_missing"])
                #continue
            else:    
                key, value = parameter.split('=', 1)
               
                if not value:
                    self.__error_summary.append(parameter + global_messages["empty_string"])
                else:   
                    if key in self.utm_allowed_parameters:
                        
                        if key in self.utm_present_parameters:
                            #print(f"duplicate_key {key}")
                            self.__error_summary.append(key+ global_messages["duplicate_key"])  
                            if key in self._utm_params and (self._utm_params[key] is None or self._utm_params[key] == ''):
                                self._utm_params[key] = value   
                        self.process_data(key, value)
                    else:        
                        self.__error_summary.append(key+ global_messages["key_not_allowed"])
                self.utm_present_parameters[key] = value

       # print(f"Error Summary {self.__error_summary}")
        self.print_errors()


        #print(f"query_params {query_params}")
            

        #return all(field in query_params for field in self.utm_fields[:3])  # source, medium, campaign required
    
    def process_data(self, key, value):
        wollf_campaign = WolffCampaign()
        wollf_content =  WolffContent()
        wolff_term = WolffTerm()
        if key in global_patterns:  
            if key == "utm_source":
                if global_patterns[key].match(value) is None:
                    self.__error_summary.append(global_messages[key]+ value + global_messages["pattern_mismatch"])
            elif key == "utm_medium":    

                if global_patterns[key].match(value) is None:
                        self.__error_summary.append(global_messages[key]+ value + global_messages["pattern_mismatch"])
                
            elif key == "utm_campaign" or key == "utm_content" or key == "utm_term":  
                if self.check_query_allowed_parameters(value):# in case of missing & it is possible that keywords will be in value instead as key
                    #print(f"check_query_allowed_parameters {self.get_utm_campaign()}")        
                    self.__error_summary.append(global_messages[key]+value+ global_messages["ampersand_missing"])
                elif self.check_reserved_words(value):
                    self.__error_summary.append(value + global_messages["reserved_characters_are_not_allowed"])
                
                if key == "utm_campaign":
                    
                    wollf_campaign.reset()
                    wollf_campaign.validate_campaign(value)
                    #self.printErrors()
                    #wollf_campaign.printErrors()
                    errors = wollf_campaign.get_errors()
                    if errors:
                        self.__error_summary += errors

                elif key == "utm_content":
                    wollf_content.reset()
                    wollf_content.validate_content(value)
                    #self.printErrors()
                    errors = wollf_content.get_errors()
                    if errors:
                        self.__error_summary += errors
                elif key == "utm_term":
                    wolff_term.reset()
                    wolff_term.validate_term(value)
                    #self.printErrors()
                    errors = wolff_term.get_errors()
                    if errors:
                        self.__error_summary += errors
        else:
            self.__error_summary.append(global_messages[key]+ global_messages["key_not_allowed"])

    def get_utm_source(self):
        return self._utm_params.get('utm_source', '')
        
    def get_utm_medium(self):
        return self._utm_params.get('utm_medium', '')
        
    def get_utm_campaign(self):
        return self._utm_params.get('utm_campaign', '')
        
    def get_utm_content(self):
        return self._utm_params.get('utm_content', '')
        
    def get_utm_term(self):
        return self._utm_params.get('utm_term', '')
    
    def extract_utm_params(self,url):
        # Parse the URL
        parsed_url = urlparse(url)
        print(f"parsed_url ",parsed_url.params)
        #print(f"query ",parsed_url.query)
        query_string = parsed_url.query
        # Parse the query string into a dictionary
        #query_params = parse_qs(parsed_url.query)
        query_params = query_string.split('&')
        for parameter in query_params:
            print(f"param {parameter}")
            
            if '=' not in parameter:
                self.__error_summary.append(parameter+global_messages["equal_missing"])
                #continue
            else:    
                key, value = parameter.split('=', 1)
               
                if not value:
                    self.__error_summary.append(parameter + global_messages["empty_string"])
                else:   
                    if key in self.utm_allowed_parameters:
                        
                        if key in self.utm_present_parameters:
                            print(f"duplicate_key {key}")
                            self.__error_summary.append(key+ global_messages["duplicate_key"])  
                            if self._utm_params[key] is None:# or value == ''
                                #self.__error_summary.append(key+ global_messages["duplicate_key"])
                                self._utm_params[key] = value   
                      
                    else:        
                        self.__error_summary.append(key+ global_messages["key_not_allowed"])
                self.utm_present_parameters[key] = value


        print(f"query_params {query_params}")
            
            
            
        #print(f"utm_params {self._utm_params}")
        # Extract UTM parameters
        #utm_params = {key: value[0] for key, value in query_params.items() if key.startswith('utm_')}
    
        #return 0
    def check_reserved_words(self,string):
        for char in self.reserved_characters:
            if char in string:
                return True
        return False
    def check_query_allowed_parameters(self,string):
        #print(f"string {string}")
        for keyword in self.utm_allowed_parameters:
            #print(f"keyword {keyword}")
            if keyword in string:
                #print(f"keyword found {keyword}")
                return True
        return False
    def print_errors(self):
        if not self.__error_summary:
            print("Congratulations! No errors found.")
        else:
            print("Errors found: ")
            for error in  self.__error_summary:
                print(f"{error}") 
    def reset(self):
        self._utm_params = {}
        self.utm_present_parameters = {}
        self.__error_summary = []
        #print(f"reset {self._utm_params}")  
