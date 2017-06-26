from . import app,db
from flask import render_template

@app.route('/datatable')
def datatable():
    c = db.execute('select * from log where value>5 order by value desc')
    res = c.fetchall()
    print res
    return render_template('datatable.html',data=res)
