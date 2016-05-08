from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import cgi

from database_setup import Restaurant, Base, MenuItem
#connect to restaurant database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		items = session.query(Restaurant).all()
		try:
			output = ""
			if self.path.endswith("/restaurant"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output += "<html><body>"
				output += "<a href='/restaurant/new'>Make a new restaurant</a>"
				output += "<br/>"
				output += "<br/>"
				for item in items:
					output += "<b>%s</b>" %item.name
					output += "<br/>"
					output += "<a href='/restaurant/%s/edit'>Edit</a>" % item.id
					output += "<br/>"
					output += "<a href='/restaurant/%s/delete'>Delete</a>" % item.id
					output += "<br/>"
					output += "<br/>"

				output += "</body></html>"
				self.wfile.write(output)
				print output
				return

			if self.path.endswith("/restaurant/new"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output +=  "<html><body>"
				output +=  "<h1>Make a new restaurant</h1>"
				output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/new'>
				<input name="restaurantname" type="text" ><input type="submit" value="Create"> </form>'''
				output += "</html></body>"
				self.wfile.write(output)
				print output
				return

			if self.path.endswith("/edit"):
				restid = self.path.split("/")[2]
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output +=  "<html><body>"
				output +=  "<h1>Rename restaurant</h1>"
				output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/edit')>
				<input name="restaurantname" type="text" ><input type="submit" value="Rename"> </form>'''  % restid
				output += "</html></body>"
				self.wfile.write(output)
				print output
				return

			if self.path.endswith("/delete"):
				restid = self.path.split("/")[2]
				restname = session.query(Restaurant).filter_by(id=restid).one().name
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output +=  "<html><body>"
				output +=  "<h1>Delete Restaurant</h1>"
				output += '''<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/delete')>
				<h3>Are you sure you want to delete %s?</h3><input type="submit" value="Delete"> </form>'''  %(restid, restname)
				output += "</html></body>"
				self.wfile.write(output)
				print output
				return


		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)


	def do_POST(self):
			try:
				if self.path.endswith("/restaurant/new"):
					ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
					if ctype == 'multipart/form-data':
						fields=cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('restaurantname')

					newRestaurant = Restaurant(name = messagecontent[0])
					session.add(newRestaurant)
					session.commit()

					self.send_response(301)
					self.send_header('Content-type',	'text/html')
					self.send_header("Location", '/restaurant')
					self.end_headers()

				if self.path.endswith("/edit"):
					restid = self.path.split("/")[2]
					ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
					if ctype == 'multipart/form-data':
						fields=cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('restaurantname')

					rest = session.query(Restaurant).filter_by(id=restid).one()
					rest.name =  messagecontent[0]
					session.add(rest)
					session.commit()

					self.send_response(301)
					self.send_header('Content-type',	'text/html')
					self.send_header("Location", '/restaurant')
					self.end_headers()

				if self.path.endswith("/delete"):
					restid = self.path.split("/")[2]
					ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
					if ctype == 'multipart/form-data':
						fields=cgi.parse_multipart(self.rfile, pdict)


					rest = session.query(Restaurant).filter_by(id=restid).one()
					session.delete(rest)
					session.commit()

					self.send_response(301)
					self.send_header('Content-type',	'text/html')
					self.send_header("Location", '/restaurant')
					self.end_headers()
			except:
				pass


def main():
	try:
		port = 8081
		server = HTTPServer(('', port), webServerHandler)
		print "Web Server running on port %s"  % port
		server.serve_forever()
	except KeyboardInterrupt:
		print " ^C entered, stopping web server...."
		server.socket.close()

if __name__ == '__main__':
	main()
