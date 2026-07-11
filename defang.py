defang = input("URL You want to Defang here : ")

def defang_url(defang):

    defang = defang.replace("https://","hxxps://").replace("hxxp://","http://")

    defang = defang.replace(".","[.]")

    return defang

print("defanged url:",defang_url(defang))