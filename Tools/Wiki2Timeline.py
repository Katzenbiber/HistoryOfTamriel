import re
import sys
inputpath = "input.txt"
outputpath = "output.txt"
if len(sys.argv)==3:
	inputpath=sys.argv[1]
	outputpath=sys.argv[2]
links = True
file = open(inputpath,"r")
string = file.read()
file.close()
print("von " + inputpath + " gelesen")
def hilfe2(matchobj):
    global links
    date = re.sub(r'.*?<h4>(.*?)</h4>',r'\1',matchobj.group(0),flags=re.DOTALL)
    if len(date)>0:
        links = not links
    tmp = ""
    if links:
        tmp= "<li>\n\t<div class=\"timeline-panel noarrow\">\n\t\t<div class=\"tl-heading\">\n\t\t\t<h4>" +date+ "</h4>"
    else:
        tmp="<li class=\"timeline-inverted\">\n\t<div class=\"timeline-panel noarrow\">\n\t\t<div class=\"tl-heading\">\n\t\t\t<h4>" +date+ "</h4>"
    if len(date)>0:
        tmp = tmp.replace("timeline-panel noarrow","timeline-panel")
    return tmp
string = string.replace("/wiki","http://elderscrolls.wikia.com/wiki")
print("links globalisiert")
string = string.replace("<ul>","</li>")
string = string.replace("</ul>","")
string = re.sub(r'<li>(.*?)</li>',r'<li>\n\t<div class="timeline-panel noarrow">\n\t\t\n\t\t<div class="tl-heading">\n\t\t\t<h4></h4>\n\t\t</div>\n\t\t<div class="tl-body">\n\t\t\t<p>\n\t\t\t\t\1\t\t\t</p>\n\t\t</div>\n\t</div>\n</li>\n\n',string,flags=re.DOTALL)
print("bodies übersetzt")
string = re.sub(r'<h2><span class="mw-headline" id="[^"]*?">(.*?)</span></h2>',r'<l i><div class="tldate">\1</div></li>',string,flags=re.DOTALL)
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
string = re.sub(r'<li.*?</h4>',hilfe2,string,flags=re.DOTALL)
string = re.sub(r'<l i>',r'<li>',string)
print("Cleanup abgeschlossen")
file = open(outputpath,"w")
file.write(string)
file.close()
print("in " + outputpath  + " gespeichert")
