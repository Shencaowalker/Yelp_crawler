#coding:utf-8
import MySQLdb
conn=MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='shen',
        db ='lunwen_yelp',
        )

cur = conn.cursor()

def insertshopdb(list):
#	cur = conn.cursor()
	sqli="insert ignore into shoplist values(%s,%s,%s,%s)"
	for i in list:
		try:
			cur.execute(sqli,(i.name.encode("utf-8"),i.star.encode("utf-8"),i.title.encode("utf-8"),i.address.strip().encode("utf-8")))
		except Exception as e:
			continue
#	cur.close()
	conn.commit()

def selectshopdb():
#	cur = conn.cursor()
	aa=cur.execute("select * from shoplist")

	info = cur.fetchmany(aa)

	for ii in info:
    		print ii[0].ljust(50,' '),"|",ii[1].ljust(5,' '),"|",ii[2].ljust(40,' '),"|",ii[3].ljust(40,' ')
		print "*"*139

	cur.close()
#        conn.commit()
	
def selectshopnamecomment(name):
	filename=open('comment/'+name+'.yp','w')
	cur = conn.cursor()
	exc="select * from shopcomment where shopname='"+name+"'"
	bb=cur.execute(exc)
	aa=cur.fetchmany(bb)
	for ii in aa:
		print ii[1].decode("utf-8"),ii[2].decode("utf-8"),ii[3].decode("utf-8"),ii[4].decode("utf-8"),ii[5].decode("utf-8")

		filename.write(ii[1])
		filename.write("\n")
		filename.write(ii[2])
		filename.write("\n")
		filename.write(ii[3])
		filename.write("\n")
		filename.write(ii[4])
		filename.write("\n")
		filename.write(ii[5])
		filename.write("\n")
		filename.write("*"*50)
		filename.write("\n")
	filename.close()
	cur.close()
	conn.commit()
	conn.close()


def insertshopuserdb(list):
#	cur = conn.cursor()
	sqli="insert ignore into shopcomment values(NULL,%s,%s,%s,%s,%s)"
	for i in list:
		for j in i:
			try:	
				cur.execute(sqli,(i.shopname.encode("utf-8"),i.username.encode("utf-8"),i.star.encode("utf-8"),i.commenttime.encode("utf-8"),i.comment.encode("utf-8")))
				print "Insert 10 data into the database"		
			except Exception as e:
				continue
#	cur.close()
	conn.commit()


def selectshopname(name):
	cur = conn.cursor()
	exc="select * from shoplist where name='"+name+"'"
	cur.execute(exc)
	aa=cur.fetchone()
	print aa[0].decode("utf-8"),aa[1].decode("utf-8"),aa[2].decode("utf-8"),aa[3].decode("utf-8")
	cur.close()
	conn.commit()
	conn.close()





	




if __name__=="__main__":
	selectshopdb()

	name=raw_input("Please enter the shopname to see,if you wan't see,please direct press enter:")
	selectshopnamecomment(name)
#	selectshopname(name)



