# Stock (Equity data)
# Index data
# Stock option data
# Stock future data
# Index option data
# Index future data
# India Vix (Volatility data)
# Expiry dates in a year and month
# PE Ratio



from datetime import datetime
from nsepy import get_history
import datetime
import pandas as pd

Rel = get_history(symbol='RELIANCE',
                   start=datetime.date(2021,1,1),
                   end=datetime.date(2021,1,15))
# print(Rel)
# print(type(Rel))
# my_array = Rel.to_numpy()
# print(my_array)
# print(type(my_array))
# my_array2 = Rel.values
# print(my_array2)


def printTohtml(Alist, htmlfile):    
    html =  "<html>\n<head></head>\n<style>p { margin: 0 !important; }</style>\n<body>\n"

    title = "Study - User - zip file -  Last date modified"
    html += '\n<p>' + title + '</p>\n'

    # for line in Alist:
    #     para = '<p>' + line + '</p>'
    #     print(line)
    #     # html += para

    with open(htmlfile, 'w') as f:
        f.write(html + "\n</body>\n</html>")
        f.write(str(Alist))


# Alist =  [['123', 'user1', 'New Compressed (zipped) Folder.zip', '05-24-17'],
# ['123', 'user2', 'Iam.zip', '05-19-17'], ['abcd', 'Letsee.zip', '05-22-17'],
# ['Here', 'whichTwo.zip', '06-01-17']]

# printTohtml(my_array, 'zip_files.html')

# data = {'Age': [25,47,38],
#         'Birth Year': [1995,1973,1982],
#         'Graduation Year': [2016,2000,2005]
#         }

# df = pd.DataFrame(data, columns = ['Age','Birth Year','Graduation Year'])

# print(df)
# print(type(df))


# https://agshiv92.medium.com/dhow-to-extract-india-stock-market-data-in-python-in-the-easiest-way-e20e7d4484c5