from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

SERVER_PORT = 8080

class PyDataAnalysisHandler(BaseHTTPRequestHandler):

	#Hanling for HTTP GET Reqests
	def do_GET(self):
		f = open("server_test.html")
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(f.read())
		f.close()
		print 'GET'
		return
	#Handling for HTTP POST Requests
	def do_POST(self):
		print 'POST'

#Main method, create the server and let it run
#to handle incoming requests as necessary.
def main():
	try:
		server = HTTPServer(('',SERVER_PORT),PyDataAnalysisHandler)
		print 'starting PyDataAnalysisServer on port: ' + str(SERVER_PORT)
		server.serve_forever()
	except KeyboardInterrupt:
		print 'Shutting down the PyDataAnalysisServer!'
		server.socket.close()


if __name__ == '__main__':
	main()
