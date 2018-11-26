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

#This function will generate terms.txt
def write_terms(file_name):
    terms = []
    terms2 = []
    terms3 = []
    terms_final = []
    #Take ids,titles and descriptions from xml 
    ids = get_content(file_name,'<aid>','</aid>')
    content = get_content(file_name,'<ti>','</desc>')
    #remove the tags from the content
    for i in range(len(content)):
        terms.append(content[i].replace("</ti><desc>"," ").lower())
    #remove the puntuation markers
    for i in range(len(content)):
        terms2.append(re.sub(r'[?|$|.|!|,|-|-|]',r'',terms[i]))
    #remove the weird expressions
    for i in range(len(content)):
        terms3.append(re.sub(r'[^a-zA-Z0-9\._-]',r' ',terms2[i]))
    #remove the words less than 3 characters
    for i in range(len(content)):
        terms_final.append(' '.join(word for word in terms3[i].split() if len(word)>2))
    dictionary = dict(zip(terms_final,ids))

    #Wrtie the temrs into a new file
    file = open('terms.txt','w')
    for k, v in dictionary.items():
        for item in k.split(" "):
            file.write(str(item) + ':'+ str(v) + '\n')
    file.close()

#This function will generate pdates.txt
def write_pdates(file_name):
    write_final = []
    d = []
    f = []
    #take the data from xml
    ids = get_content(file_name,'<aid>','</aid>')
    dates = get_content(file_name,'<date>','</date>')
    cats = get_content(file_name,'<cat>','</cat>')
    locs = get_content(file_name,'<loc>','</loc>')
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
    
#This function will generate ads.txt
def write_ads(file_name):
    ads = get_content(file_name,'<ad>','</ad>')
    ids = get_content(file_name, "<aid>", "</aid>")
    file = open("ads.txt", "w") 
    for i in range(len(ads)):
        file.write("{}:<ad>{}</ad>\n".format(ids[i], ads[i]))

#This function will generate prices.txt
def write_prices(file_name):
    write_final = []
    d = []
    f = []
    #take the data from xml
    prices = get_content(file_name,'<price>','</price>')
    ids = get_content(file_name,'<aid>','</aid>')
    cats = get_content(file_name,'<cat>','</cat>')
    locs = get_content(file_name,'<loc>','</loc>')    
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
    file_name = input('Please enter the file name: ') #Take the xml file name as input
    write_terms(file_name)
    write_pdates(file_name)
    write_ads(file_name)
    write_prices(file_name)   
main()