import requests
url=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

print(url)

print(url.text[0:5])

print('--------------------------------------------------')


from bs4 import BeautifulSoup


soup=BeautifulSoup(url.text, 'html.parser')

results=soup.findAll('span', attrs={'class':'short-desc'})
print(len(results))

print('--------------------------------------------------')

print(results[0:1])


print("____________________________________")

# from the bottom of the website

print(results[-1])

print("_____________first_result_______________________")

# extracting the data


first_result=results[0]
print(first_result)


print("____________________________________")
print(first_result.find('strong'))

print("____________________________________")

print(first_result.find('strong').text[0:-5])


print("____________________________________")

print(first_result.find('strong').text, ', 2019')


# extracting the Lie

# lets first see the results
print(first_result)

print("___________________contents_________________")
print(first_result.contents)

print("___________________contents_________________")


# first results contents[1]

print(first_result.contents[0])
print(first_result.contents[1])

# extracting the explanations

print(first_result.contents[2])


print(first_result.contents[1][1:-3])

print("____________________________________")



# extracting the explanations

print(first_result.contents[2])

print("____________________________________")

print(first_result.find('a'))

print("____________________________________")
print(first_result.find('a')['href'])


print("hello")