#################################################################
#################################################################
# Prepare the GUI for the automated marking.                    #
#################################################################
#################################################################

import sys
import math
import csv
import yaml
import os.path
import numpy as np

#################################################################
# Print the end of the file.                                    #
#################################################################

def print_tail(o_ptr,NV,variable,typ,i_internet):

    if (i_internet == 0):
        f='    <script>\n'
        o_ptr.write(f)
        f='\n'
        o_ptr.write(f)
    f='      function save() {\n'
    o_ptr.write(f)
    f='        var inputs = [];\n'
    o_ptr.write(f)
    f='        document.querySelectorAll("input").forEach((element) => inputs.push(element.value));\n'
    o_ptr.write(f)
    f='\n'
    o_ptr.write(f)
    f='        console.log(inputs);\n'
    o_ptr.write(f)
    f='        var data = ",0\\n" +\n'
    o_ptr.write(f)
    itot=1
    for iv in range (0,NV):
        if (typ[iv] == 'dropDown'):
            f='          `'+variable[iv]+',${document.getElementById("'+variable[iv]+'").value}\\n`'
            o_ptr.write(f)
            if (iv < (NV-1)):
                f=' +\n'
                o_ptr.write(f)
            if (iv == (NV-1)):
                f=';\n'
                o_ptr.write(f)
        if (typ[iv] == 'textBox'):
            itot=itot+1
            f='          `'+variable[iv]+', ${inputs['+str(itot+1)+']}\\n`'
            o_ptr.write(f)
            if (iv < (NV-1)):
                f=' +\n'
                o_ptr.write(f)
            if (iv == (NV-1)):
                f=';\n'
                o_ptr.write(f)
    f='\n'
    o_ptr.write(f)
    f='        download(new Blob([data]), `answer_${inputs[2]}_A${inputs[0]}_${inputs[1]}.csv`)\n'
    o_ptr.write(f)
    f='      }\n'
    o_ptr.write(f)
    f='\n'
    o_ptr.write(f)
    f='    </script>\n'
    o_ptr.write(f)
    f='  </body>\n'
    o_ptr.write(f)
    f='</html>\n'
    o_ptr.write(f)

    return(o_ptr)

#################################################################
# Print the save button and the function, using the internet.   #
#################################################################

def print_func_1(o_ptr):

    f='    <br/>\n'
    o_ptr.write(f)
    f='\n'
    o_ptr.write(f)
    f='    <button onclick="save()">Save</button>\n'
    o_ptr.write(f)
    f='    <script src="https://cdnjs.cloudflare.com/ajax/libs/downloadjs/1.4.8/download.min.js" integrity="sha512-WiGQZv8WpmQVRUFXZywo7pHIO0G/o3RyiAJZj8YXNN4AV7ReR1RYWVmZJ6y3H06blPcjJmG/sBpOVZjTSFFlzQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>\n'
    o_ptr.write(f)
    f='    <script>\n'
    o_ptr.write(f)
    f='      function clearText() {\n'
    o_ptr.write(f)
    f='        document.querySelectorAll("input").forEach((element) => {element.value=""});\n'
    o_ptr.write(f)
    f='      }\n'
    o_ptr.write(f)
    f='\n'
    o_ptr.write(f)

    return(o_ptr)

#################################################################
# Print the save button and the function, not using the         #
# internet.                                                     #
#################################################################

def print_func_0(o_ptr):

    f='    <br/>\n'
    o_ptr.write(f)
    f='    <button onclick="save()">Save</button>\n'
    o_ptr.write(f)
    f='    <script>\n'
    o_ptr.write(f)
    f='      //download.js v4.21, by dandavis; 2008-2018. [MIT] see http://danml.com/download.html for tests/usage\n'
    o_ptr.write(f)
    f='      ;(function(root,factory){typeof define=="function"&&define.amd?define([],factory):typeof exports=="object"?module.exports=factory():root.download=factory()})(this,function(){return function download(data,strFileName,strMimeType){var self=window,defaultMime="application/octet-stream",mimeType=strMimeType||defaultMime,payload=data,url=!strFileName&&!strMimeType&&payload,anchor=document.createElement("a"),toString=function(a){return String(a)},myBlob=self.Blob||self.MozBlob||self.WebKitBlob||toString,fileName=strFileName||"download",blob,reader;myBlob=myBlob.call?myBlob.bind(self):Blob,String(this)==="true"&&(payload=[payload,mimeType],mimeType=payload[0],payload=payload[1]);if(url&&url.length<2048){fileName=url.split("/").pop().split("?")[0],anchor.href=url;if(anchor.href.indexOf(url)!==-1){var ajax=new XMLHttpRequest;return ajax.open("GET",url,!0),ajax.responseType="blob",'
    f=f+'ajax.onload=function(e){download(e.target.response,fileName,defaultMime)},setTimeout(function(){ajax.send()},0),ajax}}if(/^data:([\w+-]+\/[\w+.-]+)?[,;]/.test(payload)){if(!(payload.length>2096103.424&&myBlob!==toString))return navigator.msSaveBlob?navigator.msSaveBlob(dataUrlToBlob(payload),fileName):saver(payload);payload=dataUrlToBlob(payload),mimeType=payload.type||defaultMime}else if(/([\\x80-\\xff])/.test(payload)){var i=0,tempUiArr=new Uint8Array(payload.length),mx=tempUiArr.length;for(i;i<mx;++i)tempUiArr[i]=payload.charCodeAt(i);payload=new myBlob([tempUiArr],{type:mimeType})}blob=payload instanceof myBlob?payload:new myBlob([payload],{type:mimeType});function dataUrlToBlob(strUrl){var parts=strUrl.split(/[:;,]/),type=parts[1],indexDecoder=strUrl.indexOf("charset")>0?3:2,decoder=parts[indexDecoder]=="base64"?atob:decodeURIComponent,binData=decoder(parts.pop()),mx=binData.length,i=0,uiArr=new Uint8Array(mx);for(i;i<mx;++i)uiArr[i]=binData.charCodeAt(i);return new myBlob([uiArr],{type:type})}function saver(url,winMode){if("download"in anchor)return anchor.href=url,anchor.setAttribute("download",fileName),anchor.className="download-js-link",anchor.innerHTML="downloading...",anchor.style.display="none",anchor.addEventListener("click",function(e){e.stopPropagation(),this.removeEventListener("click",arguments.callee)}),document.body.appendChild(anchor),setTimeout(function(){anchor.click(),document.body.removeChild(anchor),winMode===!0&&setTimeout(function(){self.URL.revokeObjectURL(anchor.href)},250)},66),!0;if(/(Version)\/(\d+)\.(\d+)(?:\.(\d+))?.*Safari\//.test(navigator.userAgent))return/^data:/.test(url)&&(url="data:"+url.replace(/^data:([\w\/\-\+]+)/,defaultMime)),window.open(url)||confirm("Displaying New Document\\n\\nUse Save As... to download, then click back to return to this page.")&&(location.href=url),!0;var f=document.createElement("iframe");document.body.appendChild(f),!winMode&&/^data:/.test(url)&&(url="data:"+url.replace(/^data:([\w\/\-\+]+)/,defaultMime)),f.src=url,setTimeout(function(){document.body.removeChild(f)},333)}if(navigator.msSaveBlob)return navigator.msSaveBlob(blob,fileName);if(self.URL)saver(self.URL.createObjectURL(blob),!0);else{if(typeof blob=="string"||blob.constructor===toString)try{return saver("data:"+mimeType+";base64,"+self.btoa(blob))}catch(y){return saver("data:"+mimeType+","+encodeURIComponent(blob))}reader=new FileReader,reader.onload=function(e){saver(this.result)},reader.readAsDataURL(blob)}return!0}});\n'
    o_ptr.write(f)
    f='    </script>\n\n'
    o_ptr.write(f)

    return(o_ptr)

#################################################################
# Print the gui raw data out.                                   #
#################################################################

def print_gui(o_ptr,nrow,ncol,xloc,yloc,variable,options,typ,title,NV):

    f='    <table>\n'
    o_ptr.write(f)
    f='      <tbody>\n'
    o_ptr.write(f)
    i=0
    irow=0
    while (irow <= nrow):
        irow=irow+1
        f='        <tr>\n'
        o_ptr.write(f)
        icol=-1
        while (icol <= ncol):
            icol=icol+1
            idone=0
            if ( (yloc[i] == irow) and (xloc[i] == icol) ):
                idone=1
                f='          <th>'+title[i]+'</th>\n'
                o_ptr.write(f)
                if (typ[i] == 'textBox'):
                    f='          <td><input type="text"></td>\n'
                    o_ptr.write(f)
                if (typ[i] == 'dropDown'):
                    opts=[]
                    for io in range(0,len(options[i])):
                        opts.append(options[i][io])
                    f='          <td><select name="'+str(title[i])
                    f=f+'" id="'+variable[i]+'">\n'
                    o_ptr.write(f)
                    f='            <option value="'+opts[0]+'" selected>'+opts[0]+'</option>\n'
                    o_ptr.write(f)
                    for io in range(1,len(opts)):
                        f='            <option value="'+opts[io]+'">'+opts[io]+'</option>\n'
                        o_ptr.write(f)

                    f='          </select></td>\n'
                    o_ptr.write(f)
            if (idone == 1):
                i=i+1
                if (i == NV):
                    irow=nrow+2
                    icol=ncol+2
        f='        </tr>\n'
        o_ptr.write(f)
    f='      </tbody>\n'
    o_ptr.write(f)
    f='    </table>\n'
    o_ptr.write(f)

    return(o_ptr)

#################################################################
# Sort the variables.						#
#################################################################

def sort_all(variable,yloc,xloc,options,typ,title):

    N=len(variable)
    for i in range(0,N):
        for j in range(i+1,N):
            if (yloc[i] > yloc[j]):
                variable=swap(variable,i,j)
                yloc=swap(yloc,i,j)
                xloc=swap(xloc,i,j)
                options=swap(options,i,j)
                typ=swap(typ,i,j)
                title=swap(title,i,j)

    N=len(variable)
    for i in range(0,N):
        for j in range(i+1,N):
            if (yloc[i] == yloc[j]):
                if (xloc[i] > xloc[j]):
                    variable=swap(variable,i,j)
                    yloc=swap(yloc,i,j)
                    xloc=swap(xloc,i,j)
                    options=swap(options,i,j)
                    typ=swap(typ,i,j)
                    title=swap(title,i,j)

    return(variable,yloc,xloc,options,typ,title)

#################################################################
# Swap two variables.						#
#################################################################

def swap(var,i,j):

    tmp=var[i]
    var[i]=var[j]
    var[j]=tmp

    return(var)

#################################################################
# Read the input file.						#
#################################################################

def read_inp(i_fn):

    print("Variables:")
    print("==========")

    ncol=-1
    nrow=-1

    variable=[]
    yloc=[]
    xloc=[]
    options=[]
    typ=[]
    title=[]

    with (open(i_fn) as file):
        data=yaml.load(file,Loader=yaml.FullLoader)

    for item, doc in data.items():
        igood=1
        if (len(item) >= 2):
            if ((item[0]+item[1]) == 'vl'):
                igood=0
        if (igood == 1):
            print(item)
            variable.append(item)
            yloc.append(int(doc['location'][0]))
            xloc.append(int(doc['location'][1]))
            y=int(doc['location'][0])
            x=int(doc['location'][1])
            options.append(doc['options'])
            title.append(doc['title'])
            typ.append(doc['type'])
            if (x > ncol):
               ncol=x
            if (y > nrow):
               nrow=y

    ncol=ncol+1

    ostr='\nNumber of rows    : '+str(nrow)
    print(ostr)
    ostr='Number of columns : '+str(ncol)
    print(ostr)

    variable,yloc,xloc,options,typ,title=sort_all(variable,yloc,xloc,
        options,typ,title)

    for i in range(0,len(options)):
        for j in range(0,len(options[i])):
            outp=''
            for k in range(0,len(options[i][j])):
                if (options[i][j][k] != '<'):
                    outp=outp+options[i][j][k]
                if (options[i][j][k] == '<'):
                    outp=outp+'&lt;'
            options[i][j]=outp

    return(ncol,nrow,variable,yloc,xloc,options,typ,title)

#################################################################
# Remove the first character from a string.			#
#################################################################

def rem_first(word):

    short=''
    L=len(word)
    for i in range(1,L):
        short=short+word[i]

    return(short)

#################################################################
# Remove the last character from a string.			#
#################################################################

def rem_last(word):

    short=''
    L=len(word)
    for i in range(0,L-1):
        short=short+word[i]

    return(short)

#################################################################
# Print out the file header.					#
#################################################################

def print_header(o_ptr,anum,qnum):

    f='<!DOCTYPE html>\n'
    o_ptr.write(f)
    f='<html>\n'
    o_ptr.write(f)
    f='  <head>\n'
    o_ptr.write(f)
    f='     <meta charset="utf-8">\n'
    o_ptr.write(f)
    f='  </head>\n'
    o_ptr.write(f)
    f='  <body>\n'
    o_ptr.write(f)
    f='\n'
    o_ptr.write(f)
    f='    <label for="assignnumber">Assignment Number:</label>\n'
    o_ptr.write(f)
    f='    <input type="text" id="assignnumber" name="assignnumber" value="'
    f=f+str(anum)+'"><br><br>\n'
    o_ptr.write(f)
    f='    <label for="assignnumber">Question Number:</label>\n'
    o_ptr.write(f)
    f='    <input type="text" id="questionnumber" name="questionnumber" '
    f=f+'value="A'+str(anum)+'Q'+str(qnum)+'"><br><br>\n'
    o_ptr.write(f)
    f='    <label for="studentid">Student ID:</label>\n'
    o_ptr.write(f)
    f='    <input type="text" id="studentid" name="studentid" value='
    f=f+'"0000"><br><br>\n'
    o_ptr.write(f)

    return(o_ptr)

#################################################################
# Prepare the GUI.                                              #
#################################################################

def process_gui(i_fn,o_fn,anum,qnum,i_internet):

    ncol,nrow,variable,yloc,xloc,options,typ,title=read_inp(i_fn)
    NV=len(variable)
    ostr='Number of variables : '+str(NV)+'.'
    print(ostr)

    o_ptr=open(o_fn,"w")

    o_ptr=print_header(o_ptr,anum,qnum)

    o_ptr=print_gui(o_ptr,nrow,ncol,xloc,yloc,variable,options,typ,title,NV)

    if (i_internet == 0):
        o_ptr=print_func_0(o_ptr)
    if (i_internet == 1):
        o_ptr=print_func_1(o_ptr)

    o_ptr=print_tail(o_ptr,NV,variable,typ,i_internet)

    o_ptr.close()

    return()

#################################################################
#################################################################
# Start the main code.                                          #
#################################################################
#################################################################

def main():

    i_fn='structure.yaml'
    o_fn='SAMPLE_GUI.html'
    anum=0
    qnum=0

    i_internet=0

    process_gui(i_fn,o_fn,anum,qnum,i_internet)

main()
