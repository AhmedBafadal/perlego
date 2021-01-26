import xml.etree.ElementTree as ET

# What countries each of the 4 books in the sample dataset can be sold in.
# Read Sales rights information short & long tags
# Store in MYSQL database
# Gracefully handle errors/ missing data
# Automated tests

mytree = ET.parse('/home/ahmed/Documents/dev/perlego/code/1.xml')
myroot = mytree.getroot()

class ETree:
    def __init__(self, path):
        self.my_tree = ET.parse(path)
        self.sales_id = ''
        self.title = ''
        self.countries_list = []
    
    def parse_xml(self):
        # for elem in self.my_tree.iter():
        self.title = self.my_tree.find('.//b029').text

        # # ID
        try:
            sales_rights_type = self.my_tree.find('.//b089')
            if sales_rights_type:
                self.sales_id = sales_rights_type.text
            elif not sales_rights_type:
                sales_rights_type = self.my_tree.find('.//SalesRightsType').text
                self.sales_id = sales_rights_type
        except:
            self.sales_id = 'None'
        
        # # territories included
        # try:
        #     territories = self.my_tree.find('.//territory')
        #     if territories:
        #         self.territories.append(territories.text)
        #     else:
        #         territories = self.my_tree.find('.//TerritoriesIncluded').text
        #         self.territories.append(territories)
        # except:
        #     self.territories = ['None']
        # if self.territories == ['\n']:
        #     self.territories = ['None']
        # try:
         # countries
        countries = self.my_tree.find('.//x449')
        if countries is not None:    
            countries_new = countries.text.split()
            self.countries_list.extend(countries_new)
        else:
            countries = self.my_tree.find('.//CountriesIncluded')
            try:
                countries_new = countries.text.split()
                self.countries_list.append(countries_new)
            except:
                self.countries_list = []
        
        # if countries:
        #     countries_new = countries.text.split()
        #     self.countries_list.append(countries_new)
        # elif not countries:
        #     countries = self.my_tree.find('.//CountriesIncluded')

        #     countries_new = countries.text.split()
        #     self.countries_list.append(countries_new)
        # except:
        #     self.countries_list = ['None']
        
            
        print(self.title, self.countries_list, self.sales_id, )
        
x = ETree('/home/ahmed/Documents/dev/perlego/code/1.xml')
x.parse_xml()
        
        
    