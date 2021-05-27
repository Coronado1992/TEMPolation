clc,clear all

for i=1:4
readfile = "file1.xlsx"; 
Analyze = "Sheet" + string(i);          %Choose humidity or temperatura (internal/external).
Excel= xlsread(readfile, Analyze);
[file1_Ti.numDP,file1_Ti.Time,file1_Ti.Sensor,file1_Ti.C,file1_Ti.Backup,file1_Ti.text] = f_ReadingFile(Excel,Analyze);
[file1_Te.numDP,file1_Te.Time,file1_Te.Sensor,file1_Te.C,file1_Te.Backup,file1_Te.text] = f_ReadingFile(Excel,Analyze);
[file1_Hi.numDP,file1_Hi.Time,file1_Hi.Sensor,file1_Hi.C,file1_Hi.Backup,file1_Hi.text] = f_ReadingFile(Excel,Analyze);
[file1_He.numDP,file1_He.Time,file1_He.Sensor,file1_He.C,file1_He.Backup,file1_He.text] = f_ReadingFile(Excel,Analyze);
end

for i=1:4
readfile = "file2.xlsx"; 
Analyze = "Sheet" + string(i);          %Choose humidity or temperatura (internal/external).
[file2_Ti.numDP,file2_Ti.Time,file2_Ti.Sensor,file2_Ti.C,file2_Ti.Backup,file2_Ti.text] = f_ReadingFile(xlsread(readfile, "Sheet1"),"Sheet1");
[file2_Te.numDP,file2_Te.Time,file2_Te.Sensor,file2_Te.C,file2_Te.Backup,file2_Te.text] = f_ReadingFile(xlsread(readfile, "Sheet3"),"Sheet3");
[file2_Hi.numDP,file2_Hi.Time,file2_Hi.Sensor,file2_Hi.C,file2_Hi.Backup,file2_Hi.text] = f_ReadingFile(xlsread(readfile, "Sheet2"),"Sheet2");
[file2_He.numDP,file2_He.Time,file2_He.Sensor,file2_He.C,file2_He.Backup,file2_He.text] = f_ReadingFile(xlsread(readfile, "Sheet4"),"Sheet4");
end

