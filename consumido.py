import mechanize
import cookielib
import time

num = ''
password = ''

#form name = frmLogin
#user name = j_username
#pass name = j_password
#form action = /mitelcel/login/auth

#url from login page
login_url = "https://www.mitelcel.com/mitelcel/login"
#url for the data consumed
data_url = "https://www.mitelcel.com/mitelce/f/home/consumos"
#url for the data consumed
puntos_url = "https://www.mitelcel.com/mitelce/f/home/miequipo"
#url for next monthly cut
plan_url = "https://www.mitelcel.com/mitelcel/f/home/plan"


#after doing the login, I must be able to enter the other pages
b = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
b.set_cookiejar(cj)

# Browser options
b.set_handle_equiv(True)
b.set_handle_gzip(True)
b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
b.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok?)
b.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

b.open(login_url)
b.select_form(name='frmLogin')
form = b.form
form['j_username'] = num
form['j_password'] = password

b.form = form
response = b.submit()
time.sleep(5)

print b.geturl()

res = b.open(plan_url)
print res.get_data()

# Ver los puntos mitelcel que tengo
# res = b.open(puntos_url)
# print res.get_data()

# Ver los datos que he consumido
# res = b.open(data_url)
# print res.get_data()
