
# Count vowels in a different way
# Using dictionary
def Check_Vow(string, vowels):



    # Forms a dictionary with key as a vowel
    # and the value as 0
    count = {}.fromkeys(vowels, 0)

    # To count the vowels
    for character in string:f
        if character in count:
            count[character] += 1
    return count

# Driver Code
vowels = 'aeiouAEIOU'
string = input("Geeks for Geeks")
print (Check_Vow(string, vowels))
