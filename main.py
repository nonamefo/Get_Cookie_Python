import sqlite3
from selenium import webdriver


driver = webdriver.Chrome()
LINK = 'INPUT THE LINK'
con = sqlite3.connect('Cookies.db')
cur = con.cursor()

try:
    cur.execute(
    '''
    CREATE TABLE cookies(name, value)
    '''
    )
except sqlite3.OperationalError:
    pass

except Exception as ex:
    print(ex)
    exit()


driver.get(LINK)
cookies = driver.get_cookies()


for cookie in cookies:
    cur.execute(
            '''
                INSERT INTO cookies VALUES(?, ?)
            ''',
            (cookie['name'], cookie['value'])
        )
    con.commit()
con.close()
