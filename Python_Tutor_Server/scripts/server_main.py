from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import graphlab as gl
from graphlab import SFrame
import cgi
import codediff

SERVER_PORT = 8080

#Class to hold the requested session data, and produce HTML diffs for this session
class PythonTutorSession:

	#Initialize the session from the clean frames (our database in this case)
	def __init__(self,version,session_id,diff):
		if(int(version) == 2):
			sf = gl.load_sframe("data/py2_session_clean")
		else:
			sf = gl.load_sframe("data/py3_session_clean")

		self.session = sf.filter_by([int(session_id)],"session_id")

		if(diff == "Full"):
			self.diffs = False
		else:
			self.diffs = True

	#Return basic information about the session
	def getSessionInformation(self):
		m_session = self.session
		information = m_session[1]

		html = "<h2>Basic Session Information</h2><hr/>"
		
		html += "<p align='center'>"
		html += "<b>Session ID:</b>&nbsp;" + str(information['session_id']) 
		html += "&nbsp;&nbsp;&nbsp;<b>IP Address:</b>&nbsp;" + str(information['ip'])
		html += "&nbsp;&nbsp;&nbsp;<b>Python:</b>&nbsp;" + str(information['py'])
		html += "</p><hr/>"
		
		return html

	#Return the diffs
	def getDiffs(self):
		html = "<h2>Diff Data for this Session</h2>"

		m_session = self.session
		m_session.sort('dt')

		print m_session.column_names()

		prev_row = ""

		for e in m_session:
			if(prev_row == ""):
				prev_row = e
			else:
				html += "<p align='center'><b>Submission Date:&nbsp;" + str(prev_row['dt']) + "&nbsp;&nbsp;with error:&nbsp;" + str(prev_row['err_msg'])
				html += "<p align='center'><b>Submission Date:&nbsp;" + str(e['dt']) + "&nbsp;&nbsp;with error:&nbsp;" + str(e['err_msg'])

				html += codediff.sdiff_lines(prev_row['user_script'].split('\n'),e['user_script'].split('\n'),prev_row['dt'],e['dt'],self.diffs,0,3)
				html += "<hr/>"

				prev_row = e
		return html

	#Return comment form
	def getComment(self):
		return "<p>COMMENT FORM!</p>"
	
#HTTP Server basic handler
class PyDataAnalysisHandler(BaseHTTPRequestHandler):

	#Hanling for HTTP GET Reqests
	def do_GET(self):
		f = open("index.html")
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(f.read())
		f.close()
		return
	#Handling for HTTP POST Requests
	def do_POST(self):
		#Grab the incoming form data and send a successfully 'we get this' response along with the headers
		web_form = cgi.FieldStorage(fp=self.rfile,
					    headers=self.headers,
                                            environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type']})
		self.send_response(200)
		self.end_headers()

		#Get the request type (in this we're embedding in the 'submit' button value
		request = web_form.getvalue("submit")

		#Handle the request as appropriate
		if(request == "Query"):
			version = web_form.getvalue("python_version")
			session = web_form.getvalue("session_id")
			diff = web_form.getvalue("diff_version")

			m_session = PythonTutorSession(version,session,diff)

			html_body = m_session.getSessionInformation()
			html_body += m_session.getDiffs()
			html_body += m_session.getComment()

		elif(request == "Comment"):
			html_body = "RECEIVED: Comment!"
		else:
			html_body = "BAD REQUEST!"

		response = "<html><head></head><body>" + html_body +"</body></html>"
		self.wfile.write(response)
		return

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
