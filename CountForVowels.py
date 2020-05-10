def counVowels(str):
    vowels = 0
    for i in str.lower():
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowels = vowels + 1

    print("The Vowels in the String <",str,"> are : ",vowels)


str = input("Enter an String : ")
counVowels(str)