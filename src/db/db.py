from flask_mysqldb import MySQL

def config_db(app):
    # DB
    app.config['MYSQL_DB']='railway'
    app.config['MYSQL_HOST']='containers-us-west-150.railway.app'
    app.config['MYSQL_PORT']=7867
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']='Y5BO5a12p3M7KBamtll4'
    mysql=MySQL(app)

    return mysql