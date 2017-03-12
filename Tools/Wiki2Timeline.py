import re
inputpath = "input.txt"
outputpath = "output.txt"
links = True
file = open(inputpath,"r")
string = file.read()
file.close()
print("von " + inputpath + " gelesen")
def hilfe(matchobj):
    global links
    links = not links
    tmp = re.sub(r'<li>(.*?)</li>',r'<li>\n\t<div class="timeline-panel noarrow">\n\t\t\n\t\t<div class="tl-heading">\n\t\t\t<h4></h4>\n\t\t</div><div class="tl-body">\n\t\t\t<p>\n\t\t\t\t\1\t\t\t</p>\n\t\t</div>\n\t</div>\n</li>\n\n',matchobj.group(0),flags=re.DOTALL)
    if links:
        tmp = tmp.replace("<li>",r'<li class="timeline-inverted">')
    return tmp
string = string.replace("/wiki","http://elderscrolls.wikia.com/wiki")
print("links globalisiert")
string = string.replace("<ul>","</li>")
string = string.replace("</ul>","")
string = re.sub(r'<li>(.*?)</li>',hilfe,string,flags=re.DOTALL)
print("bodies übersetzt")
string = re.sub(r'<h2><span class="mw-headline" id="[^"]*?">(.*?)</span></h2>',r'<li><div class="tldate">\1</div></li>',string,flags=re.DOTALL)
string = re.sub(r'<h3><span class="mw-headline" id="[^"]*?">(.*?)</span></h3>',r'',string,flags=re.DOTALL)
string = re.sub(r'<h4><span class="mw-headline" id="[^"]*?">(.*?)</span></h4>',r'<asdf>\1</asdf>',string,flags=re.DOTALL)
string = re.sub(r'<h4><span id="[^"]*?" class="mw-headline">(.*?)</span></h4>',r'<asdf>\1</asdf>',string,flags=re.DOTALL)
print("headlines übersetzt")
string = re.sub(r'<p><b>.*?</b>.*?</p>',r'',string,flags=re.DOTALL)
print("Kommentare entfernt")
string = re.sub(r'<p>Sources.*?</p>','',string,flags=re.DOTALL)
string = re.sub(r'<sup.*?class="reference".*?</sup>',r'',string,flags=re.DOTALL)
print("sources/Einzelnachweise entfernt")
string = re.sub(r'<asdf>(.*?)</asdf>(.*?)"timeline-panel noarrow"(.*?)<h4></h4>',r'\2"timeline-panel"\3<h4>\1</h4>',string,flags=re.DOTALL)
print("Daten hinzugefügt")
string = re.sub(r'</li>[' "\n" r' ]*?</li>',r'</li>\n\n',string,flags=re.DOTALL)
string = re.sub(r'</li>[' "\n" r' ]*?</li>',r'</li>\n\n',string,flags=re.DOTALL)
string = re.sub(r'</li>[' "\n" r' ]*?</li>',r'</li>\n\n',string,flags=re.DOTALL)
print("Cleanup abgeschlossen")
file = open(outputpath,"w")
file.write(string)
file.close()
print("in " + outputpath  + " gespeichert")
