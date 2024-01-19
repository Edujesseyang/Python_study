# =================================
# Ask the user to provide the URL of a website.
# (Assume the user input is valid) Using what you know about strings,
# get the domain of the website. For example,
# the domain name for https://www.deanza.edu/directory/user.html?u=readjustinLinks to an external site.
# would be deanza.edu. You can assume that the website is the standard format, i.e.
# https://www.domainname.com/something/something/etcLinks to an external site.,
# so there won't be any en.wikipedia.org or any different formats for this problem.
# ----------------------
ucl = input("Please enter website add: ")
ucl_list = ucl.split(".")
ucl_sub_list = ucl_list[2].split("/")
print(f'{ucl_list[1]}.{ucl_sub_list[0]}')
# ============================================
