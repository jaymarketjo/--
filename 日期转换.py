from datetime import datetime
date_string="2025-01-21"
date_object=datetime.strptime(date_string,'%y-%m-%d')
formatted_date_string=date_object.strftime('%y%m%d')
print(formatted_date_string)