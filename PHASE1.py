import re

#This function will extract data from xml file
#Eg. id: get_content('1k.txt','<aid>','</aid>')
def get_content(file_name,tag,slash_tag):
    container = []
    with open(file_name) as file:
        data = file.readlines()
        data_str = ' '.join(data)
        for term in data_str.split(slash_tag):
            if tag in term:
                container.append(term [term.find(tag) + len(tag) :])        
        file.close()
    return container

def write_terms():
    terms = []
    terms2 = []
    terms3 = []
    terms_final = []
    #Take ids,titles and descriptions from xml 
    ids = get_content('1k.txt','<aid>','</aid>')
    content = get_content('1k.txt','<ti>','</desc>')
    #remove strange expressions
    for i in range(len(content)):
        terms.append(content[i].replace("</ti><desc>"," ").lower())
    for i in range(len(content)):
        terms2.append(re.sub(r'[?|$|.|!|,|-|-|]',r'',terms[i]))
    for i in range(len(content)):
        terms3.append(re.sub(r'[^a-zA-Z0-9\._-]',r' ',terms2[i]))
    for i in range(len(content)):
        terms_final.append(' '.join(word for word in terms3[i].split() if len(word)>2))
    dictionary = dict(zip(terms_final,ids))

    #Wrtie the temrs into a new file
    file = open('terms.txt','w')
    #file.writelines(["%s\n" % item  for item in terms_final])
    #file.writelines(["%s\n" % item  for item in ids])
    for k, v in dictionary.items():
        for item in k.split(" "):
            file.write(str(item) + ':'+ str(v) + '\n' )
         

def write_pdates():
    write_final = []
    d = []
    f = []
    #take the data from xml
    ids = get_content('1k.txt','<aid>','</aid>')
    dates = get_content('1k.txt','<date>','</date>')
    cats = get_content('1k.txt','<cat>','</cat>')
    locs = get_content('1k.txt','<loc>','</loc>')
    #format the data
    write = zip(ids,cats,locs)
    write = list(write)
    for i in range(len(write)):
        write_final.append(','.join(write[i]))
    for i in range(len(dates)):
        d.append(dates[i] + ':')
    for i in range(len(d)):
        f.append(d[i] + write_final[i])
    #write the data to pdates.txt    
    file = open('pdates.txt','w')
    file.writelines(["%s\n" % item  for item in f])
    file.close()

def write_ads():
    ads = get_content('10.txt','<ad>','</ad>')
    ids = get_content("10.txt", "<aid>", "</aid>")
    file = open("ads.txt", "w") # TODO: Detect malformed ads? (missing an ad ID) len(ads) != len(ids)
    for i in range(len(ads)):
        file.write("{}:<ad>{}</ad>\n".format(ids[i], ads[i])) # TODO Shouldn't have to replace ad tags
    file.close()

def write_prices():
    write_final = []
    d = []
    f = []
    #take the data from xml
    prices = get_content('1k.txt','<price>','</price>')
    ids = get_content('1k.txt','<aid>','</aid>')
    cats = get_content('1k.txt','<cat>','</cat>')
    locs = get_content('1k.txt','<loc>','</loc>')    
    write = zip(ids,cats,locs)
    write = list(write)
    for i in range(len(write)):
        write_final.append(','.join(write[i]))
    for i in range(len(prices)):
        d.append(prices[i] + ':')
    for i in range(len(d)):
        f.append(d[i] + write_final[i])    
    #write the data to pdates.txt    
    file = open('prices.txt','w')
    file.writelines(["%s\n" % item  for item in f])
    file.close()    

def main():
    write_ads()
    write_pdates()
    write_terms()
    write_prices()
main()