from . import app,db

@app.route('/table')
def table():
	table = '<table border="1">'
	c = db.execute('select * from log order by value desc limit 20;')
	for l in c.fetchall():
		table += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%l
	table +='</table>'
	return table