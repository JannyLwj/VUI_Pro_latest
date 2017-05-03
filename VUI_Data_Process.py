# -*- coding:utf-8 -*-
#----------Janny----------------
#----------20170502-------------
import os
import string



Source_path=os.getcwd()
Target_path=Source_path+"_output"
if not os.path.exists(Target_path):
    os.mkdir(Target_path)

def process_file():
    for filename in os.listdir(Source_path):
        if filename=="CROSSING":
            print "-------------------------------process " + filename + "--------------------------------"
            Process_file_path=Source_path+"\\"+filename
            for file in os.listdir(Process_file_path):
                #print file
                process_crossing_file(file,filename)
                update_crossing_file_format(file,filename)
                continue
        elif filename=="POI":
            print "-------------------------------process " + filename + "--------------------------------"
            Process_file_path = Source_path + "\\" + filename
            for file in os.listdir(Process_file_path):
                process_poi_file(file, filename)
                update_poi_file_format(file,filename)
                continue
        elif filename=="ROAD":
            print "-------------------------------process " + filename + "--------------------------------"
            Process_file_path = Source_path + "\\" + filename
            for file in os.listdir(Process_file_path):
                process_road_file(file, filename)
                update_road_file_format(file,filename)
                continue
        elif filename=="ADMIN_hierarchy.txt":
            print "---------------------------process " + filename + "----------------------------"
            process_ADMIN_hierarchy_file_format(filename)
            update_ADMIN_hierarchy_file_format(filename)
            continue
        elif filename=="VUI_Data_Process.py":
            continue

def process_crossing_file(arg_file,arg_file_path):
    folder_name="CrossRoad"
    out_filepath=Target_path+"\\"+ arg_file_path
    if not os.path.exists(out_filepath):
        os.mkdir(out_filepath)
    out_filename=folder_name+"_" + arg_file.lower()+"_bak.txt"
    out_file=out_filepath+"\\"+out_filename
    #print out_file
    try:
        if os.path.exists(out_file):
            os.remove(out_file)
        output_file = open(out_file, 'a')
    except IOError:
        print "crossing file open error"
    input_filepath=Source_path+"\\"+arg_file_path+"\\"+arg_file
    #print input_filepath
    if not os.path.isdir(input_filepath):
        print "传入的参数有错%s不是一个目录" %input_filepath
        return False
    #list all txt files in input_filepath
    final_number=0
    file_number=0
    for txtFile in os.listdir(input_filepath):
        file_number+=1
        input_file=input_filepath+"\\"+txtFile
        #print input_file
        input_file=open(input_file,"rb")
        line_number = 0
        for line in input_file:
            final_number+=1
            if file_number>1:
                if "ROAD1" in line:
                    line_number+=1
                    continue;
                else:
                    line_number+=1
                    output_file.write(line.strip()+"\n")
            else:
                line_number += 1
                output_file.write(line.strip() + "\n")
        #print line_number
    print "total process file number: %d, line number : %d" % (file_number, final_number)
    return True
def update_crossing_file_format(arg_file, arg_file_path):
    CrossRoad = "CrossRoad"
    input_filepath = Target_path + "\\" + arg_file_path
    if not os.path.exists(input_filepath):
        os.mkdir(input_filepath)
    input_filename = CrossRoad + "_" + arg_file.lower() + "_bak.txt"
    final_filename=input_filepath+"\\"+CrossRoad + "_" + arg_file.lower() + ".txt"
    input_file = input_filepath + "\\" + input_filename
    input_file_process = open(input_file, "rb")
    try:
        if os.path.exists(final_filename):
            os.remove(final_filename)
        final_file_process = open(final_filename, 'a')
    except IOError:
        print "crossing file open error"
    plusword = "\t"
    linenumber=0
    for line in input_file_process:
        linenumber+=1
        words=line.split('\t')
        if linenumber==1:
            if words[1]=="ROAD1":
                words[1]="NAME1"
            if words[2]=="ROAD2":
                words[2]="NAME2"
            outputwords=words[0]+plusword\
                        +words[1]+plusword\
                        +"PINYIN1"+plusword\
                        +words[2]+plusword\
                        +"PINYIN2"+plusword\
                        +words[5].strip()+plusword\
                        +words[3]+plusword\
                        +words[4] +"\r\n"
            final_file_process.write(outputwords.strip() + "\n")
        else:
            outputwords=words[0]+plusword+words[1]+plusword+plusword+plusword+words[2]+plusword+plusword+plusword+words[5].strip()+plusword+words[3]+plusword+words[4]+"\r\n"
            final_file_process.write(outputwords.strip() + "\n")
    input_file_process.close()
    os.remove(input_file)
    print "total update line number: %d" %linenumber
    return True

def process_poi_file(arg_file,arg_file_path):
    folder_name="POI"
    out_filepath=Target_path+"\\"+ arg_file_path
    if not os.path.exists(out_filepath):
        os.mkdir(out_filepath)
    # 输出文件名
    out_filename=folder_name+"_" + arg_file.lower()+"_bak.txt"
    #输出的文件，路径+文件名
    out_file=out_filepath+"\\"+out_filename
    #print out_file
    try:
        if os.path.exists(out_file):
            os.remove(out_file)
        output_file = open(out_file, 'a')
    except IOError:
        print "poi file open error"
    input_filepath=Source_path+"\\"+ arg_file_path+"\\"+arg_file
    #print input_filepath
    if not os.path.isdir(input_filepath):
        print "传入的参数有错%s不是一个目录" %input_filepath
        return False
    #list all txt files in input_filepath
    file_number=0
    final_linnumber=0
    for txtFile in os.listdir(input_filepath):
        file_number+=1
        input_file=input_filepath+"\\"+txtFile
        #print input_file
        input_file=open(input_file,"rb")
        line_number = 0
        for line in input_file:
            final_linnumber+=1
            if file_number>1:
                if "NAME" in line:
                    line_number+=1
                    continue;
                else:
                    line_number+=1
                    output_file.write(line.strip()+"\n")
            else:
                line_number += 1
                output_file.write(line.strip() + "\n")
        #print line_number
    print "total process file number: %d, line number : %d"%(file_number,final_linnumber)
    return True
def update_poi_file_format(arg_file,arg_file_path):
    folder_name = "POI"
    input_filepath = Target_path + "\\" + arg_file_path
    if not os.path.exists(input_filepath):
        os.mkdir(input_filepath)
    input_filename = folder_name + "_" + arg_file.lower() + "_bak.txt"
    final_filename=input_filepath+"\\"+folder_name + "_" + arg_file.lower() + ".txt"
    input_file = input_filepath + "\\" + input_filename
    input_file_process = open(input_file, "rb")
    try:
        if os.path.exists(final_filename):
            os.remove(final_filename)
        final_file_process = open(final_filename, 'a')
    except IOError:
        print "poi file open error"
    plusword = "\t"
    linenumber=0
    for line in input_file_process:
        linenumber+=1
        words=line.split('\t')
        length= len(words)
        if len(words)==17:
            words.insert(17,"\t")
        if linenumber==1:
                words[0]="NDP"       #ID                words[1]="NDP_ID"
                words[1] = "NDP_ID"   #NAMEFLAG
                words[2] = "NAME"       #NAME
                words[3] = "Name_half"     #NAME_DBC
                words[4] = "ProsNum"     #PRONS_NUM
                words[5] = "LH_prons"     #LH
                words[6] = "SampaProns"    #SAMPA
                words[7] = "PY_Prons"      #PINYIN
                words[8] = "PartName"     #SEG_NAME
                words[9] = "LH_PartProns"   #SEG_LH
                words[10] = "SampaPartProns"    #SEG_SAMPA
                words[11] = "PY_PartProns"     #SEG_PINYIN
                words[12] = "ADDR"    #ADDRESS
                words[14] = "AD_CODE"      #ADMIN_ID
                words[15] = "POI_TYPE"      #POI_FLAG
                outputwords= words[0] + plusword\
                            + words[1]+ plusword \
                            + words[2] + plusword \
                            + words[3] + plusword \
                            + words[4] + plusword \
                            + words[5] + plusword \
                            + words[6] + plusword \
                            + words[7] + plusword \
                            + words[8] + plusword \
                            + words[9] + plusword \
                            + words[10] + plusword \
                            + words[11] + plusword \
                            + words[12] + plusword \
                            + words[14] + plusword \
                            + words[15] + plusword \
                            + "PRECISE" + plusword \
                            + words[13] + plusword \
                            + words[16] + plusword \
                            + words[17]
                final_file_process.write(outputwords.strip() + "\n")
        else:
            outputwords = words[0] + plusword \
                          + words[1] + plusword \
                          + words[2] + plusword \
                          + words[3] + plusword \
                          + words[4] + plusword \
                          + words[5] + plusword \
                          + words[6] + plusword \
                          + words[7] + plusword \
                          + words[8] + plusword \
                          + words[9] + plusword \
                          + words[10] + plusword \
                          + words[11] + plusword \
                          + words[12] + plusword \
                          + words[14] + plusword \
                          + words[15] + plusword \
                          + plusword + plusword \
                          + words[13] + plusword \
                          + words[16] + plusword \
                          + words[17]
            final_file_process.write(outputwords.strip() + "\n")
    input_file_process.close()
    os.remove(input_file)
    print "total update line number: %d" %linenumber
    return True

def process_road_file(arg_file,arg_file_path):
    folder_name="Road"
    out_filepath=Target_path+"\\"+arg_file_path
    if not os.path.exists(out_filepath):
        os.mkdir(out_filepath)
    # 输出文件名
    out_filename=folder_name+"_" + arg_file.lower()+"_bak.txt"
    #输出的文件，路径+文件名
    out_file=out_filepath+"\\"+out_filename
    #print out_file
    try:
        if os.path.exists(out_file):
            os.remove(out_file)
        output_file = open(out_file, 'a')
    except IOError:
        print "road file open error"
    input_filepath=arg_file_path+"\\"+arg_file
    #print input_filepath
    if not os.path.isdir(input_filepath):
        print "传入的参数有错%s不是一个目录" %input_filepath
        return False
    #list all txt files in input_filepath
    file_number=0
    final_linnumber=0
    for txtFile in os.listdir(input_filepath):
        file_number+=1
        input_file=Source_path+"\\"+input_filepath+"\\"+txtFile
        #print input_file
        input_file=open(input_file,"rb")
        line_number = 0
        for line in input_file:
            final_linnumber+=1
            if file_number>1:
                if "NAME_FLAG" in line:
                    line_number+=1
                    continue;
                else:
                    line_number+=1
                    output_file.write(line.strip()+"\n")
            else:
                line_number += 1
                output_file.write(line.strip() + "\n")
        #print line_number
    print "total process file number: %d, line number : %d" % (file_number, final_linnumber)
    return True
def update_road_file_format(arg_file, arg_file_path):
    folder_name = "Road"
    input_filepath = Target_path + "\\" + arg_file_path
    if not os.path.exists(input_filepath):
        os.mkdir(input_filepath)
    input_filename = folder_name + "_" + arg_file.lower() + "_bak.txt"
    final_filename=input_filepath+"\\"+folder_name + "_" + arg_file.lower() + ".txt"
    input_file = input_filepath + "\\" + input_filename
    input_file_process = open(input_file, "rb")
    try:
        if os.path.exists(final_filename):
            os.remove(final_filename)
        final_file_process = open(final_filename, 'a')
    except IOError:
        print "road file open error"
    plusword = "\t"
    linenumber=0
    for line in input_file_process:
        linenumber+=1
        words=line.split('\t')
        length= len(words)
        if len(words)==17:
            words.insert(17,"\t")
        if linenumber==1:
                words[0]="ID"       #ID                words[1]="NDP_ID"
                words[3] = "NAME"   #NAME
                words[13] = "ADMIN_ID"       #ADMIN_ID

                outputwords= words[0] + plusword\
                            + words[3]+ plusword \
                            + "PINYIN" + plusword \
                            + words[13].strip() + plusword \
                            + words[1] + plusword \
                            + words[2] + plusword \
                            + words[3] + plusword \
                            + words[4] + plusword \
                            + words[5] + plusword \
                            + words[6] + plusword \
                            + words[7] + plusword \
                            + words[8] + plusword \
                            + words[9] + plusword \
                            + words[10] + plusword \
                            + words[11] + plusword \
                            + words[12] + "\r\n"
                final_file_process.write(outputwords.strip() + "\n")
        else:
            outputwords = words[0] + plusword \
                          + words[3] + plusword \
                          + plusword + plusword \
                          + words[13].strip() + plusword \
                          + words[1] + plusword \
                          + words[2] + plusword \
                          + words[3] + plusword \
                          + words[4] + plusword \
                          + words[5] + plusword \
                          + words[6] + plusword \
                          + words[7] + plusword \
                          + words[8] + plusword \
                          + words[9] + plusword \
                          + words[10] + plusword \
                          + words[11] + plusword \
                          + words[12] + "\r\n"
            final_file_process.write(outputwords.strip() + "\n")
    input_file_process.close()
    os.remove(input_file)
    print "total update line number: %d" %linenumber
    return True

def process_ADMIN_hierarchy_file_format(arg_file):
    input_file=Source_path+"\\"+arg_file
    output_file=Target_path+"\\"+arg_file
    (filepath, tempfilename) = os.path.split(output_file);
    (shotname, extension) = os.path.splitext(tempfilename);
    output_file_name=Target_path+"\\"+shotname+"_bak.txt"

    try:
        if os.path.exists(output_file_name):
            os.remove(output_file_name)
        output_file = open(output_file_name, 'a')
    except IOError:
        print "ADMIN_hierarchy file open error"

    line_number=0
    process_input_file = open(input_file, "rb")
    for line in process_input_file:
        line_number+=1
        output_file.write(line.strip() + "\n")
    print "total process file number: 1, line number : %d" % line_number
    return True
def update_ADMIN_hierarchy_file_format(arg_file):
    file_path = Target_path + "\\" + arg_file
    (filepath, tempfilename) = os.path.split(file_path);
    (shotname, extension) = os.path.splitext(tempfilename);
    input_file_name = Target_path + "\\" + shotname + "_bak.txt"
    input_file_process = open(input_file_name, "rb")
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
        final_file_process = open(file_path, 'a')
    except IOError:
        print "hierarchy file open error"
    plusword = "\t"
    linenumber=0
    for line in input_file_process:
        linenumber+=1
        words=line.split('\t')
        if linenumber==1:
                words[1]="NAME_DISTRICT"
                outputwords= words[0] + plusword\
                            + words[3].strip()+ plusword \
                            + words[2] + plusword \
                            + words[1] + "\r\n"
                final_file_process.write(outputwords.strip() + "\n")
        else:
            outputwords = words[0] + plusword \
                          + words[3].strip() + plusword \
                          + words[2] + plusword \
                          + words[1] + "\r\n"
            final_file_process.write(outputwords.strip() + "\n")
    input_file_process.close()
    os.remove(input_file_name)
    print "total update line number: %d" %linenumber
    return True

if __name__ == "__main__":
    process_file()
    print "----------------------------------Done-----------------------------------"