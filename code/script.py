import xml.sax

# What countries each of the 4 books in the sample dataset can be sold in.
# Read Sales rights information short & long tags
# Store in MYSQL database
# Gracefully handle errors/ missing data
# Automated tests
k = ''

# class GroupHandler(xml.sax.ContentHandler):
#     def __init__(self, *args, **kwargs):
#         self.title = ''
#         # self.new_id = ''
#         self.countriesList = []
#         self.territories = []
    
#     def startElement(self, name, attrs):
#         # what node currently in
#         self.current = name
#         if self.current == 'b029':
#             self.title = attrs['b029']
        
        

#     def characters(self, content):
            
#         # if self.current == 'x449' or self.current =='CountriesIncluded':
#         #     l = list(content.replace('\t', ' ').split())
#         #     self.countriesList.extend(l)
#             # identify countries included
#         if self.current == 'b029':
#             self.title = content.strip()
            
#         # elif self.current == 'SalesRightsType' or self.current=='b089':
        
#         #     self.new_id = content.strip()
#             # identify id type for possible sale

#         # elif self.current == 'x450':
#         #     self.territories.append(content)
#         #     self.territories= [t for t in self.territories if t != '\n']
            
        
#     def endDocument(self):
#         print(self.title)
#         # print(self.countriesList)
#         # print(self.new_id)
#         # print(self.territories)
#         print('end')


handler = xml.sax.ContentHandler()
# handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('1.xml')
# handler.output_data()

parser.getroot()