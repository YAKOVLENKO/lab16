import re,base64,argparse
regexp_arr = [r'javascript:',
              r'</script[ \n\t]*>',
              r' (onload|onerror|onmouseover)[ ]*=',
              r'data:text/html;base64,[a-zA-Z0-9+/]*={,2}']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_file", type=str, action='store', help="Путь до файла")
    args = parser.parse_args()
    f = open(args.path_to_file,'r')
    f_s = f.read()

    found = 0

    for i in regexp_arr[:3]:
        if re.search(i,f_s,re.MULTILINE):
            found = 1
            break

    if re.search(regexp_arr[3],f_s,re.MULTILINE):
        arr_found = list(re.finditer(regexp_arr[3],f_s,re.MULTILINE))
        for i in arr_found:
            found_s = i.group(0).split(',')[1]
            try:
                b64_s = ''.join(chr(b) for b in base64.b64decode(found_s))
                for i in regexp_arr[:3]:
                    if re.search(i, b64_s, re.MULTILINE):
                        found = 1
                        break
            except:
                pass



    print(found)

