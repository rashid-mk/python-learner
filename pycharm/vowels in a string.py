def get_vowel(string):
    vow="aeiouAEIOU"
    vowel_dict={}
    for j in string:
        for k in vow:
            if j in vow:
                vowel_dict[k]=string.count(k)
                if vowel_dict[k]==0:
                    vowel_dict.pop(k)
    print ('the vowels in"',string,'"is')
    return vowel_dict


print (get_vowel(input("enter your string:")))
