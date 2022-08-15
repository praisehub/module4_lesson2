#importing sqlite3
import sqlite3
print('sqlite imported')
#connect to data base
conn = sqlite3.connect('student.db')
print('database successfull')
#create cursor
c = conn.cursor()
print('cursor successful')
# #creating table
# c.execute("""
#           CREATE TABLE data_scientists(
#               first_name text,
#               last_name text,
#               email text,
#               course text
#             )
# """)
 #check
print('data_scientists table created succesfully')
#creating rows
student_list = [('Praise', 'Emmanuel', 'praise@gmail.com', 'data_science'),
                 ('Mariam', 'Adeoti', 'adetutumariam@gmail.com', 'data_science'),
                 ('Abubakar', 'Adisa', 'adisaabubakar@gmail.com', 'Data_science'),
                 ]
#insert multiple rows into table
c.executemany('INSERT INTO data_scientists VALUES( ?,?,?,? )', student_list)
print('have inserted', c.rowcount, 'records to table data_scientists.')
#creating more rows
student_list = [ ('Adebisi',    'Afolabi',       'wasola.afolabi@yahoo.com',          'data_science'),
                 ('Adedoyin',   'Abass',         'doyinabass0@gmail.com',             'data_science'),
                 ('Awonaike',   'Tawakalitu',    'purpleduralumin@gmail.com',         'data_science'),
                 ('Babajide',   'Adesugba',      'jide_ade@hotmail.com',              'data_science'),
                 ('Bukola',     'Ajayi',         'bukolam.ajayi@gmail.com',           'data_science'),
                 ('Binta',      'Umar',          'ubinta63@yahoo.com',                'data_science'),
                 ('Christian',  'Uzondu',        'uzonduchristian2@gmail.com',        'data_science'),
                 ('Cynthia',    'Awiya',         'awiyac@yahoo.com',                  'data_science'),
                 ('Deborah',    'Olorunnishola', 'deboraholuwatobi247@gmail.com',     'data_science'),
                 ('Eke',        'Ihuoma',        'ihuomaeke28@gmail.com',             'data_science'),
                 ('Esther',     'Akpanowo',      'estherakpanowo@gmail.com',          'data-science'),
                 ('Eniola',     'Osadare',       'dorcasosadare@gmail.com',           'data_science'),
                 ('Etariemi',   'Louis',         'etariemilouis@gmail.com',           'data_science'),
                 ('Faith',      'Amure',         'amuretalodabif@gmail.com',          'data_science'),
                 ('Ganiyat',    'Shittu',        'ganiyatas@gmail.com',               'data_science'),
                 ('Gideon',     'Uko',           'ukogideon13@gmail.com',             'data_science'),
                 ('Idowu',      'Adesanya',      'idsworld22@yahoo.com',              'data_science'),
                 ('Joyce',      'Ezeonwu',       'joyceokore@gmail.com',              'data_science'),
                 ('Kehinde',    'Orolade',       'kehindeorolade@gmail.com',          'data_science'),
                 ('Kafayat',    'Ibrahim',       'kafayatadenike10@gmail.com',        'data_science'),
                 ('Lawrence',   'Aneshimokha',   'anelawrence1@gmail.com',            'data_science'),
                 ('Ogechi',     'Njemanze',      'ogenjemz@gmail.com',                'data_science'),
                 ('Omowunmi',   'Awonirana',     'mowunmi11@gmail.com',               'data_science'),
                 ('Placidus',   'Ali',           'Placidusali@gmail.com',             'data_science'),
                 ('Prince',     'Ekeocha',       'prince.ekeocha@gmail.com',          'data_science'),
                 ('Rasheedat',  'Sikiru',        'rasheedatsikiru@gmail.com',         'data_science'),
                 ('Ramotallah', 'Jubril',        'jubrilramotallah03@gmail.com',      'data_science'),
                 ('Sheriiff',   'Azeez',         'SheriffOlaitan71@gmail.com',        'data_science'),
                 ('Stephen',    'Ogungbile',     'stephenfunso@gmail.com',            'data_science'),
                 ('Temitope',   'Bamidele',      'bamideletemitope42@gmail.com',      'data_science'),
                 ('Theresa',    'Karamor',       'teriekarie@gmail.com',              'data_science'),
                 ('Tina',       'Uyateide',      'tinauyats@gmail.com',               'data_science'),
                 ('Victoria',   'Chukwuno',      'chukwunovictoria@gmail.com',        'data_science'),
                ]
#insert multiple rows into table
c.executemany('INSERT INTO data_scientists VALUES( ?,?,?,? )', student_list)
print('have inserted', c.rowcount, 'records to table data_scientists.')

c.execute("SELECT * FROM data_scientists")

item = c.fetchall()
print('FIRST_NAME' + '\tLAST_NAME' + '\t\tEMAIL'  + '\t\t\t\tCOURSE')
print('..........' + '\t.........' + '\t\t.....'  + '\t\t\t\t......')

#looping through

for item in item:
  first_name, last_name, email, course = item
  print(f"{first_name:16}{last_name:16}{email:35}{course:25}")
  
