import re
class Define:
    start = '<math>'
    end = '</math>'
    def __init__(self, definition):
        self.definition = definition #Received string from URL
        self.all_tags_pos = self.__Find_Tags_Positions()
        self.all_formulas = self.__Formulas()
        self.tokenized = self.__Tokenize()
        self.tags_removed = self.__Remove_tags()
        
    def get(self):
       return self.definition
   
    def __Find_Tags_Positions(self):
        tag = []
        start = '<math>'
        end = '</math>'
        for m in re.finditer(start, self.definition):   #Finding position of "end" in
            temp = self.definition[m.end():] #String after tag
            temp1 = re.search(end,temp)
            start_pos = temp1.span()[0] + m.end() #Closing position
            end_pos = temp1.span()[1] + m.end()  #Tag ending position
            temp = {m: [m.start(), m.end(), start_pos, end_pos]}
            tag.append(temp)
        return tag
    def __Formulas(self):
        List = set()
        tag_list = self.all_tags_pos        
        for x in tag_list:
            for tag,value in x.items():
                List.add(self.definition[value[1]:value[2]])
        List = list(List)
        return List
    def __Tokenize(self):
        text = self.definition
        for count in [count for count, line in enumerate(self.all_formulas)]:
            temp = self.start+self.all_formulas[count]+self.end
#            print(temp)
#            print(count, " ", self.all_formulas[count]) 
            token = '"Token' + str(count) + '"'
            text = text.replace(temp,token)
        return text
#     def __Remove_tags(self):
#         text = self.definition
#         text = text.replace(self.start, '')
#         text = text.replace(self.end, '')
#         return text
    def __Remove_tags(self):
          text = self.definition
#          regex = r'[\[\[A-Za-z\ A-Za-z\ A-Za-z\:\:]'
          text = text.replace(self.start, '')
          text = text.replace(self.end, '')
          text = text.replace('member of family::', '')
          text = text.replace('[[', '')
          text = text.replace(']]', '')
          return text
     