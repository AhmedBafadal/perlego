import xml.etree.ElementTree as ET


def print_subtree(subtree):
    for y in subtree.getchildren():
        if y.tag == 'x449' or y.tag == 'CountriesIncluded':
            return y.text.split(' ')
        elif y.tag == 'territory':
            for m in y.getchildren():
                if m.tag == 'x449' or m.tag == 'CountriesIncluded':
                    countries = m.text.replace('\n', '').split('\t') 
                    if len(countries) < 2:
                        countries.append(None)
                    return countries

def parse_xml(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    
    title = root.find('.//b029').text

    countries = []
    if root.findall('.//CountriesIncluded'):
        countries = root.findall('.//CountriesIncluded')[0].text.replace('\n', '').split('\t')
        if len(countries) < 2:
            countries.append(None)
        return title, countries

    if not countries:
        countries = []
        for x in root.iter('salesrights'):
            y = print_subtree(x)
            if y:
                return title, y
        return title, [] 


